#!/usr/bin/env python3
"""Parse both REF and RCE post-simulation results."""
import sys
from pathlib import Path
import math, cmath

sys.path.insert(0, str(Path(__file__).parent.parent))

from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii

def parse_results(raw_dir, label):
    ac_path = Path(raw_dir) / "output.raw" / "ac_ac.ac"
    dc_path = Path(raw_dir) / "output.raw" / "dcOp.dc"

    results = {"label": label}

    if ac_path.exists():
        ac_data = parse_spectre_psf_ascii(ac_path)
        d = ac_data.data
        freq = d.get("freq", [])
        vout_complex = d.get("VOUT", [])

        if freq and len(vout_complex) > 0:
            gain_db = [20 * math.log10(abs(v) + 1e-30) for v in vout_complex]
            phase_deg = [math.degrees(cmath.phase(v)) for v in vout_complex]

            results["dc_gain"] = gain_db[0]
            results["gain_db"] = gain_db
            results["phase_deg"] = phase_deg
            results["freq"] = freq

            # GBW
            gbw = None
            for i in range(len(gain_db) - 1):
                if gain_db[i] >= 0 and gain_db[i+1] < 0:
                    f1, f2 = freq[i], freq[i+1]
                    g1, g2 = gain_db[i], gain_db[i+1]
                    log_cross = math.log10(f1) + (math.log10(f2) - math.log10(f1)) * (-g1) / (g2 - g1)
                    gbw = 10 ** log_cross
                    break
            results["gbw"] = gbw

            # PM
            if gbw:
                log_gbw = math.log10(gbw)
                log_freqs = [math.log10(f + 1e-30) for f in freq]
                for i in range(len(log_freqs) - 1):
                    if log_freqs[i] <= log_gbw <= log_freqs[i+1]:
                        t = (log_gbw - log_freqs[i]) / (log_freqs[i+1] - log_freqs[i])
                        ph = phase_deg[i] + t * (phase_deg[i+1] - phase_deg[i])
                        results["pm"] = 180 + ph
                        break

    if dc_path.exists():
        dc_data = parse_spectre_psf_ascii(dc_path)
        raw_vout = dc_data.data.get("VOUT", [])
        if isinstance(raw_vout, list) and len(raw_vout) > 0:
            results["vout_dc"] = raw_vout[0]

    return results

results_ref = parse_results("output_ref.raw", "REF")
results_rce = parse_results("output_rce.raw", "RCE")

print("="*80)
print("📊 后仿真结果汇总")
print("="*80)
print(f"{'指标':<20} {'前仿真':<15} {'REF 后仿真':<15} {'RCE 后仿真':<15}")
print("-"*80)
print(f"{'DC 增益 (dB)':<20} {'45.65':<15} "
      f"{results_ref.get('dc_gain', 'N/A')!s:<15} "
      f"{results_rce.get('dc_gain', 'N/A')!s:<15}")

gbw_ref = results_ref.get('gbw')
gbw_rce = results_rce.get('gbw')
print(f"{'GBW (MHz)':<20} {'201.72':<15} "
      f"{'{:.2f}'.format(gbw_ref/1e6) if gbw_ref else 'N/A':<15} "
      f"{'{:.2f}'.format(gbw_rce/1e6) if gbw_rce else 'N/A':<15}")

pm_ref = results_ref.get('pm')
pm_rce = results_rce.get('pm')
print(f"{'相位裕度 (°)':<20} {'-':<15} "
      f"{'{:.1f}'.format(pm_ref) if pm_ref else 'N/A':<15} "
      f"{'{:.1f}'.format(pm_rce) if pm_rce else 'N/A':<15}")

vout_ref = results_ref.get('vout_dc')
vout_rce = results_rce.get('vout_dc')
print(f"{'VOUT DC (V)':<20} {'0.000':<15} "
      f"{'{:.4f}'.format(vout_ref) if vout_ref else 'N/A':<15} "
      f"{'{:.4f}'.format(vout_rce) if vout_rce else 'N/A':<15}")
print("="*80)

# Generate comparison Bode plot
if results_ref.get("freq") and results_rce.get("freq"):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8),
            gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08})

        ax1.semilogx(results_ref["freq"], results_ref["gain_db"], linewidth=1.5, color='blue', label='REF')
        ax1.semilogx(results_rce["freq"], results_rce["gain_db"], linewidth=1.5, color='red', label='RCE')
        ax1.set_ylabel("Gain (dB)", fontsize=12)
        ax1.axhline(y=0, color="black", linestyle="--", linewidth=0.5)
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc='upper right')
        ax1.set_title("Post-layout AC Analysis Comparison (REF vs RCE)", fontsize=14)

        ax2.semilogx(results_ref["freq"], results_ref["phase_deg"], color='blue', linewidth=1.5, label='REF')
        ax2.semilogx(results_rce["freq"], results_rce["phase_deg"], color='red', linewidth=1.5, label='RCE')
        ax2.set_xlabel("Frequency (Hz)", fontsize=12)
        ax2.set_ylabel("Phase (deg)", fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.legend(loc='lower right')

        bode_path = Path("output/opamp_comparison_bode.png")
        plt.savefig(bode_path, dpi=200, bbox_inches="tight")
        print(f"\n✅ 对比 Bode 图已保存: {bode_path}")
    except Exception as e:
        print(f"\n⚠️  对比图生成失败: {e}")
