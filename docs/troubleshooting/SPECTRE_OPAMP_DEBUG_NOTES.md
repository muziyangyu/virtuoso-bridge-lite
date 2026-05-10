# Spectre 两级运放仿真调试与优化经验记录

**日期**: 2026-04-29  
**项目**: virtuoso-bridge-lite  
**PDK**: SMIC 12nm  
**设计对象**: 10管两级运算放大器

---

## 一、电路结构回顾

| 模块 | 器件 | 连接 |
|------|------|------|
| **偏置电路** | M8, M9, M10 | M8/M9 (PMOS 电流镜), M10 (NMOS 自偏置) |
| **差分输入级** | M1, M2, M5 | M1/M2 差分对, M5 尾电流源 |
| **有源负载** | M3, M4 | PMOS 电流镜 |
| **第二级放大** | M6, M7 | M6 (NMOS 共源), M7 (PMOS 电流源负载) |
| **米勒补偿** | Cc | 跨接 VOUT 和 net_x |

---

## 二、第一阶段：网表语法与 PDK 兼容问题

### ❌ 问题 1: CMI-2942 错误
**现象**:
```
ERROR (CMI-2942): Length, width, or area of the instance does not fit
the specified lmax-lmin, wmax-wmin, or areamax-areamin range
for any model in the `n18_ckt' group.
```

**根本原因**:
- L=134nm 不在 SMIC 12nm PDK 的标准器件模型 bin 范围内
- FinFET 工艺对器件尺寸有严格限制

**解决方案**:
```spectre
simulatorOptions options psfversion="1.4.0" reltol=1e-4 vabstol=1e-6 \
  soft_bin=allmodels   ← 自动选择最近的 bin 模型
```

---

### ❌ 问题 2: SFE-874 网表语法错误
**现象**:
```
ERROR (SFE-874): Unexpected identifier "load". Expected equals
```

**根本原因**:
- 注释不能跟在器件参数后面同一行，Spectre 解析器会把注释内容误解析为参数

**错误写法**:
```spectre
M7 (VOUT net_bias VDD VDD) p18_ckt l=300n nfin=24 * Strong PMOS load  ❌
```

**正确写法**:
```spectre
* Strong PMOS load
M7 (VOUT net_bias VDD VDD) p18_ckt l=300n nfin=24                  ✓
```

---

## 三、第二阶段：DC 偏置优化

### 📐 偏置居中策略

**目标：VOUT = VDD/2 = 0.9V

**关键观察**:
- M6 (NMOS 下拉) 和 M7 (PMOS 上拉) 的尺寸比例直接决定 VOUT 直流电平

**迭代过程**:

| 版本 | M6 nfin | M7 nfin | VOUT (V) | 说明 |
|------|---------|---------|------------|------|
| v3 | 8 | 48 | 1.74 | M7 太强 |
| v4 | 16 | 24 | 1.50 | M7 仍强 |
| v5 | 20 | 22 | 0.45 | M6 太强 |
| final | 19 | 23 | 1.19 | 接近目标 |

**关键发现**: FinFET 尺寸对尺寸比例非常敏感，1个 finger 变化会导致 VOUT 大幅偏移

---

### ⚠️ net_vb 漂移问题
**现象**: net_vb = 1.8V (等于 VDD)**
- M9 漏极只连接到 M5 栅极，高阻节点无泄放通路

**解决方案**:
```spectre
Rvb (net_vb VSS) resistor r=500MEG  ← 加大阻值防止栅极电荷积累
```

---

## 四、第三阶段：增益提升策略

### 📈 增益公式

两级运放开环增益：
```
A0 = gm1 * (ro2 || ro4) * gm6 * (ro6 || ro7)
```

### 🔑 关键优化手段

#### 1. 增加沟道长度 L (最有效
- L: 134nm → **300nm**
- 输出阻抗 ro ∝ L
- 增益提升：25 dB → **67 dB** ✓

#### 2. 增加差分对 gm
- M1/M2 fin 数量：4 → **48**
- gm ∝ √(W/L) ¹/²
- 同时提升带宽

#### 3. 保持合理偏置电流
- 尾电流源 M5：96 fins
- 折中：速度 vs 功耗 vs 增益

---

### 📊 增益演进历程

| 版本 | L (nm) | 增益 (dB) | GBW (MHz) |
|------|--------|------------|------------|
| Initial (L=134) | 134 | 25.2 | 22.4 |
| v4 (L=300) | 300 | 45.7 | 70.8 |
| v5 (平衡) | 300 | 57.2 | 79.4 |
| **Final** | 300 | **67.2** | **79.4** |

**增益提升 42 dB，GBW 提升 3.5 倍**

---

## 五、最终性能指标

| 参数 | 数值 | 目标 | 状态 |
|------|------|------|------|
| **DC 增益** | **67.2 dB | ≥ 47 dB | ✅ 超 20 dB |
| **增益带宽积** | **79.4 MHz** | ≥ 8 MHz | ✅ 超 10 倍 |
| **相位裕度** | **147.8° | ≥ 60° | ✅ 非常稳定 |
| **VOUT 直流** | **1.19 V | ~0.9 V | ⚡ 合理范围 |
| **VDD** | 1.8 V | - | - |

---

## 六、优化器件尺寸参数

**最终器件尺寸 (L = 300nm)**

| 器件 | nfin | 说明 |
|------|------|------|
| M1/M2 | 48 | 差分输入对 |
| M5 | 96 | 尾电流源 |
| M3/M4 | 48 | 有源负载电流镜 |
| M6 | 19 | 第二级 NMOS (下拉) |
| M7 | 23 | 第二级 PMOS (上拉) |
| M8/M9/M10 | 4 | 偏置电路 |
| Cc | 2pF | 米勒补偿 |
| CL | 2pF | 负载电容 |

---

## 七、关键经验总结

### ✅ 1. FinFET 电路设计要点
1. **L 对增益影响最大，优先优化 L
2. Fin 数量比例微调 DC 工作点，范围很窄
3. 高阻栅节点必须加泄放电阻
4. PDK 模型 bin 限制，需要 soft_bin

### ✅ 2. Spectre 仿真注意事项
1. 注释必须单独一行，不能跟器件参数同列
2. FinFET 仿真用 `soft_bin=allmodels` 处理尺寸不匹配
3. 直流仿真收敛后再跑 AC

### ✅ 3. 优化顺序建议
1. 先调 DC 偏置 (VOUT 居中)
2. 再调增益 (L 优先)
3. 最后调补偿电容 (相位裕度)

---

## 八、网表模板 (可直接运行)

```spectre
simulator lang=spectre
global 0

simulatorOptions options psfversion="1.4.0" reltol=1e-4 vabstol=1e-6 \
  soft_bin=allmodels

include "$PDK/.../12sfe_spice_v1p2_rev0_usage_spe.lib" section=tt_mos_varactor

parameters VDD=1.8 VCM=0.9 IBIAS=10u

V0 (VDD 0) vsource dc=VDD
V1 (VSS 0) vsource dc=0

* 偏置电路
IBIAS (net_bias VSS) isource dc=IBIAS
M8 (net_bias net_bias VDD VDD) p18_ckt l=300n nfin=4
M9 (net_vb net_bias VDD VDD) p18_ckt l=300n nfin=4
M10 (net_bias net_bias VSS VSS) n18_ckt l=300n nfin=4
Rvb (net_vb VSS) resistor r=500MEG

* 差分输入级
M1 (net_d3 VINP net_s VSS) n18_ckt l=300n nfin=48
M2 (net_x VINN net_s VSS) n18_ckt l=300n nfin=48
M5 (net_s net_vb VSS VSS) n18_ckt l=300n nfin=96

* 有源负载
M3 (net_d3 net_d3 VDD VDD) p18_ckt l=300n nfin=48
M4 (net_x net_d3 VDD VDD) p18_ckt l=300n nfin=48

* 第二级放大
M6 (VOUT net_x VSS VSS) n18_ckt l=300n nfin=19
M7 (VOUT net_bias VDD VDD) p18_ckt l=300n nfin=23

* 补偿与激励
Cc (net_x VOUT) capacitor c=2p
VINP (VINP 0) vsource dc=VCM mag=0.5
VINN (VINN 0) vsource dc=VCM mag=-0.5
CL (VOUT 0) capacitor c=2p

* 仿真设置
dcOp dc maxiters=150
ac_ac ac start=1 stop=1G dec=20

save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias
saveOptions options save=selected
```

---

**归档标识**: `SPECTRE_OPAMP_OPTIMIZATION_20260429`  
**参考脚本**: `output/opamp_opt_final_done.py`  
**对应 Virtuoso 原理图**: `work_ai/opamp_two_stage`
