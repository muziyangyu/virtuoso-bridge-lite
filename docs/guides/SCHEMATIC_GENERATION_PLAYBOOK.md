# Virtuoso Schematic Generation Playbook
> **两级运算放大器原理图重建 + Spectre 仿真优化实战经验**

**状态**: ✅ 实战验证通过 (GBW=2.77 GHz @ l=168nm)
**创建日期**: 2026-04-29
**最后更新**: 2026-04-30

---

## 目录

1. [核心 API 速查](#1-核心-api-速查)
2. [完整工作流](#2-完整工作流)
3. [器件放置与连接](#3-器件放置与连接)
4. [原理图参数修改](#4-原理图参数修改)
5. [Spectre 仿真流水线](#5-spectre-仿真流水线)
6. [结果解析与 Bode 图](#6-结果解析与-bode-图)
7. [常见陷阱汇总](#7-常见陷阱汇总)
8. [参考资源](#8-参考资源)

---

## 1. 核心 API 速查

### 1.1 原理图编辑 API

| 函数 | 用途 | 参数 |
|------|------|------|
| `client.schematic.edit(LIB, CELL)` | 编辑器上下文管理器 | lib, cell |
| `schematic_create_inst_by_master_name()` | 放置器件 | lib, cell, view, name, x, y, orient |
| `schematic_label_instance_term()` | 连接终端 | inst_name, term_name, net_name |
| `schematic_create_pin()` | 创建引脚 | name, x, y, orient, direction |

### 1.2 参数修改 API

| 方法 | 适用场景 | 关键命令 |
|------|---------|---------|
| `set_instance_params()` | CDF 参数修改 | 内部用 `cdfUpdateInstParam` + 回调 |
| `execute_operations([skill_code])` | 直接属性修改 | `dbReplaceProp` |

### 1.3 仿真 API

| 类/函数 | 用途 |
|---------|------|
| `SpectreSimulator.from_env(work_dir=, output_format=)` | 创建 Spectre 仿真器 |
| `sim.run_simulation(scs_path, params)` | 运行仿真 |
| `parse_spectre_psf_ascii(path)` | 解析 PSF ASCII 结果 |

### 1.4 原理图读取 API

| 函数 | 用途 |
|------|------|
| `read_schematic(client, lib, cell)` | 读取原理图拓扑 + 参数 |

---

## 2. 完整工作流

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: 原理图创建                                          │
│  ─────────────────                                          │
│  read_schematic()  →  了解现有拓扑                              │
│  client.schematic.edit() → 放置器件 + 连接终端 + 创建 Pin       │
│                                                             │
│  Phase 2: 参数同步                                            │
│  ─────────────────                                          │
│  execute_operations([SKILL]) → dbReplaceProp 修改 l/nfin/m/c  │
│  verify: read_schematic() → 确认参数写入正确                    │
│                                                             │
│  Phase 3: 仿真优化                                            │
│  ─────────────────                                          │
│  build_testbench() → .scs netlist                           │
│  SpectreSimulator.run_simulation() → PSF ASCII 结果          │
│  parse_results() → DC Gain / GBW / PM / VOUT / Power        │
│  多轮 sweep → 找到最优参数                                      │
│                                                             │
│  Phase 4: 可视化                                              │
│  ─────────────────                                          │
│  parse_psf_ac() → matplotlib → Bode plot (png)              │
│                                                             │
│  Phase 5: 回写原理图                                          │
│  ─────────────────                                          │
│  execute_operations() → 将最优参数同步回原理图                   │
│  verify: read_schematic() → 最终确认                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. 器件放置与连接

### 3.1 终端命名规则 (⚠️ 关键!)

| 器件类型 | 终端命名 | 说明 |
|---------|---------|------|
| **MOSFET** (n18_ckt/p18_ckt) | **G, D, S, B** | Gate, Drain, Source, Bulk |
| **电容** (analogLib/cap) | **PLUS, MINUS** | 正负极 |
| **电阻** (analogLib/res) | **PLUS, MINUS** | 两端 |

❌ **错误示范**: 用 PLUS/MINUS 连接 MOSFET 端口
```python
# ❌ 错误！MOSFET 没有 PLUS/MINUS terminal！
sch.add(schematic_label_instance_term("M1", "PLUS", "VINP"))

# ✅ 正确！MOSFET terminal 是 G/D/S/B
sch.add(schematic_label_instance_term("M1", "G", "VINP"))
sch.add(schematic_label_instance_term("M1", "D", "net_d3"))
sch.add(schematic_label_instance_term("M1", "S", "net_s"))
sch.add(schematic_label_instance_term("M1", "B", "VSS"))
```

### 3.2 电源连接清单 (含 Bulk!)

```python
# ========== VDD ==========
# PMOS Source -> VDD
for name in ['M3', 'M4', 'M7', 'M8', 'M9']:
    sch.add(schematic_label_instance_term(name, 'S', 'VDD'))
    sch.add(schematic_label_instance_term(name, 'B', 'VDD'))  # PMOS Bulk -> VDD

# ========== VSS ==========
# NMOS Source -> VSS
for name in ['M5', 'M6', 'M10']:
    sch.add(schematic_label_instance_term(name, 'S', 'VSS'))
    sch.add(schematic_label_instance_term(name, 'B', 'VSS'))  # NMOS Bulk -> VSS

# 差分输入对的 Bulk 也要连 VSS
for name in ['M1', 'M2']:
    sch.add(schematic_label_instance_term(name, 'B', 'VSS'))
```

### 3.3 信号连接 (两级运放)

```python
# 差分输入
sch.add(schematic_label_instance_term('M1', 'G', 'VINP'))
sch.add(schematic_label_instance_term('M2', 'G', 'VINN'))

# M1/M2 Source -> M5 Drain
sch.add(schematic_label_instance_term('M1', 'S', 'net_s'))
sch.add(schematic_label_instance_term('M2', 'S', 'net_s'))
sch.add(schematic_label_instance_term('M5', 'D', 'net_s'))

# M3 二极管连接 (active load + current mirror reference)
sch.add(schematic_label_instance_term('M3', 'D', 'net_d3'))
sch.add(schematic_label_instance_term('M3', 'G', 'net_d3'))
sch.add(schematic_label_instance_term('M4', 'G', 'net_d3'))  # M4 gate mirrors M3
sch.add(schematic_label_instance_term('M1', 'D', 'net_d3'))

# Node X (M2 drain + M4 drain -> M6 gate)
sch.add(schematic_label_instance_term('M2', 'D', 'net_x'))
sch.add(schematic_label_instance_term('M4', 'D', 'net_x'))
sch.add(schematic_label_instance_term('M6', 'G', 'net_x'))

# 第二级输出
sch.add(schematic_label_instance_term('M6', 'D', 'VOUT'))
sch.add(schematic_label_instance_term('M7', 'D', 'VOUT'))

# ⚠️ 最容易忘记！M7 Gate 必须连偏置！
sch.add(schematic_label_instance_term('M7', 'G', 'net_bias'))

# Miller 补偿电容
sch.add(schematic_label_instance_term('Cc', 'PLUS', 'net_x'))
sch.add(schematic_label_instance_term('Cc', 'MINUS', 'VOUT'))
```

### 3.4 偏置电路连接

```python
# M8 二极管连接 (偏置参考)
sch.add(schematic_label_instance_term('M8', 'D', 'net_bias'))
sch.add(schematic_label_instance_term('M8', 'G', 'net_bias'))
sch.add(schematic_label_instance_term('M9', 'G', 'net_bias'))  # M9 mirrors M8
sch.add(schematic_label_instance_term('M10', 'D', 'net_bias'))
sch.add(schematic_label_instance_term('M10', 'G', 'net_bias'))

# M9 Drain -> M5 Gate (尾电流偏置)
sch.add(schematic_label_instance_term('M9', 'D', 'net_vb'))
sch.add(schematic_label_instance_term('M5', 'G', 'net_vb'))
```

### 3.5 Pin 创建

```python
sch.add(schematic_create_pin('VINP', -5.0,  1.0, 'R0', direction='input'))
sch.add(schematic_create_pin('VINN', -5.0,  0.0, 'R0', direction='input'))
sch.add(schematic_create_pin('VOUT',  3.0,  1.0, 'R0', direction='output'))
sch.add(schematic_create_pin('VDD',  -6.0,  2.5, 'R0', direction='inputOutput'))
sch.add(schematic_create_pin('VSS',  -6.0, -2.0, 'R0', direction='inputOutput'))
```

### 3.6 连接检查清单

创建完成后，必须检查以下项目：

- [ ] **所有 MOSFET 的 4 个端口都连接了 (G, D, S, B)**
- [ ] **NMOS 的 B 端口全部连接到 VSS**
- [ ] **PMOS 的 B 端口全部连接到 VDD**
- [ ] **电流镜的 Gate 都正确连接 (M3 G=M4 G, M8 G=M9 G)**
- [ ] **M7 的 Gate 没有 floating (连接到 net_bias)**
- [ ] **Miller 电容两端正确连接 (PLUS/MINUS)**
- [ ] **5 个 Pins 都创建了 (VINP, VINN, VOUT, VDD, VSS)**
- [ ] **没有任何 floating terminal 警告**

---

## 4. 原理图参数修改

### 4.1 方法选择

| 方法 | 优点 | 缺点 | 适用场景 |
|------|------|------|---------|
| `set_instance_params()` | 触发 CDF 回调，安全 | 受 CDF filter 限制 | 修改 CDF 认可的标准参数 |
| `execute_operations()` + `dbReplaceProp` | 直接、灵活、不受限 | 不调用回调 | 批量修改 / FinFET nfin 等特殊参数 |

### 4.2 致命陷阱：edit() 内部嵌套 dbOpen

```python
# ❌ 致命错误 - 双重打开导致原理图清空！
with client.schematic.edit(LIB, CELL) as sch:
    sch.add('let((cv) cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a") ...)')

# ✅ 正确方法 1: execute_operations 单独执行（推荐）
commands = [
    'cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a")',
    'let((i) i=car(setof(x cv~>instances x~>name=="M1")) when(i dbReplaceProp(i "m" "float" 64)))',
    'schCheck(cv)',
    'dbSave(cv)',
    'dbClose(cv)',
]
client.execute_operations(commands, timeout=60)

# ✅ 正确方法 2: edit() 内部用 cv 变量（已打开的 cellview）
with client.schematic.edit(LIB, CELL) as sch:
    sch.add('let((i) i=car(setof(x cv~>instances x~>name=="M1")) when(i dbReplaceProp(i "m" "float" 64)))')
    # 注意：cv 由 edit() 上下文管理器提供，不要再次 dbOpen！
```

### 4.3 dbReplaceProp 用法

```skill
;; 语法: dbReplaceProp(instance propName propType value)
;; propType: "float", "string", "int" 等

dbReplaceProp(inst "nfin" "float" 6)
dbReplaceProp(inst "l" "float" 1.68e-7)   ;; 168nm = 1.68e-7 米 (SI 单位!)
dbReplaceProp(inst "m" "float" 64)
dbReplaceProp(inst "c" "float" 8e-14)     ;; 0.08pF = 8e-14 法拉
```

### 4.4 ⚠️ 单位问题 (极易踩坑!)

**Virtuoso 使用 SI 基本单位：**

| 参数 | SI 单位 | 示例 | 说明 |
|------|--------|------|------|
| `l` (沟道长度) | **米 (m)** | `1.68e-7` = 168 nm | ❌ 不是微米！0.168 = 168,000,000 nm |
| `w` (宽度) | **米 (m)** | `1.0e-6` = 1 μm | |
| `c` (电容) | **法拉 (F)** | `8e-14` = 0.08 pF | |
| `nfin` | **无量纲** | `6` | FinFET 鳍片数 |
| `m` (multiplier) | **无量纲** | `64` | 器件复制倍数 |

```python
# ❌ 错误：0.168 被解析为 0.168 米 = 168,000,000 nm
dbReplaceProp(inst "l" "float" 0.168)

# ✅ 正确：168 nm = 1.68e-7 米
dbReplaceProp(inst "l" "float" 1.68e-7)

# ✅ 正确：0.08 pF = 8e-14 法拉
dbReplaceProp(inst "c" "float" 8e-14)
```

### 4.5 set_instance_params 用法

> **⚠️ SMIC 12nm 参数命名注意事项**：
> - **原理图 CDF 参数**：`l=`, `nfin=`, `fingers=`（手指数量），`m=`（并联倍数）
> - **Spectre 网表参数**：`l=`, `nfin=`, `nf=`（手指数量），`mr=`（并联倍数）
> - 两者不通用！用错会导致参数不生效或 CDF 回调错误

```python
from virtuoso_bridge.virtuoso.schematic.params import set_instance_params

# 修改 MOS 参数 (会触发 CDF 回调，SMIC 12nm 必须用 fingers 和 m)
set_instance_params(client, "M1", l="168n", nfin="6", fingers="8", m="64", param_filters=None)

# 修改电容
set_instance_params(client, "Cc", c="0.08p")

# 禁用 CDF filter (用于 FinFET nfin 等特殊参数，SMIC 12nm 必须加)
set_instance_params(client, "M1", nfin="6", fingers="8", m="64", param_filters=None)
```

### 4.6 参数验证流程

```python
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic

# 读取原理图验证参数
data = read_schematic(client, "work_ai", "opamp_two_stage")
for inst in data["instances"]:
    name = inst["name"]
    params = inst.get("params", {})
    print(f"  {name}: l={params.get('l')} nfin={params.get('nfin')} m={params.get('m')}")
```

---

## 5. Spectre 仿真流水线

### 5.1 Testbench 模板

```python
def build_testbench(cc, m1, m3, m5, m6, m7, stop="5G"):
    """构建 Spectre 网表，所有 MOS 固定 l=168n nfin=6。"""
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
ac ac start=1 stop={stop} dec=20

save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias
saveOptions options save=selected
'''
```

### 5.2 运行仿真

```python
from virtuoso_bridge.spectre.runner import SpectreSimulator

sim = SpectreSimulator.from_env(
    work_dir=str(WORK_DIR),
    output_format="psfascii",
)

tb_path = WORK_DIR / "tb_opamp.scs"
tb_path.write_text(netlist, encoding="utf-8")

result = sim.run_simulation(str(tb_path), {})
if not result.ok:
    print(f"FAILED: {result.errors[:3]}")
```

### 5.3 PDK 模型 include 要点

```python
# SMIC 12nm FinFET PDK 模型路径
PDK_MODEL = (
    "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0"
    "/smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0"
    "/models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
)

# 必须 include 的 section（顺序重要）
include "{PDK_MODEL}" section=tt_mos_varactor    # MOS + varactor
include "{PDK_MODEL}" section=tt_res_res3t_bjt_dio  # resistor, BJT, diode
include "{PDK_MODEL}" section=tt_mom_mim         # MOM + MIM capacitor
include "{PDK_MODEL}" section=pre_layout         # pre-layout settings
```

### 5.4 Spectre netlist 语法注意

- ❌ 不支持 `#` 注释，用 `//` 或省略
- ❌ `save I(V0)` 在 .scs 中不合法，会报语法错误
- ✅ `saveOptions options save=selected` 只保存声明的信号
- ✅ `soft_bin=allmodels` 自动选择 FinFET 模型 bin

### 5.5 仿真优化策略

**GBW 优化核心公式：** `GBW ≈ gm1 / (2π × Cc)`

| 操作 | 效果 | 副作用 |
|------|------|-------|
| 减小 Cc | ↑ GBW | ↑ 高频极点接近，可能影响稳定性 |
| 增大 m1 | ↑ gm1 → ↑ GBW | ↑ 功耗、输入电容 |
| 增大 m5 | ↑ 尾电流 → ↑ gm1 | ↑ 功耗 |
| 调整 m6/m7 | 改变 VOUT DC 工作点 | 影响第二级增益 |

**VOUT DC 工作点优化：**
- VOUT ≈ VDD/2 = 0.9V 为理想偏置点
- 增大 m7 (PMOS) → VOUT ↑
- 增大 m6 (NMOS) → VOUT ↓
- m6/m7 比值决定 DC 工作点

---

## 6. 结果解析与 Bode 图

### 6.1 PSF ASCII 解析

```python
from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii

result = parse_spectre_psf_ascii(Path("tb.raw/ac.ac"))
d = result.data

freq = d.get("freq")         # 频率数组 (Hz)
vout = d.get("VOUT")         # 复数电压 [real, imag, real, imag, ...]
dc_vout = d.get("dc_VOUT")   # DC 工作点
```

### 6.2 AC 指标计算

```python
import math
import cmath

# 复数转换（PSF ASCII 存储为 [real, imag, real, imag, ...]）
vout_complex = [complex(vout[i], vout[i+1]) for i in range(0, len(vout), 2)]

# 增益 (dB)
gain_db = [20 * math.log10(abs(v) * 2 + 1e-30) for v in vout_complex]

# 相位 (度)
phase_deg = [math.degrees(cmath.phase(v)) for v in vout_complex]

# DC 增益
dc_gain = gain_db[0]

# GBW (增益过 0 dB 的频率，log 插值)
for i in range(len(gain_db) - 1):
    if gain_db[i] >= 0 and gain_db[i+1] < 0:
        f1, f2 = freq[i], freq[i+1]
        g1, g2 = gain_db[i], gain_db[i+1]
        log_cross = math.log10(f1) + (math.log10(f2) - math.log10(f1)) * (-g1) / (g2 - g1)
        gbw = 10 ** log_cross
        break

# 相位裕度 (PM = 180 + phase at GBW)
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

### 6.3 DC 工作点解析

```python
# dc_VOUT 可能是 float, list, 或 complex
dc_vout_raw = result.data.get("dc_VOUT", 0)
if isinstance(dc_vout_raw, list):
    dc_vout = abs(dc_vout_raw[0])
elif isinstance(dc_vout_raw, complex):
    dc_vout = abs(dc_vout_raw)
else:
    dc_vout = abs(float(dc_vout_raw))
```

### 6.4 功率估算

```python
# IBIAS=10uA 通过电流镜复制
# M8(m=1) 镜像到 M7(m7), M9(m=1)->M5(m5), M3(m3)->M4(m3)
# 总电流 ≈ IBIAS × (m7 + m5 + m3)
ibias = 10e-6
total_m = m7 + m5 + m3
idc_est = ibias * total_m
power = VDD * idc_est  # VDD = 1.8V
```

### 6.5 Bode 图生成

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7),
    gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08})

ax1.semilogx(freq, gain_db, linewidth=1.5)
ax1.set_ylabel("Gain (dB)")
ax1.axhline(y=0, color="red", linestyle="--")  # 0 dB line
ax1.axvline(x=gbw, color="orange", linestyle="--")  # GBW

ax2.semilogx(freq, phase_deg, color="orange", linewidth=1.5)
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Phase (deg)")

plt.savefig("ac_bode.png", dpi=200, bbox_inches="tight")
```

---

## 7. 常见陷阱汇总

### Trap 1: edit() 内部嵌套 dbOpenCellViewByType → 原理图清空

| 错误 | 正确 |
|------|------|
| 在 `with client.schematic.edit()` 内部 `dbOpenCellViewByType` 同一个 cellview | 参数修改用 `execute_operations()` 单独执行 |

**后果：双重打开 → 数据库竞态 → 原理图全部清空！**

```python
# ❌ 致命
with client.schematic.edit(LIB, CELL) as sch:
    sch.add('let((cv) cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a") ...')

# ✅ 正确：execute_operations 单独执行
client.execute_operations([
    'cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a")',
    'let((i) i=car(setof(x cv~>instances x~>name=="M1")) when(i dbReplaceProp(i "m" "float" 64)))',
    'schCheck(cv)', 'dbSave(cv)', 'dbClose(cv)',
])
```

### Trap 2: SKILL 函数不存在

```skill
; ❌ dbGetPropValue 不存在！
l_val = dbGetPropValue(inst "l")

; ✅ 用 ~ 直接访问属性
l_val = inst~>l
```

### Trap 3: client.skill.eval() API 不存在

```python
# ❌ 错误
result = client.skill.eval(skill_code)  # AttributeError

# ✅ 正确
result = client.execute_operations([skill_code])
```

### Trap 4: procedure 嵌套在 let 里面

```skill
; ❌ SKILL 不支持嵌套函数定义
let((cv)
  procedure(foo() ...)  ; 语法错误！
)

; ✅ procedure 在顶层定义
procedure(foo() ...)
let((cv) foo())
```

### Trap 5: MOSFET Terminal 大小写错误

```skill
; ❌ 小写不存在
schAddInstTerm(inst "g" "VINP")  ; Terminal 'g' not found

; ✅ 必须大写 G/D/S/B
schAddInstTerm(inst "G" "VINP")
```

### Trap 6: 用 cdfSetParam 设置实例参数

```skill
; ❌ cdfSetParam 是 CDF 参数编辑，可能不生效
cdfSetParam(inst "l" 300e-9)

; ✅ 用 dbReplaceProp 设置实例属性
dbReplaceProp(inst "l" "float" 3e-7)
```

### Trap 7: dbOpenCellViewByType 只传 4 个参数

```skill
; ❌ 少了 view_type 参数
cv = dbOpenCellViewByType("work_ai" "inv" "schematic" "w")  ; 返回 nil

; ✅ 5 个参数
cv = dbOpenCellViewByType("work_ai" "inv" "schematic" "schematic" "w")
;                              lib      cell   view       view_type    mode
```

### Trap 8: l 参数单位错误 (⚠️ 新增)

```skill
; ❌ 0.168 = 0.168 米 = 168,000,000 nm（不是 168 nm！）
dbReplaceProp(inst "l" "float" 0.168)

; ✅ 168 nm = 1.68e-7 米
dbReplaceProp(inst "l" "float" 1.68e-7)
```

### Trap 9: save I(V0) 在 .scs 中不合法

```spectre
; ❌ 分支电流保存语法错误
save I(V0)  ; Syntax error: Unexpected open parenthesis

; ✅ 只保存节点电压
save VDD VSS VOUT net_x
```

### Trap 10: printf 输出不会被 Python 捕获

```skill
; ❌ printf 不会传回 Python
printf("M1 placed\n")

; ✅ 用表达式返回值
list("OK" "M1 placed")
```

### Trap 11: 电容 Terminal 用 G/D/S

```python
# ❌ 电容没有 G/D/S terminal
sch.add(schematic_label_instance_term("Cc", "G", "net_x"))

# ✅ 电容用 PLUS/MINUS
sch.add(schematic_label_instance_term("Cc", "PLUS", "net_x"))
sch.add(schematic_label_instance_term("Cc", "MINUS", "VOUT"))
```

### Trap 12: 忘记连接 M7 Gate 和 MOS Bulk

```python
# ❌ M7 Gate floating → 仿真不收敛
# ❌ MOS Bulk floating → *Warning* Terminal 'B' is floating

# ✅ 必须连接
sch.add(schematic_label_instance_term('M7', 'G', 'net_bias'))
# NMOS Bulk -> VSS
for name in ['M1', 'M2', 'M5', 'M6', 'M10']:
    sch.add(schematic_label_instance_term(name, 'B', 'VSS'))
# PMOS Bulk -> VDD
for name in ['M3', 'M4', 'M7', 'M8', 'M9']:
    sch.add(schematic_label_instance_term(name, 'B', 'VDD'))
```

---

## 8. 参考资源

| 文档 | 位置 |
|------|------|
| SKILL API 参考 | `src/virtuoso_bridge/virtuoso/schematic/ops.py` |
| SKILL 快速参考 | `docs/SKILL_QUICK_REFERENCE.md` |
| 参数修改 API | `src/virtuoso_bridge/virtuoso/schematic/params.py` |
| 原理图读取 API | `src/virtuoso_bridge/virtuoso/schematic/reader.py` |
| PSF 解析器 | `src/virtuoso_bridge/spectre/parsers.py` |
| Spectre 仿真器 | `src/virtuoso_bridge/spectre/runner.py` |

### 示例脚本

| 脚本 | 用途 |
|------|------|
| `examples/01_virtuoso/apply_optimal_opamp_params.py` | 将最优参数同步到原理图 |
| `examples/01_virtuoso/verify_opamp_params.py` | 验证原理图参数是否正确 |
| `examples/02_spectre/09_opamp_optimize_168n.py` | 多轮参数优化 sweep |
| `examples/02_spectre/plot_optimal_gbw_bode.py` | 生成 Bode 图 |

---

## 关键要点速记

```
✅ dbOpenCellViewByType 需要 5 个参数 (lib cell view view_type mode)
✅ procedure 必须在顶层定义，不能嵌套
✅ MOS 终端: G/D/S/B (大写!)
✅ 电容终端: PLUS/MINUS
✅ M7 栅极必须连接到 net_bias (不能悬空)
✅ 所有 MOS Bulk 必须连接 (NMOS→VSS, PMOS→VDD)
✅ edit() 内部不要再次 dbOpenCellViewByType
✅ printf 不会被 Python 捕获，用 list 返回
✅ l 参数单位是米 (SI): 168nm = 1.68e-7
✅ c 参数单位是法拉 (SI): 0.08pF = 8e-14
✅ save I(V0) 在 .scs 中不合法
✅ Spectre 不支持 # 注释
✅ soft_bin=allmodels 自动选择 FinFET 模型 bin
✅ GBW ≈ gm1/(2π×Cc)，减小 Cc 或增大 m1 可提高 GBW
✅ VOUT DC 工作点由 m6/m7 比值决定
```

---

**文档引用标识**: `SCHEMATIC_PLAYBOOK_20260430`
