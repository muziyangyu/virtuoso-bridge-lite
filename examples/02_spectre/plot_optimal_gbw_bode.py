#!/usr/bin/env python3
"""Generate Bode plot for the optimal GBW configuration (Cc=0.08p)."""

from __future__ import annotations
import cmath
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = ROOT / "output" / "opamp_optimize_168n"
AC_FILE = OUT_DIR / "tb_Cc0p08p_max.raw" / "ac.ac"
PNG_OUT = OUT_DIR / "ac_bode_0.08p.png"

# Optimal config params
CONFIG_DESC = (
    "Two-Stage Opamp  |  Cc = 0.08 pF  |  M1/M2: m=64  |  M6/M7: m=10/14  |  L = 168 nm  nfin = 6"
)


def parse_psf_ac(path: Path) -> tuple[list[float], list[complex]]:
    from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii
    result = parse_spectre_psf_ascii(path)
    d = result.data
    freq = d.get("freq") or d.get("ac_freq")
    vout = d.get("VOUT") or d.get("ac_VOUT")
    assert freq is not None and vout is not None
    if isinstance(vout[0], (list, tuple)) and len(vout[0]) == 2:
        vout_complex = [complex(r, i) for r, i in vout]
    elif isinstance(vout[0], complex):
        vout_complex = list(vout)
    else:
        vout_complex = [complex(vout[i], vout[i + 1]) for i in range(0, len(vout), 2)]
    return list(freq), vout_complex


def main():
    freq, vout = parse_psf_ac(AC_FILE)
    gain_db = [20 * math.log10(abs(v) * 2 + 1e-30) for v in vout]
    phase_deg = [math.degrees(cmath.phase(v)) for v in vout]

    dc_gain = gain_db[0]

    # GBW
    gbw = None
    for i in range(len(gain_db) - 1):
        if gain_db[i] >= 0 and gain_db[i + 1] < 0:
            f1, f2 = freq[i], freq[i + 1]
            g1, g2 = gain_db[i], gain_db[i + 1]
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
                ph = phase_deg[i] + t * (phase_deg[i + 1] - phase_deg[i])
                pm = 180 + ph
                break

    # Gain at 1 GHz
    gain_1g = None
    for i, f in enumerate(freq):
        if f >= 1e9:
            gain_1g = gain_db[i]
            break

    print(f"DC Gain : {dc_gain:.1f} dB")
    print(f"GBW     : {gbw/1e9:.2f} GHz")
    print(f"PM      : {pm:.1f} deg")
    print(f"G@1 GHz: {gain_1g:.1f} dB")

    # ── Plot ─
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(10, 7), gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08}
    )
    fig.patch.set_facecolor("white")
    f_arr = list(freq)

    # Gain
    ax1.semilogx(f_arr, gain_db, color="#1f77b4", linewidth=1.5)
    ax1.set_xlim(1e0, 5e9)
    ax1.set_ylabel("Gain (dB)", fontsize=11)
    ax1.grid(True, which="both", linestyle="--", alpha=0.4)
    ax1.set_xticklabels([])

    # 0 dB line
    ax1.axhline(y=0, color="red", linestyle="--", linewidth=0.8, alpha=0.7)
    ax1.axhline(y=dc_gain, color="gray", linestyle=":", linewidth=0.7, alpha=0.6)
    ax1.text(1.5, dc_gain + 1.5, f"DC Gain = {dc_gain:.1f} dB", fontsize=9, color="gray")

    # GBW
    if gbw:
        ax1.axvline(x=gbw, color="orange", linestyle="--", linewidth=0.8, alpha=0.7)
        ax1.text(gbw * 1.05, 2, f"GBW = {gbw/1e9:.2f} GHz", fontsize=9, color="orange",
                 rotation=90, va="bottom")
        ax1.plot(gbw, 0, "o", color="orange", markersize=6)

    # 1 GHz
    ax1.axvline(x=1e9, color="purple", linestyle=":", linewidth=0.8, alpha=0.6)
    if gain_1g is not None:
        ax1.plot(1e9, gain_1g, "s", color="purple", markersize=5)
        ax1.text(1e9 * 0.5, gain_1g - 3, f"@1 GHz: {gain_1g:.1f} dB", fontsize=8,
                 color="purple", ha="center")

    # Phase
    ax2.semilogx(f_arr, phase_deg, color="#ff7f0e", linewidth=1.5)
    ax2.set_xlim(1e0, 5e9)
    ax2.set_xlabel("Frequency (Hz)", fontsize=11)
    ax2.set_ylabel("Phase (deg)", fontsize=11)
    ax2.grid(True, which="both", linestyle="--", alpha=0.4)

    # Phase margin
    if gbw and pm:
        ax2.axvline(x=gbw, color="orange", linestyle="--", linewidth=0.8, alpha=0.7)
        ax2.text(gbw * 1.05, -150, f"PM = {pm:.1f}\N{DEGREE SIGN}", fontsize=9,
                 color="orange", rotation=90, va="bottom")
        log_freqs = [math.log10(f + 1e-30) for f in f_arr]
        log_gbw = math.log10(gbw)
        for i in range(len(log_freqs) - 1):
            if log_freqs[i] <= log_gbw <= log_freqs[i + 1]:
                t = (log_gbw - log_freqs[i]) / (log_freqs[i + 1] - log_freqs[i])
                ph = phase_deg[i] + t * (phase_deg[i + 1] - phase_deg[i])
                ax2.plot(gbw, ph, "o", color="orange", markersize=6)
                break

    # X-axis ticks
    ticks = [1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 5e9]
    labels = ["1", "100", "1k", "10k", "100k", "1M", "10M", "100M", "1G", "5G"]
    for ax in (ax1, ax2):
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)

    fig.suptitle(CONFIG_DESC, fontsize=11, fontweight="bold", y=0.995)
    plt.savefig(str(PNG_OUT), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"\nSaved: {PNG_OUT}")


if __name__ == "__main__":
    raise SystemExit(main())
