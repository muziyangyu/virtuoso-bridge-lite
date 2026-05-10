#!/usr/bin/env python3
"""
Test RCE DSPF - check full spectre output
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

def main():
    host = "172.17.8.14"
    user = "lixiang"
    remote_work_dir = f"/tmp/virtuoso_bridge_lixiang/rce_test_{TIMESTAMP}"

    netlist = f"""simulator lang=spectre
global 0

simulatorOptions options reltol=1e-4 vabstol=1e-6 iabstol=1e-12 temp=25 \\
    gmin=1e-12 soft_bin=allmodels

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

include "{remote_work_dir}/opamp.rce.dspf"

XOPAMP (VSS VDD VINP VINN VOUT) opamp_two_stage

dcOp dc maxiters=1000 save=allopt
ac_ac ac start=1 stop=10G dec=20 maxiters=1000 save=allopt

save VDD VSS VINP VINN VOUT
saveOptions options save=selected
"""

    scs_local = Path(f"rce_test_{TIMESTAMP}.scs")
    scs_local.write_text(netlist, encoding="utf-8")
    print(f"✅ 测试平台已创建")

    print(f"\n上传文件...")
    subprocess.run(f"ssh {user}@{host} \"mkdir -p {remote_work_dir}\"", shell=True, check=True)
    subprocess.run(f"scp opamp.rce.dspf {user}@{host}:{remote_work_dir}/", shell=True, check=True)
    subprocess.run(f"scp {scs_local} {user}@{host}:{remote_work_dir}/", shell=True, check=True)

    print(f"\n运行仿真并捕获完整输出...")
    raw_dir = f"{remote_work_dir}/output.raw"

    spectre_cmd = (
        f"cd {remote_work_dir} && "
        f"spectre -64 {remote_work_dir}/{scs_local.name} "
        f"-format psfascii -raw {raw_dir} +lqtimeout 900"
    )

    result = subprocess.run(
        f"ssh {user}@{host} \"{spectre_cmd}\"",
        shell=True, capture_output=True, text=True, timeout=1800
    )

    # Print full output
    print("\n" + "="*80)
    print("STDOUT (完整输出):")
    print("="*80)
    print(result.stdout[-5000:] if len(result.stdout) > 5000 else result.stdout)
    print("\n" + "="*80)
    print("STDERR (完整输出):")
    print("="*80)
    print(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
    print(f"\n返回码: {result.returncode}")

    # 下载结果并解析
    subprocess.run(
        f"ssh {user}@{host} \"cd {remote_work_dir} && tar czf - output.raw\" | tar xzf -",
        shell=True, capture_output=True
    )

    ac_result_path = Path("output.raw/ac_ac.ac")
    if ac_result_path.exists():
        from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii
        ac_data = parse_spectre_psf_ascii(ac_result_path)
        d = ac_data.data
        freq = d.get("freq", [])
        vout_complex = d.get("VOUT", [])

        if freq and len(vout_complex) > 0:
            import math
            gain_db = [20 * math.log10(abs(v) + 1e-30) for v in vout_complex]
            dc_gain = gain_db[0]
            print(f"\n📊 DC 增益: {dc_gain:.2f} dB")
            print(f"📊 增益列表前10个值: {gain_db[:10]}")
        else:
            print(f"❌ 结果解析失败")
            print(f"Keys in result: {list(d.keys())}")
    else:
        print(f"❌ 结果文件不存在")

    # 清理
    subprocess.run(f"ssh {user}@{host} \"rm -rf {remote_work_dir}\"", shell=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
