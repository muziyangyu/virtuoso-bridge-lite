#!/usr/bin/env python3
"""解析 api_more_info.tgf 并生成使用文档"""

from virtuoso_bridge import SSHClient
import os
from collections import defaultdict

tunnel = SSHClient.from_env()
tunnel.warm()

print("=" * 70)
print("解析 api_more_info.tgf")
print("=" * 70)

# 1. 下载文件
print("\n[1] 下载 TGF 文件...")
result = tunnel.run_command('cat /mnt/data/eda_tool/cadence/ICAD_201/doc/api_more_info/api_more_info.tgf')
content = result.stdout

# 保存原始文件
with open('./docs/api_more_info.tgf', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"原始文件已保存: ./docs/api_more_info.tgf ({len(content)} bytes)")

# 2. 解析文件
print("\n[2] 解析文件内容...")
lines = content.split('\n')

# 跳过 BOM
if lines and lines[0].startswith('\ufeff'):
    lines[0] = lines[0][1:]

# 提取注释和修订历史
comments = []
revision_history = []
in_revision = False
api_entries = []

for line in lines:
    line = line.rstrip()
    
    # 注释行
    if line.startswith(';'):
        comment_text = line[1:].strip()
        comments.append(comment_text)
        
        # 修订历史
        if 'Revision History' in comment_text:
            in_revision = True
        elif in_revision and comment_text and not comment_text.startswith('---'):
            if '/' in comment_text[:10] or comment_text[:2].isdigit():
                revision_history.append(comment_text)
        continue
    
    # 空行
    if not line.strip():
        continue
    
    # 数据行 - 制表符分隔
    if '\t' in line:
        parts = [p.strip() for p in line.split('\t') if p.strip()]
        if len(parts) >= 3:
            entry = {
                'function': parts[0],
                'doc_file': parts[1],
                'anchor': parts[2].strip('"') if len(parts) > 2 else '',
                'type': parts[3] if len(parts) > 3 else 'HTML'
            }
            api_entries.append(entry)

print(f"解析到 {len(api_entries)} 个 API 条目")
print(f"修订历史条目: {len(revision_history)} 条")

# 3. 按文档分组
print("\n[3] 按文档分组...")
doc_groups = defaultdict(list)
for entry in api_entries:
    doc_file = entry['doc_file']
    doc_groups[doc_file].append(entry)

print(f"共有 {len(doc_groups)} 个不同的文档文件")

# 4. 按函数前缀分类
print("\n[4] 按函数前缀分类...")
prefix_groups = defaultdict(list)
for entry in api_entries:
    func_name = entry['function']
    # 提取前缀 (直到第一个大写字母或数字前的小写部分)
    prefix = ''
    for i, c in enumerate(func_name):
        if c.isupper() or c.isdigit():
            prefix = func_name[:i]
            break
    if not prefix:
        prefix = func_name
    prefix_groups[prefix].append(entry)

# 显示主要分类
print("\n主要 API 分类 (按前缀):")
for prefix in sorted(prefix_groups.keys(), key=lambda x: -len(prefix_groups[x])):
    count = len(prefix_groups[prefix])
    if count >= 5:
        print(f"  {prefix:<15} {count:4d} 个函数")

# 5. 生成主文档
print("\n[5] 生成 Markdown 文档...")
main_md = """# Cadence ICADVM20.1 API 补充文档

> 数据源: `api_more_info.tgf`
> 版本: ICADVM20.1
> 生成日期: 2026-04-28

---

## 概述

本文档包含了 Cadence Virtuoso ICADVM20.1 版本中补充的 SKILL API 函数列表。
这些函数是对主文档的补充，涵盖了 ADE XL、约束管理、版图编辑、仿真等各个领域。

---

## 修订历史

"""

for rev in revision_history[:15]:
    main_md += f"- {rev}\n"
if len(revision_history) > 15:
    main_md += f"- ... 还有 {len(revision_history) - 15} 条历史记录\n"

main_md += """
---

## API 分类索引

"""

# 添加分类索引
for prefix in sorted(prefix_groups.keys()):
    count = len(prefix_groups[prefix])
    main_md += f"- [{prefix}](#{prefix.lower()}-api) ({count} 个函数)\n"

main_md += """
---

## API 详细分类

"""

# 按类别生成详细内容
for prefix in sorted(prefix_groups.keys()):
    functions = prefix_groups[prefix]
    main_md += f"\n### {prefix.upper()} API\n\n"
    main_md += f"**共 {len(functions)} 个函数**\n\n"
    main_md += "| 函数 | 文档文件 | 锚点 |\n"
    main_md += "|------|----------|------|\n"
    
    for entry in sorted(functions, key=lambda x: x['function']):
        func = entry['function']
        doc = entry['doc_file'].replace('$', '')
        anchor = entry['anchor']
        main_md += f"| {func} | `{doc}` | `{anchor}` |\n"
    
    main_md += "\n"

# 6. 生成按文档分类的文档
docs_md = """# API 文档文件索引

> 本索引展示了每个文档文件包含的 API 函数。

---

"""

for doc_file in sorted(doc_groups.keys()):
    functions = doc_groups[doc_file]
    clean_name = doc_file.replace('$', '')
    docs_md += f"\n## {clean_name}\n\n"
    docs_md += f"**包含 {len(functions)} 个函数:**\n\n"
    
    for entry in sorted(functions, key=lambda x: x['function']):
        docs_md += f"- `{entry['function']}`\n"

# 7. 生成快速参考卡
quick_ref = """# SKILL API 快速参考卡

> 常用 API 速查

---

## 常用前缀说明

| 前缀 | 功能领域 | 示例 |
|------|----------|------|
| `axl` | ADE XL 相关 | `axlSDBDebugPrint`, `axlToolSetOpPointInfo` |
| `ci` | Circuit / Constraint | `ciCommonGateIterator`, `ciAPRCascodeIterator` |
| `vdr` | Voltage Domain / 电压域 | `vdrSetNetVoltageRange`, `vdrRunSanityChecker` |
| `db` | Database / 数据库 | `dbIsInstTransparent`, `dbSetInstTransparent` |
| `ge` | Graphics Editor / 图形编辑 | `geToggleDisplayResolution` |
| `tech` | Technology / 技术文件 | `techGetFabricType`, `techSetFabricType` |
| `hi` | Host Interface / GUI | `hiInsertBlankCIWOutputPage` |
| `cst` | Constraints / 约束 | `cstGetFoundryCGName`, `cstGetFoundryConstraintGroup` |
| `ocn` | Ocean / 仿真 | `ocnPrintTMIReliabilityResults` |
| `mg` | Module Generator | `mgFreezeFGR`, `mgUnfreezeFGR` |
| `au` | Analog Utility | `auCdlPrintAdditionalCommentsOnFileHeader` |

---

## 使用方法

在 Virtuoso CIW 中调用 SKILL 函数:

```skill
; 示例: 调用 ADE XL 相关函数
axlSDBDebugPrint(t)

; 示例: 检查会话只读状态
axlIsSessionReadOnly()

; 示例: 电压域检查
vdrRunSanityChecker()
```

---

## 文档查找

1. 首先在本文件中找到函数名
2. 查看对应的文档文件路径
3. 在 `/mnt/data/eda_tool/cadence/ICAD_201/doc/` 目录下找到对应 HTML 文件
4. 使用浏览器或 `grep` 查找锚点位置获取详细文档

"""

# 8. 保存所有文档
with open('./docs/API_MORE_INFO.md', 'w', encoding='utf-8') as f:
    f.write(main_md)
print("主文档已保存: ./docs/API_MORE_INFO.md")

with open('./docs/API_DOC_INDEX.md', 'w', encoding='utf-8') as f:
    f.write(docs_md)
print("文档索引已保存: ./docs/API_DOC_INDEX.md")

with open('./docs/API_QUICK_REF.md', 'w', encoding='utf-8') as f:
    f.write(quick_ref)
print("快速参考卡已保存: ./docs/API_QUICK_REF.md")

# 9. 生成统计信息
stats_md = f"""# API 文档统计报告

## 总体统计

| 项目 | 数量 |
|------|------|
| 总 API 函数数 | {len(api_entries)} |
| 文档文件数 | {len(doc_groups)} |
| API 分类数 | {len(prefix_groups)} |

## 分类统计 (按函数前缀)

| 前缀 | 函数数量 | 占比 |
|------|----------|------|
"""

for prefix in sorted(prefix_groups.keys(), key=lambda x: -len(prefix_groups[x])):
    count = len(prefix_groups[prefix])
    pct = count / len(api_entries) * 100
    stats_md += f"| {prefix} | {count} | {pct:.1f}% |\n"

with open('./docs/API_STATS.md', 'w', encoding='utf-8') as f:
    f.write(stats_md)
print("统计报告已保存: ./docs/API_STATS.md")

print("\n" + "=" * 70)
print("文档生成完成！")
print("=" * 70)
print(f"""
生成的文件:
  1. ./docs/API_MORE_INFO.md      - 主文档 (按类别分组)
  2. ./docs/API_DOC_INDEX.md       - 文档文件索引
  3. ./docs/API_QUICK_REF.md       - 快速参考卡
  4. ./docs/API_STATS.md           - 统计报告
  5. ./docs/api_more_info.tgf      - 原始文件
""")
