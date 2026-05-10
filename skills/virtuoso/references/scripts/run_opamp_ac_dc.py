#!/usr/bin/env python3
"""
获取 work_ai/opamp_two_stage 原理图并运行 AC/DC 仿真
"""
import os
import sys
from datetime import datetime
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic
from virtuoso_bridge.spectre.runner import SpectreSimulator
from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii

# PDK 模型路径
PDK_MODEL = (
    "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0/"
    "smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0/"
    "models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
)

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LIB = "work_ai"
CELL = "opamp_two_stage"

def parse_length(l_str):
    """解析长度字符串，如 '242.0n' -> 242.0 (nm)"""
    if isinstance(l_str, (int, float)):
        return float(l_str) * 1e9  # 米 -> nm
    if isinstance(l_str, str):
        if l_str.endswith('n'):
            return float(l_str[:-1])  # nm
        elif l_str.endswith('u'):
            return float(l_str[:-1]) * 1e3  # um -> nm
        elif l_str.endswith('m'):
            return float(l_str[:-1]) * 1e9  # m -> nm
    return 242.0  # 默认值

def parse_capacitance(c_str):
    """解析电容字符串，如 '127.8488f' -> 0.1278488 (pF)"""
    if isinstance(c_str, (int, float)):
        return float(c_str) * 1e12  # 法拉 -> pF
    if isinstance(c_str, str):
        if c_str.endswith('f'):
            return float(c_str[:-1]) * 1e-3  # fF -> pF
        elif c_str.endswith('p'):
            return float(c_str[:-1])  # pF
    return 0.128  # 默认值

def main():
    print("="*60)
    print(f"读取原理图: {LIB}/{CELL}")
    print("="*60)
    
    client = VirtuosoClient.from_env()
    
    # 1. 读取原理图
    schematic_data = read_schematic(client, LIB, CELL)
    instances = schematic_data["instances"]
    
    print(f"\n✅ 读取到 {len(instances)} 个器件:")
    for inst in instances:
        name = inst["name"]
        params = inst.get("params", {})
        l = params.get("l", "N/A")
        nfin = params.get("nfin", "N/A")
        m = params.get("m", "N/A")
        c = params.get("c", "N/A")
        print(f"  {name:4s}: l={l}, nfin={nfin}, m={m}, c={c}")
    
    # 2. 提取器件参数
    mos_params = {}
    cap_params = {}
    
    for inst in instances:
        name = inst["name"]
        params = inst.get("params", {})
        if name.startswith("M"):
            mos_params[name] = {
                "l": params.get("l", "242.0n"),  # 默认 242nm
                "nfin": params.get("nfin", 6),
                "m": params.get("m", 1),
            }
        elif name.startswith("C"):
            cap_params[name] = {
                "c": params.get("c", "128f"),  # 默认 0.128pF
            }
    
    # 3. 构建 Spectre 网表
    print("\n" + "="*60)
    print("构建 Spectre 测试平台")
    print("="*60)
    
    # 获取参数（设置合理默认值）
    def get_mos(name, default_nfin=6):
        p = mos_params.get(name, {})
        l_nm = parse_length(p.get("l", "242.0n"))
        nfin = int(p.get("nfin", default_nfin))
        m = int(p.get("m", 1))
        return {"l": l_nm, "nfin": nfin, "m": m}
    
    m1 = get_mos("M1", 8)
    m3 = get_mos("M3", 6)
    m5 = get_mos("M5", 6)
    m6 = get_mos("M6", 6)
    m7 = get_mos("M7", 6)
    m8 = get_mos("M8", 6)
    m9 = get_mos("M9", 6)
    m10 = get_mos("M10", 6)
    
    cc_val = cap_params.get("Cc", {}).get("c", "128f")
    cc_pf = parse_capacitance(cc_val)
    
    print(f"\n器件参数:")
    print(f"  M1/M2: l={m1['l']}nm, nfin={m1['nfin']}, m={m1['m']}")
    print(f"  M3/M4: l={m3['l']}nm, nfin={m3['nfin']}, m={m3['m']}")
    print(f"  M5:    l={m5['l']}nm, nfin={m5['nfin']}, m={m5['m']}")
    print(f"  M6:    l={m6['l']}nm, nfin={m6['nfin']}, m={m6['m']}")
    print(f"  M7:    l={m7['l']}nm, nfin={m7['nfin']}, m={m7['m']}")
    print(f"  Cc:    {cc_pf:.3f}pF")
    
    netlist = f'''simulator lang=spectre
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

* 偏置电路
IBIAS (net_bias VSS) isource dc=IBIAS
M8 (net_bias net_bias VDD VDD) p18_ckt l={m8['l']}n nfin={m8['nfin']} m={m8['m']}
M9 (net_vb net_bias VDD VDD) p18_ckt l={m9['l']}n nfin={m9['nfin']} m={m9['m']}
M10 (net_bias net_bias VSS VSS) n18_ckt l={m10['l']}n nfin={m10['nfin']} m={m10['m']}
Rvb (net_vb VSS) resistor r=500MEG

* 差分输入级
M1 (net_d3 VINP net_s VSS) n18_ckt l={m1['l']}n nfin={m1['nfin']} m={m1['m']}
M2 (net_x VINN net_s VSS) n18_ckt l={m1['l']}n nfin={m1['nfin']} m={m1['m']}
M5 (net_s net_vb VSS VSS) n18_ckt l={m5['l']}n nfin={m5['nfin']} m={m5['m']}

* 有源负载电流镜
M3 (net_d3 net_d3 VDD VDD) p18_ckt l={m3['l']}n nfin={m3['nfin']} m={m3['m']}
M4 (net_x net_d3 VDD VDD) p18_ckt l={m3['l']}n nfin={m3['nfin']} m={m3['m']}

* 第二级放大
M6 (VOUT net_x VSS VSS) n18_ckt l={m6['l']}n nfin={m6['nfin']} m={m6['m']}
M7 (VOUT net_bias VDD VDD) p18_ckt l={m7['l']}n nfin={m7['nfin']} m={m7['m']}

* 米勒补偿电容
Cc (net_x VOUT) capacitor c={cc_pf}p

* 输入激励
VINP (VINP 0) vsource dc=VCM mag=0.5
VINN (VINN 0) vsource dc=VCM mag=-0.5
CL (VOUT 0) capacitor c=2p

* 仿真设置
dcOp dc maxiters=150
ac ac start=1 stop=5G dec=20

save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias
saveOptions options save=selected
'''
    
    # 保存网表
    scs_path = Path(f"opamp_testbench_{TIMESTAMP}.scs")  # 当前目录是 output/
    scs_path.write_text(netlist, encoding="utf-8")
    print(f"\n✅ 网表已保存: {scs_path}")
    
    # 4. 运行 Spectre 仿真
    print("\n" + "="*60)
    print("运行 Spectre AC/DC 仿真")
    print("="*60)
    
    sim = SpectreSimulator.from_env(
        work_dir=str(Path("output")),
        output_format="psfascii",
    )
    
    result = sim.run_simulation(str(scs_path), {})
    
    if not result.ok:
        print(f"\n❌ 仿真失败!")
        print(f"错误信息:\n{result.errors}")
        return 1
    
    print(f"\n✅ 仿真成功!")
    
    # 查找输出目录
    output_dir = Path(f"opamp_testbench_{TIMESTAMP}.raw")
    if not output_dir.exists():
        # 尝试在 output/output 下查找
        output_dir = Path(f"output/opamp_testbench_{TIMESTAMP}.raw")
    
    print(f"输出目录: {output_dir}")
    
    # 5. 解析仿真结果
    print("\n" + "="*60)
    print("解析仿真结果")
    print("="*60)
    
    ac_result_path = output_dir / "ac.ac"
    if ac_result_path.exists():
        ac_data = parse_spectre_psf_ascii(ac_result_path)
        d = ac_data.data
        
        # 提取频率和 VOUT
        freq = d.get("freq", [])
        vout_complex = d.get("VOUT", [])  # 已经是复数数组了！
        
        if freq and vout_complex and len(vout_complex) > 0:
            import math
            import cmath
            
            # 计算增益和相位 (VOUT 已经是复数数组)
            gain_db = [20 * math.log10(abs(v) * 2 + 1e-30) for v in vout_complex]
            phase_deg = [math.degrees(cmath.phase(v)) for v in vout_complex]
            
            # DC 增益
            dc_gain = gain_db[0]
            
            # 计算 GBW（增益过 0dB 的频率）
            gbw = None
            for i in range(len(gain_db) - 1):
                if gain_db[i] >= 0 and gain_db[i+1] < 0:
                    f1, f2 = freq[i], freq[i+1]
                    g1, g2 = gain_db[i], gain_db[i+1]
                    log_cross = math.log10(f1) + (math.log10(f2) - math.log10(f1)) * (-g1) / (g2 - g1)
                    gbw = 10 ** log_cross
                    break
            
            # 计算相位裕度
            pm = None
            if gbw:
                log_gbw = math.log10(gbw)
                log_freqs = [math.log10(f + 1e-30) for f in freq]
                for i in range(len(log_freqs) - 1):
                    if log_freqs[i] <= log_gbw <= log_freqs[i+1]:
                        t = (log_gbw - log_freqs[i]) / (log_freqs[i+1] - log_freqs[i])
                        ph = phase_deg[i] + t * (phase_deg[i+1] - phase_deg[i])
                        pm = 180 + ph
                        break
            
            # DC 工作点
            dc_vout_raw = d.get("dc_VOUT", 0)
            if isinstance(dc_vout_raw, list):
                dc_vout = abs(dc_vout_raw[0])
            elif isinstance(dc_vout_raw, complex):
                dc_vout = abs(dc_vout_raw)
            else:
                dc_vout = abs(float(dc_vout_raw))
            
            print("\n" + "="*60)
            print("📊 仿真结果汇总")
            print("="*60)
            print(f"DC 增益:       {dc_gain:.2f} dB")
            if gbw:
                print(f"增益带宽积:   {gbw/1e6:.2f} MHz")
            if pm:
                print(f"相位裕度:     {pm:.1f}°")
            print(f"VOUT 直流:     {dc_vout:.3f} V")
            print(f"电源电压:      1.8 V")
            print("="*60)
            
            # 6. 生成 Bode 图
            try:
                import matplotlib
                matplotlib.use('Agg')
                import matplotlib.pyplot as plt
                
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7),
                    gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08})
                
                ax1.semilogx(freq, gain_db, linewidth=1.5)
                ax1.set_ylabel("Gain (dB)", fontsize=12)
                ax1.axhline(y=0, color="red", linestyle="--", linewidth=1)
                if gbw:
                    ax1.axvline(x=gbw, color="orange", linestyle="--", linewidth=1)
                    ax1.text(gbw*1.2, 0, f"GBW = {gbw/1e6:.2f} MHz", color="orange")
                ax1.grid(True, alpha=0.3)
                ax1.set_title(f"AC Analysis - {LIB}/{CELL}\nDC Gain = {dc_gain:.1f} dB", fontsize=14)
                
                ax2.semilogx(freq, phase_deg, color="orange", linewidth=1.5)
                ax2.set_xlabel("Frequency (Hz)", fontsize=12)
                ax2.set_ylabel("Phase (deg)", fontsize=12)
                ax2.axhline(y=0, color="gray", linestyle="--", linewidth=0.5)
                ax2.grid(True, alpha=0.3)
                
                bode_path = Path(f"opamp_ac_bode_{TIMESTAMP}.png")  # 当前目录是 output/
                plt.savefig(bode_path, dpi=200, bbox_inches="tight")
                print(f"\n✅ Bode 图已保存: {bode_path}")
            except ImportError:
                print("\n⚠️  matplotlib 未安装，跳过 Bode 图生成")
        
        # 保存结果摘要
        summary_path = Path(f"opamp_simulation_summary_{TIMESTAMP}.txt")  # 当前目录是 output/
        gbw_str = f"{gbw/1e6:.2f} MHz" if gbw else "N/A"
        pm_str = f"{pm:.1f}°" if pm else "N/A"
        bode_str = str(bode_path) if 'bode_path' in dir() else "N/A"
        
        summary = f"""
========================================================================
          Opamp AC/DC Simulation Results - {LIB}/{CELL}
========================================================================

Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Schematics Parameters:
  M1/M2 (input pair): l={m1['l']}nm, nfin={m1['nfin']}, m={m1['m']}
  M3/M4 (load):       l={m3['l']}nm, nfin={m3['nfin']}, m={m3['m']}
  M5 (tail current):  l={m5['l']}nm, nfin={m5['nfin']}, m={m5['m']}
  M6 (2nd stage):     l={m6['l']}nm, nfin={m6['nfin']}, m={m6['m']}
  M7 (2nd load):      l={m7['l']}nm, nfin={m7['nfin']}, m={m7['m']}
  Cc (Miller cap):    {cc_pf:.3f}pF

AC Simulation Results:
  DC Gain:           {dc_gain:.2f} dB
  GBW:               {gbw_str}
  Phase Margin:      {pm_str}
  VOUT DC:           {dc_vout:.3f} V
  VDD:               1.8 V

Files:
  Testbench:  {scs_path}
  Output dir: {output_dir}
  Bode plot:  {bode_str}
========================================================================
"""
        summary_path.write_text(summary, encoding="utf-8")
        print(f"\n✅ 结果摘要已保存: {summary_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())