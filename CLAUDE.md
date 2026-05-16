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
