# SMIC 12nm SFE PDK 探索报告

## 概述

本报告详细分析了 SMIC 12nm SFE（SMIC FinFET Embedded）工艺的 PDK（Process Design Kit）结构。

**PDK 版本**: SPDK12SFE_0818_OA_CDS_V1.20_REV0_0  
**工艺节点**: 12nm FinFET  
**工作电压**: 0.8V (核心), 1.8V (IO)  
**金属层配置**: 1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK  
**技术文件版本**: techVersion("1.0")  

---

## 1. PDK 库信息

### 库名: `smic12sf`

**器件单元总数**: 165 个

---

## 2. 器件分类

### 2.1 MOS 晶体管 (21 个)

#### NMOS 器件:
| 器件名 | 描述 |
|--------|------|
| `n08_ckt` | 0.8V 常规阈值 NMOS (SVT) |
| `n08_dnw_ckt` | 0.8V DNW NMOS |
| `nlvt08_ckt` | 0.8V 低阈值 NMOS (LVT) |
| `nlvt08_dnw_ckt` | 0.8V DNW LVT NMOS |
| `nhvt08_ckt` | 0.8V 高阈值 NMOS (HVT) |
| `nhvt08_dnw_ckt` | 0.8V DNW HVT NMOS |
| `nulvt08_ckt` | 0.8V 超低阈值 NMOS (ULVT) |
| `nulvt08_dnw_ckt` | 0.8V DNW ULVT NMOS |
| `n18_ckt` | 1.8V NMOS |
| `n18_dnw_ckt` | 1.8V DNW NMOS |
| `n18ud12_ckt` | 1.8V 1.2V 耐压 NMOS |
| `n18ud12_dnw_ckt` | 1.8V 1.2V 耐压 DNW NMOS |
| `n18ud15_ckt` | 1.8V 1.5V 耐压 NMOS |
| `n18ud15_dnw_ckt` | 1.8V 1.5V 耐压 DNW NMOS |

#### PMOS 器件:
| 器件名 | 描述 |
|--------|------|
| `p08_ckt` | 0.8V 常规阈值 PMOS (SVT) |
| `plvt08_ckt` | 0.8V 低阈值 PMOS (LVT) |
| `phvt08_ckt` | 0.8V 高阈值 PMOS (HVT) |
| `pulvt08_ckt` | 0.8V 超低阈值 PMOS (ULVT) |
| `p18_ckt` | 1.8V PMOS |
| `p18ud12_ckt` | 1.8V 1.2V 耐压 PMOS |
| `p18ud15_ckt` | 1.8V 1.5V 耐压 PMOS |

#### 可变 MOS 电容:
| 器件名 | 描述 |
|--------|------|
| `pvar08_ckt` | 0.8V 可变 MOS 电容 |
| `pvar08_ckt_rf` | 0.8V RF 可变 MOS 电容 |
| `pvar18_ckt` | 1.8V 可变 MOS 电容 |
| `pvar18_ckt_rf` | 1.8V RF 可变 MOS 电容 |

---

### 2.2 无源器件

#### 电容器 (14 个):
| 器件名 | 描述 |
|--------|------|
| `mim_ckt` | MIM 电容器 |
| `mom_2t_1p25` | 2 端口 MOM 电容 (1.25V) |
| `mom_3t_1p25` | 3 端口 MOM 电容 (1.25V) |
| `mom_4t_1p25` | 4 端口 MOM 电容 (1.25V) |
| `mom_5t_1p25` | 5 端口 MOM 电容 (1.25V) |
| `mom_hq_2t` | 高品质 2 端口 MOM 电容 |
| `mom_hq_3t` | 高品质 3 端口 MOM 电容 |
| `mom_hq_3t_rf` | 高品质 RF 3 端口 MOM 电容 |
| `mom_hq_4t` | 高品质 4 端口 MOM 电容 |
| `mom_hq_5t` | 高品质 5 端口 MOM 电容 |
| `mom_ulc_2t` | 超低电容 2 端口 MOM 电容 |
| `mom_ulc_3t` | 超低电容 3 端口 MOM 电容 |
| `mom_ulc_4t` | 超低电容 4 端口 MOM 电容 |
| `mom_ulc_5t` | 超低电容 5 端口 MOM 电容 |

#### 电阻器 (15 个):
| 器件名 | 描述 |
|--------|------|
| **金属电阻** | |
| `rm1_ckt` | M1 金属电阻 |
| `rm2_ckt` | M2 金属电阻 |
| `rm3_ckt` | M3 金属电阻 |
| `rm4_ckt` | M4 金属电阻 |
| `rm5_ckt` | M5 金属电阻 |
| `rm6_ckt` | M6 金属电阻 |
| `rm7_ckt` | M7 金属电阻 |
| `rtm1_ckt` | TM1 顶层金属电阻 |
| `rtm2_ckt` | TM2 顶层金属电阻 |
| `ralpa_ckt` | ALPA 铝层电阻 |
| **多晶硅电阻** | |
| `rhrpo_2t_ckt` | 高阻多晶硅电阻 (2 端口) |
| `rhrpo_3t_ckt` | 高阻多晶硅电阻 (3 端口) |
| **阱电阻** | |
| `rnwsti_2t_ckt` | N 阱 STI 电阻 (2 端口) |
| `rnwsti_3t_ckt` | N 阱 STI 电阻 (3 端口) |
| **栅电阻** | |
| `NGR` | N 型栅电阻 |
| `PGR` | P 型栅电阻 |

---

### 2.3 二极管 (7 个)

| 器件名 | 描述 |
|--------|------|
| `ndio08_ckt` | 0.8V N 型二极管 |
| `ndio18_ckt` | 1.8V N 型二极管 |
| `pdio08_ckt` | 0.8V P 型二极管 |
| `pdio18_ckt` | 1.8V P 型二极管 |
| `dnwdio` | DNW 二极管 |
| `nwdio` | N 阱二极管 |
| `rwdio` | R 阱二极管 |

---

### 2.4 BJT 双极型晶体管 (4 usable in schematic)

> ⚠️ PDK 库中有名称带 `_ckt` 后缀的 BJT 单元（如 `pnp18a8_ckt`），但它们**没有 schematic symbol 视图**，无法在原理图中使用。以下仅列出可在原理图中放置的器件。

| 器件名 | 描述 | 可用视图 |
|--------|------|---------|
| `npn08` | 0.8V NPN 管 (C, B, E) | symbol ✓ |
| `npn18` | 1.8V NPN 管 (C, B, E) | symbol ✓ |
| `pnp08` | 0.8V PNP 管 (C, B, E) | symbol ✓ |
| `pnp18` | 1.8V PNP 管 (C, B, E) | symbol ✓ |

不可用（仅有 layout，无 symbol）:
`npn08a2p56_ckt`, `npn08a4_ckt`, `npn18a3_ckt`, `npn18a8_ckt`, `pnp08a2p56_ckt`, `pnp08a4_ckt`, `pnp18a3_ckt`, `pnp18a8_ckt`

---

### 2.5 ESD 保护器件 (10 个)

| 器件名 | 描述 |
|--------|------|
| `n18_esd` | 1.8V NMOS ESD |
| `ndio18_esd` | 1.8V N 二极管 ESD |
| `ngdio18_esd` | 1.8V N 栅二极管 ESD |
| `pdio18_esd` | 1.8V P 二极管 ESD |
| `pgdio18_esd` | 1.8V P 栅二极管 ESD |
| `npn5_esd` | 5 指 NPN ESD |

---

### 2.6 其他器件

- **寄生器件**: `*_parasitic_*` 系列 (3T, 4T, 5T 等寄生提取器件)
- **RF 器件**: `RF*` 系列 (射频专用器件)

---

## 3. 典型器件参数

### MOS 晶体管参数

基于 PDK 中 CDF 和器件分析，MOS 器件支持以下参数化:

| 参数名 | 描述 | 典型范围 |
|--------|------|---------|
| `l` | 栅长 | 0.014um - 10um |
| `w` | 栅宽 | 0.1um - 100um |
| `nf` | 指状数 (fingers) | 1 - 1000 |
| `m` | 并联倍数 (multiplier) | 1 - 100 |
| `sa` | 源极延伸 | - |
| `sb` | 漏极延伸 | - |
| `sd` | 源漏间距 | - |

### MOM 电容参数

| 参数名 | 描述 |
|--------|------|
| `w` | 电容宽度 |
| `l` | 电容长度 |
| `nf` | 指状数 |
| `m` | 并联数 |

### 电阻参数

| 参数名 | 描述 |
|--------|------|
| `w` | 电阻宽度 |
| `l` | 电阻长度 |
| `m` | 并联数 |
| `seg` | 分段数 |

---

## 4. 层定义 (Layer Definitions)

### 4.1 基本工艺层

| 层名 | 层号 | 缩写 | 描述 |
|------|------|------|------|
| `AA` | 50009 | AA | 有源区 (Active Area) |
| `FIN` | 50137 | FIN | FinFET 鳍 |
| `GT` | 50028 | GT | 栅极 (Gate) |
| `DG` | 50027 | DG | 双栅 |
| `P2` | 50029 | P2 | 第二多晶 |
| `SN` | 50036 | SN | N 型源漏注入 |
| `SP` | 50038 | SP | P 型源漏注入 |
| `NW` | 50013 | NW | N 阱 |
| `DNW` | 50018 | DNW | 深 N 阱 |
| `NPAA` | 50011 | NPAA | N 型 AA 注入 |
| `PPAA` | 50012 | PPAA | P 型 AA 注入 |

### 4.2 金属互连层

| 层名 | 层号 | 缩写 | 描述 |
|------|------|------|------|
| `M0` | 50054 | M0 | 第 0 层金属 (局部互连) |
| `M0C` | 50106 | M0C | M0 切割层 |
| `M1` | 50056 | M1 | 第 1 层金属 |
| `M2` | 50057 | M2 | 第 2 层金属 |
| `M3` | 50058 | M3 | 第 3 层金属 |
| `M4n` | 50059 | M4n | 第 4 层金属 (窄) |
| `M5n` | 50060 | M5n | 第 5 层金属 (窄) |
| `M6n` | 50061 | M6n | 第 6 层金属 (窄) |
| `M7n` | 50062 | M7n | 第 7 层金属 (窄) |
| `TM1` | 50115 | TM1 | 顶层金属 1 (厚) |
| `TM2` | 50117 | TM2 | 顶层金属 2 (厚) |
| `ALPA` | 50078 | ALPA | 铝焊盘层 |
| `PA` | 50075 | PA | 钝化层开口 |
| `BUMP` | 50156 | BUMP | 凸块层 |

### 4.3 通孔层 (Via)

| 层名 | 层号 | 缩写 | 描述 |
|------|------|------|------|
| `V0` | 50103 | V0 | M0 - M1 通孔 |
| `V1` | - | V1 | M1 - M2 通孔 |
| `V2` | - | V2 | M2 - M3 通孔 |
| `V3` | - | V3 | M3 - M4 通孔 |
| `V4` | - | V4 | M4 - M5 通孔 |
| `V5` | - | V5 | M5 - M6 通孔 |
| `V6` | - | V6 | M6 - M7 通孔 |
| `TV1` | 50116 | TV1 | M7 - TM1 通孔 |
| `TV2` | 50118 | TV2 | TM1 - TM2 通孔 |
| `BV1` | 50191 | BV1 | TM2 - ALPA 通孔 |
| `BV2` | 50192 | BV2 | - |

### 4.4 特殊用途层

| 层名 | 层号 | 用途 |
|------|------|------|
| `TXT` | 50082 | 文本标注 |
| `CELLB` | 50144 | 单元边界 |
| `CHIPB` | 50085 | 芯片边界 |
| `LOGO` | 50025 | Logo 层 |
| `MARK*` | 各种 | 对准标记 |
| `ESD*` | 各种 | ESD 标识层 |

---

## 5. 工艺技术文件信息

### 5.1 基本设置

```
techVersion: 1.0
processNode: 0.014 (14nm 标称节点)
mfgGridResolution: 0.001 um (1nm)
```

### 5.2 单位设置

- **版图单位**: micron (微米)
- **数据库单位**: 1000 dbu/um (1nm 分辨率)
- **原理图单位**: inch

### 5.3 金属选项

```
METAL_OPTION: 1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK
```

含义:
- `1P9M`: 1 层 Poly + 9 层金属
- `DV`: 双电压域
- `3DM`: 3 层致密金属
- `Q1_3Q2`: Q1 和 Q2 品质因子配置
- `2TMa`: 2 层厚顶层金属选项 a
- `ALPA`: 铝焊盘层
- `14SHK`: 14 层屏蔽层配置

---

## 6. 总结

### PDK 特点:

1. **完整的 FinFET 器件库**: 支持多种阈值电压 (ULVT/LVT/SVT/HVT) 和耐压等级
2. **丰富的无源器件**: MIM/MOM 电容、多种金属/多晶硅/阱电阻
3. **ESD 和 RF 专用器件**: 专门的 ESD 保护结构和射频优化器件
4. **9 层金属互连**: 包含局部互连 M0、7 层标准金属、2 层厚顶层金属
5. **高分辨率**: 1nm 制造网格精度

### Schematic 使用注意事项

1. **Symbol viewType**: 所有 PDK symbol 的 viewType 为 `"schematicSymbol"` (不是 `"schematic"`)。打开方式：
   ```skill
   dbOpenCellViewByType("smic12sf" "pnp18" "symbol" "schematicSymbol" "r")
   ```
2. **BJT 可用性**: 仅有 `pnp08`、`pnp18`、`npn08`、`npn18` 四个 BJT 有 symbol 视图，其余带 `_ckt` 后缀的 BJT 仅有 layout 视图
3. **PDK Resistor 终端**: `rhrpo_3t_ckt` 和 `rnwsti_3t_ckt` 的终端为 PLUS, MINUS, BULK（第三个为衬底连接）

### 主要器件类别统计:

| 类别 | 数量 |
|------|------|
| MOS 晶体管 | 21 |
| 可变 MOS 电容 | 4 |
| MIM/MOM 电容 | 14 |
| 电阻器 | 15 |
| 二极管 | 7 |
| BJT 晶体管 | 4 (usable) | 其余 8 个仅为 layout view，无 symbol |
| ESD 器件 | 6 |
| **总计 (主要器件)** | **79** |

剩余为寄生提取器件、RF 专用器件和内部使用器件。

---

**探索完成时间**: 2026年4月28日  
**探索方法**: 远程文件系统分析 + techfile 解析 + 器件分类文件分析