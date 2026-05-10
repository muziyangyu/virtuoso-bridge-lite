# Sub Skills 索引

## 概述

本目录包含 virtuoso-bridge-lite 项目的所有子技能（Sub Skills）文档，按功能领域组织。

## Skill 总览

| Skill | 功能领域 | 入口文件 | 参考文档数量
|---|---|---|---
| **[virtuoso](./virtuoso/SKILL.md)** | Virtuoso/SKILL、原理图/版图编辑、Maestro/ADE、网表生成 | `SKILL.md` | 13
| **[spectre](./spectre/SKILL.md)** | Spectre仿真、网表驱动仿真、并行仿真 | `SKILL.md` | 2
| **[optimizer](./optimizer/SKILL.md)** | 黑盒优化、电路尺寸优化、参数调优 | `SKILL.md` | 0

---

## virtuoso Skill 文档

| 文档 | 描述
|---|---
| [SKILL.md](./virtuoso/SKILL.md) | Virtuoso Skill 主文档 - 完整API和使用指南
| [batch-netlist-si.md](./virtuoso/batch-netlist-si.md) | 使用si批量翻译器生成网表（无需Maestro）
| [cellview-on-disk-layout.md](./virtuoso/cellview-on-disk-layout.md) | Cellview磁盘布局：sch.oa、maestro状态XML、锁文件等
| [layout-python-api.md](./virtuoso/layout-python-api.md) | 版图编辑Python API（LayoutEditor、形状/通孔/实例创建）
| [layout-skill-api.md](./virtuoso/layout-skill-api.md) | 版图SKILL API（读取/查询、马赛克、层控制）
| [maestro-python-api.md](./virtuoso/maestro-python-api.md) | Maestro Python API（快照、XML过滤、结果读取）
| [maestro-skill-api.md](./virtuoso/maestro-skill-api.md) | Maestro SKILL API（mae*函数、OCEAN、Corners）
| [netlist.md](./virtuoso/netlist.md) | CDL/Spectre网表格式、spiceIn导入
| [schematic-python-api.md](./virtuoso/schematic-python-api.md) | 原理图编辑Python API（SchematicEditor、SchematicOps）
| [schematic-recreation.md](./virtuoso/schematic-recreation.md) | 从现有设计重建原理图（网格布局、差分对约定）
| [schematic-skill-api.md](./virtuoso/schematic-skill-api.md) | 原理图SKILL API、终端感知助手、CDF参数
| [simulation-flow.md](./virtuoso/simulation-flow.md) | 标准仿真流程（8步指南、陷阱、优化循环）
| [smic12sf-pdk.md](./virtuoso/smic12sf-pdk.md) | SMIC 12nm FinFET PDK（层常量、器件生成器、参数参考）
| [troubleshooting.md](./virtuoso/troubleshooting.md) | 常见问题排查（GUI阻塞、CDF异常、连接问题）

---

## spectre Skill 文档

| 文档 | 描述
|---|---
| [SKILL.md](./spectre/SKILL.md) | Spectre Skill 主文档 - 完整API和使用指南
| [netlist_syntax.md](./spectre/netlist_syntax.md) | Spectre网表格式、分析语句、参数化
| [parallel.md](./spectre/parallel.md) | 并行仿真、多服务器、CLI作业管理、.env配置

---

## optimizer Skill 文档

| 文档 | 描述
|---|---
| [SKILL.md](./optimizer/SKILL.md) | Optimizer Skill 主文档 - 黑盒优化框架、TuRBO、scipy

---

## 技能关联关系

```
optimizer
  └── 依赖 → spectre (Spectre仿真后端)
  └── 依赖 → virtuoso (Maestro GUI后端)

spectre
  └── 关联 → virtuoso (GUI Maestro仿真)

virtuoso
  └── 关联 → spectre (独立网表仿真)
```

## 触发条件

### virtuoso Skill 触发
当用户提及：Virtuoso、Maestro、ADE、CIW、SKILL、layout、schematic、cellview、OCEAN、或任何Cadence EDA操作时触发。

### spectre Skill 触发
当用户想要：从网表文件运行SPICE/Spectre仿真、在Virtuoso GUI外执行瞬态/AC/PSS/pnoise分析、解析PSF波形数据、在一台或多台服务器上并行运行多个仿真、检查仿真作业状态、或提及Spectre APS/AXS模式时触发。也会触发sim-jobs、sim-cancel或并行/并发仿真请求。

### optimizer Skill 触发
当用户想要：优化、调整、尺寸设定、扫描或探索设计空间以满足规格时触发。包括电路尺寸优化（W/L、偏置、无源器件）、寻找最佳工作点、最小化功耗-延迟或噪声-功耗权衡、或任何需要搜索多个参数以达到目标的任务。

---

*最后更新：2026-04-30*
