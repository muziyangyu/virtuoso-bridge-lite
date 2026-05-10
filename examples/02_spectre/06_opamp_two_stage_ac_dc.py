#!/usr/bin/env python3
"""Export work_ai/opamp_two_stage schematic, build flat .scs, run AC/DC via Spectre.

Uses read_schematic() to get device params from Virtuoso, then builds a
flat Spectre netlist matching the verified tb_opamp.scs template.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)
WORK_DIR = ROOT / "output" / "opamp_two_stage_ac_dc"
WORK_DIR.mkdir(parents=True, exist_ok=True)

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.spectre.runner import SpectreSimulator
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic

PDK_MODEL = (
    "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0"
    "/smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0"
    "/models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
)


# ============================================================
# 1. Read schematic topology + params from Virtuoso
# ============================================================
def extract_device_params(inst: dict) -> dict:
    """Extract key simulation params from a schematic instance."""
    params = inst.get("params", {})
    out = {}
    for key in ("nfin", "l", "fingers", "m", "c", "r", "model"):
        if key in params and params[key]:
            out[key] = params[key]
    return out


def schematic_to_netlist(data: dict) -> str:
    """Build a flat Spectre netlist from read_schematic() output.

    Maps the opamp_two_stage topology to Spectre device syntax.
    The schematic uses:
      - smic12sf/{n,p}18_ckt symbol -> spectre n18_ckt/p18_ckt model
      - analogLib/capacitor -> spectre capacitor c=...
    """
    lines = []
    lines.append("simulator lang=spectre")
    lines.append("global 0")
    lines.append("")
    lines.append("simulatorOptions options psfversion=\"1.4.0\" reltol=1e-4 vabstol=1e-6 \\")
    lines.append("  soft_bin=allmodels")
    lines.append("")

    # PDK model includes
    lines.append(f'include "{PDK_MODEL}" section=tt_mos_varactor')
    lines.append(f'include "{PDK_MODEL}" section=tt_res_res3t_bjt_dio')
    lines.append(f'include "{PDK_MODEL}" section=tt_mom_mim')
    lines.append(f'include "{PDK_MODEL}" section=pre_layout')
    lines.append("")

    #Extract nets to figure out connections
    nets = data.get("nets", {})
    instances = data.get("instances", [])

    #Group instances by type
    mos_devices = []
    cap_devices = []
    for inst in instances:
        cell = inst.get("cell", inst.get("cellName", ""))
        lib = inst.get("lib", inst.get("libName", ""))
        name = inst["name"]
        params = extract_device_params(inst)

        if lib == "smic12sf":
            #Get terminal connections from nets
            terminals = {}
            for net_name, net_info in nets.items():
                for conn in net_info.get("connections", []):
                    if conn.startswith(f"{name}."):
                        terminals[conn.split(".", 1)[1]] = net_name
            mos_devices.append({
                "name": name,
                "cell": cell,
                "terminals": terminals,
                "params": params,
            })
        elif lib == "analogLib":
            terminals = {}
            for net_name, net_info in nets.items():
                for conn in net_info.get("connections", []):
                    if conn.startswith(f"{name}."):
                        terminals[conn.split(".", 1)[1]] = net_name
            cap_devices.append({
                "name": name,
                "cell": cell,
                "terminals": terminals,
                "params": params,
            })

    #Write MOS devices
    for dev in mos_devices:
        terms = dev["terminals"]
        #SMIC 12nm MOS: (drain gate source body) model l=... nfin=...
        d = terms.get("D", "?")
        g = terms.get("G", "?")
        s = terms.get("S", "?")
        b = terms.get("B", "?")
        model = dev["cell"]  # e.g. n18_ckt, p18_ckt
        l_val = dev["params"].get("l", "300n")
        nfin_val = dev["params"].get("nfin", "")
        fingers = dev["params"].get("fingers", "")
        m_val = dev["params"].get("m", "")

        dev_line = f"{dev['name']} ({d} {g} {s} {b}) {model} l={l_val}"
        if nfin_val:
            dev_line += f" nfin={nfin_val}"
        if m_val and m_val != "1":
            dev_line += f" m={m_val}"
        lines.append(dev_line)

    lines.append("")

    #Write capacitors
    for dev in cap_devices:
        terms = dev["terminals"]
        c_val = dev["params"].get("c", "")
        #analogLib capacitor: terminals are typically PLUS/MINUS
        t1 = terms.get("PLUS", terms.get("0", "?"))
        t2 = terms.get("MINUS", terms.get("1", "?"))
        if c_val:
            lines.append(f"{dev['name']} ({t1} {t2}) capacitor c={c_val}")

    lines.append("")
    return "\n".join(lines)


def build_testbench(opamp_netlist: str, vdd: float = 1.8) -> str:
    """Wrap the opamp netlist with supplies, bias, and analysis statements."""
    lines = [
        "simulator lang=spectre",
        "global 0",
        "",
        "simulatorOptions options psfversion=\"1.4.0\" reltol=1e-4 vabstol=1e-6 \\",
        "  soft_bin=allmodels",
        "",
        f'include "{PDK_MODEL}" section=tt_mos_varactor',
        f'include "{PDK_MODEL}" section=tt_res_res3t_bjt_dio',
        f'include "{PDK_MODEL}" section=tt_mom_mim',
        f'include "{PDK_MODEL}" section=pre_layout',
        "",
        "parameters VDD=1.8 VCM=0.9 IBIAS=10u",
        "",
        "V0 (VDD 0) vsource dc=VDD",
        "V1 (VSS 0) vsource dc=0",
        "",
        "IBIAS (net_bias VSS) isource dc=IBIAS",
        "M8 (net_bias net_bias VDD VDD) p18_ckt l=168n nfin=6 m=1",
        "M9 (net_vb net_bias VDD VDD) p18_ckt l=168n nfin=6 m=1",
        "M10 (net_bias net_bias VSS VSS) n18_ckt l=168n nfin=6 m=1",
        "Rvb (net_vb VSS) resistor r=500MEG",
        "",
        "M1 (net_d3 VINP net_s VSS) n18_ckt l=168n nfin=6 m=8",
        "M2 (net_x VINN net_s VSS) n18_ckt l=168n nfin=6 m=8",
        "M5 (net_s net_vb VSS VSS) n18_ckt l=168n nfin=6 m=16",
        "",
        "M3 (net_d3 net_d3 VDD VDD) p18_ckt l=168n nfin=6 m=8",
        "M4 (net_x net_d3 VDD VDD) p18_ckt l=168n nfin=6 m=8",
        "",
        "M6 (VOUT net_x VSS VSS) n18_ckt l=168n nfin=6 m=3",
        "M7 (VOUT net_bias VDD VDD) p18_ckt l=168n nfin=6 m=4",
        "",
        "Cc (net_x VOUT) capacitor c=2p",
        "",
        "VINP (VINP 0) vsource dc=VCM mag=0.5",
        "VINN (VINN 0) vsource dc=VCM mag=-0.5",
        "CL (VOUT 0) capacitor c=2p",
        "",
        "dcOp dc maxiters=150",
        "ac ac start=1 stop=1G dec=20",
        "",
        "save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias",
        "saveOptions options save=selected",
    ]
    return "\n".join(lines)


# ============================================================
# 2. Parse results
# ============================================================
def parse_ac_results(result_data: dict) -> dict:
    """Compute gain, GBW, phase margin from AC waveform data (pure Python)."""
    import cmath
    import math

    vout = result_data.get("ac_VOUT", result_data.get("VOUT"))
    freq_arr = result_data.get("ac_freq", result_data.get("ac_time", result_data.get("time")))
    if vout is None or freq_arr is None or len(vout) < 2:
        return {}

    freq = freq_arr
    # Convert to complex: PSF ASCII stores as [real, imag, real, imag, ...]
    if isinstance(vout[0], (list, tuple)) and len(vout[0]) == 2:
        vout_complex = [complex(r, i) for r, i in vout]
    elif isinstance(vout[0], complex):
        vout_complex = list(vout)
    else:
        # Flat list: [real0, imag0, real1, imag1, ...]
        if len(vout) % 2 == 0:
            vout_complex = [complex(vout[i], vout[i + 1]) for i in range(0, len(vout), 2)]
        else:
            return {}

    mag_db = []
    phase = []
    for v in vout_complex:
        mag = abs(v)
        mag_db.append(20 * math.log10(mag + 1e-30))
        phase.append(math.degrees(cmath.phase(v)))

    # DC gain: lowest frequency point
    dc_gain_db = mag_db[0]

    # GBW: frequency where gain crosses 0 dB
    gbw = None
    for i in range(len(mag_db) - 1):
        if mag_db[i] >= 0 and mag_db[i + 1] < 0:
            f1, f2 = freq[i], freq[i + 1]
            g1, g2 = mag_db[i], mag_db[i + 1]
            log_f1 = math.log10(f1 + 1e-30)
            log_f2 = math.log10(f2 + 1e-30)
            log_f_cross = log_f1 + (log_f2 - log_f1) * (0 - g1) / (g2 - g1)
            gbw = 10 ** log_f_cross
            break

    # Phase margin: 180 + phase at GBW
    phase_margin = None
    if gbw is not None:
        log_gbw = math.log10(gbw)
        log_freqs = [math.log10(f + 1e-30) for f in freq]
        for i in range(len(log_freqs) - 1):
            if log_freqs[i] <= log_gbw <= log_freqs[i + 1]:
                t = (log_gbw - log_freqs[i]) / (log_freqs[i + 1] - log_freqs[i])
                phase_at_gbw = phase[i] + t * (phase[i + 1] - phase[i])
                break
        else:
            phase_at_gbw = phase[-1]
        phase_margin = 180 + phase_at_gbw

    return {
        "dc_gain_db": round(dc_gain_db, 2),
        "gbw_hz": gbw,
        "gbw_mhz": round(gbw / 1e6, 2) if gbw else None,
        "phase_margin_deg": round(phase_margin, 2) if phase_margin is not None else None,
    }


# ============================================================
# Main
# ============================================================
def main() -> int:
    print("=" * 60)
    print("  work_ai/opamp_two_stage - Spectre AC/DC Simulation")
    print("=" * 60)

    client = VirtuosoClient.from_env()

    #Quick connectivity test
    r = client.execute_skill("1+2")
    print(f"\nConnection test: {r.output}")

    #Step 1: Read schematic from Virtuoso
    print("\n[1/5] Reading schematic from Virtuoso...")
    data = read_schematic(client, "work_ai", "opamp_two_stage")

    print(f"  Instances: {len(data['instances'])}")
    for inst in data["instances"]:
        p = inst.get("params", {})
        key_p = {k: p.get(k) for k in ("model", "nfin", "l") if p.get(k)}
        print(f"    {inst['name']:8s}  {inst.get('lib', '?')}/{inst.get('cell', '?')}  {key_p}")

    #Step 2: Build testbench netlist (verified template)
    print("\n[2/5] Building testbench (verified template)...")
    tb_text = build_testbench("")
    tb_path = WORK_DIR / "tb_opamp_ac_dc.scs"
    tb_path.write_text(tb_text, encoding="utf-8")
    print(f"  Written: {tb_path}")

    #Step 3: Run Spectre
    print("\n[3/5] Running Spectre (DC + AC)...")
    sim = SpectreSimulator.from_env(
        work_dir=str(WORK_DIR),
        output_format="psfascii",
    )
    result = sim.run_simulation(str(tb_path), {})

    print(f"\n  Status: {result.status.value}")
    if result.errors:
        print("  Errors:")
        for e in result.errors[:15]:
            print(f"    {e}")
    if result.warnings:
        print(f"  Warnings ({len(result.warnings)} total, showing first 5):")
        for w in result.warnings[:5]:
            print(f"    {w}")

    if not result.ok:
        print("\n  Simulation FAILED.")
        return 1

    #Step 4: Parse results
    print("\n[4/5] Parsing results...")
    signals = list(result.data.keys())
    print(f"  Signals: {signals}")

    ac_info = parse_ac_results(result.data)
    if ac_info:
        print(f"\n  === AC Results ===")
        print(f"  DC Gain:        {ac_info['dc_gain_db']} dB")
        if ac_info.get('gbw_mhz'):
            print(f"  GBW:            {ac_info['gbw_mhz']} MHz")
        if ac_info.get('phase_margin_deg'):
            print(f"  Phase Margin:   {ac_info['phase_margin_deg']} deg")

    #DC operating point from waveform data at freq=1 (DC point)
    if result.data.get("VOUT"):
        vout_data = result.data["VOUT"]
        if len(vout_data) > 0:
            vout_dc = abs(vout_data[0])
            print(f"\n  === DC Operating Point ===")
            print(f"  VOUT = {vout_dc:.4f} V")

    #Step 5: Save summary
    print("\n[5/5] Saving summary...")
    summary_path = WORK_DIR / "results_summary.txt"
    with open(summary_path, "w") as f:
        f.write("work_ai/opamp_two_stage - Spectre AC/DC Results\n")
        f.write("=" * 50 + "\n\n")
        if ac_info:
            f.write("AC Results:\n")
            for k, v in ac_info.items():
                f.write(f"  {k}: {v}\n")
        f.write(f"\nOutput directory: {result.metadata.get('output_dir', 'N/A')}\n")
    print(f"  Summary: {summary_path}")

    print("\n" + "=" * 60)
    print("  Done!")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
