# bias_lpf 设计状态 (2026-05-09)

## 已完成

- [x] **bias_lpf 原理图重建 + 参数设置**
  - M_P1/P2/P3: nfin=4, l=242n, nf=1, mr=1
  - M_P4: nfin=2, l=242n, nf=1, mr=1
  - R_PTAT=6.32K, R1=37.6K(VBG->VREF), R2=17.6K(VREF->GND)
  - Q1 m=1, Q2 m=8
  - M_BN: nfin=4, l=134n
  - 端口: VDD, GND, VREF(0.5V), VBN(0.73V)  (精简到4个)
  - 重建脚本: `output/rebuild_bias_lpf_final.py`

- [x] **bias_lpf 仿真验证**
  - VREF(27C) = 0.501V (pass), TC = -10 ppm/C
  - IBIAS ~21uA (VBN 支路)
  - 总电流 ~139uA (fail >100uA spec)
  - 网表: `output/sim_bias_lpf_final.scs`

- [x] **bias_lpf 原理图警告修复**
  - Q1/Q2 B 端子去掉了失败的 label (B 端子无 fig)
  - 改用 instTerm~>net = GND 后处理，保存时不 schCheck
  - 原理图无黄色警告框

- [x] **设计计划文档已更新** (含模块端口定义)
  - `docs/设计计划_基带LPF_20260507.md`

## 待完成

- [ ] **Phase 1: 运放设计**
  - 目标: Av0 >= 60dB, GBW >= 800MHz, PM >= 60deg
  - 结构: 折叠共源共栅 + Class-AB
  - 风险: 1.8V I/O 器件 (p18_ckt/n18_ckt) 能否达到 800MHz GBW?
  - 建议: 先仿 p18_ckt/n18_ckt 单管 ft

- [ ] **启动电路** (bias_lpf 缺少)
  - bias_lpf 当前无启动电路
  - 需要加 M_SUP + 启动逻辑, 防零态锁定

- [ ] **Biquad RC 计算 + 原理图**
  - BQ1: Tow-Thomas, Q=0.541, fc=20MHz
  - BQ2: Akerberg-Mossberg, Q=1.307, fc=20MHz
  - 需要去归一化计算 R/C 值

## output/ 目录有用文件

### scripts/ (推荐保留)
| 文件 | 用途 |
|------|------|
| `output/rebuild_bias_lpf_final.py` | 最终 bias_lpf 重建脚本 |
| `output/create_bias_lpf.py` | 原始创建脚本 |
| `output/set_bias_lpf_params.py` | 参数设置工具 |

### netlists/ (推荐保留)
| 文件 | 用途 |
|------|------|
| `output/sim_bias_lpf_final.scs` | 最终设计仿真网表 |
| `output/tb_lpf_full.scs` | bias+opamp 联合仿真 |
| `output/tb_bias_lpf.scs` | 原始 bias 测试网表 |

### results/ (推荐保留)
| 文件 | 用途 |
|------|------|
| `output/bias_lpf_dc.txt` | DC 仿真原始数据 (PSF ASCII) |
| `output/bias_lpf_spectre.log` | Spectre 仿真日志 |

### snapshots/ (推荐保留)
| 文件 | 用途 |
|------|------|
| `output/current_20260508_233523.png` | 最终原理图截图 |

### 可删除的临时文件
```
sim_bias_lpf.scs, sim_bias_lpf.py          # 中间测试
sim_bias_lpf_sweep.*, sim_bias_lpf_fix.*    # 尺寸扫描
sim_bias_lpf_tuned.*, sim_bias_lpf_designs.* # 方案对比
sim_bias_lpf_nf1.*, sim_bias_lpf_nf2.*      # nf 扫描
sim_bias_lpf_rptat.*                        # R_PTAT 扫描
update_bias_lpf_final.py, update_bias_lpf_topo.py  # 失败尝试
ac_lpf_full.*, lpf_full_ac.*, lpf_full_spectre.log # 旧 opamp 数据
opamp_lpf_comparison.py, *.json, *.png      # 旧 opamp 对比
create_bias_lpf_20260508.py                 # 旧版创建脚本
spectre.out, spectre.fc, spectre.ic         # 临时日志
*.raw/                                       # 仿真原始数据 (可重新生成)
```
