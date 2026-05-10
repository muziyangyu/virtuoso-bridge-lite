#!/usr/bin/env python3
"""优化 work_ai inv 版图 - ICAD_201 兼容"""

from virtuoso_bridge import VirtuosoClient

client = VirtuosoClient.from_env()

print("=" * 70)
print("work_ai inv 版图优化工具")
print("=" * 70)

# 1. 版图诊断
print("\n[1] 版图诊断")
print("-" * 50)

# 获取当前版图信息
result = client.execute_skill('''
let((cv bbox w h area figs wires labels)
    cv = geGetEditCellView()
    bbox = cv~>bBox
    x1 = car(car(bbox))
    y1 = cadr(car(bbox))
    x2 = car(cadr(bbox))
    y2 = cadr(cadr(bbox))
    w = x2 - x1
    h = y2 - y1
    area = w * h
    
    ; 统计各类图形
    figs = cv~>shapes
    wires = length(foreach(mapcar fig figs when(fig~>layerName == "wire" fig)))
    labels = length(foreach(mapcar fig figs when(fig~>layerName == "pin" fig)))
    
    printf("=== 当前版图状态 ===\\n")
    printf("版图尺寸: %.3f um x %.3f um = %.3f um^2\\n", w, h, area)
    printf("左下角: (%.3f, %.3f)\\n", x1, y1)
    printf("右上角: (%.3f, %.3f)\\n", x2, y2)
    printf("\\n")
    printf("wire 图形: %d 个\\n", wires)
    printf("label 图形: %d 个\\n", labels)
    printf("总图形数: %d 个\\n", length(figs))
    
    list(w h area)
)
''')
print(f"尺寸数据: {result.output}")

# 2. 器件位置分析
print("\n[2] 器件位置分析")
print("-" * 50)
result = client.execute_skill('''
let((cv insts positions)
    cv = geGetEditCellView()
    insts = cv~>instances
    positions = foreach(mapcar inst insts
        list(
            inst~>name
            inst~>master~>name
            car(inst~>transform)   ; 位置
            cadr(car(cdr(inst~>transform)))  ; 旋转
        )
    )
    foreach(pos positions
        printf("%-5s @ %-20s rot=%s\\n", nth(0 pos) nth(2 pos) nth(3 pos))
    )
    positions
)
''')

# 3. 优化建议
print("\n[3] 优化建议")
print("-" * 50)
print("""
建议的优化方向:
1. 版图居中 - 将器件对齐到原点
2. 减小面积 - 优化器件间距
3. 布线优化 - 减少 wire 数量和长度
4. DRC 检查 - 确保间距符合规则
""")

# 4. 执行优化
print("\n[4] 执行优化")
print("-" * 50)

# 优化1: 版图居中
print("优化1: 将版图居中对齐到原点...")
result = client.execute_skill('''
let((cv bbox dx dy)
    cv = geGetEditCellView()
    bbox = cv~>bBox
    x1 = car(car(bbox))
    y1 = cadr(car(bbox))
    x2 = car(cadr(bbox))
    y2 = cadr(cadr(bbox))
    
    ; 计算偏移量 (中心移到原点)
    dx = - (x1 + x2) / 2.0
    dy = - (y1 + y2) / 2.0
    
    printf("原始中心: (%.3f, %.3f)\\n", (x1+x2)/2 (y1+y2)/2)
    printf("偏移量: (%.3f, %.3f)\\n", dx, dy)
    
    ; 移动所有图形
    foreach(fig cv~>shapes
        dbMoveFig(fig list(dx:dy))
    )
    
    ; 移动所有实例
    foreach(inst cv~>instances
        ; 计算新位置
        pos = car(inst~>transform)
        new_pos = list((car(pos) + dx): (cadr(pos) + dy))
        ; 保持旋转和缩放不变
        rest = cdr(inst~>transform)
        inst~>transform = cons(new_pos rest)
    )
    
    printf("版图已居中\\n")
    
    ; 刷新
    win = hiGetCurrentWindow()
    when(win hiRedrawDisplay(win))
    
    list(dx dy)
)
''')
print(f"偏移结果: {result.output}")

# 优化2: 检查并报告新尺寸
print("\n优化后尺寸:")
result = client.execute_skill('''
let((cv bbox w h)
    cv = geGetEditCellView()
    bbox = cv~>bBox
    x1 = car(car(bbox))
    y1 = cadr(car(bbox))
    x2 = car(cadr(bbox))
    y2 = cadr(cadr(bbox))
    w = x2 - x1
    h = y2 - y1
    printf("新边界: (%.3f, %.3f) to (%.3f, %.3f)\\n", x1, y1, x2, y2)
    printf("新尺寸: %.3f um x %.3f um = %.3f um^2\\n", w, h, w*h)
    printf("新中心: (%.3f, %.3f)\\n", (x1+x2)/2, (y1+y2)/2)
    list(w h)
)
''')

# 5. 保存建议
print("\n[5] 保存建议")
print("-" * 50)
print("""
优化完成！建议:
1. 检查 DRC: 在 Virtuoso 中运行 Verify -> DRC
2. 检查 LVS: 确保版图与原理图匹配
3. 保存设计: File -> Save

后续优化方向:
- 优化晶体管宽度匹配
- 改善电源/地布线
- 添加保护环 (Guard Ring)
- 优化引脚位置
""")

print("\n" + "=" * 70)
print("优化完成")
print("=" * 70)
