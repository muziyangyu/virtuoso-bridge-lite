#!/usr/bin/env python3
"""检查 SKILL 函数在 ICAD_201 文档中是否存在"""

from virtuoso_bridge import SSHClient
import re

tunnel = SSHClient.from_env()
tunnel.warm()

# 我们使用的核心函数列表
core_functions = [
    # 数据库对象操作
    'ddGetObj',
    'ddGetObjName', 
    'ddGetObjCells',
    'ddGetObjViews',
    'ddGetObjList',
    'ddObjP',
    
    # CellView 操作
    'dbOpenCellViewByType',
    'dbSave',
    
    # 图形创建
    'dbCreateRect',
    'dbCreatePath',
    'dbCreatePolygon',
    'dbCreateCircle',
    'dbCreateInst',
    'dbCreatePin',
    
    # 图形操作
    'dbCopyFig',
    'dbMoveFig', 
    'dbDeleteFig',
    'dbGetOverlaps',
    'dbGetTrueOverlaps',
    
    # 图形编辑器
    'geGetEditCellView',
    'geGetCellView',
    'geGetSelectedSet',
    'geSelectFig',
    'geDeselectFig',
    
    # 版图层
    'leGetAllLayers',
    'leGetLayerNum',
    'leGetLayerName',
    
    # 其他常用
    'dbGetHierPath',
    'dbFindAnyInstByName',
    'dbGetInstTransform',
    
    # 窗口/显示
    'hiGetCurrentWindow',
    'hiRedrawDisplay',
    
    # 工具函数
    'printf',
    'getShellEnvVar',
    'getWorkingDir',
    'type',
    'length',
    'car',
    'cadr',
    'mapcar',
    'foreach',
    'sort',
    'strstr',
    'makeTable',
    'getKeys',
    'errset',
    'traceback',
]

doc_path = "/mnt/data/eda_tool/cadence/ICAD_201/doc/skdfref"

print("=" * 80)
print("检查 SKILL 函数在 ICAD_201 文档中的存在性")
print("=" * 80)
print(f"文档路径: {doc_path}")
print(f"检查函数数量: {len(core_functions)}")
print()

# 结果统计
found = []
not_found = []
alternative_names = {}

# 1. 首先检查 HTML 文件中是否有函数定义
print("[1] 检查 HTML 文件中的函数定义...")
for func in core_functions:
    # 搜索函数锚点 <a name="functionName">
    result = tunnel.run_command(f'grep -l "<a name=\"{func}\">" {doc_path}/*.html 2>/dev/null | head -1')
    html_file = result.stdout.strip()
    
    if html_file:
        found.append((func, html_file.split('/')[-1]))
    else:
        # 搜索函数调用 pattern
        result = tunnel.run_command(f'grep -l "{func}(" {doc_path}/*.html 2>/dev/null | head -1')
        html_file = result.stdout.strip()
        if html_file:
            found.append((func, html_file.split('/')[-1] + ' (usage)'))
        else:
            # 搜索函数名出现
            result = tunnel.run_command(f'grep -l "\\b{func}\\b" {doc_path}/*.html 2>/dev/null | head -1')
            html_file = result.stdout.strip()
            if html_file:
                found.append((func, html_file.split('/')[-1] + ' (ref)'))
            else:
                not_found.append(func)

print()
print("=" * 80)
print(f"找到的函数 ({len(found)} 个):")
print("=" * 80)
for func, src in sorted(found):
    print(f"  ✓ {func:<30} @ {src}")

print()
print("=" * 80)
print(f"未找到的函数 ({len(not_found)} 个):")
print("=" * 80)
for func in sorted(not_found):
    print(f"  ✗ {func}")

# 2. 检查未找到函数的可能替代名称
print()
print("=" * 80)
print("未找到函数的进一步检查:")
print("=" * 80)

for func in not_found:
    # 搜索类似名称
    if func.startswith('dd'):
        result = tunnel.run_command(f'grep -o "dd[A-Z][a-zA-Z]*" {doc_path}/*.html | sort -u | grep -i "{func[2:4]}" | head -5')
    elif func.startswith('db'):
        result = tunnel.run_command(f'grep -o "db[A-Z][a-zA-Z]*" {doc_path}/*.html | sort -u | grep -i "{func[2:5]}" | head -5')
    elif func.startswith('ge'):
        result = tunnel.run_command(f'grep -o "ge[A-Z][a-zA-Z]*" {doc_path}/*.html | sort -u | grep -i "{func[2:4]}" | head -5')
    elif func.startswith('le'):
        result = tunnel.run_command(f'grep -o "le[A-Z][a-zA-Z]*" {doc_path}/*.html | sort -u | grep -i "{func[2:4]}" | head -5')
    elif func.startswith('hi'):
        result = tunnel.run_command(f'grep -o "hi[A-Z][a-zA-Z]*" {doc_path}/*.html | sort -u | grep -i "{func[2:4]}" | head -5')
    else:
        result = tunnel.run_command(f'grep -o "\\b[a-z][A-Z][a-zA-Z]*{func[1:3]}" {doc_path}/*.html | sort -u | head -5')
    
    similar = result.stdout.strip()
    if similar:
        print(f"\n{func} 的可能替代:")
        for line in similar.split('\n'):
            if line.strip():
                print(f"  - {line.strip()}")

# 3. 在 Virtuoso 中实际测试函数是否存在
print()
print("=" * 80)
print("在 Virtuoso 中实际测试函数可用性:")
print("=" * 80)

from virtuoso_bridge import VirtuosoClient
client = VirtuosoClient.from_env()

testable_funcs = [f for f in core_functions if not any(f.startswith(x) for x in ['printf', 'type', 'length', 'car', 'cadr', 'foreach', 'sort', 'strstr'])]

for func in testable_funcs[:20]:  # 只测试前20个核心函数
    # 测试函数是否存在 (检查 procedurep)
    result = client.execute_skill(f'procedurep({func})')
    if result.output and result.output != 'nil':
        status = "✓ 可用"
    else:
        # 进一步测试: 尝试获取帮助
        result = client.execute_skill(f'document("{func}")')
        if result.output and len(result.output) > 10:
            status = "✓ 有文档"
        else:
            status = "? 不确定"
    print(f"  {func:<30} {status}")

# 4. 保存测试报告
report = f"""# SKILL 函数可用性测试报告 - ICAD_201

测试时间: 2026-04-28
文档路径: {doc_path}

## 函数可用性统计

- 总数: {len(core_functions)}
- 文档中找到: {len(found)}
- 文档中未找到: {len(not_found)}

## 文档中存在的函数

| 函数 | 来源文件 |
|------|----------|
"""

for func, src in sorted(found):
    report += f"| {func} | {src} |\n"

report += """
## 文档中未找到的函数（需测试）

"""

for func in sorted(not_found):
    report += f"- {func}\n"

report += """
## 重要说明

1. **文档中未找到 ≠ 函数不存在**: 有些基础函数可能在其他文档目录中
2. **函数名大小写**: SKILL 函数名通常区分大小写
3. **版本差异**: ICAD_201 与新版 Virtuoso 的函数可能有差异

## 推荐使用的文档目录

- skdfref/ - 数据库和版图函数
- sklangref/ - SKILL 语言核心函数
- oceanref/ - Ocean 仿真函数
"""

with open('SKILL_FUNCTION_AVAILABILITY.md', 'w', encoding='utf-8') as f:
    f.write(report)

print()
print("报告已保存: SKILL_FUNCTION_AVAILABILITY.md")
