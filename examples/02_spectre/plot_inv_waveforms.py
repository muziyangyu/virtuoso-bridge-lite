#!/usr/bin/env python3
"""Plot inverter waveforms and calculate performance metrics."""

from pathlib import Path
import sys
import numpy as np

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib not found, installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

# Parse PSF ASCII data
def parse_psf_ascii(filepath):
    """Parse Spectre PSF ASCII output file."""
    data = {}
    current_signal = None
    values = []

    with open(filepath, 'r') as f:
        lines = f.readlines()

    in_header = True
    signal_names = []

    for i, line in enumerate(lines):
        line = line.strip()

        if line.startswith('#INDICES') or line.startswith('#VALUES'):
            in_header = False
            continue

        if in_header and line.startswith('NAME'):
            parts = line.split()
            if len(parts) > 1:
                signal_names.append(parts[1])

        if not in_header and line and not line.startswith('#'):
            try:
                val = float(line)
                values.append(val)
            except ValueError:
                pass

    # Reformat: time + N signals
    n_signals = len(signal_names)
    n_points = len(values) // (n_signals + 1)

    array_data = np.array(values[:n_points * (n_signals + 1)]).reshape(-1, n_signals + 1)

    # Time is first column
    data['time'] = array_data[:, 0]
    for i, name in enumerate(signal_names):
        data[name] = array_data[:, i + 1]

    return data


def calculate_metrics(time, vin, vout, vdd_val=1.2):
    """Calculate inverter performance metrics."""
    metrics = {}
    v_half = vdd_val / 2

    # Output high/low levels
    metrics['voh'] = np.max(vout)
    metrics['vol'] = np.min(vout)

    # Find rising and falling edges
    # Find where VIN crosses v_half (falling edge)
    vin_falling_idx = np.where(np.diff(np.sign(vin - v_half)) < 0)[0]
    vin_rising_idx = np.where(np.diff(np.sign(vin - v_half)) > 0)[0]

    # VOUT response
    if len(vin_falling_idx) > 0:
        # VIN falling -> VOUT rising
        t_start = time[vin_falling_idx[0]]
        vout_rising = vout[vin_falling_idx[0]:]
        time_rising = time[vin_falling_idx[0]:]

        # Rise time: 20% to 80% of VDD
        v_20 = 0.2 * vdd_val
        v_80 = 0.8 * vdd_val

        idx_20 = np.where(vout_rising > v_20)[0]
        idx_80 = np.where(vout_rising > v_80)[0]

        if len(idx_20) > 0 and len(idx_80) > 0:
            t_20 = time_rising[idx_20[0]]
            t_80 = time_rising[idx_80[0]]
            metrics['rise_time'] = (t_80 - t_20) * 1e12  # ps

    if len(vin_rising_idx) > 0:
        # VIN rising -> VOUT falling
        t_start = time[vin_rising_idx[0]]
        vout_falling = vout[vin_rising_idx[0]:]
        time_falling = time[vin_rising_idx[0]:]

        # Fall time: 80% to 20% of VDD
        v_20 = 0.2 * vdd_val
        v_80 = 0.8 * vdd_val

        idx_80 = np.where(vout_falling < v_80)[0]
        idx_20 = np.where(vout_falling < v_20)[0]

        if len(idx_80) > 0 and len(idx_20) > 0:
            t_80 = time_falling[idx_80[0]]
            t_20 = time_falling[idx_20[0]]
            metrics['fall_time'] = (t_20 - t_80) * 1e12  # ps

    # Propagation delay: VIN 50% to VOUT 50%
    if len(vin_rising_idx) > 0 and len(vin_falling_idx) > 0:
        # VIN rising to VOUT falling
        t_vin_50_rise = time[vin_rising_idx[0]]

        # Find where VOUT crosses v_half (falling)
        vout_fall_start_idx = vin_rising_idx[0]
        vout_after = vout[vout_fall_start_idx:]
        time_after = time[vout_fall_start_idx:]

        cross_idx = np.where(np.diff(np.sign(vout_after - v_half)) != 0)[0]
        if len(cross_idx) > 0:
            t_vout_50 = time_after[cross_idx[0]]
            metrics['tp_hl'] = (t_vout_50 - t_vin_50_rise) * 1e12  # ps

        # VIN falling to VOUT rising
        if len(vin_falling_idx) > 0:
            t_vin_50_fall = time[vin_falling_idx[0]]

            vout_rise_start_idx = vin_falling_idx[0]
            vout_after_rise = vout[vout_rise_start_idx:]
            time_after_rise = time[vout_rise_start_idx:]

            cross_idx_rise = np.where(np.diff(np.sign(vout_after_rise - v_half)) != 0)[0]
            if len(cross_idx_rise) > 0:
                t_vout_50_rise = time_after_rise[cross_idx_rise[0]]
                metrics['tp_lh'] = (t_vout_50_rise - t_vin_50_fall) * 1e12  # ps

    return metrics


def main():
    output_dir = Path('examples/02_spectre/output/work_ai_inv')
    raw_dir = output_dir / 'tb_inv_run.raw'

    if not raw_dir.exists():
        print(f"ERROR: {raw_dir} not found!")
        return 1

    print(f"Parsing {raw_dir}...")
    from virtuoso_bridge.spectre.parsers import parse_psf_ascii_directory
    data = parse_psf_ascii_directory(raw_dir)

    # Convert to numpy arrays
    time_ns = np.array(data['time']) * 1e9
    vin = np.array(data['VIN'])
    vout = np.array(data['VOUT'])

    # Plot waveforms
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    axes[0].plot(time_ns, vin, 'b-', linewidth=2, label='VIN')
    axes[0].set_ylabel('Voltage (V)')
    axes[0].set_title('Inverter Transient Response')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim(-0.1, 1.3)

    axes[1].plot(time_ns, vout, 'r-', linewidth=2, label='VOUT')
    axes[1].set_xlabel('Time (ns)')
    axes[1].set_ylabel('Voltage (V)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim(-0.1, 1.3)

    plt.tight_layout()
    plot_path = output_dir / 'inv_waveforms.png'
    plt.savefig(plot_path, dpi=150)
    print(f"\nWaveform plot saved to: {plot_path}")

    # Calculate and print metrics
    metrics = calculate_metrics(data['time'], vin, vout)

    print("\n" + "="*50)
    print("INVERTER PERFORMANCE METRICS")
    print("="*50)
    print(f"VDD: {1.2} V")
    print(f"Output High (VOH): {metrics.get('voh', 0):.4f} V")
    print(f"Output Low (VOL): {metrics.get('vol', 0):.4f} V")
    print(f"Output Swing: {metrics.get('voh', 0) - metrics.get('vol', 0):.4f} V")
    print()

    if 'rise_time' in metrics:
        print(f"Rise Time (20-80%): {metrics['rise_time']:.1f} ps")
    if 'fall_time' in metrics:
        print(f"Fall Time (80-20%): {metrics['fall_time']:.1f} ps")
    if 'tp_hl' in metrics:
        print(f"Propagation Delay TP_HL: {metrics['tp_hl']:.1f} ps")
    if 'tp_lh' in metrics:
        print(f"Propagation Delay TP_LH: {metrics['tp_lh']:.1f} ps")
    if 'tp_hl' in metrics and 'tp_lh' in metrics:
        avg_tp = (metrics['tp_hl'] + metrics['tp_lh']) / 2
        print(f"Average Propagation Delay: {avg_tp:.1f} ps")
    print("="*50)

    # Save metrics to JSON
    import json
    metrics_path = output_dir / 'metrics.json'
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"\nMetrics saved to: {metrics_path}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
