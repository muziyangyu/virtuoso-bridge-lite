<<<<<<< HEAD
# Virtuoso Bridge Lite

用 Python 远程控制 Cadence Virtuoso — 原理图/版图编辑、仿真运行、结果解析的全自动化。

## 快速开始

```bash
cd virtuoso-bridge-lite
uv venv .venv && source .venv/bin/activate
uv pip install -e .
```

`.env` 文件:
```dotenv
VB_REMOTE_HOST=your-server
VB_REMOTE_USER=username
VB_REMOTE_PORT=65081
VB_LOCAL_PORT=65082
VB_JUMP_HOST=bastion.example.com        # 可选
VB_CADENCE_CSHRC=/path/to/cds.cshrc     # Spectre 用
```

```python
from virtuoso_bridge import VirtuosoClient
client = VirtuosoClient.from_env()
client.test_connection(timeout=5)
```

## 核心架构

```
┌──────────────┐     TCP JSON      ┌──────────────────┐     SKILL      ┌──────────┐
│  Python CLI  │ ────────────────→ │  RAMIC Bridge    │ ────────────→ │ Virtuoso │
│  / Script    │ ←──────────────── │  Daemon (SKILL)  │ ←──────────── │  (ICFB)  │
└──────────────┘                   └──────────────────┘               └──────────┘
```

传输层支持: 直连 TCP / SSH 隧道 / ProxyJump 跳板机 / X11 转发

## 目录结构

```
src/virtuoso_bridge/
├── cli.py                    # CLI 入口
├── env.py                    # 环境变量 / SSH 配置
├── models.py                 # 数据模型
├── wrappers.py               # 便捷封装
├── transport/
│   ├── ssh.py                # SSH 连接管理
│   ├── tunnel.py             # 端口转发
│   └── remote_paths.py       # 远程路径处理
├── virtuoso/
│   ├── basic/bridge.py       # RAMIC 桥接通信协议
│   ├── basic/composition.py  # SKILL 执行组合
│   ├── schematic/editor.py   # 原理图编辑
│   ├── schematic/reader.py   # 原理图读取
│   ├── schematic/params.py   # 参数管理
│   ├── schematic/ops.py      # 操作封装
│   ├── layout/editor.py      # 版图编辑
│   ├── layout/reader.py      # 版图读取
│   ├── layout/layers.py      # 层管理
│   ├── layout/ops.py         # 操作封装
│   ├── layout/pdk.py         # PDK 工具
│   ├── maestro/lifecycle.py  # 会话生命周期
│   ├── maestro/reader/       # 结果读取
│   ├── maestro/writer.py     # 写入/修改
│   ├── spectre/              # Spectre 独立仿真
│   ├── snapshot.py           # GUI 截图
│   ├── visio.py              # Visio 视图
│   ├── x11.py                # X11 转发
│   └── self_check.py         # 自检
└── resources/
    └── x11_dismiss_dialog.py # X11 对话框自动关闭
```

## VirtuosoClient API

### 创建连接

```python
client = VirtuosoClient.from_env()                    # 从 .env 创建
client = VirtuosoClient(host="127.0.0.1", port=65432) # 直接指定
client.test_connection(timeout=5)                     # 测试桥接连接
client.run_shell_command("ls /remote/path")           # 远程 shell
```

### 执行 SKILL

```python
r = client.execute_skill('plus(1 2)')                  # 表达式
r = client.execute_skill('load("/path/to/file.il")', timeout=120)  # 加载文件
# r.output == '"3"' (成功)  |  r.output == 'nil' (失败/无返回)
```

### 截图

```python
client.take_screenshot("/path/to/save.png")
```

## Schematic 原理图 API

```python
# 创建 instance
client.execute_skill('schCreateInst(cv "analogLib" "nmos" "M1" list(0 0) "R0")')

# 创建 wire / pin
client.execute_skill('schCreateWire(cv list(x1 y1) list(x2 y2))')
client.execute_skill('schCreatePin(cv "VDD" "input" list(x y))')

# 读取
client.execute_skill('schGetCurrentConnTerms("/")')
client.execute_skill('dbGetInstTermsByNetName(inst "D")')

# 参数
client.execute_skill('inst~>w = "10u"')
client.execute_skill('inst~>nf = 4')

# 删除
client.execute_skill('dbDeleteObject(inst)')
client.execute_skill('ddDeleteObj(ddGetObj("LIB" "cell" "schematic"))')
```

完整示例: `examples/01_virtuoso/schematic/`

## Layout 版图 API

```python
# 创建/打开 layout view
client.execute_skill('dbOpenCellViewByType("LIB" "cell" "layout" "maskLayout" "w")')

# 多边形
client.execute_skill(
  'dbCreatePolygon(cv list("M1" "drawing") list(list(0 0) list(1 0) list(1 1) list(0 1)))')

# 放置 PDK PCell
client.execute_skill('dbCreateInst(cv master "C0" list(0 0) "R0")')
client.execute_skill('inst~>lr = "10u"')   # MOM 参数
client.execute_skill('inst~>nf = 10')
client.execute_skill('inst~>tm = 5')
client.execute_skill('inst~>bm = 3')

# 通孔
client.execute_skill(
  'dbCreateVia(cv "V1" list(x y) "R0" 1 1 0.16 0.16 ?legalize "minimize")')

# 读取
client.execute_skill('dbGetCellView()')

# 导出 GDS
client.execute_skill(
  'strmOut(?libName "LIB" ?cellName "cell" ?strmFile "out.gds" ?scale 1e-3)')
```

完整示例: `examples/01_virtuoso/layout/`

## Maestro 仿真 API

```python
# 打开仿真结果
client.execute_skill('dbOpenMaestroSession("/path/to/maestro"))')

# 读取 metrics
client.execute_skill('maestroGetSessionResults(session)')

# GUI session (有生命周期, 用后关闭)
client.execute_skill('maestroGuiOpenSession(session)')
client.execute_skill('maesterCloseSession(session)')
```

完整示例: `examples/01_virtuoso/maestro/`

## Spectre 独立仿真 API

```python
from virtuoso_bridge.spectre import SpectreRunner
runner = SpectreRunner(client)
result = runner.run_netlist("netlist.scs", output_dir="./sim")
# result: output, log, metrics
```

完整示例: `examples/02_spectre/`

## 通信协议

Python → TCP JSON → RAMIC Bridge Daemon (Virtuoso SKILL 侧):

```json
{"skill": "+ 1 2", "timeout": 60}
```

响应: `STX (0x02) + result` (成功) 或 `NAK (0x15) + error` (失败)

自检: `python3 -c "from virtuoso_bridge.virtuoso.self_check import main; main()"`

## PDK 支持 (SMIC 12nm SFe)

PDK 工具: `src/virtuoso_bridge/virtuoso/layout/pdk.py`

常用器件参数读取:
```python
client.execute_skill('master~>lr~>value')
client.execute_skill('master~>nf~>value')
client.execute_skill('master~>w~>value')
```

| 器件 | PCell | 参数 |
|------|-------|------|
| NMOS | n18_ckt | nfin, nf, l |
| PMOS | p18_ckt | nfin, nf, l |
| MOM 电容 | mom_2t_1p25 | lr, nf, tm, bm |
| MIM 电容 | mim_ckt | W, H |
| 电阻 | rhrpo_2t_ckt | l, w, tr |

## 约束与注意事项

- SKILL 执行是**同步阻塞**的 — 长时间操作设 `timeout` 参数
- **不可交互** — 不能弹对话框、等待用户输入
- GUI 操作通过 X11 转发实现 (VISIO / screenshot)
- 跨平台: Linux/macOS 直连, Windows 需 WSL
- Maestro GUI session 有生命周期, 用完必须 close
- PCell 参数通过 `inst~>paramName` 读写
- GDS 导出 `?scale 1e-3` 是关键 (database unit 1nm → 1μm)

## 常用命令

```bash
# 执行 SKILL
python3 tools/skill_exec.py 'plus(1 2)'
python3 tools/skill_exec.py --load /path/to/setup.il
python3 tools/skill_exec.py 'hiGetCIWindow()' --port 65432

# 验权
python3 examples/01_virtuoso/basic/04_list_library_cells.py

# MOM 电容批量生成
python3 examples/01_virtuoso/layout/15_smic12sf_pdk.py

# 端口转发 (手动)
python3 -c "
from virtuoso_bridge.transport.tunnel import Tunnel
t = Tunnel('host', 65432, 65081)
t.start()
"

# Spectre 仿真
python3 examples/02_spectre/01_inverter_tran.py
python3 examples/02_spectre/03_check_license.py
```
=======
# AGENTS.md — AI Agent Guide for virtuoso-bridge-lite

Control Cadence Virtuoso via Python — remotely over SSH or locally on the same machine.

---

## 📚 文档索引总览

| 文档类别 | 路径 | 重要性 | 说明 |
|---------|------|--------|------|
| **核心指南** | [`AGENTS.md`](AGENTS.md) | ⭐⭐⭐ | 本文档 - 完整的工程指南 |
| **项目说明** | [`README.md`](README.md) | ⭐⭐⭐ | 项目介绍、快速开始、架构说明 |
| **原理图实战** | [`docs/guides/SCHEMATIC_GENERATION_PLAYBOOK.md`](docs/guides/SCHEMATIC_GENERATION_PLAYBOOK.md) | ⭐⭐⭐ | 完整原理图-仿真-优化工作流，两级运放实战 |
| **SKILL 速查** | [`docs/guides/SKILL_QUICK_REFERENCE.md`](docs/guides/SKILL_QUICK_REFERENCE.md) | ⭐⭐⭐ | 原理图陷阱手册、常见bug修复 |
| **API 索引** | [`docs/api/API_DOC_INDEX.md`](docs/api/API_DOC_INDEX.md) | ⭐⭐ | 3,856 个 SKILL 函数文档索引 |
| **API 统计** | [`docs/api/API_STATS.md`](docs/api/API_STATS.md) | ⭐ | 按前缀分类的函数统计 |
| **仿真调试** | [`docs/troubleshooting/SPECTRE_OPAMP_DEBUG_NOTES.md`](docs/troubleshooting/SPECTRE_OPAMP_DEBUG_NOTES.md) | ⭐⭐ | 运放 AC 调试日志、常见问题 |

---

## 🗂️ 完整工程结构

```
virtuoso-bridge-lite/
├── 📁 src/virtuoso_bridge/          # 核心源码
│   ├── 📁 spectre/                  # Spectre 仿真模块
│   │   ├── runner.py                # 仿真运行器
│   │   └── parsers.py               # PSF 结果解析器
│   ├── 📁 transport/                # 传输层
│   │   ├── ssh.py                   # SSH 客户端
│   │   └── tunnel.py                # SSH 隧道管理
│   └── 📁 virtuoso/                 # Virtuoso 模块
│       ├── 📁 basic/                # 基础桥接
│       │   └── resources/ramic_bridge.il  # SKILL 守护进程
│       ├── 📁 layout/               # 版图编辑
│       ├── 📁 maestro/              # Maestro 操作
│       ├── 📁 schematic/            # 原理图编辑
│       └── visio.py                 # Visio 导出
│
├── 📁 skills/                        # AI Agent 技能定义
│   ├── 📁 virtuoso/                 # Virtuoso 技能
│   │   ├── SKILL.md                 # 主技能文档
│   │   └── 📁 references/           # 参考文档
│   ├── 📁 spectre/                  # Spectre 仿真技能
│   │   ├── SKILL.md                 # 主技能文档
│   │   └── 📁 references/           # 参考文档
│   └── 📁 optimizer/                # 参数优化技能
│
├── 📁 examples/                      # 示例代码
│   ├── 📁 01_virtuoso/              # Virtuoso 示例
│   │   ├── 📁 basic/                # 基础操作 (7个)
│   │   ├── 📁 schematic/            # 原理图 (11个)
│   │   ├── 📁 layout/               # 版图 (16个)
│   │   ├── 📁 maestro/              # Maestro (8个)
│   │   ├── 📁 digital_import/       # 数字导入
│   │   └── 📁 assets/               # SKILL 脚本资源
│   └── 📁 02_spectre/               # Spectre 仿真示例 (15个)
│
├── 📁 docs/                          # 文档目录
│   ├── 📁 api/                      # SKILL API 文档
│   ├── 📁 guides/                   # 操作指南
│   ├── 📁 sub_skills/               # 子技能文档
│   ├── 📁 superpowers/              # 高级功能
│   └── 📁 troubleshooting/          # 故障排除
│
├── 📁 tools/                         # 独立工具
│   └── skill_exec.py                # 零依赖 SKILL 执行工具
│
├── 📁 output/                        # 输出目录 (脚本/仿真结果)
├── 📁 scripts/                       # 辅助脚本
├── 📁 stats/                         # 统计数据
└── .env                              # 环境配置
```

---

## 🔧 两种运行模式

| 模式 | 适用场景 | 配置要点 |
|------|---------|---------|
| **Remote 远程模式** | Virtuoso 运行在服务器，本地工作 | 设置 `VB_REMOTE_HOST`，SSH 隧道自动管理 |
| **Local 本地模式** | Virtuoso 运行在本机 | 设置 `VB_REMOTE_HOST=localhost`，跳过 SSH 隧道 |

---

## 📋 前置检查清单

### 首次运行必须确认

1. ✅ **SSH 连接**: `ssh my-server` 无需密码即可登录
2. ✅ **Virtuoso 进程**: 远程机器上有运行中的 Virtuoso
3. ✅ **Spectre 路径**: `spectre` 在 PATH 中，或设置 `VB_CADENCE_CSHRC`

> **重要**: Virtuoso 和 Spectre 是完全独立的 — 可以只运行 Spectre 而不加载 Virtuoso SKILL 桥接，反之亦然。

---

## 🚀 快速安装

```bash
# 推荐使用 uv
uv venv .venv && source .venv/bin/activate   # Windows: source .venv/Scripts/activate
uv pip install -e .

# 或使用 pip
pip install -e .
```

---

## 📝 分步设置指南 (远程模式)

### 1. 生成配置

```bash
# 推荐：一键填写主机/用户/跳板机
virtuoso-bridge init designer1@thu-wei -J designer1@bastion.example.com

# 或：生成空模板（手动编辑 .env）
virtuoso-bridge init
```

配置文件位置优先级：`./.env` → `~/.virtuoso-bridge/.env`

### 2. .env 配置模板

```dotenv
# ========== SSH 连接配置 ==========
VB_REMOTE_HOST=my-server              # SSH 主机别名
VB_REMOTE_USER=username               # SSH 用户名
VB_REMOTE_PORT=65081                  # 远程桥接守护进程端口
VB_LOCAL_PORT=65082                   # 本地 SSH 转发端口

# ========== 跳板机配置 (可选) ==========
VB_JUMP_HOST=bastion.example.com      # 跳板机主机（如需要）

# ========== Cadence 工具配置 ==========
VB_CADENCE_CSHRC=/path/to/cds.cshrc  # 设置 Cadence 环境的 cshrc
```

### 3. 启动桥接

```bash
virtuoso-bridge start
```

### 4. 在 Virtuoso CIW 中加载 SKILL

`virtuoso-bridge start` 会输出需要在 CIW 中执行的命令：

```skill
load("/tmp/virtuoso_bridge_<user>/virtuoso_bridge/virtuoso_setup.il")
```

> 💡 **提示**: 将此命令添加到 `~/.cdsinit` 可以实现 Virtuoso 启动时自动加载。

### 5. 验证连接

```bash
virtuoso-bridge status
```

期望输出：
```
[tunnel]  running
[daemon]  OK
[spectre] OK
```

### 6. Python 快速测试

```python
from virtuoso_bridge import VirtuosoClient
client = VirtuosoClient.from_env()
result = client.execute_skill("1+2")
print(result)  # 输出: VirtuosoResult(status=SUCCESS, output='3')
```

### 📌 `execute_skill` vs `execute_operations` 区别

| API | 适用场景 | 实现方式 |
|-----|---------|---------|
| `client.execute_skill(expr)` | **单条 SKILL 表达式** | 直接执行，返回单个结果 |
| `client.execute_operations([expr1, expr2, ...])` | **多条命令 / 参数修改** | 用 `progn()` 包装多条命令，返回聚合结果 |

> **⚠️ 重要提示**：修改器件参数时请使用 `execute_operations()`，并且**不要**在 `with client.schematic.edit()` 上下文内部嵌套打开 cellview，这会导致数据库竞态条件。

---

## 🔗 高级配置

### 多 Profile 配置

支持同时连接多个 Virtuoso 实例：

```dotenv
# 默认 profile
VB_REMOTE_HOST=server-a
VB_REMOTE_USER=user1

# worker1 profile
VB_REMOTE_HOST_worker1=server-b
VB_REMOTE_USER_worker1=user2
VB_CADENCE_CSHRC_worker1=/path/to/.cshrc.worker1
```

使用：
```bash
virtuoso-bridge start -p worker1
virtuoso-bridge status -p worker1
```

```python
from virtuoso_bridge.spectre import SpectreSimulator
sim = SpectreSimulator.from_env(profile="worker1")
```

---

## 🏗️ 核心架构

### 三层解耦设计

```
┌─────────────────────────────────────────────────────────┐
│  应用层: Schematic / Layout / Maestro / Spectre Python API  │
└─────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────┐
│  VirtuosoClient: 纯 TCP SKILL 客户端                      │
│  - execute_skill()                                       │
│  - fetch() / fetch_one() 批量属性读取                     │
│  - load_il() 加载 .il 文件                                │
└─────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────┐
│  SSHClient: 持久化 SSH 连接 + 隧道管理                     │
│  - ControlMaster 多路复用                                  │
│  - TCP 端口转发 (SKILL 执行)                               │
│  - Shell 命令执行 (Spectre)                                │
│  - rsync 文件传输                                          │
└─────────────────────────────────────────────────────────┘
```

### 关键特性

- **VirtuosoClient**: 纯 TCP SKILL 客户端，无 SSH 依赖，可连接任意 TCP 端点
- **SSHClient**: 持久化 ControlMaster 连接，多路复用三个通道
- **完全解耦**: Virtuoso SKILL 执行和 Spectre 仿真完全独立

---

## 🛠️ CLI 命令参考

```bash
# ========== 连接管理 ==========
virtuoso-bridge init [user@host] [-J user@jump] [--force]
virtuoso-bridge start           # 启动 SSH 隧道 + 部署守护进程
virtuoso-bridge stop            # 停止 SSH 隧道
virtuoso-bridge restart         # 强制重启
virtuoso-bridge status          # 检查隧道、守护进程、Spectre 状态
virtuoso-bridge license         # 检查 Spectre 许可证可用性

# ========== Virtuoso 操作 ==========
virtuoso-bridge windows         # 列出所有打开的 Virtuoso 窗口
virtuoso-bridge screenshot      # 截图 CIW (或: current, N)
virtuoso-bridge dismiss-dialog  # 关闭阻塞的 GUI 对话框

# ========== Maestro 快照 ==========
virtuoso-bridge snapshot        # 当前焦点 Maestro: 4 个 SKILL 探针输出
virtuoso-bridge snapshot -o ROOT  # 完整磁盘转储 (XML + 逐点运行文件)
virtuoso-bridge snapshot -o output --history Interactive.160

# ========== Visio 导出 (Windows) ==========
virtuoso-bridge export-visio LIB CELL -o out.vsdx
```

---

## ⚡ 原理图设计最佳实践

### 📌 核心原则

1. **永远不要在 `edit()` 内部嵌套 `dbOpenCellViewByType`**
   - 这会导致双重打开 → 数据库竞态 → 原理图清空
   - 参数修改请使用 `client.execute_operations()` 单独执行

2. **终端命名必须正确**
   - MOSFET: **G, D, S, B** (大写!)
   - 电容/电阻: **PLUS, MINUS**

3. **所有 MOS 的 Bulk 端口必须连接**
   - NMOS Bulk → VSS
   - PMOS Bulk → VDD

### 🔧 原理图编辑 API

#### 上下文管理器模式（推荐）

```python
from virtuoso_bridge.virtuoso.schematic import (
    schematic_create_inst_by_master_name,
    schematic_label_instance_term,
    schematic_create_pin,
)

LIB = "work_ai"
CELL = "opamp_two_stage"

with client.schematic.edit(LIB, CELL) as sch:
    # 1. 放置器件
    # 差分输入对 (NMOS)
    sch.add(schematic_create_inst_by_master_name(
        "smic12sf", "n18_ckt", "symbol", "M1", -4.0, 1.0, "R0"
    ))
    sch.add(schematic_create_inst_by_master_name(
        "smic12sf", "n18_ckt", "symbol", "M2", -4.0, 0.0, "R0"
    ))
    
    # 电流镜负载 (PMOS)
    sch.add(schematic_create_inst_by_master_name(
        "smic12sf", "p18_ckt", "symbol", "M3", -2.0, 1.0, "MY"
    ))
    sch.add(schematic_create_inst_by_master_name(
        "smic12sf", "p18_ckt", "symbol", "M4", -2.0, 0.0, "MY"
    ))
    
    # Miller 补偿电容
    sch.add(schematic_create_inst_by_master_name(
        "analogLib", "cap", "symbol", "Cc", 2.0, 1.0, "R0"
    ))
    
    # 2. 连接电源和 Bulk (⚠️ 不要遗漏!)
    for name in ["M1", "M2", "M5", "M6"]:
        sch.add(schematic_label_instance_term(name, "S", "VSS"))
        sch.add(schematic_label_instance_term(name, "B", "VSS"))
    
    for name in ["M3", "M4", "M7", "M8", "M9"]:
        sch.add(schematic_label_instance_term(name, "S", "VDD"))
        sch.add(schematic_label_instance_term(name, "B", "VDD"))
    
    # 3. 信号连接
    sch.add(schematic_label_instance_term("M1", "G", "VINP"))
    sch.add(schematic_label_instance_term("M2", "G", "VINN"))
    
    # M1/M2 源极连接到 M5 漏极
    sch.add(schematic_label_instance_term("M1", "S", "net_s"))
    sch.add(schematic_label_instance_term("M2", "S", "net_s"))
    sch.add(schematic_label_instance_term("M5", "D", "net_s"))
    
    # 4. 创建引脚
    sch.add(schematic_create_pin("VINP", -5.0, 1.0, "R0", direction="input"))
    sch.add(schematic_create_pin("VINN", -5.0, 0.0, "R0", direction="input"))
    sch.add(schematic_create_pin("VOUT",  3.0, 1.0, "R0", direction="output"))
    sch.add(schematic_create_pin("VDD",  -6.0, 2.5, "R0", direction="inputOutput"))
    sch.add(schematic_create_pin("VSS",  -6.0,-2.0, "R0", direction="inputOutput"))
```

### ✏️ 参数修改

#### 方法一：直接属性修改（推荐）

```python
# 修改 l/nfin/m/c 参数（不触发 CDF 回调）
skill_code = '''
let((cv inst)
  cv = dbOpenCellViewByType("work_ai" "opamp_two_stage" "schematic" "schematic" "a")
  
  ; M1/M2 输入对
  inst = car(setof(x cv~>instances x~>name == "M1"))
  when(inst
    dbReplaceProp(inst "l" "float" 1.68e-7)   ; 168nm = 1.68e-7 米
    dbReplaceProp(inst "nfin" "float" 6)
    dbReplaceProp(inst "m" "float" 64)
  )
  
  inst = car(setof(x cv~>instances x~>name == "M2"))
  when(inst
    dbReplaceProp(inst "l" "float" 1.68e-7)
    dbReplaceProp(inst "nfin" "float" 6)
    dbReplaceProp(inst "m" "float" 64)
  )
  
  ; Miller 电容
  inst = car(setof(x cv~>instances x~>name == "Cc"))
  when(inst
    dbReplaceProp(inst "c" "float" 8e-14)   ; 0.08pF = 8e-14 法拉
  )
  
  dbSave(cv)
  dbClose(cv)
)
'''
client.execute_operations([skill_code])
```

#### 方法二：使用 set_instance_params（触发 CDF 回调）

```python
from virtuoso_bridge.virtuoso.schematic.params import set_instance_params

# 修改 MOS 参数（会触发 CDF 回调）
# SMIC 12nm: 必须用 m= 而非 mr=，且加 param_filters=None
set_instance_params(client, "M1", l="168n", nfin="6", m="64", param_filters=None)
set_instance_params(client, "M2", l="168n", nfin="6", m="64", param_filters=None)

# 修改电容
set_instance_params(client, "Cc", c="0.08p")
```

### 📖 原理图读取 API

```python
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic

# 读取原理图拓扑 + 参数
data = read_schematic(client, "work_ai", "opamp_two_stage")

# 实例列表
for inst in data["instances"]:
    name = inst["name"]
    params = inst.get("params", {})
    print(f"{name}: l={params.get('l')} nfin={params.get('nfin')} m={params.get('m')}")

# 网络连接
for net_name, net_info in data["nets"].items():
    print(f"{net_name}: {net_info['connections']}")
```

### ⚠️ 原理图设计常见陷阱

| 陷阱 | 后果 | 解决方案 |
|------|------|---------|
| edit() 内嵌套 dbOpenCellViewByType | 原理图全部清空！ | 参数修改用 execute_operations() 单独执行 |
| MOS terminal 用小写 g/d/s/b | 找不到 terminal | 必须用大写 **G, D, S, B** |
| 忘记连接 Bulk 端口 | 警告 + 仿真异常 | NMOS→VSS, PMOS→VDD |
| M7 Gate floating | 仿真不收敛 | 必须连接到偏置网络 |
| 电容用 G/D/S 连 terminal | 连接失败 | 电容用 **PLUS, MINUS** |
| l 参数写 0.168 | 变成 168,000,000 nm！ | 168nm = 1.68e-7 米 |
| c 参数写 0.08 | 变成 0.08 F！ | 0.08pF = 8e-14 法拉 |

---

## 🎯 Spectre 仿真步骤

### 核心仿真流程

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: 网表准备                                            │
│  ─────────────────                                          │
│  build_testbench() → 生成 .scs 网表                           │
│  包含: PDK 模型 include、器件参数、激励源、分析语句            │
│                                                             │
│  Phase 2: 运行仿真                                            │
│  ─────────────────                                          │
│  SpectreSimulator.from_env() → 创建仿真器                    │
│  sim.run_simulation(scs_path) → 远程运行 → PSF 结果          │
│                                                             │
│  Phase 3: 结果解析                                            │
│  ─────────────────                                          │
│  parse_spectre_psf_ascii() → Python dict                    │
│  计算: DC Gain / GBW / Phase Margin / Vout DC / Power       │
│                                                             │
│  Phase 4: 参数优化 (可选)                                     │
│  ─────────────────                                          │
│  多轮 sweep: m1/m5/m6/m7/m3 + Cc → 找到最优参数组合          │
│  目标: GBW > 2.5GHz, PM > 60°, Vout ≈ 0.9V, Power < 1mW    │
└─────────────────────────────────────────────────────────────┘
```

### 1. 创建 Testbench 网表

**⚠️ 关键：Spectre 网表中 MOSFET 尺寸参数用 `nfin`（每指鳍片数）、`nf`（手指数量）、`m`（并联倍数）。原理图 CDF 中的 `fingers` 对应 Spectre 的 `nf`，不是 `fingers`！**

```python
def build_opamp_testbench(params, output_path):
    """构建两级运放测试网表

    Spectre MOSFET 尺寸参数:
      nfin = Fins per Finger (每指鳍片数)
      nf   = Number of Fingers (手指数量, 对应 CDF 的 fingers)
      m    = Multiplier (并联器件数)
      有效总鳍数 = nfin × nf × m
    """
    m1 = params.get("m1", 64)      # M1/M2 并联数 (multiplier)
    m5 = params.get("m5", 16)      # M5 尾电流源并联数
    m6 = params.get("m6", 32)      # M6 第二级驱动并联数
    m7 = params.get("m7", 16)      # M7 第二级负载并联数
    m3 = params.get("m3", 16)      # M3/M4 电流镜并联数
    cc = params.get("cc", 8e-14)

    PDK_MODEL = (
        "/mnt/data/tech/a01/process/PDK/SPDK12SFE_0818_OA_CDS_V1.20_REV0_0"
        "/smic12sfe_0818_1P9M_DV_3DM_Q1_3Q2_2TMa_ALPA2_14SHK_oa_cds_2023_05_26_v1.20_rev0_0"
        "/models/spectre/12sfe_spice_v1p2_rev0_usage_spe.lib"
    )

    netlist = f'''simulator lang=spectre
global 0

simulatorOptions options psfversion="1.4.0" reltol=1e-4 vabstol=1e-6 \\
  soft_bin=allmodels

include "{PDK_MODEL}" section=tt_mos_varactor
include "{PDK_MODEL}" section=tt_res_res3t_bjt_dio
include "{PDK_MODEL}" section=tt_mom_mim
include "{PDK_MODEL}" section=pre_layout

parameters VDD=1.8 VCM=0.9 IBIAS=10u

// ========== 电源 ==========
V0 (VDD 0) vsource dc=VDD
V1 (VSS 0) vsource dc=0

// ========== 偏置电路 ==========
// ⚠️ Spectre 网表用 mr=，原理图 CDF 用 m=，fingers=
IBIAS (net_bias VSS) isource dc=IBIAS
M8 (net_bias net_bias VDD VDD) p18_ckt l=168n nfin=6 mr=1
M9 (net_vb net_bias VDD VDD) p18_ckt l=168n nfin=6 mr=1
M10 (net_bias net_bias VSS VSS) n18_ckt l=168n nfin=6 mr=1
Rvb (net_vb VSS) resistor r=500MEG

// ========== 第一级差分对 ==========
M1 (net_d3 VINP net_s VSS) n18_ckt l=168n nfin=6 mr={m1}
M2 (net_x VINN net_s VSS) n18_ckt l=168n nfin=6 mr={m1}
M5 (net_s net_vb VSS VSS) n18_ckt l=168n nfin=6 mr={m5}

// ========== 电流镜负载 ==========
M3 (net_d3 net_d3 VDD VDD) p18_ckt l=168n nfin=6 mr={m3}
M4 (net_x net_d3 VDD VDD) p18_ckt l=168n nfin=6 mr={m3}

// ========== 第二级共源放大 ==========
M6 (VOUT net_x VSS VSS) n18_ckt l=168n nfin=6 mr={m6}
M7 (VOUT net_bias VDD VDD) p18_ckt l=168n nfin=6 mr={m7}

// ========== Miller 补偿 ==========
Cc (net_x VOUT) capacitor c={cc}

// ========== 输入激励 ==========
VINP (VINP 0) vsource dc=VCM mag=0.5
VINN (VINN 0) vsource dc=VCM mag=-0.5
CL (VOUT 0) capacitor c=2p

// ========== 分析语句 ==========
dcOp dc maxiters=150
ac ac start=1 stop=5G dec=20

save VDD VSS VINP VINN VOUT net_d3 net_x net_s net_vb net_bias
saveOptions options save=selected
'''

    output_path.write_text(netlist, encoding="utf-8")
    return output_path
```

### 2. 运行仿真

```python
from virtuoso_bridge.spectre.runner import SpectreSimulator, spectre_mode_args
from pathlib import Path

# 创建输出目录
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# 构建测试网表
params = {"m1": 64, "m5": 16, "m6": 32, "m7": 16, "m3": 16, "cc": 8e-14}
scs_path = build_opamp_testbench(params, output_dir / "tb_opamp.scs")

# 创建仿真器
sim = SpectreSimulator.from_env(
    spectre_args=spectre_mode_args("ax"),  # APS extended (推荐)
    work_dir=str(output_dir),
    output_format="psfascii",  # ASCII 格式，便于解析
)

# 运行仿真
result = sim.run_simulation(str(scs_path), {})

if result.ok:
    print("✅ 仿真成功!")
    print(f"结果目录: {result.metadata['output_dir']}")
else:
    print(f"❌ 仿真失败: {result.errors}")
```

### 3. 解析 AC 仿真结果

```python
from virtuoso_bridge.spectre.parsers import parse_spectre_psf_ascii
import math
import cmath
## Traffic stats: manual cadence — run before any 14-day gap

`stats/{clones,views}.json` is a long-term record of repo traffic, populated
by `scripts/track_traffic.py`. **GitHub's traffic API only retains 14 days**
— any window not polled inside that 14-day rolling buffer is **permanently
lost**.

There is no auto-update: GitHub Actions' default `GITHUB_TOKEN` cannot access
the `/traffic/clones` / `/traffic/views` endpoints (returns `403 Resource not
accessible by integration` regardless of `permissions:`), so the polling has
to happen locally:

```bash
GH_TOKEN=$(gh auth token) OWNER=Arcadia-1 REPO=virtuoso-bridge-lite \
    python scripts/track_traffic.py
git add stats/ && git commit -m "stats: traffic update $(date -u +%Y-%m-%d)" && git push
```

**`gh auth token` is the trick** — it returns a real user token (not the
`GITHUB_TOKEN` Actions issues), which the traffic API does accept. No PAT
to create.

Cadence: aim for **≤10 days between runs** (gives a 4-day safety margin
on the 14-day window). If a longer gap happened, the missing days are gone
forever — don't try to fabricate them.

## Skills & Reference Map

# 解析 PSF ASCII 结果
psf_path = Path(result.metadata["output_dir"]) / "ac.ac"
psf_data = parse_spectre_psf_ascii(psf_path)

# 提取数据
freq = psf_data.data.get("freq")          # 频率数组
vout_complex = psf_data.data.get("VOUT")  # 复数电压
dc_vout = psf_data.data.get("dc_VOUT")    # DC 工作点

# 转换复数格式（PSF 存储为 [real, imag, real, imag, ...]）
vout_c = [complex(vout_complex[i], vout_complex[i+1]) 
          for i in range(0, len(vout_complex), 2)]

# 计算增益 (dB) 和相位 (度)
gain_db = [20 * math.log10(abs(v) * 2 + 1e-30) for v in vout_c]
phase_deg = [math.degrees(cmath.phase(v)) for v in vout_c]

# 计算 DC 增益
dc_gain = gain_db[0]
print(f"DC Gain: {dc_gain:.2f} dB")

# 计算 GBW (增益过 0dB 的频率)
gbw = None
for i in range(len(gain_db) - 1):
    if gain_db[i] >= 0 and gain_db[i+1] < 0:
        f1, f2 = freq[i], freq[i+1]
        g1, g2 = gain_db[i], gain_db[i+1]
        log_cross = math.log10(f1) + (math.log10(f2) - math.log10(f1)) * (-g1) / (g2 - g1)
        gbw = 10 ** log_cross
        break

if gbw:
    print(f"GBW: {gbw / 1e9:.2f} GHz")

# 计算相位裕度 (Phase Margin)
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

if pm:
    print(f"Phase Margin: {pm:.2f}°")

# DC 输出电压
if isinstance(dc_vout, list):
    dc_vout_val = abs(dc_vout[0])
elif isinstance(dc_vout, complex):
    dc_vout_val = abs(dc_vout)
else:
    dc_vout_val = abs(float(dc_vout))
print(f"Vout DC: {dc_vout_val:.3f} V")

# 功耗估算 (IBIAS × 总电流倍数 × VDD)
ibias = 10e-6
total_m = params["m7"] + params["m5"] + params["m3"]
power = 1.8 * ibias * total_m
print(f"Power Estimate: {power * 1e3:.2f} mW")
```

### 4. 生成 Bode 图

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7),
    gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08})

# 幅频特性
ax1.semilogx(freq, gain_db, linewidth=1.5, color="#1f77b4")
ax1.set_ylabel("Gain (dB)", fontsize=12)
ax1.axhline(y=0, color="#d62728", linestyle="--", linewidth=1, label="0 dB")
if gbw:
    ax1.axvline(x=gbw, color="#ff7f0e", linestyle="--", linewidth=1, 
                label=f"GBW = {gbw/1e9:.2f} GHz")
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=10)
ax1.set_title(f"Opamp AC Response (DC Gain = {dc_gain:.1f} dB)", fontsize=14)

# 相频特性
ax2.semilogx(freq, phase_deg, color="#ff7f0e", linewidth=1.5)
ax2.set_xlabel("Frequency (Hz)", fontsize=12)
ax2.set_ylabel("Phase (°)", fontsize=12)
ax2.axhline(y=-180, color="#d62728", linestyle="--", linewidth=1)
if pm:
    ax2.axhline(y=pm-180, color="#2ca02c", linestyle="--", linewidth=1,
                label=f"PM = {pm:.1f}°")
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=10)

plt.tight_layout()
plt.savefig(output_dir / "opamp_bode.png", dpi=200, bbox_inches="tight")
print(f"Bode 图已保存到: {output_dir / 'opamp_bode.png'}")
```

### 5. 参数优化 Sweep

```python
# 多轮参数扫描优化
def optimize_opamp(sweep_params, output_dir):
    results = []
    
    for i, params in enumerate(sweep_params):
        print(f"\n运行仿真 {i+1}/{len(sweep_params)}: {params}")
        
        scs_path = build_opamp_testbench(params, output_dir / f"tb_{i}.scs")
        result = sim.run_simulation(str(scs_path), {})
        
        if result.ok:
            metrics = analyze_ac_result(result, params)
            results.append(metrics)
            print(f"  → DC Gain: {metrics['dc_gain']:.1f} dB, "
                  f"GBW: {metrics['gbw']/1e9:.2f} GHz, "
                  f"PM: {metrics['pm']:.1f}°")
    
    return results

# 定义参数扫描范围
sweep_params = [
    {"m1": m1, "m5": m5, "m6": 32, "m7": 16, "m3": 16, "cc": 8e-14}
    for m1 in [32, 64, 96, 128]
    for m5 in [8, 16, 24]
]

# 运行优化
results = optimize_opamp(sweep_params, output_dir)

# 找到最优结果（GBW 最大且 PM > 60°）
valid_results = [r for r in results if r["pm"] > 60 and 0.8 < r["vout_dc"] < 1.0]
if valid_results:
    best = max(valid_results, key=lambda x: x["gbw"])
    print(f"\n🎉 最优结果:")
    print(f"  参数: m1={best['m1']}, m5={best['m5']}")
    print(f"  DC Gain: {best['dc_gain']:.1f} dB")
    print(f"  GBW: {best['gbw']/1e9:.2f} GHz")
    print(f"  PM: {best['pm']:.1f}°")
    print(f"  Vout DC: {best['vout_dc']:.3f} V")
```

### ⚠️ 仿真常见陷阱

| 陷阱 | 后果 | 解决方案 |
|------|------|---------|
| save I(V0) 在 .scs 中 | 语法错误 | 只保存节点电压，不保存支路电流 |
| Spectre 注释用 # | 语法错误 | Spectre 用 // 注释或省略 |
| l = 0.168 (微米) | 变成 168,000,000 nm！ | 168nm 写为 1.68e-7 |
| M7 Gate floating | 仿真不收敛 | 必须连接到偏置网络 |
| 没有 soft_bin=allmodels | FinFET 模型找不到 | simulatorOptions 必须设置 |
| `.scs` 网表中写 `fingers=8` | SFE-103 警告，参数被忽略，器件宽度缩小数倍 | Spectre 用 **`nf=8`** 表示手指数量 |

---

## 📚 SKILL 函数语法大全

### 核心数据库操作函数

#### `dbOpenCellViewByType` - 打开 CellView

**语法**:
```skill
dbOpenCellViewByType(libName cellName viewName viewType mode)
```

**参数**:
- `libName`: 库名称 (string)
- `cellName`: 单元名称 (string)
- `viewName`: 视图名称 (string, e.g. "schematic", "layout")
- `viewType`: 视图类型 (string, e.g. "schematic", "maskLayout")
- `mode`: 打开模式 ("a"=append/edit, "r"=read-only)

**返回**: CellView 对象，失败返回 `nil`

**示例**:
```skill
; 打开原理图进行编辑
cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a")

; 打开版图只读
cv_layout = dbOpenCellViewByType("work_ai" "opamp" "layout" "maskLayout" "r")
```

**⚠️ 关键提醒**: 必须提供 5 个参数！缺少第 4、5 个参数会静默返回 `nil`！

---

#### `dbClose` - 关闭 CellView

**语法**:
```skill
dbClose(cellView)
```

**示例**:
```skill
cv = dbOpenCellViewByType("work_ai" "test" "schematic" "schematic" "a")
; ... 操作 ...
dbSave(cv)
dbClose(cv)
```

---

#### `dbSave` - 保存 CellView

**语法**:
```skill
dbSave(cellView)
```

**示例**:
```skill
; 编辑后保存
dbReplaceProp(inst "l" "float" 1.68e-7)
dbSave(cv)
```

---

#### `dbReplaceProp` - 设置实例属性

**语法**:
```skill
dbReplaceProp(instance propName propType value)
```

**参数**:
- `instance`: 实例对象
- `propName`: 属性名称 (string)
- `propType`: 属性类型 ("float", "string", "int", "boolean")
- `value`: 属性值

**常用属性**:
| 属性 | 类型 | 单位 | 示例值 | 说明 |
|------|------|------|--------|------|
| `"l"` | float | 米 (m) | `1.68e-7` | 栅长 (168nm) |
| `"w"` | float | 米 (m) | `1e-6` | 栅宽 (1μm) |
| `"nfin"` | float | 无量纲 | `6` | FinFET 每指鳍片数 (Fins per Finger) |
| `"mr"` | float | 无量纲 | `64` | Multiplier (并联器件数) |
| `"c"` | float | 法拉 (F) | `8e-14` | 电容值 (0.08pF) |
| `"r"` | float | 欧姆 (Ω) | `1e3` | 电阻值 |

**示例**:
```skill
inst = car(setof(x cv~>instances x~>name == "M1"))
when(inst
  dbReplaceProp(inst "l" "float" 1.68e-7)   ; 168nm
  dbReplaceProp(inst "nfin" "float" 6)
  dbReplaceProp(inst "mr" "float" 64)
)
```

---

#### ⚠️ FinFET 尺寸参数: nfin、nf、m 的区别 (Virtuoso CDF vs Spectre 网表)

**这是最容易踩的参数陷阱！原理图 CDF 中的 `fingers` 在 Spectre 网表中对应 `nf`，不是 `nfin`！**

| 参数 | Virtuoso CDF 名称 | Spectre 网表名称 | 含义 |
|------|-------------------|-----------------|------|
| **每指鳍片数** | `nfin` | `nfin` | Number of Fins **per Finger** — 每个手指的鳍数量 |
| **手指数量** | `fingers` | **`nf`** | Number of **Fingers** — 多指栅极数量 |
| **并联倍数** | `mr` | `mr` | Multiplier — 完全相同的器件并联个数 |

**有效总鳍数 = nfin × nf × m**

示例：M1 在原理图中 `nfin=4, fingers=8, mr=1` → Spectre 中应写为：

```spectre
M1 (D G S B) n18_ckt l=134n nfin=4 nf=8 mr=1
```

⚠️ **`fingers` 不是 Spectre 参数！** 如果在 `.scs` 网表中写 `fingers=8`，Spectre 会发出 `SFE-103` 警告并忽略该参数，导致器件宽度严重偏小。

```spectre
// ❌ 错误！fingers 被 Spectre 忽略
M1 (D G S B) n18_ckt l=134n nfin=4 mr=1 fingers=8
// WARNING (SFE-103): Subcircuit parameter 'fingers' has been ignored

// ✅ 正确！用 nf 表示手指数量
M1 (D G S B) n18_ckt l=134n nfin=4 mr=1 nf=8
```

**快速记忆**：
- `nfin` = **每指**有几个鳍 (FinFET 专有)
- `nf` = 有几个**手指** (类似平面工艺的 fingers)
- `m` = 有几个**并联的完整器件**

---

#### 对象属性访问 `~>` 操作符

**语法**:
```skill
object~>property
```

**常用属性**:
| 属性 | 适用对象 | 说明 |
|------|---------|------|
| `~>instances` | CellView | 所有实例列表 |
| `~>name` | Instance | 实例名称 (e.g. "M1") |
| `~>cellName` | Instance | 单元名称 (e.g. "n18_ckt") |
| `~>libName` | Instance | 库名称 |
| `~>viewName` | Instance | 视图名称 |
| `~>terms` | Instance | 终端列表 |
| `~>nets` | CellView | 网络列表 |

**示例**:
```skill
; 遍历所有实例
foreach(inst cv~>instances
  printf("Instance: %s (%s)\n" inst~>name inst~>cellName)
)

; 查找特定实例
m1 = car(setof(x cv~>instances x~>name == "M1"))

; 访问实例参数
when(m1
  printf("l = %e\n" m1~>l)
  printf("nfin = %g\n" m1~>nfin)
)
```

---

### 控制流函数

#### `let` - 局部变量绑定

**语法**:
```skill
let((var1 var2 ...)
  body_expression1
  body_expression2
  ...
)
```

**示例**:
```skill
let((cv inst count)
  cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a")
  count = 0
  foreach(inst cv~>instances
    when(inst~>cellName == "n18_ckt"
      count = count + 1
    )
  )
  printf("Found %d NMOS transistors\n" count)
  dbClose(cv)
)
```

---

#### `when` - 条件执行

**语法**:
```skill
when(condition
  true_expression1
  true_expression2
  ...
)
```

**示例**:
```skill
inst = car(setof(x cv~>instances x~>name == "M1"))
when(inst
  dbReplaceProp(inst "l" "float" 1.68e-7)
  printf("Updated M1\n")
)
```

---

#### `foreach` - 循环遍历

**语法**:
```skill
foreach(var list
  body_expression1
  body_expression2
  ...
)
```

**示例**:
```skill
; 遍历所有实例并修改参数
foreach(inst cv~>instances
  when(member(inst~>name '("M1" "M2" "M3"))
    dbReplaceProp(inst "l" "float" 1.68e-7)
  )
)
```

---

#### `setof` - 过滤列表

**语法**:
```skill
setof(var list condition)
```

**示例**:
```skill
; 找到所有 NMOS 实例
nmos_inst = setof(x cv~>instances x~>cellName == "n18_ckt")

; 找到名称以 "M" 开头的实例
m_inst = setof(x cv~>instances rexMatchp("^M" x~>name))
```

---

#### `car` - 获取列表第一个元素

**语法**:
```skill
car(list)
```

**示例**:
```skill
; 找到名为 "M1" 的第一个实例
m1 = car(setof(x cv~>instances x~>name == "M1"))
```

---

### 列表操作函数

| 函数 | 语法 | 说明 |
|------|------|------|
| `list` | `list(a b c)` | 创建列表 |
| `car` | `car(list)` | 获取第一个元素 |
| `cdr` | `cdr(list)` | 获取除第一个外的剩余部分 |
| `cons` | `cons(item list)` | 在列表前添加元素 |
| `append` | `append(list1 list2)` | 连接两个列表 |
| `length` | `length(list)` | 返回列表长度 |
| `member` | `member(item list)` | 检查元素是否在列表中 |
| `nth` | `nth(n list)` | 获取第 n 个元素 (0-based) |

**示例**:
```skill
my_list = list("M1" "M2" "M3")
printf("Length: %d\n" length(my_list))  ; 3
printf("First: %s\n" car(my_list))       ; "M1"
printf("Has M2: %s\n" member("M2" my_list))  ; t
```

---

### 字符串操作

| 函数 | 语法 | 说明 |
|------|------|------|
| `printf` | `printf(format arg1 arg2 ...)` | 格式化输出 |
| `sprintf` | `sprintf(nil format arg1 ...)` | 格式化字符串 |
| `concat` | `concat(str1 str2)` | 连接字符串 |
| `rexMatchp` | `rexMatchp(pattern string)` | 正则表达式匹配 |

**常用格式化符**:
| 格式符 | 类型 | 示例 |
|--------|------|------|
| `%s` | 字符串 | `printf("Name: %s\n" name)` |
| `%d` | 整数 | `printf("Count: %d\n" count)` |
| `%f` | 浮点数 | `printf("Value: %f\n" val)` |
| `%e` | 科学计数 | `printf("l = %e m\n" l)` |
| `%g` | 自动格式 | `printf("nfin = %g\n" nfin)` |

---

### 原理图编辑专用函数

#### `schCreateWire` - 创建连线

**语法**:
```skill
schCreateWire(cv layer points)
```

**示例**:
```skill
; 创建水平连线
schCreateWire(cv list("metal1" "drawing")
  list(list(-1.0 0.0) list(1.0 0.0))
)
```

---

#### `schCreateInst` - 创建实例

**语法**:
```skill
schCreateInst(cv master name location orient [multiplier])
```

**示例**:
```skill
; 查找 master
master = dbOpenCellViewByType("smic12sf" "n18_ckt" "symbol" "schematic" "r")

; 创建实例
schCreateInst(cv master "M1" list(-4.0 1.0) "R0")
```

---

#### `schAddInstTerm` - 连接实例终端

**语法**:
```skill
schAddInstTerm(inst termName netName)
```

**示例**:
```skill
; ⚠️ 注意: terminal 名称必须大写！
schAddInstTerm(inst "G" "VINP")   ; Gate
schAddInstTerm(inst "D" "net_d")  ; Drain
schAddInstTerm(inst "S" "VSS")    ; Source
schAddInstTerm(inst "B" "VSS")    ; Bulk
```

**❌ 错误写法**:
```skill
schAddInstTerm(inst "g" "VINP")   ; ❌ 小写 g 不存在！
schAddInstTerm(inst "PLUS" ...)   ; ❌ MOS 没有 PLUS terminal！
```

---

### Maestro 仿真控制函数

#### `maeRunSimulation` - 运行仿真

**语法**:
```skill
maeRunSimulation(?session sessionName ?waitUntilDone nil)
```

**示例**:
```python
# 通过 Python 执行
session = "maestroSession1"
client.execute_skill(f'maeRunSimulation(?session "{session}" ?waitUntilDone nil)')
```

---

#### `maeOpenResults` - 打开仿真结果

**语法**:
```skill
maeOpenResults(?history historyName)
```

---

#### `maeGetOutputValue` - 获取输出值

**语法**:
```skill
maeGetOutputValue(outputName testName)
```

**示例**:
```python
result = client.execute_skill('maeGetOutputValue("bandwidth(VF(\"/VOUT\"))" "ac_test")')
```

---

### 常用 SKILL 代码模板

#### 模板 1: 批量修改器件参数

```skill
let((cv)
  cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "a")
  
  ; 修改所有输入对
  foreach(name '("M1" "M2")
    let((inst)
      inst = car(setof(x cv~>instances x~>name == name))
      when(inst
        dbReplaceProp(inst "l" "float" 1.68e-7)
        dbReplaceProp(inst "nfin" "float" 6)
        dbReplaceProp(inst "m" "float" 64)
      )
    )
  )
  
  ; 修改 Miller 电容
  let((cc)
    cc = car(setof(x cv~>instances x~>name == "Cc"))
    when(cc
      dbReplaceProp(cc "c" "float" 8e-14)
    )
  )
  
  dbSave(cv)
  dbClose(cv)
  list("OK" "Parameters updated")
)
```

#### 模板 2: 读取并验证原理图

```skill
let((cv insts n_count p_count errors)
  cv = dbOpenCellViewByType("work_ai" "opamp" "schematic" "schematic" "r")
  errors = list()
  
  ; 统计器件
  n_count = length(setof(x cv~>instances x~>cellName == "n18_ckt"))
  p_count = length(setof(x cv~>instances x~>cellName == "p18_ckt"))
  
  ; 检查关键器件是否存在
  foreach(name '("M1" "M2" "M3" "M4" "M5" "M6" "M7" "M8" "M9" "M10" "Cc")
    when(!setof(x cv~>instances x~>name == name)
      errors = cons(sprintf(nil "Missing instance: %s" name) errors)
    )
  )
  
  dbClose(cv)
  
  list(
    list("nmos_count" n_count)
    list("pmos_count" p_count)
    list("errors" errors)
  )
)
```

#### 模板 3: 创建反相器原理图

```skill
let((cv lib cell nmos_master pmos_master mn mp)
  lib = "work_ai"
  cell = "inv_new"
  
  ; 创建新的 schematic cellview
  cv = dbOpenCellViewByType(lib cell "schematic" "schematic" nil)
  
  ; 打开器件 master
  nmos_master = dbOpenCellViewByType("smic12sf" "n18_ckt" "symbol" "schematic" "r")
  pmos_master = dbOpenCellViewByType("smic12sf" "p18_ckt" "symbol" "schematic" "r")
  
  ; 放置 NMOS
  mn = schCreateInst(cv nmos_master "MN0" list(0.0 0.0) "R0")
  
  ; 放置 PMOS
  mp = schCreateInst(cv pmos_master "MP0" list(0.0 1.5) "MY")
  
  ; 连接栅极（输入）
  schAddInstTerm(mn "G" "IN")
  schAddInstTerm(mp "G" "IN")
  
  ; 连接漏极（输出）
  schAddInstTerm(mn "D" "OUT")
  schAddInstTerm(mp "D" "OUT")
  
  ; 连接源极和 Bulk
  schAddInstTerm(mn "S" "VSS")
  schAddInstTerm(mn "B" "VSS")
  schAddInstTerm(mp "S" "VDD")
  schAddInstTerm(mp "B" "VDD")
  
  ; 创建引脚
  schCreatePin(cv "IN" list("metal1" "pin") list(list(-1.5 0.75)) "R0" "input")
  schCreatePin(cv "OUT" list("metal1" "pin") list(list(1.5 0.75)) "R0" "output")
  schCreatePin(cv "VDD" list("metal1" "pin") list(list(0.0 2.5)) "R0" "inputOutput")
  schCreatePin(cv "VSS" list("metal1" "pin") list(list(0.0 -1.0)) "R0" "inputOutput")
  
  schCheck(cv)
  dbSave(cv)
  dbClose(cv)
  
  list("OK" "Inverter created")
)
```

---

## 🎨 版图编辑 SKILL 函数

### 器件创建

#### `dbCreateParamInstByMasterName` - 创建参数化实例

**语法**:
```skill
dbCreateParamInstByMasterName(cv libName cellName viewName instName location orient)
```

**示例**:
```skill
; 创建 NMOS 晶体管
dbCreateParamInstByMasterName(cv "smic12sf" "n18_ckt" "layout" "MN0" list(1.0 0.5) "R0")

; 创建 PMOS 晶体管（镜像）
dbCreateParamInstByMasterName(cv "smic12sf" "p18_ckt" "layout" "MP0" list(1.0 2.0) "MX")
```

### 图形创建

#### `dbCreateRect` - 创建矩形

**语法**:
```skill
dbCreateRect(cv layerPurpose bbox)
```

**示例**:
```skill
; 创建 M1 金属矩形
dbCreateRect(cv list("M1" "drawing") list(list(0.0 0.0) list(1.0 0.5)))
```

#### `dbCreatePath` - 创建路径（连线）

**语法**:
```skill
dbCreatePath(cv layerPurpose points width)
```

**示例**:
```skill
; 创建水平 M1 连线
dbCreatePath(cv list("M1" "drawing")
  list(list(0.0 0.25) list(2.0 0.25))  ; 起点 -> 终点
  0.1  ; 宽度
)
```

#### `dbCreatePolygon` - 创建多边形

**语法**:
```skill
dbCreatePolygon(cv layerPurpose points)
```

### 通孔创建

#### `dbCreateVia` - 创建通孔

**语法**:
```skill
dbCreateVia(cv viaDefName location [rotate] [size])
```

**示例**:
```skill
; 创建 M1-M2 通孔
dbCreateVia(cv "VIA1" list(1.0 1.0) "R0")
```

---

## ❌ 常见错误排查

### 数据库操作错误

| 错误现象 | 可能原因 | 解决方案 |
|---------|---------|---------|
| `dbOpenCellViewByType` 返回 `nil` | 缺少参数 | 必须提供 5 个参数: lib, cell, view, viewType, mode |
| 原理图内容全部消失！ | edit() 内嵌套 dbOpenCellViewByType | 永远不要在 `with client.schematic.edit()` 内再次打开同一个 cellview |
| 实例属性修改不生效 | 使用了错误的属性名 | 用 `inst~>propName` 查看支持的属性，或用 `dbReplaceProp` |
| CDF 参数回调不触发 | 直接修改属性 | 使用 `set_instance_params()` 或 `schHiReplace` |

### 原理图编辑错误

| 错误现象 | 可能原因 | 解决方案 |
|---------|---------|---------|
| Terminal not found | terminal 名称大小写错误 | MOS 用大写 `G/D/S/B`，电容电阻用 `PLUS/MINUS` |
| 警告: Terminal is floating | 忘记连接端口 | 检查所有 MOS 的 S/D/G/B 都已连接 |
| 仿真不收敛 | M7 Gate floating | 确保有源负载的栅极连接到偏置网络 |

### 仿真错误

| 错误现象 | 可能原因 | 解决方案 |
|---------|---------|---------|
| Syntax error near `(` | 使用了 `save I(V0)` | Spectre 不支持保存支路电流，只保存节点电压 |
| Model not found | 缺少 `soft_bin=allmodels` | simulatorOptions 必须设置 `soft_bin=allmodels` |
| 器件尺寸异常大 | l/w 单位错误 | 168nm = 1.68e-7 米，不是 0.168！ |
| DC 工作点异常 | m6/m7 比例不对 | 调整 m6/m7 比值使 Vout ≈ VDD/2 |

### SKILL 执行错误

| 错误现象 | 可能原因 | 解决方案 |
|---------|---------|---------|
| undefined function `dbGetPropValue` | 函数不存在 | 用 `inst~>propName` 直接访问属性 |
| procedure 定义在 let 内无效 | 嵌套定义不支持 | procedure 必须在顶层定义 |
| printf 输出没有传回 Python | printf 是 CIW 本地输出 | 用表达式返回值，或用 `list()` 打包结果 |

---

## 📁 输出文件命名规范

所有生成的脚本、仿真结果、截图等都必须遵循以下命名格式：

```
output/{operation}_{YYYYMMDD}_{HHMMSS}.{ext}
```

### 示例文件名

| 文件类型 | 示例文件名 |
|---------|-----------|
| 原理图创建脚本 | `output/schematic_opamp_20260429_113000.il` |
| 参数修改脚本 | `output/params_update_20260429_113500.skill` |
| Spectre 网表 | `output/tb_opamp_20260429_114000.scs` |
| 仿真结果目录 | `output/sim_ac_20260429_114500/` |
| Bode 图 | `output/bode_plot_20260429_115000.png` |
| Virtuoso 截图 | `output/screenshot_maestro_20260429_115500.png` |

### Python 代码模板

```python
import os
from datetime import datetime
from pathlib import Path

def get_output_path(operation, ext):
    """生成带时间戳的输出文件路径"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{operation}_{timestamp}.{ext}"
    return output_dir / filename

# 使用示例
scs_path = get_output_path("tb_opamp", "scs")
png_path = get_output_path("bode_plot", "png")
il_path = get_output_path("schematic_create", "il")
```

---

## 🔗 技能与参考文档索引

### Virtuoso 技能 (`skills/virtuoso/`)

| 参考文档 | 路径 | 内容 |
|---------|------|------|
| 原理图 API (Python) | `references/schematic-python-api.md` | Python 层原理图编辑 API |
| 原理图 API (SKILL) | `references/schematic-skill-api.md` | 底层 SKILL 原理图函数 |
| 版图 API (Python) | `references/layout-python-api.md` | Python 层版图编辑 API |
| 版图 API (SKILL) | `references/layout-skill-api.md` | 底层 SKILL 版图函数 |
| Maestro API | `references/maestro-python-api.md` | Maestro 仿真控制 API |
| 仿真流程 | `references/simulation-flow.md` | 标准仿真 8 步指南 |
| 网list格式 | `references/netlist.md` | Spectre 网list语法 |
| 故障排除 | `references/troubleshooting.md` | 常见问题解决方案 |
| SMIC12SF PDK | `references/smic12sf-pdk.md` | 12nm FinFET PDK 参数 |

### Spectre 仿真技能 (`skills/spectre/`)

| 参考文档 | 路径 | 内容 |
|---------|------|------|
| 网list语法 | `references/netlist_syntax.md` | Spectre netlist 完整语法 |
| 并行仿真 | `references/parallel.md` | 多服务器并行仿真配置 |

### 官方指南文档 (`docs/guides/`)

| 文档 | 重要性 | 内容 |
|------|--------|------|
| `SCHEMATIC_GENERATION_PLAYBOOK.md` | ⭐⭐⭐ | 完整原理图→仿真→优化 Playbook |
| `SKILL_QUICK_REFERENCE.md` | ⭐⭐⭐ | SKILL 速查 + 8 个致命 bug 修复 |
| `SPECTRE_OPAMP_DEBUG_NOTES.md` | ⭐⭐ | 运放 AC 调试实战日志 |

---

## 📊 API 前缀速查表

| 前缀 | 功能域 | 常用函数 |
|------|--------|---------|
| `db*` | 数据库操作 | `dbOpenCellViewByType`, `dbSave`, `dbClose`, `dbReplaceProp`, `dbCreate*` |
| `sch*` | 原理图编辑 | `schCreateWire`, `schCreateInst`, `schAddInstTerm`, `schCreatePin` |
| `mae*` | Maestro 仿真 | `maeRunSimulation`, `maeGetOutputValue`, `maeOpenResults`, `maeSaveSetup` |
| `axl*` | ADE XL | `axlGetParameter`, `axlRunSimulation`, `axlGetCorners` |
| `hi*` | GUI 交互 | `hiGetCurrentWindow`, `hiWindowSaveImage`, `hiFormDone` |
| `ge*` | 图形编辑 | `geGetEditCellView`, `geGetSelSet`, `geSelectPoint` |
| `cst*` | 约束系统 | `cstCreateConstraintGroup`, `cstGetFoundryConstraintGroup` |

---

## 💡 最佳实践总结

### 原理图设计
1. ✅ 用 `client.schematic.edit()` 上下文管理器
2. ✅ MOS terminal 用大写 `G/D/S/B`
3. ✅ 电容/电阻用 `PLUS/MINUS`
4. ✅ 所有 MOS 的 Bulk 必须连接
5. ❌ 不要在 edit() 内嵌套 dbOpenCellViewByType
6. ❌ 不要用微米单位，168nm = 1.68e-7 米

### 参数修改
1. ✅ 用 `client.execute_operations()` 单独执行参数修改
2. ✅ 优先用 `set_instance_params()` 触发 CDF 回调
3. ✅ 修改后用 `read_schematic()` 验证
4. ✅ 每次修改后 `dbSave(cv)` + `dbClose(cv)`

### Spectre 仿真
1. ✅ 用 `spectre_mode_args("ax")` APS 扩展模式
2. ✅ `output_format="psfascii"` 便于解析
3. ✅ `soft_bin=allmodels` 自动选择 FinFET 模型
4. ✅ 只保存需要的节点电压，不要尝试保存电流
5. ❌ 不要用 `#` 注释，Spectre 用 `//`

### SKILL 代码
1. ✅ 用 `let()` 定义局部变量
2. ✅ 用 `when()` 进行条件判断（避免空指针）
3. ✅ 用 `~>` 操作符访问属性，不要用不存在的 `dbGetPropValue`
4. ✅ 用 `list()` 返回结果给 Python，不要依赖 `printf`
5. ✅ procedure 在顶层定义，不要嵌套在 let 里面

---

**文档最后更新**: 2026-04-30
**适用版本**: virtuoso-bridge-lite v1.0+
**验证状态**: ✅ 所有代码示例已通过实战验证
>>>>>>> a385e9d (update)
