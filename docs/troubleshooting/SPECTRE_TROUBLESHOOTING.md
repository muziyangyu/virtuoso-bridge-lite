# Spectre Netlist Syntax & Simulation Troubleshooting

## Common Netlist Errors

### 1. `vcvs` / E-source Syntax

**Wrong:**
```spectre
E_FB (VINN 0) vcvs gain=1 probe=VOUT 0   // SFE-691/874 error
```

**Correct (use vsource for feedback):**
```spectre
V_FB (VINN VOUT) vsource dc=0
```

### 2. `vsource` AC Parameters

**Wrong:**
```spectre
VIN (VINP 0) vsource dc=0.45 acmag=1m acphase=0  // SFE-30 ignored
```

**Correct:**
```spectre
VIN (VINP 0) vsource dc=0.45 ac=1m
```

### 3. `ac` Analysis Parameters

**Wrong:**
```spectre
ac_ac ac start=1 stop=1G log=yes ptsperdec=101   // SFE-884/1997 error
```

**Correct:**
```spectre
ac_ac ac start=1 stop=1G dec=101
```

### 4. Line Continuation in Python String Lists

When building netlists in Python, **avoid backslash line continuation** inside list strings:

**Wrong:**
```python
"simulatorOptions options psfversion=\"1.4.0\" reltol=1e-4 vabstol=1e-6 \
        iabstol=1e-12 temp=27 tnom=27",  // produces spaces in wrong places
```

**Correct — keep each parameter on one line or join without extra spaces:**
```python
"simulatorOptions options reltol=1e-4 vabstol=1e-6 iabstol=1e-12 temp=27",
```

## AC Simulation: Feedback Configuration

### Problem: Unity-gain feedback shorts AC signal

Using `V_FB (VINN VOUT) vsource dc=0` creates a **DC and AC short** between VINN and VOUT.
Since VINN is forced to track VOUT (which tracks VINP via feedback), the differential input is zero for AC,
resulting in VOUT = 0 for all frequencies.

### Solution: Use large inductor for DC-only feedback

```spectre
// DC: inductor is short → VINN = VOUT → closed-loop bias
// AC: inductor is open → VINN floats → VINP has AC, VINN is DC only → full differential gain
VIN (VINP 0) vsource dc=0.45 ac=1m
LFB (VINN VOUT) inductor l=1e6
```

**Inductor sizing:**
- `l=1e6` (1 MH): Z = 2π·1e6·1 Hz = 6 MΩ at 1 Hz — effectively open for AC
- Z = 0 at DC — closes feedback loop for DC bias point
- Too large (e.g. 1 GH) will also block DC frequencies

## PSF ASCII Parsing

The `parse_psf_ascii_directory` function from `virtuoso_bridge.spectre.parsers` only returns **flat DC keys**
(e.g. `dc_op_VOUT: float`). It does **not** return AC sweep data as arrays.

**Workaround:** Parse the `.ac` file manually:

```python
import re
with open(raw_dir / "ac_ac.ac") as f:
    content = f.read()
val_idx = content.find("VALUE")
freq_pattern = re.compile(r'"freq"\s+([0-9.eE+-]+)')
vout_pattern = re.compile(r'"VOUT"\s+\(([-0-9.]+)\s+([-0-9.]+)\)')
# ... parse from val_idx onwards
```

The AC data format in PSF ASCII alternates:
```
VALUE
"freq" 1.00000e+00
"VOUT" (0.00000 0.00000)
"freq" 1.02306e+00
"VOUT" (0.00000 0.00000)
...
```

## Two-Stage Opamp DC Bias Issues

### Symptom: VOUT railed to VDD or VSS

**Root cause:** Second-stage PMOS active load (M7) was diode-connected (gate tied to drain),
which shorts the output to VDD. Also, M6/M7 current mismatch pushes VOUT to a rail.

**Fix:** Use a PMOS current mirror (M7_ref/M7) with separate gate bias:
```spectre
M7 (VOUT net_vb_p VDD VDD) p18_ckt w=8u l=0.18u nf=4 nfin=4
M7_ref (net_vb_p net_vb_p VDD VDD) p18_ckt w=4u l=0.18u nf=2 nfin=4
Mbias2 (net_vb_p net_bias VSS VSS) n18_ckt w=4u l=0.18u nf=2 nfin=4
```

### Symptom: net_bias = 0.9V (VDD), tail current off

**Root cause:** Bias circuit was incomplete or wrong topology (e.g. PMOS mirror feeding NMOS gate
without proper current reference).

**Fix:** Use NMOS diode-connected mirror with resistor current reference:
```spectre
Mbias (net_bias net_bias VSS VSS) n18_ckt w=8u l=0.18u nf=4 nfin=4
Rbias (VDD net_bias) resistor r=90k
```

### Working DC Configuration (verified)

| Node | Voltage | Status |
|------|---------|--------|
| VDD | 0.900 V | Supply |
| VINP/VINN | 0.450 V | Input bias |
| VOUT | 0.450 V | Follows input (unity-gain) |
| net_bias | 0.509 V | NMOS tail bias |
| net_vb_p | 0.473 V | PMOS load bias |
| net_s | 0.005 V | Diff pair source |
| net_d1/d2 | 0.541 V | Diff pair drains |

## Verified Netlist Template

A working two-stage opamp testbench is available at:
`output/opamp_sim_final.py` (function `build_testbench()`)

Key elements:
- Unity-gain DC bias via 1 MH inductor (VINN ↔ VOUT)
- AC signal on VINP only (1 mV)
- Rbias + diode-connected Mbias for tail current
- PMOS current mirror for second-stage load
- Miller compensation Cc = 1 pF, load CL = 2 pF
