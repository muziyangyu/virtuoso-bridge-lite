# Virtuoso Bridge Lite 文档中心

## 文档导航

### 📚 [Sub Skills](./sub_skills/) - 子技能文档
完整的技能文档库，包含 virtuoso、spectre、optimizer 三大技能领域的所有参考文档。

| Skill | 描述 | 文档数
|---|---|---
| [virtuoso](./sub_skills/virtuoso/) | Virtuoso/SKILL、原理图/版图、Maestro/ADE | 14
| [spectre](./sub_skills/spectre/) | Spectre仿真、并行仿真、网表语法 | 3
| [optimizer](./sub_skills/optimizer/) | 黑盒优化、参数调优 | 1

---

### 🔧 [API 参考](./api/) - SKILL API 文档
Cadence Virtuoso SKILL 函数 API 参考手册。

| 文档 | 描述
|---|---
| [API_DOC_INDEX.md](./api/API_DOC_INDEX.md) | 完整 API 索引 - 3856 个函数映射到 Cadence 文档
| [API_REFERENCE.md](./api/API_REFERENCE.md) | API 参考手册（完整版）
| [API_QUICK_REF.md](./api/API_QUICK_REF.md) | 快速参考卡 - 常见 API 前缀和使用示例
| [API_QUICK_CARD.md](./api/API_QUICK_CARD.md) | 紧凑 API 速查表
| [API_STATS.md](./api/API_STATS.md) | API 统计报告 - 按前缀的函数计数
| [API_MORE_INFO.md](./api/API_MORE_INFO.md) | 附加 API 文档详情

---

### 📖 [指南手册](./guides/) - 工作流指南
完整的端到端工作流程指南。

| 文档 | 描述
|---|---
| ⚠️ **[SKILL_QUICK_REFERENCE.md](./guides/SKILL_QUICK_REFERENCE.md)** | **必读！** 原理图死亡陷阱手册 - 8个生产级BUG及修复方案
| ⭐ **[SCHEMATIC_GENERATION_PLAYBOOK.md](./guides/SCHEMATIC_GENERATION_PLAYBOOK.md)** | 原理图→Spectre→优化完整流程手册 - 5阶段工作流

---

### 🐛 [故障排除](./troubleshooting/) - 问题排查
常见问题诊断与解决方案。

| 文档 | 描述
|---|---
| ⭐ [SPECTRE_OPAMP_DEBUG_NOTES.md](./troubleshooting/SPECTRE_OPAMP_DEBUG_NOTES.md) | 运放AC调试日志 - -600dB增益问题修复
| [SPECTRE_TROUBLESHOOTING.md](./troubleshooting/SPECTRE_TROUBLESHOOTING.md) | Spectre 故障排除 - 网表语法错误、AC反馈配置、DC偏置修复、PSF解析

---

### 🛠️ [工具归档](./tools/) - 开发脚本
项目开发阶段使用的一次性工具脚本归档。

| 工具 | 描述
|---|---
| [check_skill_functions.py](./tools/check_skill_functions.py) | SKILL 函数可用性检查工具 - 验证 ICAD_201 文档中函数是否存在
| [explore_pdk.py](./tools/explore_pdk.py) | PDK 探索脚本 - 分析 SMIC 12nm FinFET PDK 层定义和器件
| [extract_skill_docs.py](./tools/extract_skill_docs.py) | SKILL 文档提取工具 - 从 Cadence HTML 文档中提取函数列表
| [parse_api_more_info.py](./tools/parse_api_more_info.py) | API 文档解析工具 - 生成 API 统计报告
| [optimize_layout.py](./tools/optimize_layout.py) | 版图优化实验脚本
| [pdk_exploration_report.md](./tools/pdk_exploration_report.md) | PDK 探索输出报告

> **重要说明**：电路优化过程中的工作脚本、仿真网表、运行结果都归档在**项目根目录的 `output/` 文件夹**下，不在 `docs/tools/` 中。`output/` 包含带时间戳的优化运行目录、Spectre 结果文件、生成的 Bode 图等。

---

## 目录结构

```
docs/
├── README.md                          # 本文档（总索引）
├── SUB_SKILLS_MAP.md                  # 文档映射表（源目录→发布目录）
│
├── tools/                             # 🛠️ 工具脚本归档
│   ├── README.md                      # 工具说明
│   ├── check_skill_functions.py       # SKILL函数可用性检查
│   ├── explore_pdk.py                 # PDK探索脚本
│   ├── extract_skill_docs.py          # SKILL文档提取
│   ├── optimize_layout.py             # 版图优化实验
│   ├── parse_api_more_info.py         # API统计生成
│   └── pdk_exploration_report.md      # PDK探索报告
│
├── api/                               # 🔧 API 参考文档
│   ├── README.md
│   ├── API_DOC_INDEX.md
│   ├── API_REFERENCE.md
│   ├── API_QUICK_REF.md
│   ├── API_QUICK_CARD.md
│   ├── API_STATS.md
│   └── API_MORE_INFO.md
│
├── guides/                            # 📖 指南手册
│   ├── README.md
│   ├── SKILL_QUICK_REFERENCE.md       # ⚠️ 原理图陷阱手册（必读）
│   └── SCHEMATIC_GENERATION_PLAYBOOK.md  # ⭐ 完整流程手册
│
├── troubleshooting/                   # 🐛 故障排除
│   ├── README.md
│   ├── SPECTRE_OPAMP_DEBUG_NOTES.md   # ⭐ 运放AC调试
│   └── SPECTRE_TROUBLESHOOTING.md     # Spectre常见问题
│
└── sub_skills/                        # 📚 子技能文档
    ├── README.md                      # 子技能索引
    ├── virtuoso/                      # Virtuoso Skill (14文档)
    ├── spectre/                       # Spectre Skill (3文档)
    └── optimizer/                     # Optimizer Skill (1文档)
```

## 新手阅读顺序

1. **第一优先级**：[guides/SKILL_QUICK_REFERENCE.md](./guides/SKILL_QUICK_REFERENCE.md) - 避免致命BUG
2. **第二优先级**：[sub_skills/README.md](./sub_skills/README.md) - 了解三大技能领域
3. **第三优先级**：[guides/SCHEMATIC_GENERATION_PLAYBOOK.md](./guides/SCHEMATIC_GENERATION_PLAYBOOK.md) - 完整工作流

## 源文件位置

- skills/ 目录是技能定义源文件
- docs/sub_skills/ 是同步后的文档发布版本

---

*最后更新：2026-04-30*
