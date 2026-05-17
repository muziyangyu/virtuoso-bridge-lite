# 工具脚本归档

## 概述

本目录存放项目开发过程中使用的一次性工具脚本，供参考和归档用途。

## 工具列表

| 脚本 | 描述 | 相关输出
|---|---|---
| [check_skill_functions.py](./check_skill_functions.py) | SKILL 函数可用性检查工具 - 验证 ICAD_201 文档中函数是否存在 | `SKILL_FUNCTION_AVAILABILITY.md`
| [explore_pdk.py](./explore_pdk.py) | PDK 探索脚本 - 分析 SMIC 12nm FinFET PDK 层定义和器件 | [pdk_exploration_report.md](./pdk_exploration_report.md)
| [extract_skill_docs.py](./extract_skill_docs.py) | SKILL 文档提取工具 - 从 Cadence HTML 文档中提取函数列表 | `docs/API_DOC_INDEX.md`
| [optimize_layout.py](./optimize_layout.py) | 版图优化实验脚本 | -
| [parse_api_more_info.py](./parse_api_more_info.py) | API 文档解析工具 - 处理 `API_MORE_INFO.md` | `docs/API_STATS.md`

---

## 工具说明

### check_skill_functions.py

**用途**：验证项目中使用的 52 个核心 SKILL 函数在 ICAD_201 文档中是否存在，并在 Virtuoso 中实际测试可用性。

**三层检查：**
1. HTML 锚点精确匹配：`<a name="functionName">`
2. 函数调用匹配：`functionName(`
3. 函数名文本匹配

**Virtuoso 测试：**
- `procedurep(func)` - 检查是否为已定义过程
- `document(func)` - 检查是否有官方文档

---

### explore_pdk.py

**用途**：探索 SMIC 12nm FinFET PDK，提取层定义、器件参数、PCell 信息。

**输出报告：** [pdk_exploration_report.md](./pdk_exploration_report.md)
- 层列表（层号 + 用途）
- MOS 器件参数（L/W/NF 范围）
- 电阻/电容类型
- PCell 参数定义

---

### extract_skill_docs.py

**用途**：从 Cadence 官方 HTML 文档中批量提取 SKILL 函数索引，生成 `docs/API_DOC_INDEX.md`。

**功能：**
- 扫描 `skdfref/*.html` 所有函数锚点
- 按前缀分类统计
- 生成函数 → 文档文件映射表

---

### parse_api_more_info.py

**用途**：解析 `API_MORE_INFO.md` 中的函数列表，生成 API 统计报告 `docs/API_STATS.md`。

**统计维度：**
- 按函数前缀分类（ci*, db*, axl*, hi*, mae*, le*, ge* 等）
- 函数数量分布
- 前缀用途说明

---

## 使用注意

⚠️ **这些脚本是开发阶段的一次性工具：**

1. **不保证可直接运行** - 可能需要特定环境配置
2. **硬编码路径** - 脚本中可能包含特定的服务器路径
3. **需要 SSH/Virtuoso 连接** - 部分脚本需要远程环境
4. **仅作参考归档** - 实际工作流已整合到 virtuoso_bridge 包中

---

## 优化脚本归档说明

**优化过程中的工作脚本都归档在项目根目录的 `output/` 文件夹下，而不是 `docs/tools/`。**

### output/ 目录存放：
- ✅ 实际运行的优化脚本（`optimize_formula.py`, `optimize_converge.py` 等）
- ✅ 带时间戳的仿真运行目录
- ✅ Spectre 网表（`.scs`）和原始结果（`.raw/`）
- ✅ 生成的 Bode 图、性能图表（`.png`）
- ✅ 原理图参数同步脚本（`sync_to_schematic.py`, `sync_l.py`）
- ✅ 仿真结果汇总（`optimize_summary.txt`）
- ✅ 最优配置参数（`gain_opt_*/specs.json`）

### docs/tools/ 目录仅存放：
- 📌 通用的基础设施脚本（文档提取、PDK 探索等）
- 📌 可复用的工具代码
- 📌 不会频繁变动的参考脚本

### 为什么这样区分？
1. **体积原因** - 优化产生的 `.raw` 数据文件可能很大（几百 MB）
2. **时效性** - 优化脚本是实验性质，随时可能修改或废弃
3. **可重现** - 脚本 + 结果放在同一目录，便于复现当时的仿真环境
4. **Git 友好** - `output/` 通常在 `.gitignore` 中，避免大文件提交

---

---

*最后更新：2026-05-17*
