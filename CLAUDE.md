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

### Spectre 网表注意事项

**AC 激励参数是 `mag=` 不是 `ac=`**：

```spectre
// 正确 — AC 分析用 mag= 参数
VTOP (net9 0) vsource dc=0 mag=1 type=dc

// 错误 — spectre vsource 不支持 ac=
VTOP (net9 0) vsource dc=0 ac=1 type=dc  // Warning: ignored
```

参考 `examples/02_spectre/assets/cap_dc_ac/tb_cap_dc_ac.scs`。

**Maestro netlister 会优化掉零值 DC 源**（如 dc=0 的 VTOP 不输出到网表），需要手动补回或让 DC ≠ 0。

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

| 器件 | PCell | 关键参数 | 参数设置 |
|------|-------|---------|---------|
| NMOS | n18_ckt | nfin, nf, l | `dbReplaceProp(inst "nfin" "float" 6)` |
| PMOS | p18_ckt | nfin, nf, l | `dbReplaceProp(inst "nfin" "float" 6)` |
| MOM 电容 | mom_2t_1p25 | lr, nf, tm, bm | `inst~>lr = "10u"` |
| MIM 电容 | mim_ckt | w, l, m | `dbReplaceProp(inst "w" "string" "5u")` |
| 电阻 | rhrpo_2t_ckt | l, w, tr | — |

## PDK 参数设置经验

### SMIC12SF MIM 电容 (mim_ckt)

通过 SKILL 设置 `mim_ckt` 参数时，必须用 `dbReplaceProp` 且 propType 为 `"string"`：

```python
# ✅ 正确
client.execute_skill('dbReplaceProp(inst "w" "string" "5u")')
client.execute_skill('dbReplaceProp(inst "l" "string" "5u")')

# ❌ 错误 — float 类型不生效（PCell 可能不转换单位）
client.execute_skill('dbReplaceProp(inst "w" "float" 5e-6)')
```

CDF 回调链（`cdfGetInstCDF` + `cdfGetCellCDF` + callback）理论上可行但过于复杂，`dbReplaceProp` + `"string"` 是最简方案。

### PCell Layout 生成

创建 PCell 的 layout view 用 `dbCreateParamInstByMasterName`：

```python
skill = 'let((cv inst) cv = dbOpenCellViewByType(LIB CELL "layout" "maskLayout" "a") inst = dbCreateParamInstByMasterName(cv "smic12sf" "mim_ckt" "layout" "MIM0" list(0 0) "R0") dbReplaceProp(inst "w" "string" "wu") dbReplaceProp(inst "l" "string" "lu") dbSave(cv) dbClose(cv))'
client.execute_skill(skill, timeout=30)
```

### GDS 导出

用 `xstSetField` + `xstOutDoTranslate`，**务必在 `let()` 内执行**以隔离全局状态：

```python
skill = 'let((r) xstSetField("library" LIB) xstSetField("topCell" CELL) xstSetField("strmFile" GDS) xstSetField("view" "layout") xstSetField("showCompletionMsgBox" "false") r = xstOutDoTranslate())'
client.execute_skill(skill, timeout=60)
```

循环导出时必须用 `let()` 包裹，否则 `xstSetField` 全局状态污染导致 0 字节输出。

### 新建 cell 的参数设置

批量创建含参数的 cell 时，先全删旧 cell：

```python
# 先清空再创建
for c in (r.output or "").strip("()").split():
    client.execute_skill('dbDeleteCell(ddGetObj(LIB) "{}")'.format(c))

# 单行 SKILL: 创建 + 设参 + 保存
skill = 'let((cv inst) cv = dbOpenCellViewByType(LIB CELL "schematic" "schematic" "a") inst = dbCreateInst(...) dbReplaceProp(...) dbSave(cv) dbClose(cv))'
client.execute_skill(skill, timeout=30)
```

`set_instance_params()` 需要 cellview 处于 `geGetEditCellView()` 激活状态，不适合批量离线创建。

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

## 文档索引

| 文档 | 位置 | 说明 |
|------|------|------|
| ⚠️ 原理图陷阱手册 | `docs/guides/SKILL_QUICK_REFERENCE.md` | 必读 — 8 个生产级 BUG（edit() 嵌套清空、终端大小写、参数单位等）|
| ⭐ 原理图→仿真完整流程 | `docs/guides/SCHEMATIC_GENERATION_PLAYBOOK.md` | 5 阶段工作流 + 12 个陷阱 + 仿真优化策略 |
| Spectre 网表故障排除 | `docs/troubleshooting/SPECTRE_TROUBLESHOOTING.md` | 网表语法、AC 反馈、DC 偏置修复、PSF 解析 |
| 运放调试日志 | `docs/troubleshooting/SPECTRE_OPAMP_DEBUG_NOTES.md` | 10 管两级运放从 -600dB 到 67dB 的完整优化历程 |
