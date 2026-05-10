---
name: smic12sf-pdk
description: "SMIC 12nm FinFET PDK reference: layer definitions, device parameters, design rules, and Python API helpers."
---

# SMIC 12nm FinFET PDK Reference

**PDK Version:** SPDK12SFE_0818_OA_CDS_V1.20_REV0_0  
**Process Node:** 12nm FinFET (14nm nominal)  
**Manufacturing Grid:** 1nm (0.001 um)  
**Library Name:** `smic12sf`  

---

## Python API: `virtuoso_bridge.virtuoso.layout.pdk`

### MOS Device Generators

```python
from virtuoso_bridge.virtuoso.layout import (
    smic12sf_create_nmos,
    smic12sf_create_pmos,
    smic12sf_nmos_svt,    # Shortcut: standard Vt 0.8V NMOS
    smic12sf_pmos_svt,    # Shortcut: standard Vt 0.8V PMOS
    smic12sf_nmos_lvt,    # Shortcut: low Vt 0.8V NMOS
    smic12sf_pmos_lvt,    # Shortcut: low Vt 0.8V PMOS
)
```

**Full function signature:**
```python
def smic12sf_create_nmos(
    instance_name: str,
    x: float,
    y: float,
    orientation: str = "R0",
    *,
    l: float = 0.014,      # gate length (um)
    w: float = 0.1,        # gate width per finger (um)
    nf: int = 1,           # number of fingers
    m: int = 1,            # multiplier / parallel instances
    vth: str = "svt",      # "ulvt" | "lvt" | "svt" | "hvt"
    voltage: str = "08",   # "08" = 0.8V core | "18" = 1.8V I/O
    dnw: bool = False,     # deep N-well isolation (NMOS only)
) -> str:
```

**PMOS signature is identical except no `dnw` parameter.**

### Threshold Voltage Options

| Type | Vt | Speed | Leakage | Use Case |
|------|----|-------|---------|----------|
| `ulvt` | Ultra Low | Fastest | Highest | Critical path, high performance |
| `lvt` | Low | Fast | High | Performance-critical logic |
| `svt` | Standard | Balanced | Medium | Default, most logic |
| `hvt` | High | Slow | Lowest | Low-power, non-critical paths |

### Voltage Domains

| Domain | Voltage | Use |
|--------|---------|-----|
| `08` | 0.8V | Core logic, default |
| `18` | 1.8V | I/O, ESD protection, analog |

### MOS Naming Pattern

```
  n   08   _   ckt
  │    │       └── cell type suffix
  │    └────────── voltage: 08 = 0.8V, 18 = 1.8V
  └─────────────── type: n=NMOS(svt), p=PMOS(svt),
                        nlvt=NMOS(lvt), plvt=PMOS(lvt),
                        nhvt=NMOS(hvt), phvt=PMOS(hvt),
                        nulvt=NMOS(ulvt), pulvt=PMOS(ulvt)
```

With DNW: `n08_dnw_ckt`, `nlvt08_dnw_ckt`, etc.

---

## Python API: `virtuoso_bridge.virtuoso.layout.layers`

### Layer Constants

```python
from virtuoso_bridge.virtuoso.layout import SMIC12SF, SMIC12SFLayers

# Using the pre-instantiated SMIC12SF
aa_layer = SMIC12SF.AA           # "AA"
gt_layer = SMIC12SF.GT           # "GT"
m1_layer = SMIC12SF.M1           # "M1"
purpose = SMIC12SF.DRAWING       # "drawing"

# Get (layer, purpose) tuple directly
lpp = SMIC12SF.lpp(SMIC12SF.M1, SMIC12SF.PIN)  # ("M1", "pin")
```

### Front-End Layers

| Constant | Layer | Purpose |
|----------|-------|---------|
| `AA` | AA | Active Area |
| `FIN` | FIN | FinFET fins |
| `GT` | GT | Gate |
| `DG` | DG | Double Gate |
| `P2` | P2 | Poly 2 |
| `SN` | SN | N-type Source/Drain implant |
| `SP` | SP | P-type Source/Drain implant |
| `NW` | NW | N-Well |
| `DNW` | DNW | Deep N-Well |
| `NPAA` | NPAA | N-type AA implant |
| `PPAA` | PPAA | P-type AA implant |

### Metal Layers

| Constant | Layer | Typical Use |
|----------|-------|-------------|
| `M0` | M0 | Local interconnect |
| `M0C` | M0C | M0 cut |
| `M1` | M1 | Signal, local routing |
| `M2` | M2 | Signal |
| `M3` | M3 | Signal |
| `M4` | M4n | Signal (narrow) |
| `M5` | M5n | Signal (narrow) |
| `M6` | M6n | Signal (narrow) |
| `M7` | M7n | Signal (narrow) |
| `TM1` | TM1 | Top Metal 1 (thick), power, clock |
| `TM2` | TM2 | Top Metal 2 (thick), bump pads |
| `ALPA` | ALPA | Aluminum pad |
| `PA` | PA | Passivation opening |
| `BUMP` | BUMP | Bump layer |

### Via Layers

| Constant | Connects |
|----------|----------|
| `V0` | M0 ↔ M1 |
| `V1` | M1 ↔ M2 |
| `V2` | M2 ↔ M3 |
| `V3` | M3 ↔ M4 |
| `V4` | M4 ↔ M5 |
| `V5` | M5 ↔ M6 |
| `V6` | M6 ↔ M7 |
| `TV1` | M7 ↔ TM1 |
| `TV2` | TM1 ↔ TM2 |
| `BV1` | TM2 ↔ ALPA |
| `BV2` | — |

### Purposes

| Constant | Value |
|----------|-------|
| `DRAWING` | `"drawing"` |
| `PIN` | `"pin"` |
| `LABEL` | `"label"` |
| `NET` | `"net"` |

---

## Passive Device Generators

### Resistors

```python
from virtuoso_bridge.virtuoso.layout import smic12sf_create_resistor

smic12sf_create_resistor(
    "R1", x, y, orientation="R0",
    w=0.1,          # width (um)
    l=10,           # length (um)
    m=1,            # multiplier
    res_type="rm1"  # resistor type
)
```

**Available resistor types:**

| Type | Material |
|------|----------|
| `rm1` – `rm7` | Metal 1 through Metal 7 |
| `rtm1`, `rtm2` | Top Metal 1, 2 |
| `ralpa` | Aluminum pad |
| `rhrpo` | High Resistance Poly |
| `rnwsti` | N-Well STI |
| `NGR` | N-type Gate Resistor |
| `PGR` | P-type Gate Resistor |

### MOM Capacitors

```python
from virtuoso_bridge.virtuoso.layout import smic12sf_create_mom_cap

smic12sf_create_mom_cap(
    "C0", x, y, orientation="R0",
    w=1.0,                  # width (um)
    l=1.0,                  # length (um)
    nf=1,                   # fingers
    ports=2,                # 2, 3, 4, or 5 terminals
    high_quality=False,     # HQ version
    ultra_low=False,        # ultra-low capacitance
)
```

**Cell naming pattern:** `mom_{quality}{ports}t_1p25`

- Quality: `""` (std), `"hq_"`, `"ulc_"`
- Ports: 2, 3, 4, 5 → `"2t"`, `"3t"`, etc.

### Diodes

```python
from virtuoso_bridge.virtuoso.layout import smic12sf_create_diode

smic12sf_create_diode(
    "D0", x, y, orientation="R0",
    diode_type="ndio08",    # diode type
    w=0.5,                  # width
    l=0.5,                  # length
)
```

**Diode types:**

| Type | Description |
|------|-------------|
| `ndio08` | 0.8V N-type diode |
| `ndio18` | 1.8V N-type diode |
| `pdio08` | 0.8V P-type diode |
| `pdio18` | 1.8V P-type diode |
| `dnwdio` | DNW diode |
| `nwdio` | N-Well diode |
| `rwdio` | R-Well diode |

---

## BJT Transistors

Only the following cells have usable schematic symbols:

| Cell | Terminals | Description |
|------|-----------|-------------|
| `npn08` | C, B, E | 0.8V NPN |
| `npn18` | C, B, E | 1.8V NPN |
| `pnp08` | C, B, E | 0.8V PNP (vertical, C=substrate→VSS) |
| `pnp18` | C, B, E | 1.8V PNP (vertical, C=substrate→VSS) |

> Cells with `_ckt` suffix (e.g. `pnp18a8_ckt`) appear in the library but **lack symbol views** — not usable in schematics.

---

## Schematic Symbol Terminal Names

When connecting PDK devices in schematics, terminals are case-sensitive:

| Device | Terminals | Notes |
|--------|-----------|-------|
| **MOSFET** (n18_ckt, p18_ckt, etc.) | G, D, S, B | B = bulk. NMOS B→VSS, PMOS B→VDD |
| **PNP** (pnp18, pnp08) | C, B, E | C = collector (substrate) → VSS |
| **NPN** (npn18, npn08) | C, B, E | |
| **Diode** (pdio18_ckt, ndio18_ckt) | A, C | A = anode, C = cathode |
| **MOM cap** (mom_hq_2t, etc.) | PLUS, MINUS | |
| **Resistor** (rhrpo_3t_ckt, etc.) | PLUS, MINUS, BULK | BULK = substrate/well tie |

> **Symbol viewType:** All smic12sf PDK symbols use `viewType="schematicSymbol"` (not "schematic").
> Open with: `dbOpenCellViewByType("smic12sf" "pnp18" "symbol" "schematicSymbol" "r")`

---

| Cell | Description |
|------|-------------|
| `n18_esd` | 1.8V NMOS ESD |
| `ndio18_esd` | 1.8V N-diode ESD |
| `ngdio18_esd` | 1.8V N-gate diode ESD |
| `pdio18_esd` | 1.8V P-diode ESD |
| `pgdio18_esd` | 1.8V P-gate diode ESD |
| `npn5_esd` | 5-finger NPN ESD |

---

## Variable MOS Capacitors

| Cell | Description |
|------|-------------|
| `pvar08_ckt` | 0.8V varactor |
| `pvar08_ckt_rf` | 0.8V RF varactor |
| `pvar18_ckt` | 1.8V varactor |
| `pvar18_ckt_rf` | 1.8V RF varactor |

---

## Device Statistics

Total PDK cells: ~165

| Category | Count | Notes |
|----------|-------|-------|
| MOS transistors | ~21 | Core + I/O, multiple Vt |
| Varactors | 4 | 0.8V / 1.8V, std + RF |
| Resistors | ~15 | Metal, poly, well, gate |
| MOM capacitors | 14 | HQ, ULC, standard, multi-port |
| Diodes | 7 | ndio, pdio, dnw, nw, rw |
| BJTs | 4 usable | pnp08/pnp18/npn08/npn18 only — rest lack symbol view |
| ESD devices | ~6 | |
| Parasitic extraction | ~30 | |
| RF variants | ~20 | |
| Internal/utility | ~30 | |

---

## Parameter Reference

### MOS Parameters

| Parameter | Type | Typical Range | Notes |
|-----------|------|--------------|-------|
| `l` | float | 0.014 – 10 um | Gate length |
| `w` | float | 0.1 – 100 um | Gate width per finger |
| `nf` | int | 1 – 1000 | Number of fingers |
| `m` | int | 1 – 100 | Multiplier (parallel instances) |
| `sa` | float | – | Source diffusion extension |
| `sb` | float | – | Drain diffusion extension |
| `sd` | float | – | Source-drain spacing |

### Passive Parameters

| Device | Parameters |
|--------|------------|
| Resistor | `w`, `l`, `m`, `seg` |
| Capacitor | `w`, `l`, `nf`, `m` |
| Diode | `w`, `l` |

---

## Metal Option Configuration

**`METAL_OPTION: 1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK`**

Breakdown:
- `1P9M` — 1 Poly layer + 9 Metal layers
- `DV` — Dual Voltage domains
- `3DM` — 3 Dense Metal layers
- `Q1_3Q2` — Q factor configuration options
- `2TMa` — 2 Thick Top Metal layers (option A)
- `ALPA` — Aluminum pad layer present
- `14SHK` — 14 Shield layer configuration

---

## Common Gotchas

### 1. CDF Parameter Read-Only Fields

PDK MOS devices expose `nf` as read-only. Use `fingers` instead when setting via schematic CDF:

```python
# ✅ Use "fingers"
schHiReplace(...?newPropName "fingers" ...)

# ❌ Don't use "nf"
schHiReplace(...?newPropName "nf" ...)  # → SCH-1725 "not editable"
```

### 2. Parameter Callbacks

Always trigger CDF callbacks after setting params:

```python
CCSinvokeCdfCallbacks(cv ?order list("fingers" "w" "l"))
```

See `references/schematic-skill-api.md` for the full CDF parameter guide.

### 3. Layout Grid

All coordinates must be snapped to **1nm grid** (0.001 um). Off-grid coordinates cause DRC errors.

### 4. DNW Availability

Deep N-well (`dnw=True`) is only available for NMOS devices, not PMOS.

### 5. I/O vs Core

1.8V devices (`voltage="18"`) are significantly larger than 0.8V core devices. Use only for I/O and ESD circuits.

### 6. Symbol viewType

All smic12sf PDK symbols use `viewType="schematicSymbol"`, not `"schematic"`. The helper function `schematic_create_inst_by_master_name()` handles this automatically, but if calling `dbOpenCellViewByType` directly:

```skill
;; ✅ Correct
dbOpenCellViewByType("smic12sf" "pnp18" "symbol" "schematicSymbol" "r")

;; ❌ Returns nil
dbOpenCellViewByType("smic12sf" "pnp18" "symbol" "schematic" "r")
```

---

## Example: Inverter Layout with SMIC12SF

```python
from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.layout import (
    smic12sf_nmos_svt,
    smic12sf_pmos_svt,
    SMIC12SF,
)
from virtuoso_bridge.virtuoso.layout.ops import (
    layout_create_rect as rect,
    layout_create_path as path,
    layout_create_label as label,
)

client = VirtuosoClient.from_env()

LIB, CELL = "MY_LIB", "INV_X1"
with client.layout.edit(LIB, CELL) as lay:
    # NMOS at bottom (y=0)
    lay.add(smic12sf_nmos_svt("MN0", 0, 0, l=0.014, w=0.1, nf=2))
    
    # PMOS at top (y=2um)
    lay.add(smic12sf_pmos_svt("MP0", 0, 2, l=0.014, w=0.2, nf=2))
    
    # VDD rail on TM1
    lay.add(rect(SMIC12SF.TM1, SMIC12SF.DRAWING, -1, 3.5, 5, 3.9))
    lay.add(label(SMIC12SF.TM1, SMIC12SF.PIN, 0, 3.7, "VDD", "centerLeft"))
    
    # VSS rail
    lay.add(rect(SMIC12SF.TM1, SMIC12SF.DRAWING, -1, -0.4, 5, 0))
    lay.add(label(SMIC12SF.TM1, SMIC12SF.PIN, 0, -0.2