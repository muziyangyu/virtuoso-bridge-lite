#!/usr/bin/env python3
"""Sweep opamp parameters to target 1 GHz GBW.

Strategy: GBW ≈ gm1/(2π*Cc)
- Reduce Cc to increase GBW
- Increase M1/M2 transconductance via m
- Adjust M6/M7 ratio for DC operating point
"""

from __future__ import annotations
import os
import sys
import math
import cmath
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)
WORK_DIR = ROOT / "output" / "opamp_two_stage_sweep"
WORK_DIR.mkdir(parents=True, exist_ok=True)

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.spectre.runner import SpectreSimulator

PDK_MODEL = (
    "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0"
    "/smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0"
    "/models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
)


def build_testbench(cc, m1, m5, m3, m6, m7):
    """Build testbench with configurable parameters."""
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
ac ac start=1 stop=1G dec=20

save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias
saveOptions options save=selected
'''


def parse_results(result):
    """Extract key metrics from simulation results."""
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

    # Phase margin at GBW
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

    return {
        "dc_gain": dc_gain,
        "gbw": gbw,
        "pm": pm,
        "vout_dc": dc_vout,
    }


def main():
    print("=" * 70)
    print("  Opamp Parameter Sweep for 1 GHz GBW")
    print("=" * 70)

    client = VirtuosoClient.from_env()
    r = client.execute_skill("1+2")
    print(f"\nConnected: {r.output}")

    sim = SpectreSimulator.from_env(
        work_dir=str(WORK_DIR),
        output_format="psfascii",
    )

    configs = [
        # (Cc,   m1, m5, m3, m6, m7, desc)
        ("1p",   16, 32, 16,  6,  8, "Cc=1p 2x gm"),
        ("0.5p", 16, 32, 16,  6,  8, "Cc=0.5p 2x gm"),
        ("0.5p", 32, 64, 32,  6,  8, "Cc=0.5p 4x gm"),
        ("0.5p", 32, 64, 32, 10, 14, "Cc=0.5p 4x gm rebal"),
        ("0.5p", 48, 96, 48, 10, 14, "Cc=0.5p 6x gm"),
        ("0.3p", 48, 96, 48, 10, 14, "Cc=0.3p 6x gm"),
        ("0.2p", 48, 96, 48, 10, 14, "Cc=0.2p 6x gm"),
        ("0.1p", 64, 128, 64, 10, 14, "Cc=0.1p 8x gm"),
        ("0.1p", 64, 128, 64,  8, 12, "Cc=0.1p 8x gm rebal"),
    ]

    results_table = []
    for cc, m1, m5, m3, m6, m7, desc in configs:
        print(f"\n[{desc}]")
        tb = build_testbench(cc, m1, m5, m3, m6, m7)
        tb_path = WORK_DIR / f"tb_{desc.replace(' ', '_').replace('.', 'p')}.scs"
        tb_path.write_text(tb, encoding="utf-8")

        result = sim.run_simulation(str(tb_path), {})
        if not result.ok:
            print(f"  FAILED: {result.errors[:3]}")
            continue

        metrics = parse_results(result)
        if metrics:
            gbw_str = f"{metrics['gbw']/1e6:.1f} MHz" if metrics['gbw'] else ">1G"
            pm_str = f"{metrics['pm']:.1f} deg" if metrics['pm'] else "N/A"
            print(f"  Gain: {metrics['dc_gain']:.1f} dB  "
                  f"GBW: {gbw_str}  "
                  f"PM: {pm_str}  "
                  f"VOUT: {metrics['vout_dc']:.3f} V")
            results_table.append((desc, metrics))

    # Summary
    print("\n" + "=" * 70)
    print("  Sweep Summary")
    print("=" * 70)
    print(f"  {'Config':<25s}  {'Gain':>7s}  {'GBW':>8s}  {'PM':>7s}  {'VOUT':>6s}")
    print("  " + "-" * 60)
    for desc, m in results_table:
        gbw_str = f"{m['gbw']/1e6:.1f} MHz" if m['gbw'] else "N/A"
        pm_str = f"{m['pm']:.1f}" if m['pm'] else "N/A"
        print(f"  {desc:<25s}  {m['dc_gain']:6.1f} dB  {gbw_str:>8s}  "
              f"{pm_str:>5s} deg  {m['vout_dc']:5.3f} V")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
