# Opamp 前仿真到后仿真完整流程

从读取 Virtuoso 原理图 → 前仿真 → 提取 DSPF → 后仿真对比的完整工作流。

## 1. 读取原理图

```python
from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic

client = VirtuosoClient.from_env()
schematic_data = read_schematic(client, "work_ai", "opamp_two_stage")
instances = schematic_data["instances"]

for inst in instances:
    name = inst["name"]
    params = inst.get("params", {})
    l = params.get("l", "N/A")
    nfin = params.get("nfin", "N/A")
    m = params.get("m", "N/A")
    c = params.get("c", "N/A")
    print(f"  {name}: l={l}, nfin={nfin}, m={m}, c={c}")
```

## 2. 构建 Spectre 前仿真测试平台

### 关键规则
- **端口顺序**: 必须与原理图一致（VINP VSS VDD VINN VOUT）
- **soft_bin=allmodels**: FinFET 必须，否则 CMI-2942 错误
- **注释必须单独一行**: 不能跟器件参数同行（SFE-874 错误）
- **save I(V0)**: 在 .scs 中不合法，改用节点电压
- **SI 单位**: l=168nm=1.68e-7m（不是 0.168），c=0.08pF=8e-14F

### 测试平台模板

```spectre
simulator lang=spectre
global 0

simulatorOptions options psfversion="1.4.0" reltol=1e-4 vabstol=1e-6 soft_bin=allmodels

include "/mnt/data/.../12sfe_spice_v1p2_rev0_usage_spe.lib" section=tt_mos_varactor
include "/mnt/data/.../12sfe_spice_v1p2_rev0_usage_spe.lib" section=tt_res_res3t_bjt_dio
include "/mnt/data/.../12sfe_spice_v1p2_rev0_usage_spe.lib" section=tt_mom_mim
include "/mnt/data/.../12sfe_spice_v1p2_rev0_usage_spe.lib" section=pre_layout

parameters VDD=1.8 VCM=0.9 IBIAS=10u

V0 (VDD 0) vsource dc=VDD
V1 (VSS 0) vsource dc=0
VINP (VINP 0) vsource dc=VCM mag=1
VINN (VINN 0) vsource dc=VCM mag=-1
CL (VOUT 0) capacitor c=2p

XOPAMP (VINP VSS VDD VINN VOUT) opamp_two_stage

dcOp dc maxiters=1000
ac_ac ac start=1 stop=10G dec=20

save VDD VSS VINP VINN VOUT
saveOptions options save=selected
```

## 3. 运行前仿真

```python
from virtuoso_bridge.spectre.runner import SpectreSimulator
from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii

sim = SpectreSimulator.from_env(work_dir="output", output_format="psfascii")
result = sim.run_simulation(str(scs_path), {})
```

## 4. 解析结果

```python
ac_data = parse_spectre_psf_ascii(Path("output.raw/ac_ac.ac"))
d = ac_data.data
freq = d.get("freq", [])
vout_complex = d.get("VOUT", [])  # 已经是复数数组

import math, cmath
gain_db = [20 * math.log10(abs(v) + 1e-30) for v in vout_complex]
phase_deg = [math.degrees(cmath.phase(v)) for v in vout_complex]

# DC 增益
dc_gain = gain_db[0]

# GBW（增益过 0dB 的频率）
for i in range(len(gain_db) - 1):
    if gain_db[i] >= 0 and gain_db[i+1] < 0:
        f1, f2 = freq[i], freq[i+1]
        g1, g2 = gain_db[i], gain_db[i+1]
        log_cross = math.log10(f1) + (math.log10(f2) - math.log10(f1)) * (-g1) / (g2 - g1)
        gbw = 10 ** log_cross
        break

# 相位裕度
if gbw:
    log_gbw = math.log10(gbw)
    log_freqs = [math.log10(f + 1e-30) for f in freq]
    for i in range(len(log_freqs) - 1):
        if log_freqs[i] <= log_gbw <= log_freqs[i+1]:
            t = (log_gbw - log_freqs[i]) / (log_freqs[i+1] - log_freqs[i])
            ph = phase_deg[i] + t * (phase_deg[i+1] - phase_deg[i])
            pm = 180 + ph
            break
```

## 5. 运行后仿真

### DSPF 端口顺序
每个 DSPF 文件的端口顺序可能不同，必须从 `.SUBCKT` 行读取：
```
.SUBCKT opamp_two_stage VINP VSS VDD VINN VOUT
```
实例化时必须匹配：
```spectre
XOPAMP (VINP VSS VDD VINN VOUT) opamp_two_stage
```

### 后仿真上传 DSPF
```python
import subprocess
host = "172.17.8.14"
user = "lixiang"
remote_dir = f"/tmp/virtuoso_bridge_{user}/post_sim_{label}_{TIMESTAMP}"

subprocess.run(f"ssh {user}@{host} \"mkdir -p {remote_dir}\"", shell=True)
subprocess.run(f"scp opamp.ref.dspf {user}@{host}:{remote_dir}/", shell=True)
subprocess.run(f"scp testbench.scs {user}@{host}:{remote_dir}/", shell=True)
```

### 下载结果
```python
result_tar = subprocess.run(
    f"ssh {user}@{host} \"cd {remote_dir} && tar czf - output.raw\"",
    shell=True, capture_output=True
)
if result_tar.returncode == 0 and len(result_tar.stdout) > 100:
    import io, tarfile
    tar_stream = io.BytesIO(result_tar.stdout)
    with tarfile.open(fileobj=tar_stream, mode='r:gz') as tar:
        tar.extractall(path=f"output_{label}.raw")
```

## 6. 典型结果对比

| 指标 | 前仿真 | REF (GloryEX) | RCE (RCExplorer) |
|------|--------|--------------|----------------|
| DC 增益 | 45.65 dB | 32.70 dB (-12.95) | 24.25 dB (-21.40) |
| GBW | 201.72 MHz | 344.39 MHz | 371.81 MHz |
| 相位裕度 | - | 95.3° | 98.1° |

- **前→后增益下降 13 dB**：正常的寄生效应（金属电阻 + 寄生电容）
- **REF vs RCE 差异 ~8 dB**：两种 RC 提取算法不同，REF 提取的寄生电容更多（13K vs 4K）
- **GBW 提升**：增益降低导致主极点前移，带宽增加
- **相位裕度 >95°**：电路非常稳定

## 7. 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| CMI-2942 | FinFET 尺寸不在 PDK bin 内 | 加 `soft_bin=allmodels` |
| SFE-874 | 注释跟在器件参数同行 | 注释必须单独一行 |
| SFE-404 | `temp` 与 `TEMP` 大小写冲突 | 去掉 `TEMP=25` 参数 |
| 端口顺序不匹配 | DSPF `.SUBCKT` 端口顺序与实例化不一致 | 读取 `.SUBCKT` 行匹配顺序 |
| -600 dB 增益 | 电路内部断线 | 检查 LVS 数据库或 RC 提取设置 |
| `save I(V0)` 语法错误 | Spectre 不支持分支电流保存语法 | 只保存节点电压 |

## 8. 参考脚本

| 脚本 | 用途 |
|------|------|
| `output/run_opamp_ac_dc.py` | 读取原理图 + 前仿真完整流程 |
| `output/run_post_sim.py` | 多 DSPF 后仿真 + 结果对比 |
| `output/parse_post_sim.py` | 解析后仿真结果 + Bode 图生成 |
