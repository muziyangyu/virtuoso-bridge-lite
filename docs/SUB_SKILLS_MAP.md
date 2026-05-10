# Sub Skills 文档映射表

## 概述

本文档梳理了 virtuoso-bridge-lite 项目中所有文档与 sub skills 的对应关系。

## docs/ 分类目录文档与 Skill 映射

| 文档 | 位置 | 对应 Skill | 描述
|---|---|---|---
| API_DOC_INDEX.md | [api/](./api/) | virtuoso | 完整API索引 - 映射每个SKILL函数到Cadence文档
| API_REFERENCE.md | [api/](./api/) | virtuoso | API参考手册（完整版）
| API_QUICK_REF.md | [api/](./api/) | virtuoso | 快速参考卡 - 常见API前缀和使用示例
| API_QUICK_CARD.md | [api/](./api/) | virtuoso | 紧凑API速查表
| API_STATS.md | [api/](./api/) | virtuoso | API统计报告 - 按前缀的函数计数
| API_MORE_INFO.md | [api/](./api/) | virtuoso | 附加API文档详情
| SCHEMATIC_GENERATION_PLAYBOOK.md | [guides/](./guides/) | virtuoso | ⭐ 原理图→Spectre→优化完整流程手册
| SKILL_QUICK_REFERENCE.md | [guides/](./guides/) | virtuoso | ⚠️ 原理图死亡陷阱手册（必读）
| SPECTRE_OPAMP_DEBUG_NOTES.md | [troubleshooting/](./troubleshooting/) | spectre | ⭐ 运放AC调试日志（-600dB增益问题修复）
| SPECTRE_TROUBLESHOOTING.md | [troubleshooting/](./troubleshooting/) | spectre | Spectre故障排除（网表语法错误、AC反馈配置等）

## docs/sub_skills/ 子技能目录结构

```
docs/sub_skills/
├── README.md                          # 本索引文件
├── virtuoso/                          # Virtuoso Skill 文档
│   ├── SKILL.md                       # Virtuoso Skill 主文档
│   ├── batch-netlist-si.md            # 批量网表si翻译
│   ├── cellview-on-disk-layout.md     # Cellview磁盘布局
│   ├── layout-python-api.md           # 版图Python API
│   ├── layout-skill-api.md            # 版图SKILL API
│   ├── maestro-python-api.md          # Maestro Python API
│   ├── maestro-skill-api.md           # Maestro SKILL API
│   ├── netlist.md                     # 网表格式与导入
│   ├── schematic-python-api.md        # 原理图Python API
│   ├── schematic-recreation.md        # 原理图重建指南
│   ├── schematic-skill-api.md         # 原理图SKILL API
│   ├── simulation-flow.md             # 标准仿真流程
│   ├── smic12sf-pdk.md                # SMIC12SF PDK文档
│   └── troubleshooting.md             # Virtuoso故障排除
├── spectre/                           # Spectre Skill 文档
│   ├── SKILL.md                       # Spectre Skill 主文档
│   ├── netlist_syntax.md              # 网表语法参考
│   └── parallel.md                    # 并行仿真指南
└── optimizer/                         # Optimizer Skill 文档
    └── SKILL.md                       # Optimizer Skill 主文档
```

## 根目录其他文档

| 文档 | 位置 | 用途
|---|---|---
| [AGENTS.md](../AGENTS.md) | 项目根目录 | AI Agent指南 - 整体架构、模式、关键约定
| [README.md](../README.md) | 项目根目录 | 项目README、安装说明
| [SKILL_FUNCTIONS_REFERENCE.md](../SKILL_FUNCTIONS_REFERENCE.md) | 项目根目录 | SKILL函数参考手册（语法与示例）
| [skill_functions_ref.md](../skill_functions_ref.md) | 项目根目录 | SKILL函数参考（简化版）
| [pdk_exploration_report.md](../pdk_exploration_report.md) | 项目根目录 | PDK探索报告

## skills/ 源目录与 docs/sub_skills/ 发布目录

**注意：** `skills/` 目录是源代码技能定义，`docs/sub_skills/` 是文档发布版本。
两者内容一致，`docs/sub_skills/` 用于统一的文档索引和导航。

```
skills/                          docs/sub_skills/
  ├── virtuoso/                    ├── virtuoso/
  │   ├── SKILL.md      ──►       │   ├── SKILL.md
  │   └── references/  ──►        │   └── *.md
  ├── spectre/                     ├── spectre/
  │   ├── SKILL.md      ──►       │   ├── SKILL.md
  │   └── references/  ──►        │   └── *.md
  └── optimizer/                   └── optimizer/
      └── SKILL.md      ──►           └── SKILL.md
```

## 快速导航

### 新手必读
1. ⚠️ [guides/SKILL_QUICK_REFERENCE.md](./guides/SKILL_QUICK_REFERENCE.md) - 原理图死亡陷阱手册（第一）
2. [AGENTS.md](../AGENTS.md) - 整体Agent指南
3. [sub_skills/README.md](./sub_skills/README.md) - Sub Skills索引
4. [guides/SCHEMATIC_GENERATION_PLAYBOOK.md](./guides/SCHEMATIC_GENERATION_PLAYBOOK.md) - 完整流程手册

### 按领域查找
- **原理图编辑**：[sub_skills/virtuoso/SKILL.md](./sub_skills/virtuoso/SKILL.md) → 原理图API部分
- **版图设计**：[sub_skills/virtuoso/smic12sf-pdk.md](./sub_skills/virtuoso/smic12sf-pdk.md)
- **仿真运行**：[sub_skills/virtuoso/simulation-flow.md](./sub_skills/virtuoso/simulation-flow.md)
- **Spectre独立仿真**：[sub_skills/spectre/SKILL.md](./sub_skills/spectre/SKILL.md)
- **参数优化**：[sub_skills/optimizer/SKILL.md](./sub_skills/optimizer/SKILL.md)

---

*最后更新：2026-04-30*
