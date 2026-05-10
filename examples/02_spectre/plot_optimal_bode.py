#!/usr/bin/env python3
"""Generate publication-quality Bode plot for the optimal opamp configuration."""

from __future__ import annotations
import cmath
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = ROOT / "output" / "opamp_two_stage_refine"
AC_FILE = OUT_DIR / "tb_0.3p_m32.raw" / "ac.ac"
PNG_OUT = OUT_DIR / "ac_bode_optimal.png"


def parse_psf_ac(path: Path) -> tuple[list[float], list[complex]]:
    """Parse PSF-ASCII AC data using the project's parser."""
    from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii

    result = parse_spectre_psf_ascii(path)
    d = result.data
    freq = d.get("freq") or d.get("ac_freq") or d.get("ac_time")
    vout = d.get("VOUT") or d.get("ac_VOUT")
    assert freq is not None and vout is not None, f"Missing signals in {list(d.keys())}"

    # Convert to complex
    if isinstance(vout[0], (list, tuple)) and len(vout[0]) == 2:
        vout_complex = [complex(r, i) for r, i in vout]
    elif isinstance(vout[0], complex):
        vout_complex = list(vout)
    elif isinstance(vout[0], float):
        # Flat [real, imag, ...]
        vout_complex = [complex(vout[i], vout[i + 1]) for i in range(0, len(vout), 2)]
    else:
        raise ValueError(f"Unexpected VOUT format: {type(vout[0])}")

    return list(freq), vout_complex


def eng_fmt(value: float, unit: str = "") -> str:
    """Format a number with engineering prefix."""
    if value >= 1e9:
        return f"{value/1e9:.2f} G{unit}"
    elif value >= 1e6:
        return f"{value/1e6:.1f} M{unit}"
    elif value >= 1e3:
        return f"{value/1e3:.1f} k{unit}"
    else:
        return f"{value:.1f} {unit}"


def main():
    freq, vout = parse_psf_ac(AC_FILE)

    # Compute magnitude and phase
    gain_db = [20 * math.log10(abs(v) * 2 + 1e-30) for v in vout]
    phase_deg = [math.degrees(cmath.phase(v)) for v in vout]

    # Find key metrics
    dc_gain = gain_db[0]

    # GBW (0 dB crossover)
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

    # Gain at exactly 1 GHz
    gain_1g = None
    for i, f in enumerate(freq):
        if f >= 1e9:
            gain_1g = gain_db[i]
            break

    print(f"DC Gain : {dc_gain:.1f} dB")
    print(f"GBW     : {eng_fmt(gbw)}Hz")
    print(f"PM      : {pm:.1f} deg")
    print(f"G@1 GHz: {gain_1g:.1f} dB")

    # ---- Plot ----
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(10, 7), gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08}
    )
    fig.patch.set_facecolor("white")

    f_arr = list(freq)

    # Gain plot
    ax1.semilogx(f_arr, gain_db, color="#1f77b4", linewidth=1.5, label="|Gain|")
    ax1.set_xlim(1e0, 5e9)
    ax1.set_ylabel("Gain (dB)", fontsize=11)
    ax1.grid(True, which="both", linestyle="--", alpha=0.4)
    ax1.set_xticklabels([])  # No x labels on top plot

    # 0 dB line
    ax1.axhline(y=0, color="red", linestyle="--", linewidth=0.8, alpha=0.7)
    ax1.axhline(y=dc_gain, color="gray", linestyle=":", linewidth=0.7, alpha=0.6)
    ax1.text(
        1.5, dc_gain + 1.5,
        f"DC Gain = {dc_gain:.1f} dB",
        fontsize=9, color="gray",
    )

    # GBW annotation
    if gbw:
        ax1.axvline(x=gbw, color="orange", linestyle="--", linewidth=0.8, alpha=0.7)
        ax1.text(
            gbw * 1.05, 2,
            f"GBW = {gbw/1e9:.2f} GHz",
            fontsize=9, color="orange", rotation=90, va="bottom",
        )
        # Mark 0 dB crossover point
        ax1.plot(gbw, 0, "o", color="orange", markersize=6)

    # 1 GHz line
    ax1.axvline(x=1e9, color="purple", linestyle=":", linewidth=0.8, alpha=0.6)
    if gain_1g is not None:
        ax1.plot(1e9, gain_1g, "s", color="purple", markersize=5)
        ax1.text(
            1e9 * 0.5, gain_1g - 3,
            f"@1 GHz: {gain_1g:.1f} dB",
            fontsize=8, color="purple", ha="center",
        )

    # Phase plot
    ax2.semilogx(f_arr, phase_deg, color="#ff7f0e", linewidth=1.5, label="Phase")
    ax2.set_xlim(1e0, 5e9)
    ax2.set_xlabel("Frequency (Hz)", fontsize=11)
    ax2.set_ylabel("Phase (deg)", fontsize=11)
    ax2.grid(True, which="both", linestyle="--", alpha=0.4)

    # Phase margin annotation
    if gbw and pm:
        ax2.axvline(x=gbw, color="orange", linestyle="--", linewidth=0.8, alpha=0.7)
        ax2.text(
            gbw * 1.05, -170,
            f"PM = {pm:.1f}\N{DEGREE SIGN}",
            fontsize=9, color="orange", rotation=90, va="bottom",
        )
        # Mark PM point
        log_freqs = [math.log10(f + 1e-30) for f in f_arr]
        log_gbw = math.log10(gbw)
        for i in range(len(log_freqs) - 1):
            if log_freqs[i] <= log_gbw <= log_freqs[i + 1]:
                t = (log_gbw - log_freqs[i]) / (log_freqs[i + 1] - log_freqs[i])
                ph = phase_deg[i] + t * (phase_deg[i + 1] - phase_deg[i])
                ax2.plot(gbw, ph, "o", color="orange", markersize=6)
                ax2.axhline(y=ph, color="orange", linestyle=":", linewidth=0.6, alpha=0.5)
                ax2.text(
                    1.2, ph + 3,
                    f"Phase@GBW = {ph:.1f}\N{DEGREE SIGN}",
                    fontsize=8, color="orange",
                )
                break

    # X-axis formatting with engineering notation
    def eng_xticks(ax, ticks):
        labels = []
        for t in ticks:
            if t >= 1e9:
                labels.append(f"{t/1e9:.0f}G")
            elif t >= 1e6:
                labels.append(f"{t/1e6:.0f}M")
            elif t >= 1e3:
                labels.append(f"{t/1e3:.0f}k")
            else:
                labels.append(f"{t:.0f}")
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)

    eng_xticks(ax2, [1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 5e9])
    eng_xticks(ax1, [1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 5e9])

    # Title
    config_text = (
        "Two-Stage Opamp  |  Cc = 0.3 pF  |  M1/M2: m=32  |  M6/M7: m=6/8  |  L = 168 nm  nfin = 6"
    )
    fig.suptitle(config_text, fontsize=11, fontweight="bold", y=0.995)

    plt.savefig(str(PNG_OUT), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"\nSaved: {PNG_OUT}")


if __name__ == "__main__":
    raise SystemExit(main())
