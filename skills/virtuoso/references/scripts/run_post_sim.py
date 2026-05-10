#!/usr/bin/env python3
"""
Run post-layout simulation for both RCE and REF DSPF files.
Both use port order: VINP VSS VDD VINN VOUT
"""
import sys
from datetime import datetime
from pathlib import Path
import subprocess

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

PDK_MODEL = (
    "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0/"
    "smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0/"
    "models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
)

host = "172.17.8.14"
user = "lixiang"

def run_post_sim(dspf_file, label):
    """Run post-layout simulation for a given DSPF file."""
    print(f"\n{'='*60}")
    print(f"后仿真: {label} ({dspf_file})")
    print(f"{'='*60}")

    dspf_path = Path(dspf_file)
    if not dspf_path.exists():
        print(f"❌ DSPF 文件不存在: {dspf_path}")
        return None

    remote_work_dir = f"/tmp/virtuoso_bridge_lixiang/post_sim_{label}_{TIMESTAMP}"

    # 创建测试平台
    netlist = f"""simulator lang=spectre
global 0

simulatorOptions options reltol=1e-4 vabstol=1e-6 \\
    iabstol=1e-12 temp=25 \\
    tstab=1n method=gear2only \\
    gmin=1e-12 gmin_step=10 \\
    soft_bin=allmodels

include "{PDK_MODEL}" section=tt_mos_varactor
include "{PDK_MODEL}" section=tt_res_res3t_bjt_dio
include "{PDK_MODEL}" section=tt_mom_mim
include "{PDK_MODEL}" section=pre_layout

parameters VDD=1.8 VCM=0.9

V0 (VDD 0) vsource dc=VDD type=dc
V1 (VSS 0) vsource dc=0 type=dc

VINP (VINP 0) vsource dc=VCM mag=1 source_type=dc ac=1
VINN (VINN 0) vsource dc=VCM mag=-1 source_type=dc ac=1
CL (VOUT 0) capacitor c=2p

// 包含寄生参数网表
include "{remote_work_dir}/{dspf_file}"

// 实例化 opamp - 端口顺序: VINP VSS VDD VINN VOUT
XOPAMP (VINP VSS VDD VINN VOUT) opamp_two_stage

// DC 和 AC 仿真
dcOp dc maxiters=1000 save=allopt
ac_ac ac start=1 stop=10G dec=20 maxiters=1000 save=allopt

save VDD VSS VINP VINN VOUT
saveOptions options save=selected
"""

    scs_local = Path(f"post_sim_{label}_{TIMESTAMP}.scs")
    scs_local.write_text(netlist, encoding="utf-8")
    print(f"✅ 测试平台已创建: {scs_local}")

    # 上传文件
    print(f"上传文件到远程服务器...")
    subprocess.run(f"ssh {user}@{host} \"mkdir -p {remote_work_dir}\"", shell=True, check=True)
    subprocess.run(f"scp {dspf_file} {user}@{host}:{remote_work_dir}/", shell=True, check=True)
    subprocess.run(f"scp {scs_local} {user}@{host}:{remote_work_dir}/", shell=True, check=True)

    # 运行仿真
    print(f"运行 Spectre 仿真...")
    raw_dir = f"{remote_work_dir}/output.raw"
    log_file = f"{remote_work_dir}/spectre.out"

    spectre_cmd = (
        f"cd {remote_work_dir} && "
        f"spectre -64 {remote_work_dir}/{scs_local.name} +escchars +log {log_file} "
        f"-format psfascii -raw {raw_dir} +lqtimeout 900 -maxw 5 -maxn 5"
    )

    result = subprocess.run(
        f"ssh {user}@{host} \"{spectre_cmd}\"",
        shell=True, capture_output=True, text=True, timeout=1800
    )

    if result.returncode != 0:
        print(f"⚠️ 仿真返回码: {result.returncode}")
        if len(result.stdout) > 1000:
            print(f"stdout (最后500字符): {result.stdout[-500:]}")
        else:
            print(f"stdout: {result.stdout}")
    else:
        print(f"✅ 仿真完成")

    # 下载结果
    output_dir = Path(f"output_{label}.raw")
    print(f"下载仿真结果...")
    tar_cmd = f"ssh {user}@{host} \"cd {remote_work_dir} && tar czf - output.raw\""
    result_tar = subprocess.run(tar_cmd, shell=True, capture_output=True)

    if result_tar.returncode == 0 and len(result_tar.stdout) > 100:
        import io
        import tarfile
        tar_stream = io.BytesIO(result_tar.stdout)
        with tarfile.open(fileobj=tar_stream, mode='r:gz') as tar:
            tar.extractall(path=output_dir)
        print(f"✅ 结果下载成功: {output_dir}")
    else:
        print(f"⚠️ 结果下载失败")
        output_dir = None

    # 清理远程文件
    print(f"清理远程临时文件...")
    subprocess.run(f"ssh {user}@{host} \"rm -rf {remote_work_dir}\"", shell=True)

    # 解析结果
    dc_gain = None
    gbw = None
    pm = None
    vout_dc = None

    if output_dir:
        ac_result_path = output_dir / "ac_ac.ac"
        dc_result_path = output_dir / "dcOp.dc"

        if ac_result_path.exists():
            from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii
            ac_data = parse_spectre_psf_ascii(ac_result_path)
            d = ac_data.data
            freq = d.get("freq", [])
            vout_complex = d.get("VOUT", [])

            if freq and len(vout_complex) > 0:
                import math
                import cmath

                gain_db = [20 * math.log10(abs(v) + 1e-30) for v in vout_complex]
                phase_deg = [math.degrees(cmath.phase(v)) for v in vout_complex]

                dc_gain = gain_db[0]

                # GBW
                for i in range(len(gain_db) - 1):
                    if gain_db[i] >= 0 and gain_db[i+1] < 0:
                        f1, f2 = freq[i], freq[i+1]
                        g1, g2 = gain_db[i], gain_db[i+1]
                        log_cross = math.log10(f1) + (math.log10(f2) - math.log10(f1)) * (-g1) / (g2 - g1)
                        gbw = 10 ** log_cross
                        break

                # PM
                if gbw:
                    log_gbw = math.log10(gbw)
                    log_freqs = [math.log10(f + 1e-30) for f in freq]
                    for i in range(len(log_freqs) - 1):
                        if log_freqs[i] <= log_gbw <= log_freqs[i+1]:
                            t = (log_gbw - log_freqs[i]) / (log_freqs[i+1] - log_freqs[i])
                            ph = phase_deg[i] + t * (phase_deg[i+1] - phase_deg[i])
                            pm = 180 + ph
                            break

                # 生成 Bode 图
                try:
                    import matplotlib
                    matplotlib.use('Agg')
                    import matplotlib.pyplot as plt

                    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8),
                        gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08})

                    ax1.semilogx(freq, gain_db, linewidth=1.5, color='darkblue')
                    ax1.set_ylabel("Gain (dB)", fontsize=12)
                    ax1.axhline(y=0, color="red", linestyle="--", linewidth=1)
                    if gbw:
                        ax1.axvline(x=gbw, color="orange", linestyle="--", linewidth=1)
                        ax1.text(gbw*1.2, 0, f'GBW={gbw/1e6:.1f}MHz', color="orange")
                    ax1.grid(True, alpha=0.3)
                    ax1.set_title(f"Post-layout AC Analysis ({label})\nDC Gain = {dc_gain:.1f} dB", fontsize=14)

                    ax2.semilogx(freq, phase_deg, color="orange", linewidth=1.5)
                    ax2.set_xlabel("Frequency (Hz)", fontsize=12)
                    ax2.set_ylabel("Phase (deg)", fontsize=12)
                    ax2.grid(True, alpha=0.3)

                    bode_path = Path(f"opamp_{label}_post_sim_bode_{TIMESTAMP}.png")
                    plt.savefig(bode_path, dpi=200, bbox_inches="tight")
                    print(f"✅ Bode 图已保存: {bode_path}")
                except ImportError:
                    print("⚠️ matplotlib 未安装")
                except Exception as e:
                    print(f"⚠️ Bode 图生成失败: {e}")

        if dc_result_path.exists():
            from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii
            dc_data = parse_spectre_psf_ascii(dc_result_path)
            raw_vout = dc_data.data.get("VOUT", [])
            if isinstance(raw_vout, list) and len(raw_vout) > 0:
                vout_dc = raw_vout[0]

    print(f"\n📊 {label} 后仿真结果:")
    print(f"  DC 增益: {dc_gain:.2f} dB" if dc_gain is not None else "  DC 增益: N/A")
    print(f"  GBW: {gbw/1e6:.2f} MHz" if gbw else "  GBW: N/A")
    print(f"  相位裕度: {pm:.1f}°" if pm else "  相位裕度: N/A")
    print(f"  VOUT DC: {vout_dc} V" if vout_dc else "  VOUT DC: N/A")

    return {
        "label": label,
        "dc_gain": dc_gain,
        "gbw": gbw,
        "pm": pm,
        "vout_dc": vout_dc,
    }

def main():
    print("="*60)
    print("Opamp 后仿真 (RCE + REF)")
    print("="*60)

    results = {}

    # 先跑 REF (参考工具提取)
    results["ref"] = run_post_sim("opamp.ref.dspf", "ref")

    # 再跑 RCE
    results["rce"] = run_post_sim("opamp.rce.dspf", "rce")

    # 对比汇总
    print(f"\n\n{'='*80}")
    print(f"📋 后仿真对比汇总")
    print(f"{'='*80}")
    print(f"{'指标':<20} {'前仿真':<15} {'REF 后仿真':<15} {'RCE 后仿真':<15}")
    print(f"{'-'*80}")

    dc_gain_ref = results["ref"]["dc_gain"] if results["ref"] else None
    dc_gain_rce = results["rce"]["dc_gain"] if results["rce"] else None
    gbw_ref = results["ref"]["gbw"] if results["ref"] else None
    gbw_rce = results["rce"]["gbw"] if results["rce"] else None
    pm_ref = results["ref"]["pm"] if results["ref"] else None
    pm_rce = results["rce"]["pm"] if results["rce"] else None

    print(f"{'DC 增益 (dB)':<20} {'45.65':<15} "
          f"{'{:.2f}'.format(dc_gain_ref) if dc_gain_ref else 'N/A':<15} "
          f"{'{:.2f}'.format(dc_gain_rce) if dc_gain_rce else 'N/A':<15}")
    print(f"{'GBW (MHz)':<20} {'201.72':<15} "
          f"{'{:.2f}'.format(gbw_ref/1e6) if gbw_ref else 'N/A':<15} "
          f"{'{:.2f}'.format(gbw_rce/1e6) if gbw_rce else 'N/A':<15}")
    print(f"{'相位裕度 (°)':<20} {'-':<15} "
          f"{'{:.1f}'.format(pm_ref) if pm_ref else 'N/A':<15} "
          f"{'{:.1f}'.format(pm_rce) if pm_rce else 'N/A':<15}")
    print(f"{'='*80}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
