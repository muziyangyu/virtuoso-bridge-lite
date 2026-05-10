# 指南手册

## 概述

本目录包含 virtuoso-bridge-lite 项目的完整工作流程指南。

## 必读指南

| 优先级 | 文档 | 描述
|---|---|---
| 🔴 **最高** | [SKILL_QUICK_REFERENCE.md](./SKILL_QUICK_REFERENCE.md) | **⚠️ 原理图死亡陷阱手册** - 8个生产级BUG及修复方案。第一必读！
| ⭐ **高** | [SCHEMATIC_GENERATION_PLAYBOOK.md](./SCHEMATIC_GENERATION_PLAYBOOK.md) | **完整流程手册** - 5阶段工作流：原理图创建 → 参数同步 → Spectre扫描 → Bode图 → 回写

## 指南详情

### ⚠️ SKILL_QUICK_REFERENCE.md - 原理图死亡陷阱手册

**杀手级 BUG 0：嵌套 `dbOpenCellViewByType`**
```python
# ❌ 致命错误 - 这样会让你一下午白干！
with client.schematic.edit(LIB, CELL) as sch:
    sch.add('let((cv i) cv = dbOpenCellViewByType(...) ...)')

# ✅ 正确方法：参数修改单独执行
client.execute_operations([skill_code])
```

包含 8 个实际生产中遇到的 BUG：
- 双重 cellview 打开崩溃
- 错误的 API 调用方法
- `procedure` 嵌套导致的问题
- 终端大小写不匹配
- 参数 setter 错误
- 4 参数 `dbOpen` 陷阱
- 等等...

---

### ⭐ SCHEMATIC_GENERATION_PLAYBOOK.md - 完整流程手册

**5 阶段工作流：**

1. **原理图创建** - 实例放置、连线、引脚添加
2. **参数同步** - SI 单位转换（nfin=23 NOT nfin=23n）
3. **Spectre 扫描** - AC/DC/瞬态分析配置
4. **Bode 图** - 增益/相位裕度计算
5. **参数回写** - 优化结果写回原理图

**12 个陷阱提示：**
- `edit()` 内部嵌套 `dbOpen` = 原理图删除
- `l=0.168` vs `l=1.68e-7` (SI 单位！)
- `save I(V0)` 语法错误
- M7 栅极/衬底浮空问题
- CDF vs `dbReplaceProp`

---

## 其他参考

| 文档类型 | 位置
|---|---
| Sub Skills 文档 | [../sub_skills/](../sub_skills/)
| API 参考 | [../api/](../api/)
| 故障排除 | [../troubleshooting/](../troubleshooting/)

*最后更新：2026-04-30*
