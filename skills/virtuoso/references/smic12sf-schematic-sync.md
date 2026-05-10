# SMIC 12nm Schematic Parameter Sync Guide

Conventions and gotchas for synchronizing device parameters to SMIC 12nm schematics via `virtuoso_bridge`.

---

## CDF Parameter Naming

SMIC 12nm `n18_ckt` / `p18_ckt` MOSFETs use different CDF parameter names than TSMC PDKs:

| Concept | TSMC convention | SMIC 12nm CDF name |
|---------|----------------|-------------------|
| Channel length | `l` | `l` |
| Fin count | `nfin` | `nfin` |
| Finger count | `nf` | `fingers` |
| Multiplier | `mr` | `m` |

**Key difference:** `nf` -> `fingers`, `mr` -> `m`. Using `nf` triggers a CDF callback error:
```
*Error* fprintf/sprintf: format spec. incompatible with data -
"Format is '%s = %s ', argument #2 is nil"
```

This happens because `nf` is not a valid CDF parameter on SMIC devices — the callback returns nil.

---

## Using `set_instance_params`

```python
from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.schematic.params import set_instance_params

client = VirtuosoClient.from_env()

set_instance_params(
    client, "M1",
    l="242n",              # channel length as string with unit
    param_filters=None,    # required for SMIC devices
    nfin="8",
    fingers="8",           # NOT nf
    m="8",                 # NOT mr
)
```

**Why `param_filters=None`:** The `cdf_param_filters.yaml` file has explicit filters for TSMC devices. SMIC 12nm devices (`n18_ckt`, `p18_ckt`) fall through to the `fallback: all` rule. Passing `param_filters=None` bypasses the filter map entirely, sending all parameters directly to CDF.

---

## MOM Capacitors: Direct SKILL Required

The `mom_2t_1p25` MOM capacitor's `mr` (multiplier) parameter **cannot** be updated via `set_instance_params`. Use direct SKILL:

```python
skill = (
    'let((cv inst) '
    'cv = geGetEditCellView() '
    'inst = car(setof(x cv~>instances x~>name == "Cc")) '
    'unless(inst error("instance not found: Cc")) '
    'inst~>mr = "1" '       # set multiplier directly
    'dbSave(cv) t)'
)
result = client.execute_skill(skill, timeout=30)
```

This bypasses CDF entirely and writes the database attribute directly.

---

## Channel Length Update Issues

Setting `l` via `set_instance_params` may silently fail — the parameter appears updated in CDF but the actual device L doesn't change in the schematic.

**Symptom:** After running `set_instance_params(..., l="242n", ...)`, checking via CDF shows `l=242n` but the device geometry still uses the old value.

**Workaround:** Use direct SKILL to set `l` on the database object:

```python
MOS_DEVICES = ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]
NEW_L = "242n"

skill = '''let((cv inst out)
  cv = geGetEditCellView()
  unless(cv error("no cellview"))
  out = ""
  foreach(name list(''' + " ".join(f'"{n}"' for n in MOS_DEVICES) + ''')
    inst = car(setof(x cv~>instances x~>name == name))
    when(inst
      inst~>l = "''' + NEW_L + '''"
      out = strcat(out sprintf(nil "%s l=%s\\n" name inst~>l))
    )
  )
  dbSave(cv)
  out)'''

result = client.execute_skill(skill, timeout=30)
```

**Verification:** Read back via CDF to confirm:
```python
skill2 = '''let((cv inst out)
  cv = geGetEditCellView()
  out = ""
  foreach(name list(''' + " ".join(f'"{n}"' for n in MOS_DEVICES) + ''')
    inst = car(setof(x cv~>instances x~>name == name))
    when(inst
      icdf = cdfGetInstCDF(inst)
      out = strcat(out sprintf(nil "%s: l=%s\\n" name icdf~>l~>value))
    )
  )
  out)'''
```

---

## Instance Naming Conventions

### Multi-instance decomposition

When a MOSFET is placed with `m > 1` in the schematic, Virtuoso may decompose it into individual instances with qualified names:

| Original | Decomposed to |
|----------|--------------|
| M1 (m=8) | qq.1, qq.2, ..., qq.8 |
| M2 (m=8) | M2.1, M2.2, ..., M2.8 |
| M6 (m=2) | M6.1, M6.2 |

The `qq.N` naming occurs for the differential pair due to how the schematic was originally drawn.

### Recommended approach

Use single instances (not decomposed) for easier programmatic access:

```skill
;; Target by simple name when schematic uses single instances
inst = car(setof(x cv~>instances x~>name == "M1"))
```

If instances are decomposed, target each individually or use pattern matching:

```skill
;; Match all instances starting with "M1"
setof(x cv~>instances strmatch(x~>name "M1*"))
```

**Best practice:** Design the schematic with one instance per logical device (M1, M2, ..., M7) and control sizing through `nfin`, `fingers`, and `m` parameters rather than placing multiple physical instances.

---

## Typical Sync Workflow

```python
#!/usr/bin/env python3
"""Sync device parameters to SMIC 12nm schematic."""
from virtuoso_bridge import VirtuosoClient, decode_skill_output
from virtuoso_bridge.virtuoso.schematic.params import set_instance_params

client = VirtuosoClient.from_env()

# 1. Test connection
client.execute_skill("1+2")

# 2. Update MOS devices via set_instance_params
L = "242n"
DEVICES = {
    "M1": {"nfin": "8", "fingers": "8", "m": "8"},
    "M2": {"nfin": "8", "fingers": "8", "m": "8"},
    "M3": {"nfin": "6", "fingers": "1", "m": "2"},
    "M4": {"nfin": "6", "fingers": "1", "m": "2"},
    "M5": {"nfin": "6", "fingers": "1", "m": "2"},
    "M6": {"nfin": "6", "fingers": "1", "m": "2"},
    "M7": {"nfin": "6", "fingers": "1", "m": "1"},
}

for name, params in DEVICES.items():
    set_instance_params(client, name, l=L, param_filters=None, **params)

# 3. If L didn't update, use direct SKILL (see "Channel Length Update Issues" above)

# 4. Update MOM capacitor via direct SKILL
skill = (
    'let((cv inst) cv = geGetEditCellView() '
    'inst = car(setof(x cv~>instances x~>name == "Cc")) '
    'inst~>mr = "1" dbSave(cv) t)'
)
client.execute_skill(skill, timeout=30)

# 5. Verify all parameters by reading back via CDF
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `unknown CDF param: nf` | SMIC uses `fingers` not `nf` | Use `fingers` in params dict |
| `argument #2 is nil` error | Invalid CDF param name triggers nil callback | Check parameter name against PDK |
| L value doesn't change after set_instance_params | CDF callback doesn't propagate L change | Use direct SKILL `inst~>l = "242n"` |
| Instance not found: M1 | Schematic has decomposed instances (qq.1) | Rename instances in schematic or use pattern match |
| Cc mr parameter ignored | MOM cap mr not exposed via CDF | Use direct SKILL `inst~>mr = "1"` |
| IBIAS parameter has no effect | Self-biasing circuit (M8/M9/M10) fixes current | Modify bias network device sizing, not IBIAS param |
