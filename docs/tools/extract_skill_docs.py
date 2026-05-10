#!/usr/bin/env python3
"""提取 SKILL 函数文档"""

from virtuoso_bridge import SSHClient
import re
import html

tunnel = SSHClient.from_env()
tunnel.warm()

# 常用函数列表
funcs = [
    # 数据库操作 - 库/单元管理
    'ddGetObj',
    'ddGetObjName',
    'ddGetObjCells',
    'ddGetObjCellNames',
    'ddGetObjViews',
    
    # 数据库操作 - CellView 操作
    'dbOpenCellViewByType',
    'dbSave',
    
    # 图形创建
    'dbCreateRect',
    'dbCreatePath',
    'dbCreatePolygon',
    'dbCreateCircle',
    'dbCreateInst',
    'dbCreatePin',
    
    # 图形查询/修改
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
    
    # 版图相关
    'leGetAllLayers',
    'leGetLayerNum',
    'leGetLayerName',
    
    # 其他常用
    'dbGetHierPath',
    'dbFindAnyInstByName',
    'dbGetInstTransform',
]

# 生成 Markdown 文档
md_content = '''# Virtuoso SKILL 常用函数参考

> 文档来源: Cadence ICAD_201 官方文档 (`/mnt/data/eda_tool/cadence/ICAD_201/doc/skdfref/`)
>
> 在线文档: 在 Virtuoso CIW 中运行 `cdsDoc` 或按 F1

---

## 函数分类

### 1. 数据库操作 (dd* - Data Design)
| 函数 | 说明 |
|------|------|
| ddGetObj | 获取数据库对象 |
| ddGetObjName | 获取对象名称 |
| ddGetObjCells | 获取库中的所有单元 |
| ddGetObjCellNames | 获取库中的所有单元名称 |
| ddGetObjViews | 获取单元的所有视图 |

### 2. CellView 操作 (db* - DataBase)
| 函数 | 说明 |
|------|------|
| dbOpenCellViewByType | 按类型打开 CellView |
| dbSave | 保存 CellView |

### 3. 图形创建
| 函数 | 说明 |
|------|------|
| dbCreateRect | 创建矩形 |
| dbCreatePath | 创建路径 |
| dbCreatePolygon | 创建多边形 |
| dbCreateCircle | 创建圆 |
| dbCreateInst | 创建实例 |
| dbCreatePin | 创建引脚 |

### 4. 图形查询/修改
| 函数 | 说明 |
|------|------|
| dbCopyFig | 复制图形 |
| dbMoveFig | 移动图形 |
| dbDeleteFig | 删除图形 |
| dbGetOverlaps | 获取重叠图形 |
| dbGetTrueOverlaps | 获取真实重叠图形（含层次） |

### 5. 图形编辑器 (ge* - Graphics Editor)
| 函数 | 说明 |
|------|------|
| geGetEditCellView | 获取当前编辑的 CellView |
| geGetCellView | 获取指定窗口的 CellView |
| geGetSelectedSet | 获取选中的图形集合 |
| geSelectFig | 选中图形 |
| geDeselectFig | 取消选中图形 |

### 6. 版图层操作 (le* - Layout Editor)
| 函数 | 说明 |
|------|------|
| leGetAllLayers | 获取所有层 |
| leGetLayerNum | 获取层号 |
| leGetLayerName | 获取层名 |

---

## 详细函数文档

'''

for func in funcs:
    # 搜索函数定义
    result = tunnel.run_command(f'grep -A 50 "<a name=\"{func}\">" /mnt/data/eda_tool/cadence/ICAD_201/doc/skdfref/*.html | head -70')
    
    if result.stdout.strip():
        md_content += f'\n### {func}\n\n```text\n'
        
        lines = result.stdout.split('\n')
        for line in lines[:50]:
            # 去掉 HTML 标签
            clean = re.sub(r'<[^>]+>', '', line)
            # 取消 HTML 实体编码
            clean = html.unescape(clean)
            
            # 去掉前缀的文件名
            if ':' in clean and '.html' in clean[:50]:
                clean = clean.split(':', 1)[1]
            
            if clean.strip() and not clean.strip().startswith('[TOPIC_'):
                md_content += clean + '\n'
        
        md_content += '```\n\n'
    else:
        # 尝试其他搜索方式
        result = tunnel.run_command(f'grep -B 5 -A 30 "{func}(" /mnt/data/eda_tool/cadence/ICAD_201/doc/skdfref/*.html | head -50')
        if result.stdout.strip():
            md_content += f'\n### {func}\n\n```text\n'
            
            lines = result.stdout.split('\n')
            for line in lines[:40]:
                clean = re.sub(r'<[^>]+>', '', line)
                clean = html.unescape(clean)
                if ':' in clean and '.html' in clean[:50]:
                    clean = clean.split(':', 1)[1]
                if clean.strip() and not clean.strip().startswith('[TOPIC_'):
                    md_content += clean + '\n'
            
            md_content += '```\n\n'
        else:
            md_content += f'\n### {func}\n\n*(文档暂缺)*\n\n'

# 保存文档
with open('SKILL_FUNCTIONS_REFERENCE.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print('文档已生成: SKILL_FUNCTIONS_REFERENCE.md')
