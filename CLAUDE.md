# Virtuoso Bridge Lite

用 Python 远程控制 Cadence Virtuoso — 原理图/版图编辑、仿真运行、结果解析的全自动化。

## 快速开始

```bash
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

## 目录结构

```
virtuoso-bridge-lite/
├── src/virtuoso_bridge/          # 核心库
│   ├── cli.py                    # CLI 入口
│   ├── env.py                    # 环境变量 / SSH 配置
│   ├── models.py                 # 数据模型
│   ├── wrappers.py               # 便捷封装
│   ├── transport/                # SSH 传输层
│   │   ├── ssh.py                # SSH 连接管理
│   │   ├── tunnel.py             # 端口转发
│   │   └── remote_paths.py       # 远程路径处理
│   ├── virtuoso/                 # Virtuoso 控制
│   │   ├── basic/bridge.py       # RAMIC 桥接通信协议
│   │   ├── basic/composition.py  # SKILL 执行组合
│   │   ├── schematic/            # 原理图 API
│   │   │   ├── editor.py         # 原理图编辑
│   │   │   ├── reader.py         # 原理图读取
│   │   │   ├── params.py         # 参数管理
│   │   │   └── ops.py            # 操作封装
│   │   ├── layout/               # 版图 API
│   │   │   ├── editor.py         # 版图编辑
│   │   │   ├── reader.py         # 版图读取
│   │   │   ├── layers.py         # 层管理
│   │   │   ├── ops.py            # 操作封装
│   │   │   └── pdk.py            # PDK 工具
│   │   ├── maestro/              # Maestro 仿真
│   │   │   ├── lifecycle.py      # 会话生命周期
│   │   │   ├── reader/           # 结果读取
│   │   │   └── writer.py         # 写入/修改
│   │   ├── spectre/              # Spectre 独立仿真
│   │   ├── snapshot.py           # GUI 截图
│   │   ├── visio.py              # Visio 视图
│   │   ├── x11.py                # X11 转发
│   │   └── self_check.py         # 自检
│   └── resources/                # 静态资源
├── examples/                     # 示例脚本
│   ├── 01_virtuoso/              # Virtuoso 操作
│   │   ├── basic/                # 基础 (SKILL 执行/加载/截图)
│   │   ├── schematic/            # 原理图 (创建/读取/参数)
│   │   ├── layout/               # 版图 (创建/布线/PDK)
│   │   ├── maestro/              # Maestro 仿真
│   │   ├── symbol/               # 符号创建
│   │   ├── digital_import/       # 数字导入 (GDS/Verilog)
│   │   └── veriloga/             # Verilog-A 导入
│   ├── 02_spectre/               # Spectre 独立仿真
│   └── test_visio_export.py      # Visio 导出测试
├── skills/                       # AI Agent 技能定义
├── tools/                        # 工具脚本
│   ├── skill_exec.py             # SKILL 一键执行
│   └── dspf_analysis.py          # DSPF 分析
├── tests/                        # 单元测试
└── docs/                         # 文档 / API 参考
```

## API 概览

### VirtuosoClient — 核心入口

```python
from virtuoso_bridge import VirtuosoClient

# 创建
client = VirtuosoClient.from_env()                 # 从 .env 创建
client = VirtuosoClient(host="127.0.0.1", port=65432)  # 直接指定

# 连接测试
client.test_connection(timeout=5)                  # 测试桥接连接
client.run_shell_command("ls /remote/path")        # 远程 shell

# SKILL 执行
r = client.execute_skill('plus(1 2)')               # 执行 SKILL 表达式
r = client.execute_skill('load("/path/to/file.il")', timeout=120)  # 加载文件
# r.output == '"3"'  (成功)  |  r.output == 'nil'  (失败/无返回)
```

### Schematic — 原理图

```python
# 创建 cell + 放置实例
client.execute_skill(f'''dbCreateInst(...)''')

# 读取连接
client.execute_skill('schGetCurrentConnTerms("/")')

# 参数管理
client.execute_skill('inst~>w = "10u"')
```

常用 SKILL: `schCreateInst()`, `schCreateWire()`, `schCreatePin()`, `dbGetInstTermsByNetName()`, `inst~>param`

示例: `examples/01_virtuoso/schematic/`

### Layout — 版图

```python
# 创建版图
client.execute_skill('dbOpenCellViewByType("LIB" "cell" "layout" "maskLayout" "w")')

# 画多边形
client.execute_skill('dbCreatePolygon(cv list("M1" "drawing") list(list(0 0) list(1 0) list(1 1) list(0 1)))')

# 放置 PDK PCell
client.execute_skill('dbCreateInst(cv master "C0" list(0 0) "R0")')
client.execute_skill('inst~>lr = "10u"')

# 通孔
client.execute_skill('dbCreateVia(cv "V1" list(x y) "R0" 1 1 0.16 0.16 ?legalize "minimize")')

# 导出 GDS
client.execute_skill('strmOut(?libName "LIB" ?cellName "cell" ?strmFile "out.gds" ?scale 1e-3)')
```

示例: `examples/01_virtuoso/layout/`

### Maestro — 仿真

```python
# 打开仿真结果 / 读取波形/metrics / GUI 模式
client.execute_skill('dbOpenMaestroSession(...)')
client.execute_skill('maestroGetSessionResults(...)')
```

示例: `examples/01_virtuoso/maestro/`

### Spectre — 独立仿真

```python
from virtuoso_bridge.spectre import SpectreRunner
runner = SpectreRunner(client)
result = runner.run_netlist("netlist.scs", output_dir="./sim")
```

示例: `examples/02_spectre/`

### 截图

```python
client.take_screenshot("/path/to/save.png")
```

## 通信协议

Python → TCP JSON → RAMIC Bridge Daemon (SKILL) → Virtuoso:

```python
# 发送
{"skill": "+ 1 2", "timeout": 60}
# 成功: STX (0x02) + 结果字符串
# 错误: NAK (0x15) + 错误信息
```

传输层: 直连 TCP / SSH 隧道 / ProxyJump / X11 转发

协议实现: `src/virtuoso_bridge/virtuoso/basic/bridge.py`
SSH 隧道: `src/virtuoso_bridge/transport/tunnel.py`

## PDK 支持 (SMIC 12nm SFe)

```python
# 读取 PCell 参数
client.execute_skill('master~>lr~>value')
client.execute_skill('master~>nf~>value')
```

常用器件: `n18_ckt`, `p18_ckt`, `mom_2t_1p25` (lr/nf/tm/bm), `mim_ckt` (W/H), `rhrpo_2t_ckt`

PDK 工具: `src/virtuoso_bridge/virtuoso/layout/pdk.py`

## 常用命令速查

```bash
# 执行 SKILL
python3 tools/skill_exec.py 'plus(1 2)'
python3 tools/skill_exec.py --load /path/to/setup.il

# MOM 电容批量生成 + GDS 导出
python3 examples/01_virtuoso/layout/15_smic12sf_pdk.py

# Spectre 仿真
python3 examples/02_spectre/01_inverter_tran.py

# 验权
python3 examples/01_virtuoso/basic/04_list_library_cells.py
```

## 关键约束

- SKILL 执行是**同步阻塞**的 — 长时间操作设 `timeout` 参数
- **不可交互** — 不能弹对话框、等待用户输入
- GUI 操作通过 X11 转发实现 (VISIO / screenshot)
- 跨平台: Linux/macOS 直连, Windows 需 WSL
- Maestro GUI session 有生命周期, 用完必须 close
- PCell 参数通过 `inst~>paramName` 读写
- GDS 导出 `?scale 1e-3` 是关键 (database unit 1nm → 1μm)
