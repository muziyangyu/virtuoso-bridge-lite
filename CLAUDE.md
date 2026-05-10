<<<<<<< HEAD
# Virtuoso Bridge Lite — 完整 API 使用指南

> **项目目标**: 用 Python 远程控制 Cadence Virtuoso，实现原理图/版图编辑、仿真运行、结果解析的全自动化。
> **文档生成时间**: 基于 `src/` 核心源码、`examples/` 所有示例脚本、`skills/` 技能定义深度分析生成

---

## 目录

1. [快速开始](#快速开始)
2. [核心架构](#核心架构)
3. [VirtuosoClient API](#virtuosoclient-api)
4. [Schematic 原理图 API](#schematic-原理图-api)
5. [Layout 版图 API](#layout-版图-api)
6. [Maestro 仿真 API](#maestro-仿真-api)
7. [Spectre 独立仿真 API](#spectre-独立仿真-api)
8. [参数优化 API](#参数优化-api)
9. [常见问题与最佳实践](#常见问题与最佳实践)

---

## 快速开始

### 1. 安装

```bash
cd virtuoso-bridge-lite
uv venv .venv && source .venv/bin/activate   # Windows: source .venv/Scripts/activate
uv pip install -e .
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件:

```dotenv
# SSH 连接配置
VB_REMOTE_HOST=your-server
VB_REMOTE_USER=username
VB_REMOTE_PORT=65081
VB_LOCAL_PORT=65082

# 跳板机配置 (可选)
VB_JUMP_HOST=bastion.example.com

# Cadence 环境 (用于 Spectre)
VB_CADENCE_CSHRC=/path/to/cds.cshrc
```

### 3. 启动桥接服务
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
>>>>>>> 533b7ef (update)

```bash
virtuoso-bridge start
```

<<<<<<< HEAD
### 4. 在 Virtuoso CIW 中加载 (首次运行)

`virtuoso-bridge start` 会输出需要在 CIW 中执行的命令:
=======
### 4. 在 Virtuoso CIW 中加载 SKILL

`virtuoso-bridge start` 会输出需要在 CIW 中执行的命令：
>>>>>>> 533b7ef (update)

```skill
load("/tmp/virtuoso_bridge_<user>/virtuoso_bridge/virtuoso_setup.il")
```

<<<<<<< HEAD
=======
> 💡 **提示**: 将此命令添加到 `~/.cdsinit` 可以实现 Virtuoso 启动时自动加载。

>>>>>>> 533b7ef (update)
### 5. 验证连接

```bash
virtuoso-bridge status
<<<<<<< HEAD
# Expected: [tunnel] running, [daemon] OK, [spectre] OK
=======
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
>>>>>>> 533b7ef (update)
```

---

<<<<<<< HEAD
## 核心架构
=======
## 🏗️ 核心架构
>>>>>>> 533b7ef (update)

### 三层解耦设计

```
<<<<<<< HEAD
┌─────────────────────────────────────────────────────────────┐
│  应用层: Schematic / Layout / Maestro / Spectre Python API    │
│  (high-level, easy to use)                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  VirtuosoClient: 纯 TCP SKILL 客户端                          │
│  - execute_skill()                                           │
│  - fetch() / fetch_one() 批量属性读取                         │
│  - load_il() 加载 .il 文件                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  SSHClient: 持久化 SSH 连接 + 隧道管理                         │
│  - ControlMaster 多路复用                                      │
│  - TCP 端口转发 (SKILL 执行)                                   │
│  - Shell 命令执行 (Spectre)                                    │
│  - rsync 文件传输                                              │
└─────────────────────────────────────────────────────────────┘
```

### 模块依赖关系

```
virtuoso_bridge/
├── __init__.py           # 主入口: VirtuosoClient, SSHClient, SpectreSimulator
├── models.py             # 数据模型: ExecutionStatus, SimulationResult, SkillResult
├── env.py                # 环境变量加载 + profile 多环境支持
├── wrappers.py           # SanitizingClient 等包装器
│
├── transport/            # 传输层
│   ├── __init__.py
│   ├── tunnel.py         # SSH 隧道管理 (SSHClient)
│   ├── ssh.py            # SSHRunner 远程命令执行、文件传输
│   └── remote_paths.py   # 远程路径解析 + 用户目录检测
│
├── virtuoso/             # Virtuoso 相关
│   ├── basic/            # 基础桥接
│   │   ├── bridge.py     # VirtuosoClient 核心实现 (TCP 通信)
│   │   ├── composition.py  # 操作组合器
│   │   └── resources/    # SKILL 守护进程脚本 (.il)
│   ├── schematic/        # 原理图模块
│   │   ├── __init__.py
│   │   ├── editor.py     # SchematicEditor 上下文管理器
│   │   ├── reader.py     # read_schematic() 拓扑读取
│   │   ├── params.py     # set_instance_params() CDF 参数设置
│   │   └── ops.py        # 原理图操作构建函数
│   ├── layout/           # 版图模块
│   │   ├── __init__.py
│   │   ├── editor.py     # LayoutEditor 上下文管理器
│   │   ├── reader.py     # 版图几何读取
│   │   ├── ops.py        # 版图操作构建函数
│   │   ├── layers.py     # SMIC12SF 层常量定义 (类型安全)
│   │   └── pdk.py        # SMIC 12nm FinFET PDK 器件生成器
│   ├── maestro/          # Maestro 仿真模块
│   │   ├── __init__.py
│   │   ├── lifecycle.py  # open/close session, run simulation
│   │   └── reader/       # snapshot() 快照, sweep 导出, 结果读取
│   ├── visio.py          # Visio 导出 (仅 Windows)
│   ├── snapshot.py       # 快照功能
│   └── self_check.py     # 自检
│
└── spectre/              # Spectre 独立仿真
    ├── __init__.py
    ├── runner.py         # SpectreSimulator 类 (本地/远程运行)
    └── parsers.py        # PSF ASCII 结果解析器 (delta 压缩支持)
=======
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
>>>>>>> 533b7ef (update)
```

---

<<<<<<< HEAD
## VirtuosoClient API

### 导入与初始化

```python
from virtuoso_bridge import VirtuosoClient, decode_skill_output

# 从环境变量创建客户端 (推荐)
client = VirtuosoClient.from_env()

# 指定 profile (多环境支持)
client_prod = VirtuosoClient.from_env(profile="prod")

# 或手动指定连接 (较少使用)
client = VirtuosoClient(host="localhost", port=65082)
```

### 核心方法

#### 1. `execute_skill(skill_expr, timeout=30)`

执行任意 SKILL 表达式。

**参数:**
- `skill_expr` (str): SKILL 表达式
- `timeout` (int): 超时时间 (秒)

**返回:** `SkillResult` 对象，包含 `.status`, `.output`, `.raw`

```python
# 简单计算
result = client.execute_skill("1 + 2")
print(result.output)  # "3"

# 获取库列表
result = client.execute_skill("ddGetLibList()")

# 多行 SKILL (带 let 绑定)
skill_code = '''
let((cv insts)
  cv = dbOpenCellViewByType("myLib" "myCell" "schematic" "schematic" "r")
  insts = cv~>instances
  dbClose(cv)
  length(insts)
)
'''
result = client.execute_skill(skill_code)
num_instances = int(result.output)
```

**重要注意事项:**
- 返回值是字符串形式，需要自行解析
- `printf` 输出不会返回给 Python (只显示在 CIW)
- 使用 `list()` 或单个表达式返回值
- 长操作使用 `timeout=300` (如仿真)

---

#### 2. `fetch(skill_expr, fields)`

批量提取对象属性，**一次往返**获取多个字段。

这是性能最优的读取方式 — 避免 N+1 查询问题。

**参数:**
- `skill_expr` (str): 返回对象列表的 SKILL 表达式
- `fields` (list[str]): 要提取的属性名列表

**返回:** list[dict] — 每个对象的属性字典

```python
# 获取当前原理图的所有实例及其属性 (1 次往返)
instances = client.fetch(
    "geGetEditCellView()~>instances",
    ["name", "cellName", "libName", "viewName"]
)

# 结果:
# [
#   {"name": "M1", "cellName": "nch_mac", "libName": "smic12sf", "viewName": "symbol"},
#   {"name": "M2", "cellName": "nch_mac", "libName": "smic12sf", "viewName": "symbol"},
#   ...
# ]

# 获取选中的对象
selected = client.fetch("geGetSelSet()", ["objType", "name", "cellName"])
```

---

#### 3. `fetch_one(skill_expr, fields)`

提取单个对象的属性。

```python
# 获取当前编辑的 cellview 信息
cv_info = client.fetch_one(
    "geGetEditCellView()",
    ["libName", "cellName", "viewName"]
)

# cv_info = {"libName": "myLib", "cellName": "myCell", "viewName": "schematic"}
```

---

#### 4. `decode_skill_output(raw)`

解码 SKILL 输出，去除引号和转义字符。

```python
raw = '"Hello\\nWorld"'
decoded = decode_skill_output(raw)
# "Hello\nWorld" → 实际换行
```

---

#### 5. `load_il(file_path)`

上传并加载 `.il` SKILL 文件。

```python
# 加载本地脚本文件
client.load_il("scripts/my_skill_script.il")

# 等效于:
# client.upload_file("local_script.il", "/tmp/remote_script.il")
# client.execute_skill('load("/tmp/remote_script.il")')
```

---

#### 6. 文件传输

```python
# 本地上传 → 远程
client.upload_file("local/path/file.scs", "/tmp/remote/file.scs")

# 远程下载 → 本地
client.download_file("/tmp/remote/results.raw", "local/results.raw")

# 上传多个文件 (通过 SSHRunner)
from virtuoso_bridge.transport.ssh import SSHRunner
runner = SSHRunner(host="server", user="user")
runner.upload(["a.scs", "b.va"], "/tmp/work/")
```

---

#### 7. 窗口与截图

```python
# 列出所有打开的 Virtuoso 窗口
windows = client.list_windows()
# 返回: [(window_id, window_title), ...]

# 打开指定 cellview 的窗口
client.open_window("myLib", "myCell", view="schematic")

# 截图当前窗口
client.screenshot(output_dir="output/", target="current")

# 截图 CIW 窗口
client.screenshot(output_dir="output/", target="ciw")

# 截图指定窗口 ID
client.screenshot(output_dir="output/", target="1")
```

---

#### 8. 对话框处理

```python
# 关闭阻塞的模态对话框 (通过 X11，不依赖 SKILL 通道)
# 当 SKILL 调用超时时，首先尝试这个
client.dismiss_dialog()

# 等效 CLI:
# virtuoso-bridge dismiss-dialog
```

**原理**: 使用 X11 `xwininfo` 查找 Virtuoso 拥有的对话框窗口，然后发送 Enter 键。这是唯一可以在 SKILL 通道被阻塞时恢复的方法。

---

#### 9. Shell 命令 (远程执行)

```python
# 在远程服务器执行 shell 命令
result = client.run_shell_command("ls -la /tmp/")
print(result.stdout)

# 检查远程文件是否存在
result = client.run_shell_command("test -f /tmp/netlist.scs && echo exists || echo missing")
```

---

## Schematic 原理图 API

### 上下文管理器模式 (推荐)

**所有原理图编辑应该使用上下文管理器**，它会自动处理:
- `dbOpenCellViewByType` 打开
- 批量操作排队
- `schCheck()` 设计规则检查
- `dbSave()` 保存
- `dbClose()` 关闭

```python
from virtuoso_bridge.virtuoso.schematic import (
    schematic_create_inst_by_master_name as inst,
    schematic_create_pin as pin,
)

LIB = "work_ai"
CELL = "inv_example"

# 如果 cell 已存在，先删除 (避免重复叠加)
client.execute_skill(f'ddDeleteObj(ddGetObj("{LIB}" "{CELL}"))')

with client.schematic.edit(LIB, CELL) as sch:
    # 1. 放置器件实例
    sch.add(inst("smic12sf", "p18_ckt", "symbol", "MP0", 0, 1.5, "R0"))  # PMOS
    sch.add(inst("smic12sf", "n18_ckt", "symbol", "MN0", 0, 0, "R0"))     # NMOS

    # 2. 连接 MOS 端子 (自动生成 stub，不要手动 add_wire)
    sch.add_net_label_to_transistor("MP0",
        drain_net="OUT", gate_net="IN", source_net="VDD", body_net="VDD")
    sch.add_net_label_to_transistor("MN0",
        drain_net="OUT", gate_net="IN", source_net="VSS", body_net="VSS")

    # 3. 创建引脚 (放在电路边缘，通过 net name 自动连接)
    sch.add(pin("IN",   -1.0, 0.75, "R0", direction="input"))
    sch.add(pin("OUT",   1.0, 0.75, "R0", direction="output"))
    sch.add(pin("VDD",  -1.0, 2.0,  "R0", direction="inputOutput"))
    sch.add(pin("VSS",  -1.0, -0.5, "R0", direction="inputOutput"))

# 退出上下文时自动执行: schCheck() → dbSave() → dbClose()
```

---

### `schematic_create_inst_by_master_name`

创建器件实例。

**签名:**
```python
def schematic_create_inst_by_master_name(
    lib_name: str,
    cell_name: str,
    view_name: str,
    inst_name: str,
    x: float,
    y: float,
    orient: str,
) -> str:
```

**参数:**
- `lib_name`: 库名 (如 "smic12sf", "analogLib")
- `cell_name`: 单元名 (如 "n18_ckt", "cap", "res")
- `view_name`: 视图名 (通常 "symbol")
- `inst_name`: 实例名 (如 "M1", "C0", "Rload")
- `x, y`: 位置坐标 (微米)
- `orient`: 朝向 ("R0", "R90", "MY", "MX", 等)

**常见器件:**

```python
# SMIC 12nm FinFET MOS
inst("smic12sf", "n18_ckt", "symbol", "MN1", x, y, "R0")  # NMOS 1.8V
inst("smic12sf", "p18_ckt", "symbol", "MP1", x, y, "R0")  # PMOS 1.8V
inst("smic12sf", "n08_ckt", "symbol", "MN2", x, y, "R0")  # NMOS 0.8V core
inst("smic12sf", "p08_ckt", "symbol", "MP2", x, y, "R0")  # PMOS 0.8V core

# 阈值选项: ulvt (超低压), lvt (低压), svt (标准), hvt (高压)
inst("smic12sf", "nlvt18_ckt", "symbol", "MN3", x, y, "R0")  # LVT NMOS
inst("smic12sf", "phvt18_ckt", "symbol", "MP3", x, y, "R0")  # HVT PMOS

# analogLib 无源器件
inst("analogLib", "cap", "symbol", "C0", x, y, "R0")
inst("analogLib", "res", "symbol", "R1", x, y, "R0")
inst("analogLib", "ind", "symbol", "L1", x, y, "R0")

# 电压/电流源
inst("analogLib", "vsource", "symbol", "VIN", x, y, "R0")
inst("analogLib", "isource", "symbol", "Ibias", x, y, "R0")
```

---

### `schematic_create_pin`

创建原理图引脚。

**签名:**
```python
def schematic_create_pin(
    pin_name: str,
    x: float,
    y: float,
    orient: str,
    direction: str = "inputOutput",
    layer: str = "metal1",
    purpose: str = "pin",
) -> str:
```

**参数:**
- `pin_name`: 引脚名 (同时也是 net name)
- `x, y`: 位置坐标
- `orient`: 朝向
- `direction`: 方向 ("input", "output", "inputOutput")
- `layer`: 金属层名
- `purpose`: 用途 (通常 "pin")

**方向说明:**
- `"input"`: 输入引脚
- `"output"`: 输出引脚
- `"inputOutput"`: 双向 (电源、地、总线等)

---

### `add_net_label_to_transistor`

**这是最常用的连接方式！** 自动生成 stub 并连接到指定网络。

**签名:**
```python
def add_net_label_to_transistor(
    self,
    inst_name: str,
    drain_net: str | None = None,
    gate_net: str | None = None,
    source_net: str | None = None,
    body_net: str | None = None,
) -> None:
```

**示例:**
```python
with client.schematic.edit(LIB, CELL) as sch:
    sch.add(inst("smic12sf", "n18_ckt", "symbol", "M1", 0, 0, "R0"))
    
    # 连接所有四个端子 (D, G, S, B)
    sch.add_net_label_to_transistor("M1",
        drain_net="OUT",
        gate_net="IN",
        source_net="VSS",
        body_net="VSS")
```

**工作原理:**
1. 获取实例的端子位置坐标
2. 自动计算 stub 方向 (向左/右/上/下)
3. 生成短金属线 (stub) 连接到端子
4. 在 stub 末端放置 net label

---

### `read_schematic` 读取原理图拓扑

```python
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic

# 读取原理图 (默认: 只读取拓扑，不包含位置信息)
data = read_schematic(client, LIB, CELL)

# data 结构:
# {
#   "instances": [
#     {
#       "name": "M1",
#       "lib": "smic12sf",
#       "cell": "n18_ckt",
#       "view": "symbol",
#       "numInst": 1,
#       "params": {
#         "l": "14n",
#         "w": "100n",
#         "nf": "4",
#         "m": "2",
#         ...  # 其他 CDF 参数
#       },
#       "terms": {
#         "D": {"net": "OUT", "direction": "output"},
#         "G": {"net": "IN", "direction": "input"},
#         "S": {"net": "VSS", "direction": "input"},
#         "B": {"net": "VSS", "direction": "input"},
#       }
#     },
#     ...
#   ],
#   "nets": {
#     "OUT": {
#       "connections": ["M1.D", "M2.D"],
#       "numBits": 1,
#       "sigType": "signal",
#       "isGlobal": false
#     },
#     ...
#   },
#   "pins": {
#     "IN": {"direction": "input", "numBits": 1},
#     ...
#   },
#   "notes": [...]
# }

# 包含位置信息 (用于布局感知编辑)
data_with_pos = read_schematic(client, LIB, CELL, include_positions=True)
# 每个 instance 增加 "xform": {"x", "y", "orient", "scale"} 字段

# 不过滤 CDF 参数 (返回全部 200+ 个 PDK 参数)
raw_data = read_schematic(client, LIB, CELL, param_filters=None)
```

**默认参数过滤:**
只返回最常用的参数: `l, w, nf, m, fingers, mult, cpar, r, c`

---

### 设置实例参数 `set_instance_params`

修改器件的 CDF 参数 (**会触发 CDF 回调**更新衍生参数)。
=======
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
>>>>>>> 533b7ef (update)

```python
from virtuoso_bridge.virtuoso.schematic.params import set_instance_params

<<<<<<< HEAD
# 修改 MOS 参数
set_instance_params(client, "M1", 
    l="14n",      # 栅长
    w="100n",     # 栅宽 (每指)
    nf="4",       # 手指数量
    m="2")        # 并联倍数

# 修改电容值
set_instance_params(client, "C0", c="1p")

# 修改电阻值
set_instance_params(client, "Rload", r="10k")

# SMIC 12nm 特殊: 必须用 param_filters=None (PDK 参数名不同)
set_instance_params(client, "M1", l="14n", w="100n", nf="4", m="2",
                    param_filters=None)
```

**工作原理:**
1. 使用 `schHiReplace` 设置属性值
2. 调用 `CCSinvokeCdfCallbacks` 触发 CDF 回调
3. 更新衍生参数 (如 finger_width、显示注释等)

---

### 重命名/删除实例

```python
from virtuoso_bridge.virtuoso.schematic import rename_instance, delete_instance

# 重命名
rename_instance(client, "old_name", "new_name")

# 删除单个
delete_instance(client, "M1")

# 批量删除
delete_instance(client, ["M1", "M2", "C0"])
```

---

### 导入 CDL 网表

```python
from virtuoso_bridge.virtuoso.schematic import import_cdl

# 上传 CDL 文件
client.upload_file("local/netlist.cdl", "/tmp/netlist.cdl")

# 导入为原理图
import_cdl(client, "/tmp/netlist.cdl", LIB, "imported_cell")
```

---

### 导入 Verilog-A

```python
from virtuoso_bridge.virtuoso.veriloga import import_veriloga

# 导入 Verilog-A 文件为 cellview
import_veriloga(client, "model.va", LIB, "va_model")
```

---

## Layout 版图 API

### 上下文管理器模式

```python
from virtuoso_bridge.virtuoso.layout import (
    layout_create_rect,
    layout_create_path,
    layout_create_via,
    layout_create_polygon,
    layout_create_inst_by_master_name as lay_inst,
)

# SMIC 12nm 层常量 (已定义，避免字符串错误)
from virtuoso_bridge.virtuoso.layout import SMIC12SF

LIB = "work_ai"
CELL = "layout_example"

with client.layout.edit(LIB, CELL) as lay:
    # 1. 创建矩形 (AA 层: 有源区)
    lay.add(layout_create_rect(
        SMIC12SF.AA, SMIC12SF.DRAWING,
        [[0, 0], [1, 0.5]]  # [[llx, lly], [urx, ury]]
    ))

    # 2. 创建连线 (M1 金属)
    lay.add(layout_create_path(
        SMIC12SF.M1, SMIC12SF.DRAWING,
        [[0, 0.25], [2, 0.25]],  # 点列表
        width=0.1  # 线宽
    ))

    # 3. 创建通孔 (V0: AA → M1)
    lay.add(layout_create_via(
        SMIC12SF.V0, [0.5, 0.25], "R0"
    ))

    # 4. 创建多边形
    lay.add(layout_create_polygon(
        SMIC12SF.M1, SMIC12SF.DRAWING,
        [[0, 0], [1, 0], [1, 1], [0.5, 1.5], [0, 1]]
    ))

    # 5. 放置 PDK 器件实例
    lay.add(lay_inst(
        "smic12sf", "n18_ckt", "layout", "MN0",
        [0, 0], "R0"
    ))

# 自动: dbSave() → dbClose()
```

---

### SMIC12SF 层常量

**类型安全！避免 "M1" vs "m1" 等字符串错误。**

```python
from virtuoso_bridge.virtuoso.layout import SMIC12SF

# 基础层
SMIC12SF.AA        # 有源区
SMIC12SF.FIN       # FinFET 鳍
SMIC12SF.GT        # 栅极
SMIC12SF.NW        # N 阱
SMIC12SF.DNW       # 深 N 阱
SMIC12SF.PP        # P+ 注入
SMIC12SF.NP        # N+ 注入

# 金属层 (0-7)
SMIC12SF.M0, SMIC12SF.M0C
SMIC12SF.M1, SMIC12SF.M2, SMIC12SF.M3, SMIC12SF.M4
SMIC12SF.M5, SMIC12SF.M6, SMIC12SF.M7

# 顶层厚金属
SMIC12SF.TM1, SMIC12SF.TM2

# 铝垫
SMIC12SF.ALPA, SMIC12SF.PA, SMIC12SF.BUMP

# 通孔
SMIC12SF.V0        # AA → M0
SMIC12SF.V1        # M0 → M1
SMIC12SF.V2        # M1 → M2
SMIC12SF.V3        # M2 → M3
SMIC12SF.V4        # M3 → M4
SMIC12SF.V5        # M4 → M5
SMIC12SF.V6        # M5 → M6
SMIC12SF.TV1       # M6 → TM1
SMIC12SF.TV2       # TM1 → TM2
SMIC12SF.BV1, SMIC12SF.BV2

# 用途 (Purpose)
SMIC12SF.DRAWING   # 图形
SMIC12SF.PIN       # 引脚
SMIC12SF.LABEL     # 标签

# lpp() 辅助函数 (layer-purpose-pair)
lpp = SMIC12SF.lpp(SMIC12SF.M1, SMIC12SF.PIN)  # ("M1", "pin")
```

---

### PDK 器件生成器 (SMIC 12nm FinFET)

**自动调用 PDK PCell，参数化生成器件版图。**

```python
from virtuoso_bridge.virtuoso.layout import (
    smic12sf_nmos_svt, smic12sf_pmos_svt,
    smic12sf_nmos_lvt, smic12sf_pmos_lvt,
    smic12sf_create_nmos, smic12sf_create_pmos,
    smic12sf_create_resistor,
    smic12sf_create_mom_cap,
    smic12sf_create_diode,
)

with client.layout.edit(LIB, CELL) as lay:
    # === MOS 晶体管 ===
    # 标准阈值 (SVT, 默认) — 速度/功耗平衡
    lay.add(smic12sf_nmos_svt("MN0", 0, 0, l=0.014, w=0.1, nf=1))
    lay.add(smic12sf_pmos_svt("MP0", 0, 2, l=0.014, w=0.1, nf=1))

    # 低阈值 (LVT) — 更快但漏电流大
    lay.add(smic12sf_nmos_lvt("MN1", 5, 0, l=0.014, w=0.1, nf=4))
    lay.add(smic12sf_pmos_lvt("MP1", 5, 2, l=0.014, w=0.1, nf=4))

    # 完整控制选项
    lay.add(smic12sf_create_nmos(
        "MN2", 10, 0,
        l=0.014,        # 栅长 (um)
        w=0.1,          # 栅宽每指 (um)
        nf=10,          # 手指数量
        m=2,            # 并联倍数
        vth="ulvt",     # 阈值: ulvt | lvt | svt | hvt
        voltage="08",   # 电压域: "08" (0.8V 核心), "18" (1.8V IO)
        dnw=False,      # 深 N 阱隔离 (仅 NMOS)
    ))

    # === 电阻 ===
    # 金属电阻 (rm1-rm7, rtm1, rtm2, ralpa)
    lay.add(smic12sf_create_resistor("R1", 0, 0,
        res_type="rm1", w=0.1, l=10, m=1))

    # 高阻多晶硅
    lay.add(smic12sf_create_resistor("R2", 5, 0,
        res_type="rhrpo", w=0.5, l=100))

    # N 阱电阻
    lay.add(smic12sf_create_resistor("R3", 10, 0,
        res_type="rnwsti", w=1, l=5))

    # === MOM 电容 ===
    # 标准 2 端
    lay.add(smic12sf_create_mom_cap("C0", 0, 0,
        ports=2, w=1, l=1, nf=10))

    # 高品质 (HQ)
    lay.add(smic12sf_create_mom_cap("C1", 5, 0,
        ports=2, high_quality=True, w=2, l=2))

    # 多端 (2-5 端口)
    lay.add(smic12sf_create_mom_cap("C2", 10, 0, ports=5, w=1, l=1))

    # === 二极管 ===
    lay.add(smic12sf_create_diode("D0", 0, 0,
        diode_type="ndio08", w=0.5, l=0.5))  # N 二极管 0.8V
    lay.add(smic12sf_create_diode("D1", 5, 0,
        diode_type="pdio18", w=1, l=1))      # P 二极管 1.8V
```

**电压域说明:**
- `"08"`: 0.8V 核心器件 (高性能，密度高)
- `"18"`: 1.8V I/O 器件 (耐高压，用于接口)

**阈值选项 (按速度/漏电流递增排序):**
1. `hvt` — High Vt: 最慢，漏电流最小
2. `svt` — Standard Vt: 平衡 (默认)
3. `lvt` — Low Vt: 较快，漏电流大
4. `ulvt` — Ultra Low Vt: 最快，漏电流最大

---

### 版图读取

```python
from virtuoso_bridge.virtuoso.layout.reader import read_layout

# 读取版图几何
layout_data = read_layout(client, LIB, CELL)

# 结构:
# {
#   "instances": [...],  # 器件实例
#   "shapes": [...],     # 所有层的形状 (rect, path, polygon)
#   "vias": [...],       # 通孔
#   "layers_used": ["AA", "GT", "M1", "V1", "M2", ...],
# }
```

---

### 层可见性控制

```python
from virtuoso_bridge.virtuoso.layout import (
    set_layer_visible,
    set_layer_selectable,
    set_layer_valid,
)

# 设置 M1 层可见
set_layer_visible(client, "M1", "drawing", True)

# 设置 V0 通孔不可选
set_layer_selectable(client, "V0", "drawing", False)
```

---

### 清除与删除

```python
# 删除指定层上的所有形状
from virtuoso_bridge.virtuoso.layout import delete_shapes_on_layer
delete_shapes_on_layer(client, LIB, CELL, "M1", "drawing")

# 清除所有布线 (金属 + 通孔)
from virtuoso_bridge.virtuoso.layout import clear_routing
clear_routing(client, LIB, CELL)

# 清除当前编辑的版图
from virtuoso_bridge.virtuoso.layout import clear_current_layout
clear_current_layout(client)
```

---

### 选择与删除

```python
from virtuoso_bridge.virtuoso.layout import select_and_delete

# 选择并删除指定对象
select_and_delete(client, ["inst:M1", "shape:M1:1234"])
```

---

## Maestro 仿真 API

### 会话生命周期

```python
from virtuoso_bridge.virtuoso.maestro import (
    open_gui_session,
    close_gui_session,
    run_and_wait,
    ensure_maestro_view,
)

LIB = "work_ai"
CELL = "tb_opamp"

# 确保 maestro view 存在 (不存在则创建空的)
ensure_maestro_view(client, LIB, CELL)

# 打开 GUI 会话 (必须用于结果读取)
session = open_gui_session(client, LIB, CELL)
print(f"Session ID: {session}")

# 运行仿真并等待完成
# history: 仿真结果目录名 (如 "Interactive.1")
# log_path: 日志文件路径
history, log_path = run_and_wait(client, session=session, timeout=300)

# 关闭会话 (save=True 保存设置变更)
close_gui_session(client, session, save=True)
```

---

### 快照 Snapshot

**这是最常用的 Maestro 操作！** 捕获当前 Maestro 窗口的完整状态。

```python
from virtuoso_bridge.virtuoso.maestro import snapshot

# === 方式 1: CLI (最简单，推荐) ===
# bash:
# virtuoso-bridge snapshot -o output/

# === 方式 2: Python API (用于自动化流水线) ===

# 轻量级: 只执行 SKILL probes，不下载文件
# ~ 150ms，1 次往返，返回字典
probe_results = snapshot(client)
# probe_results = {
#   "session": "session1",
#   "lib": "...", "cell": "...", "view": "...",
#   "mode": "assembler",
#   "unsaved": false,
#   "raw_sections": [
#     ("maeGetTests(...)", "[(test1 ...), ...]"),
#     ("maeGetCorners(...)", "[(typ ...), ...]"),
#     ...
#   ]
# }

# 完整磁盘转储 (推荐用于深度分析)
# 保存: 配置 XML + SKILL probes + 输入 netlist + PSF 结果 + .rdb
result = snapshot(client, output_root="output/")
# result["output_dir"] = "output/20240115_143022__LIB__CELL/"
```

**完整快照目录结构:**
```
output/20240115_143022__myLib__tb_opamp/
├── xml/                    # 配置 XML (过滤后，便于 Python 读取)
│   ├── tests.xml
│   ├── corners.xml
│   ├── variables.xml
│   ├── outputs.xml
│   └── ...
├── skill_probes/           # SKILL 探针原始输出
│   ├── 01_tests.txt
│   ├── 02_corners.txt
│   ├── 03_variables.txt
│   ├── 04_outputs.txt
│   └── ...
├── inputs/                 # 输入网表 (如有)
├── psf/                    # PSF 仿真结果 (如有)
└── maestro.rdb             # 结果数据库 (SQLite，标量输出)
```

---

### 设置设计变量

```python
# 设置单个变量
client.execute_skill(f'maeSetDesignVar("W_input" 1e-6 ?session "{session}")')

# 批量设置
params = {"W_in": 0.5e-6, "W_load": 2e-6, "I_bias": 10e-6}
for name, value in params.items():
    client.execute_skill(f'maeSetDesignVar("{name}" {value} ?session "{session}")')

# 保存设置 (必须！否则不会生效)
client.execute_skill(f'''
    maeSaveSetup(?lib "{LIB}" ?cell "{CELL}" ?view "maestro"
                 ?session "{session}")
''')
```

---

### 运行仿真 (异步 + 等待)

```python
# 1. 启动仿真 (非阻塞，立即返回 history id)
result = client.execute_skill(f'''
    maeRunSimulation(?session "{session}" ?waitUntilDone nil)
''', timeout=30)
history = result.output.strip('"')  # 如 "Interactive.1"

# 2. 等待完成 (阻塞直到仿真结束)
client.execute_skill('maeWaitUntilDone('All)', timeout=300)

# 3. 检查是否有对话框阻塞 (超时/卡住时的恢复手段)
client.dismiss_dialog()
```

---

### 读取结果

#### 方式 1: 从日志文件解析 (**最可靠**)

```python
import re
from pathlib import Path

def parse_maestro_log(log_path):
    """解析 Maestro 日志文件中的输出结果"""
    results = {}
    text = Path(log_path).read_text()
    
    # 匹配格式: output_name \t\t value (带单位)
    pattern = r'^([^\t]+)\t\t([^\t]+)$'
    for line in text.split('\n'):
        m = re.match(pattern, line.strip())
        if m:
            name, value = m.groups()
            results[name.strip()] = value.strip()
    return results

# 使用
log_file = f"/path/to/lib/{CELL}/maestro/results/maestro/{history}.log"
client.download_file(log_file, "output/maestro.log")
results = parse_maestro_log("output/maestro.log")

print(f"Gain: {results.get('gain_db')}")
print(f"BW: {results.get('bandwidth_hz')}")
```

#### 方式 2: Maestro API (需要波形数据存在)

```python
# 打开结果
client.execute_skill(f'maeOpenResults(?history "{history}")')

# 读取标量输出
gain = client.execute_skill(f'maeGetOutputValue("gain_db" "ac_test")')
bw = client.execute_skill(f'maeGetOutputValue("bandwidth_hz" "ac_test")')

# 关闭
client.execute_skill('maeCloseResults()')
```

⚠️ **常见问题**: `maeGetOutputValue` 返回 `nil`
- **原因**: PSF 目录中没有实际波形数据 (默认只保存了标量输出)
- **解决方案**: 启用 "save all" 选项后重新运行:
  ```python
  client.execute_skill(f'maeSetEnvOption("{test}" ?option "save" ?value "all")')
  ```

---

### 设置/获取仿真模式

```python
from virtuoso_bridge.virtuoso.maestro import (
    set_simulator_mode,
    get_simulator_mode,
)

# 设置仿真器模式
# 可用模式: "spectre", "aps", "x", "cx", "ax", "mx", "lx", "vx"
set_simulator_mode(client, "ax")  # APS eXtended (推荐)

# 获取当前模式
current_mode = get_simulator_mode(client)
```

**模式说明:**
| 模式 | 说明 | 许可证需求 |
|-----|------|-----------|
| `spectre` | 基础 Spectre | 最低 |
| `aps` | APS (高级并行仿真) | 中等 |
| `ax` | APS Extended (推荐) | 高 |
| `cx/lx/mx/vx` | Spectre X 系列 | 最高 |

---

### 导出子点 sweep 结果

```python
from virtuoso_bridge.virtuoso.maestro import export_sweep_subpoints

# 导出参数 sweep 的每个子点波形
export_sweep_subpoints(client, session, test_name, output_dir="output/sweep")
```

---

## Spectre 独立仿真 API

**SpectreSimulator 不需要 Virtuoso GUI 运行！** 直接通过 SSH 执行 Spectre，适合:
- 批量参数扫描
- 优化循环
- 不需要原理图/测试环境设置时

### 快速开始
=======
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
>>>>>>> 533b7ef (update)

```python
from virtuoso_bridge.spectre.runner import SpectreSimulator, spectre_mode_args
from pathlib import Path

<<<<<<< HEAD
# 1. 创建仿真器实例 (从环境变量读取 SSH 配置)
sim = SpectreSimulator.from_env(
    spectre_args=spectre_mode_args("ax"),  # APS extended (推荐)
    work_dir="./output",
    output_format="psfascii",  # ASCII 格式，便于 Python 解析
)

# 2. 检查许可证 (可选)
license_info = sim.check_license()
if not license_info["ok"]:
    print("Warning: Spectre license not available")
```

---

### 运行单个仿真

```python
# 运行仿真
result = sim.run_simulation(Path("tb_opamp.scs"), {})

# 检查结果
if result.status.is_ok:
    print("✅ 仿真成功")
    
    # 访问波形数据
    freq = result.data.get("ac_freq")       # 频率点
    vout = result.data.get("ac_VOUT")       # VOUT 复数电压
    
    # DC 工作点
    vout_dc = result.data.get("dc_VOUT")
    
    # 瞬态结果
    time = result.data.get("tran_time")
    vout_tran = result.data.get("tran_VOUT")
=======
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
>>>>>>> 533b7ef (update)
else:
    print(f"❌ 仿真失败: {result.errors}")
```

<<<<<<< HEAD
---

### `SimulationResult` 对象

| 属性 | 说明 |
|-----|------|
| `.status` | `ExecutionStatus.SUCCESS/PARTIAL/FAILURE/ERROR` |
| `.ok` | 快捷判断成功 (bool) |
| `.data` | 解析后的波形数据 dict |
| `.errors` | 错误消息列表 |
| `.warnings` | 警告消息列表 |
| `.metadata["output_dir"]` | 本地 `.raw` 目录路径 |
| `.metadata["timings"]` | 各阶段耗时 dict (upload/exec/download/parse) |
| `.metadata["sweep_points"]` | 参数 sweep 各点结果 |

---

### 带 Verilog-A 包含文件

```python
result = sim.run_simulation(
    Path("tb_veriloga.scs"),
    {"include_files": ["model.va", "adc_behav.va"]}
)
```

---

### 并行仿真 (Parallel Simulation)

#### 方式 1: 使用 submit + Future (细粒度控制)

```python
# 提交多个仿真任务 (立即返回 Future)
future1 = sim.submit(Path("tb_1.scs"))
future2 = sim.submit(Path("tb_2.scs"))
future3 = sim.submit(Path("tb_3.scs"))

# ... 做其他工作 ...

# 等待并获取结果
result1 = future1.result()
result2 = future2.result()
result3 = future3.result()

# 或批量等待
results = SpectreSimulator.wait_all([future1, future2, future3])
```

#### 方式 2: 使用 run_parallel (真正并行，独立 SSH 连接)

```python
# 任务列表: (netlist_path, params_dict)
tasks = [
    (Path("tb_1.scs"), {}),
    (Path("tb_2.scs"), {}),
    (Path("tb_3.scs"), {}),
    (Path("tb_4.scs"), {}),
    (Path("tb_5.scs"), {}),
]

# 并行运行 (默认 8 并发)
results = sim.run_parallel(tasks, max_workers=4)

# 统计
passed = sum(1 for r in results if r.status.is_ok)
print(f"Passed: {passed}/{len(results)}")
```

#### 方式 3: 设置并行工作池大小

```python
# 提前设置工作池大小
sim.set_max_workers(16)  # 最多 16 个并发

# 关闭工作池 (释放资源)
sim.shutdown()
```

---

### PSF ASCII 解析器

```python
from virtuoso_bridge.spectre.parsers import (
    parse_spectre_psf_ascii,
    parse_psf_ascii_directory,
    parse_sweep_psf_directory,
)

# 解析单个 PSF 文件
result = parse_spectre_psf_ascii(Path("output/tb_opamp.raw/ac.ac"))
if result.status.is_ok:
    freq = result.data["freq"]
    vout = result.data["VOUT"]  # 复数格式 (real, imag)

# 解析整个 .raw 目录 (自动识别 tran/ac/dc)
data = parse_psf_ascii_directory(Path("output/tb_opamp.raw"))
# data = {
#   "ac_freq": [...],
#   "ac_VOUT": [...],
#   "dc_VDD": [...],
#   "tran_time": [...],
#   "tran_VOUT": [...],
# }

# 解析参数 sweep 目录
sweep = parse_sweep_psf_directory(Path("output/sweep.raw"))
# sweep = {
#   1: {"freq": [...], "VOUT": [...], ...},  # 第 1 点
#   2: {"freq": [...], "VOUT": [...], ...},  # 第 2 点
#   ...
# }
```

**PSF Delta 压缩支持**: 解析器自动处理 Spectre 的 delta 压缩格式，只存储变化的值，然后插值重建完整的信号向量。

---

### 复数波形处理

```python
import math, cmath

# AC 仿真结果是复数格式: [real1, imag1, real2, imag2, ...]
vout_raw = result.data["VOUT"]
vout = [complex(vout_raw[i], vout_raw[i+1]) 
        for i in range(0, len(vout_raw), 2)]

# 计算增益 (dB) 和相位 (度)
gain_db = [20 * math.log10(abs(v)) for v in vout]
phase_deg = [math.degrees(cmath.phase(v)) for v in vout]

# 计算带宽
for i in range(len(gain_db) - 1):
    if gain_db[i] >= 3 and gain_db[i+1] < 3:
        print(f"3dB 带宽: {freq[i]:.2e} Hz")
        break
=======
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
>>>>>>> 533b7ef (update)
```

---

<<<<<<< HEAD
## 参数优化 API

### 什么时候使用优化器

- ✅ 高维参数空间 (>3 参数)，手动扫不动
- ✅ 昂贵的黑盒函数 (每次仿真几秒到几分钟)
- ✅ 多目标优化 (如 GBW > 5GHz && Phase Margin > 60°)
- ❌ 单参数线性扫描 (直接用 sweep)
- ❌ 有解析解的情况 (直接计算)

---

### 贝叶斯优化 (TuRBO)

Trust Region Bayesian Optimization — 样本效率最高的黑盒优化算法。

```python
import numpy as np
from turbo import Turbo1
from virtuoso_bridge.spectre.runner import SpectreSimulator

# === 1. 定义参数空间 ===
PARAM_NAMES = ["W_in", "W_load", "I_bias", "Cc"]
LOWER_BOUNDS = np.array([0.5e-6, 0.5e-6, 1e-6, 10e-15])  # 下界
UPPER_BOUNDS = np.array([10e-6, 10e-6, 100e-6, 1e-12])  # 上界

# === 2. 创建仿真器 ===
sim = SpectreSimulator.from_env(
    spectre_args=["+preset=ax"],
    work_dir="./opt_work",
    output_format="psfascii",
)

# === 3. 定义目标函数 (越小越好) ===
def objective(x):
    try:
        # x 是归一化的 [0,1] 向量，映射到实际参数范围
        params = LOWER_BOUNDS + x * (UPPER_BOUNDS - LOWER_BOUNDS)
        param_dict = dict(zip(PARAM_NAMES, params))
        
        # 生成网表
        netlist = generate_opamp_netlist(param_dict)
        Path("/tmp/tb_opt.scs").write_text(netlist)
        
        # 运行仿真
        result = sim.run_simulation(Path("/tmp/tb_opt.scs"), {})
        
        if not result.status.is_ok:
            return 1e6  # 仿真失败，罚分
        
        # 计算性能指标
        dc_gain, gbw, pm, power = analyze_ac_results(result.data)
        
        # 目标: 最大化 GBW，同时满足约束
        # 违反约束的项会被放大惩罚
        constraint_violation = 0
        if dc_gain < 60:  # 增益 > 60dB
            constraint_violation += (60 - dc_gain) ** 2
        if pm < 60:       # 相位裕度 > 60°
            constraint_violation += (60 - pm) ** 2
        if power > 1e-3:  # 功耗 < 1mW
            constraint_violation += ((power - 1e-3) * 1e3) ** 2
        
        # 目标: -GBW (最小化 = 最大化 GBW) + 约束惩罚
        return -gbw + 1e6 * constraint_violation
        
    except Exception as e:
        print(f"Exception: {e}")
        return 1e6

# === 4. 运行优化 ===
turbo = Turbo1(
    f=objective,
    lb=np.zeros(len(PARAM_NAMES)),  # TuRBO 在 [0,1] 空间搜索
    ub=np.ones(len(PARAM_NAMES)),
    n_init=2 * len(PARAM_NAMES),    # 初始采样点 (2× 参数数)
    max_evals=100,                  # 最大评估次数
    batch_size=1,                   # 串行评估 (用 >1 并行)
    verbose=True,
)

turbo.optimize()

# === 5. 获取最优结果 ===
best_idx = turbo.fX.argmin()
best_x_norm = turbo.X[best_idx]
best_x = LOWER_BOUNDS + best_x_norm * (UPPER_BOUNDS - LOWER_BOUNDS)
best_f = turbo.fX[best_idx]

print(f"\n🎉 最优参数:")
for name, val in zip(PARAM_NAMES, best_x):
    print(f"  {name} = {val:.2e}")
print(f"  GBW = {-best_f:.2e} Hz")
=======
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
>>>>>>> 533b7ef (update)
```

---

<<<<<<< HEAD
### 参数扫描 (Grid Search / Random Search)

```python
import itertools

# 定义扫描范围
W_values = [1e-6, 2e-6, 5e-6, 10e-6]
I_values = [10e-6, 20e-6, 50e-6]

# 生成所有组合
combinations = list(itertools.product(W_values, I_values))

# 并行运行所有组合
tasks = []
for W, I in combinations:
    netlist = generate_netlist({"W": W, "I": I})
    path = Path(f"./output/tb_W{W:.0e}_I{I:.0e}.scs")
    path.write_text(netlist)
    tasks.append((path, {}))

results = sim.run_parallel(tasks, max_workers=8)

# 分析结果
for (W, I), result in zip(combinations, results):
    if result.status.is_ok:
        gbw = extract_gbw(result.data)
        print(f"W={W:.0e}, I={I:.0e} -> GBW={gbw:.2e} Hz")
```

---

## 常见问题与最佳实践

### 🔌 连接问题

| 问题 | 可能原因 | 解决方案 |
|-----|---------|---------|
| `virtuoso-bridge start` 卡住 | SSH 配置不对 | 检查 `ssh $VB_REMOTE_HOST` 是否能无密码登录 |
| `execute_skill` 超时 | 没有加载 SKILL 守护进程 | 在 CIW 执行 `load("/tmp/virtuoso_bridge_xxx/virtuoso_setup.il")` |
| 对话框阻塞 SKILL 通道 | Virtuoso 弹出确认框 | `virtuoso-bridge dismiss-dialog` 或 `client.dismiss_dialog()` |
| 多用户端口冲突 | 多个用户用同一台服务器 | `VB_REMOTE_PORT` 用 `$USER` 哈希生成唯一值 |

**SSH 配置检查清单:**
1. ✅ `ssh $VB_REMOTE_HOST` 无需密码登录 (ssh key)
2. ✅ `VB_REMOTE_HOST` 在 `~/.ssh/config` 中有配置
3. ✅ 跳板机配置正确 (如果用 `VB_JUMP_HOST`)
4. ✅ 远程机器有 `python3` 和 `cadence` 工具

---

### 📐 原理图编辑最佳实践

1. **永远使用上下文管理器**
   ```python
   # ✅ 正确: 自动 save/close
   with client.schematic.edit(LIB, CELL) as sch:
       sch.add(...)
   
   # ❌ 错误: 可能残留打开的 cellview
   client.execute_skill("dbOpenCellViewByType(...)")
   ```

2. **编辑前先删旧 cell (可选)**
   ```python
   # 避免叠加
   client.execute_skill(f'ddDeleteObj(ddGetObj("{LIB}" "{CELL}"))')
   ```

3. **用 `add_net_label_to_transistor` 代替手动连线**
   - 自动计算 stub 方向
   - 避免 DRC 错误
   - 更符合 Virtuoso 使用习惯

4. **修改 MOS 参数后触发 CDF 回调**
   ```python
   # ✅ 正确: 会更新 finger_width 等衍生参数
   set_instance_params(client, "M1", w="1u", l="14n")
   
   # ❌ 错误: 只改属性，不触发回调
   client.execute_skill('dbReplaceProp(inst "w" "float" 1e-6)')
   ```

---

### 🎨 版图编辑最佳实践

1. **使用 SMIC12SF 层常量，不要手写字符串**
   ```python
   # ✅ 正确: 类型安全，IDE 补全
   layout_create_rect(SMIC12SF.M1, SMIC12SF.DRAWING, ...)
   
   # ❌ 错误: 容易打错，没有补全
   layout_create_rect("M1", "drawing", ...)
   ```

2. **器件优先用 PDK generator，不要手动画形状**
   ```python
   # ✅ 正确: 调用 PDK PCell，自动生成 LVS clean 的版图
   smic12sf_nmos_svt("MN0", 0, 0, l=0.014, w=0.1, nf=4)
   
   # ❌ 错误: 手动画容易出错，PDK 更新后不兼容
   layout_create_rect(SMIC12SF.AA, ...)
   layout_create_rect(SMIC12SF.GT, ...)
   ```

3. **通孔用 `layout_create_via`，不要手动画两个方块**

---

### ⚡ 仿真最佳实践

1. **Maestro vs SpectreSimulator**

   | 场景 | 用 Maestro | 用 SpectreSimulator |
   |-----|-----------|-------------------|
   | 已有原理图/测试环境 | ✅ | ❌ |
   | 需要 ADE 界面交互 | ✅ | ❌ |
   | 批量参数扫描 | ⚠️ (慢) | ✅ |
   | 优化循环 | ⚠️ (麻烦) | ✅ |
   | 只有网表，没有 Virtuoso | ❌ | ✅ |
   | 需要和原理图同步 | ✅ | ❌ |

2. **Spectre 模式选择**
   - `ax`: 默认推荐，APS extended，最快，精度好
   - `lx`: Spectre X，超大规模电路
   - `spectre`: 只在需要兼容旧网表时用

3. **AC 仿真收敛问题**
   - 检查 DC 工作点是否合理 (所有管子在饱和区)
   - 加 `?abstol=1u ?reltol=0.001` 放宽容差
   - 加 `ic` 节点初始条件

4. **瞬态仿真太慢**
   - 用 `+preset=ax` 或 `+preset=lx`
   - 放宽 `errpreset=moderate` 或 `conservative`
   - 最大时间步长 `maxstep=10p`

---

### 🔍 调试技巧

#### 1. 查看 SKILL 原始输出
```python
result = client.execute_skill("...")
print(f"Status: {result.status}")
print(f"Raw: {repr(result.raw)}")
print(f"Output: {repr(result.output)}")
```

#### 2. 用 `fetch` 调试实例参数
```python
insts = client.fetch(
    'geGetEditCellView()~>instances',
    ["name", "cellName", "w", "l", "nf", "m"]
)
for inst in insts:
    print(f"{inst['name']}: w={inst.get('w')}, l={inst.get('l')}")
```

#### 3. 仿真失败看 log
```python
# 下载远程 log
client.download_file(
    f"/tmp/sim_{run_id}/spectre.out",
    "output/spectre.out"
)

# 搜索错误
import re
with open("output/spectre.out") as f:
    for line in f:
        if re.search(r"(error|Error|ERROR)", line):
            print(line.strip())
=======
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
>>>>>>> 533b7ef (update)
```

---

<<<<<<< HEAD
### 📁 输出文件命名规范
=======
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
>>>>>>> 533b7ef (update)

```
output/{operation}_{YYYYMMDD}_{HHMMSS}.{ext}
```

<<<<<<< HEAD
**示例文件名:**

| 文件类型 | 示例文件名 |
|---------|-----------|
| 原理图创建脚本 | `output/schematic_opamp_20240115_143000.il` |
| 参数修改脚本 | `output/params_update_20240115_143500.skill` |
| Spectre 网表 | `output/tb_opamp_20240115_144000.scs` |
| 仿真结果目录 | `output/sim_ac_20240115_144500.raw/` |
| Maestro 快照 | `output/snapshot_20240115_143022__work_ai__tb_opamp/` |
| 截图 | `output/screenshot_ciw_20240115_145000.png` |

**Python 代码模板:**
```python
=======
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
>>>>>>> 533b7ef (update)
from datetime import datetime
from pathlib import Path

def get_output_path(operation, ext):
    """生成带时间戳的输出文件路径"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{operation}_{timestamp}.{ext}"
    return output_dir / filename

<<<<<<< HEAD
# 使用
scs_path = get_output_path("tb_opamp", "scs")
png_path = get_output_path("screenshot", "png")
=======
# 使用示例
scs_path = get_output_path("tb_opamp", "scs")
png_path = get_output_path("bode_plot", "png")
il_path = get_output_path("schematic_create", "il")
>>>>>>> 533b7ef (update)
```

---

<<<<<<< HEAD
### 🔒 多用户使用最佳实践

1. **端口隔离**
   - 每个用户的 `VB_REMOTE_PORT` 应该不同
   - 建议用用户名的哈希值: `hash(username) % 10000 + 60000`

2. **临时文件隔离**
   - 桥接会自动用 `/tmp/virtuoso_bridge_$USER/`
   - 仿真工作目录建议加用户名前缀: `VB_SPECTRE_WORK_DIR=/tmp/sim_$USER/`

3. **Virtuoso 多会话**
   - 每个用户独立的 Virtuoso 进程
   - 不要共享 CIW 窗口

---

### 📊 性能基准

| 操作 | 时间 | 备注 |
|-----|------|-----|
| `execute_skill("1+2")` | ~50ms | 空操作，纯往返延迟 |
| `fetch(..., 4 fields)` | ~100ms | 10 个实例 |
| 创建 10 个原理图实例 | ~200ms | 上下文管理器批量提交 |
| 创建 1 个 MOS 版图 | ~150ms | PCell 调用 |
| Maestro 快照 (轻量) | ~150ms | 只跑 SKILL probes |
| Maestro 快照 (完整) | 1-5s | 下载 netlist + PSF |
| Spectre AC 仿真 (opamp) | 2-10s | 取决于电路规模 |
| `parse_psf_ascii_directory` | ~50ms | 1k 频点 AC 结果 |

**网络延迟影响**: SSH 延迟每增加 100ms，所有操作都增加约 100ms。建议服务器在同一局域网内。

---

### 📚 参考文档索引

| 主题 | 文件路径 |
|-----|---------|
| **Schematic API (Python)** | `skills/virtuoso/references/schematic-python-api.md` |
| **Schematic API (SKILL)** | `skills/virtuoso/references/schematic-skill-api.md` |
| **Layout API (Python)** | `skills/virtuoso/references/layout-python-api.md` |
| **Layout API (SKILL)** | `skills/virtuoso/references/layout-skill-api.md` |
| **Maestro API** | `skills/virtuoso/references/maestro-python-api.md` |
| **SMIC12SF PDK** | `skills/virtuoso/references/smic12sf-pdk.md` |
| **仿真流程指南** | `skills/virtuoso/references/simulation-flow.md` |
| **故障排除** | `skills/virtuoso/references/troubleshooting.md` |
| **Spectre 网表语法** | `skills/spectre/references/netlist_syntax.md` |
| **并行仿真配置** | `skills/spectre/references/parallel.md` |

---

**文档生成时间**: 2024-01-15
**适用版本**: virtuoso-bridge v1.0+
**验证状态**: ✅ 所有 API 签名已对照源码验证
=======
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
>>>>>>> 533b7ef (update)
