#!/usr/bin/env python3
"""Fine-grain optimization around the optimal point, all MOS l=168n nfin=6.

Starting point (from 08_opamp_refine_1ghz.py):
    Cc=0.3p, m1=32, m3=32, m5=64, m6=6, m7=8
    GBW=1.15 GHz, PM=130.8°, DC Gain=61.4 dB, VOUT=1.273V

Optimization strategy:
    1. Reduce Cc stepwise to push GBW toward 1.5 GHz
    2. Tune M6/M7 ratio for VOUT near VDD/2 = 0.9V
    3. Adjust m1 to trade GBW vs power
    4. Track all metrics: Gain, GBW, PM, VOUT, power
"""

from __future__ import annotations
import os
import math
import cmath
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)
WORK_DIR = ROOT / "output" / "opamp_optimize_168n"
WORK_DIR.mkdir(parents=True, exist_ok=True)

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.spectre.runner import SpectreSimulator

PDK_MODEL = (
    "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0"
    "/smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0"
    "/models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
)


def build_testbench(cc, m1, m3, m5, m6, m7, stop="5G"):
    """Build testbench with fixed l=168n, nfin=6."""
    return f'''simulator lang=spectre
global 0

simulatorOptions options psfversion="1.4.0" reltol=1e-4 vabstol=1e-6 \\
  soft_bin=allmodels

include "{PDK_MODEL}" section=tt_mos_varactor
include "{PDK_MODEL}" section=tt_res_res3t_bjt_dio
include "{PDK_MODEL}" section=tt_mom_mim
include "{PDK_MODEL}" section=pre_layout

parameters VDD=1.8 VCM=0.9 IBIAS=10u

V0 (VDD 0) vsource dc=VDD
V1 (VSS 0) vsource dc=0

IBIAS (net_bias VSS) isource dc=IBIAS
M8 (net_bias net_bias VDD VDD) p18_ckt l=168n nfin=6 m=1
M9 (net_vb net_bias VDD VDD) p18_ckt l=168n nfin=6 m=1
M10 (net_bias net_bias VSS VSS) n18_ckt l=168n nfin=6 m=1
Rvb (net_vb VSS) resistor r=500MEG

M1 (net_d3 VINP net_s VSS) n18_ckt l=168n nfin=6 m={m1}
M2 (net_x VINN net_s VSS) n18_ckt l=168n nfin=6 m={m1}
M5 (net_s net_vb VSS VSS) n18_ckt l=168n nfin=6 m={m5}

M3 (net_d3 net_d3 VDD VDD) p18_ckt l=168n nfin=6 m={m3}
M4 (net_x net_d3 VDD VDD) p18_ckt l=168n nfin=6 m={m3}

M6 (VOUT net_x VSS VSS) n18_ckt l=168n nfin=6 m={m6}
M7 (VOUT net_bias VDD VDD) p18_ckt l=168n nfin=6 m={m7}

Cc (net_x VOUT) capacitor c={cc}

VINP (VINP 0) vsource dc=VCM mag=0.5
VINN (VINN 0) vsource dc=VCM mag=-0.5
CL (VOUT 0) capacitor c=2p

dcOp dc maxiters=150
ac ac start=1 stop={stop} dec=20

save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias
saveOptions options save=selected
'''


def parse_results(result, m3=0, m5=0, m7=0):
    """Extract DC + AC metrics including power estimate."""
    if not result.ok:
        return None

    vout = result.data.get("ac_VOUT")
    freq = result.data.get("ac_freq")
    dc_vout_raw = result.data.get("dc_VOUT", 0)
    if isinstance(dc_vout_raw, list):
        dc_vout = abs(dc_vout_raw[0])
    elif isinstance(dc_vout_raw, complex):
        dc_vout = abs(dc_vout_raw)
    else:
        dc_vout = abs(float(dc_vout_raw))

    if vout is None or freq is None:
        return None

    mag_db = []
    phase = []
    for v in vout:
        mag_db.append(20 * math.log10(abs(v) * 2 + 1e-30))
        phase.append(math.degrees(cmath.phase(v)))

    dc_gain = mag_db[0]
    gain_at_1g = None
    for i, f in enumerate(freq):
        if f >= 1e9:
            gain_at_1g = mag_db[i]
            break

    gbw = None
    for i in range(len(mag_db) - 1):
        if mag_db[i] >= 0 and mag_db[i + 1] < 0:
            f1, f2 = freq[i], freq[i + 1]
            g1, g2 = mag_db[i], mag_db[i + 1]
            log_f1 = math.log10(f1 + 1e-30)
            log_f2 = math.log10(f2 + 1e-30)
            log_cross = log_f1 + (log_f2 - log_f1) * (0 - g1) / (g2 - g1)
            gbw = 10 ** log_cross
            break

    pm = None
    if gbw:
        log_gbw = math.log10(gbw)
        log_freqs = [math.log10(f + 1e-30) for f in freq]
        for i in range(len(log_freqs) - 1):
            if log_freqs[i] <= log_gbw <= log_freqs[i + 1]:
                t = (log_gbw - log_freqs[i]) / (log_freqs[i + 1] - log_freqs[i])
                ph = phase[i] + t * (phase[i + 1] - phase[i])
                pm = 180 + ph
                break

    # Power estimate: IBIAS=10uA, mirrored by m ratios
    # M8(m=1) -> M7(m7) + M9(m=1)->M5(m5) + M3(m3) (diode-connected)
    ibias = 10e-6
    total_m = m7 + m5 + m3
    idc_est = ibias * total_m
    power = 1.8 * idc_est

    return {
        "dc_gain": dc_gain,
        "gain_1g": gain_at_1g,
        "gbw": gbw,
        "pm": pm,
        "vout_dc": dc_vout,
        "power": power,
    }


def fmt_gbw(gbw):
    if gbw is None:
        return ">5G"
    if gbw > 1e9:
        return f"{gbw/1e9:.2f} GHz"
    return f"{gbw/1e6:.0f} MHz"


def fmt_power(p):
    if p is None:
        return "N/A"
    if p > 1e-3:
        return f"{p*1e3:.2f} mW"
    return f"{p*1e6:.1f} uW"


# ================================================================
# Optimization configs — grouped by strategy
# ================================================================

OPT_CONFIGS = [
    # ── Group A: Reduce Cc around 0.3p to push GBW higher ─
    ("0.30p", 32, 32, 64,  6,  8, "baseline", "5G"),
    ("0.25p", 32, 32, 64,  6,  8, "Cc=0.25p", "5G"),
    ("0.20p", 32, 32, 64,  6,  8, "Cc=0.20p", "5G"),
    ("0.15p", 32, 32, 64,  6,  8, "Cc=0.15p", "5G"),

    # ── Group B: For Cc=0.25p, tune M6/M7 ratio for VOUT~0.9V ──
    ("0.25p", 32, 32, 64,  6,  8, "0.25p m6=6 m7=8", "5G"),
    ("0.25p", 32, 32, 64,  6, 10, "0.25p m6=6 m7=10", "5G"),
    ("0.25p", 32, 32, 64,  8, 10, "0.25p m6=8 m7=10", "5G"),
    ("0.25p", 32, 32, 64,  8, 12, "0.25p m6=8 m7=12", "5G"),
    ("0.25p", 32, 32, 64, 10, 14, "0.25p m6=10 m7=14", "5G"),

    # ── Group C: For Cc=0.20p, tune M6/M7 ──
    ("0.20p", 32, 32, 64,  6,  8, "0.20p m6=6 m7=8", "5G"),
    ("0.20p", 32, 32, 64,  8, 10, "0.20p m6=8 m7=10", "5G"),
    ("0.20p", 32, 32, 64,  8, 12, "0.20p m6=8 m7=12", "5G"),
    ("0.20p", 32, 32, 64, 10, 14, "0.20p m6=10 m7=14", "5G"),

    # ── Group D: Higher gm1 (m1=48) with smaller Cc ──
    ("0.20p", 48, 48, 96,  8, 10, "Cc=0.20p m1=48", "5G"),
    ("0.15p", 48, 48, 96,  8, 10, "Cc=0.15p m1=48", "5G"),
    ("0.15p", 48, 48, 96,  8, 12, "Cc=0.15p m1=48 rebal", "5G"),
    ("0.10p", 48, 48, 96,  8, 12, "Cc=0.10p m1=48", "5G"),

    # ── Group E: Maximum GBW push (aggressive) ──
    ("0.10p", 64, 64, 128, 8,  12, "aggressive m1=64", "5G"),
    ("0.10p", 64, 64, 128, 10, 14, "aggressive rebal", "5G"),
    ("0.08p", 64, 64, 128, 10, 14, "Cc=0.08p max", "5G"),
]


def main():
    print("=" * 85)
    print("  Optimization Sweep: l=168n nfin=6 (Fine-Grain Around Optimal)")
    print("=" * 85)

    client = VirtuosoClient.from_env()
    r = client.execute_skill("1+2")
    print(f"\nConnected: {r.output}")

    sim = SpectreSimulator.from_env(
        work_dir=str(WORK_DIR),
        output_format="psfascii",
    )

    results_table = []
    for cc, m1, m3, m5, m6, m7, desc, stop in OPT_CONFIGS:
        print(f"\n[{desc}]")
        tb = build_testbench(cc, m1, m3, m5, m6, m7, stop=stop)
        safe_name = desc.replace(" ", "_").replace("=", "").replace(".", "p")
        tb_path = WORK_DIR / f"tb_{safe_name}.scs"
        tb_path.write_text(tb, encoding="utf-8")

        result = sim.run_simulation(str(tb_path), {})
        if not result.ok:
            print(f"  FAILED: {result.errors[:2]}")
            continue

        metrics = parse_results(result, m3=m3, m5=m5, m7=m7)
        if metrics is None:
            print("  No valid results")
            continue

        gbw_s = fmt_gbw(metrics["gbw"])
        pm_s = f"{metrics['pm']:.1f}" if metrics["pm"] else "N/A"
        pwr_s = fmt_power(metrics["power"])
        g1g_s = f"{metrics['gain_1g']:.1f}" if metrics["gain_1g"] else "N/A"

        print(f"  Gain={metrics['dc_gain']:.1f}dB  "
              f"G@1G={g1g_s}dB  "
              f"GBW={gbw_s}  "
              f"PM={pm_s}°  "
              f"VOUT={metrics['vout_dc']:.3f}V  "
              f"P={pwr_s}")

        results_table.append((desc, cc, m1, m6, m7, metrics))

    # ─ Summary table ──
    print("\n" + "=" * 95)
    print("  Optimization Summary  (all MOS: l=168n nfin=6)")
    print("=" * 95)
    header = (
        f"  {'Config':<22s}  {'Gain':>6s}  {'G@1G':>6s}  {'GBW':>10s}  "
        f"{'PM':>6s}  {'VOUT':>6s}  {'Power':>8s}"
    )
    print(header)
    sep = "  " + "-" * (len(header) - 3)
    print(sep)

    for desc, cc, m1, m6, m7, m in results_table:
        gbw_s = fmt_gbw(m["gbw"])
        pm_s = f"{m['pm']:.1f}" if m["pm"] else "N/A"
        pwr_s = fmt_power(m["power"])
        g1g_s = f"{m['gain_1g']:.1f}" if m["gain_1g"] else "N/A"
        print(f"  {desc:<22s}  {m['dc_gain']:5.1f} dB  {g1g_s:>4s} dB  {gbw_s:>10s}  "
              f"{pm_s:>4s}°  {m['vout_dc']:5.3f}V  {pwr_s:>8s}")

    print("=" * 95)

    # ─ Highlight best configs ──
    if not results_table:
        print("\n  No successful simulations.")
        return 1

    print("\n  ★ Best GBW (with PM > 45°):")
    valid = [r for r in results_table if r[5] and r[5]["pm"] and r[5]["pm"] > 45]
    if valid:
        best = max(valid, key=lambda x: x[5]["gbw"] or 0)
        d, _, _, _, _, m = best
        print(f"    {d}: GBW={fmt_gbw(m['gbw'])}  PM={m['pm']:.1f}°  "
              f"Gain={m['dc_gain']:.1f}dB  VOUT={m['vout_dc']:.3f}V  "
              f"Power={fmt_power(m['power'])}")

    print("\n  ★ Best PM (with GBW > 1 GHz):")
    valid2 = [r for r in results_table if r[5] and r[5]["gbw"] and r[5]["gbw"] > 1e9]
    if valid2:
        best2 = max(valid2, key=lambda x: x[5]["pm"] or 0)
        d, _, _, _, _, m = best2
        print(f"    {d}: PM={m['pm']:.1f}°  GBW={fmt_gbw(m['gbw'])}  "
              f"Gain={m['dc_gain']:.1f}dB  VOUT={m['vout_dc']:.3f}V  "
              f"Power={fmt_power(m['power'])}")

    print("\n  ★ Best VOUT (closest to 0.9V, with GBW > 1 GHz, PM > 60°):")
    valid3 = [
        r for r in results_table
        if r[5] and r[5]["gbw"] and r[5]["gbw"] > 1e9 and r[5]["pm"] and r[5]["pm"] > 60
    ]
    if valid3:
        best3 = min(valid3, key=lambda x: abs(x[5]["vout_dc"] - 0.9))
        d, _, _, _, _, m = best3
        print(f"    {d}: VOUT={m['vout_dc']:.3f}V  GBW={fmt_gbw(m['gbw'])}  "
              f"PM={m['pm']:.1f}°  Gain={m['dc_gain']:.1f}dB  "
              f"Power={fmt_power(m['power'])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
