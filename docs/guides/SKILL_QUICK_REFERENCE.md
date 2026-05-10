# SKILL 快速参考手册

> 通过 virtuoso-bridge 调用 SKILL 的实用指南

---

## ⚠️ 原理图丢失杀手级 BUG 置顶警告

**这是能让你一下午白干的最严重错误！**

### 🔴 致命: `edit()` 内部嵌套 `dbOpenCellViewByType`

| 错误 | 正确 |
|------|------|
| 在 `with client.schematic.edit()` 内部 AGAIN 用 `dbOpenCellViewByType` 打开同一个 cellview | 参数修改用 `client.execute_operations()` 单独执行，不要在 edit() 内部嵌套打开 |

**后果：双重打开→数据库竞态→原理图全部清空！**

```python
# ❌ 致命错误 - 这样会让你一下午白干！
with client.schematic.edit(LIB, CELL) as sch:
    # 🔴 嵌套打开同一个 cellview！两次编辑会话冲突！
    sch.add('let((cv i) cv = dbOpenCellViewByType("work_ai" "opamp_two_stage" "schematic" "schematic" "a") i = car(setof(...)) dbReplaceProp(i "nfin" "float" 23))')

# ✅ 正确方法 1: 参数修改单独执行（推荐，最简单安全）
skill_code = '''
let((cv inst)
  cv = dbOpenCellViewByType("work_ai" "opamp_two_stage" "schematic" "schematic" "a")
  inst = car(setof(x cv~>instances x~>name == "M7"))
  when(inst
    dbReplaceProp(inst "nfin" "float" 23)
    dbSave(cv)    ; 显式保存
  )
  dbClose(cv)     ; 显式关闭
)
'''
client.execute_operations([skill_code])

# ✅ 正确方法 2: 用 edit() + add() 但不要再次打开！
with client.schematic.edit(LIB, CELL) as sch:
    # 用上下文管理器已经准备好的 cv 变量，不要再次 dbOpen！
    sch.add('let((inst) inst = car(setof(x cv~>instances x~>name == "M7")) when(inst dbReplaceProp(inst "nfin" "float" 23)))')
```

**四大必死特征：**
1. `edit()` 上下文 + 内部 `dbOpenCellViewByType` = 双重打开
2. 绕过 bridge 的编辑保护，穿墙修改数据库
3. `car(setof())` 找不到器件时的空指针放大效应
4. 引用计数混乱触发 fail-safe 清空机制

---

## ❌ 常见错误函数调用 & 正确写法

这是我们实际踩过的坑，请务必对照检查！

### 1. **错误: `dbGetPropValue` - 不存在的函数**
```skill
; ❌ 错误: 这个函数根本不存在！
l_val = dbGetPropValue(inst "l")   ; *Error* eval: undefined function - dbGetPropValue

; ✅ 正确: 用波浪线 ~ 直接访问对象属性
l_val = inst~>l
nfin_val = inst~>nfin
w_val = inst~>w
```

### 2. **错误: `client.skill.eval()` - API 不存在**
```python
# ❌ 错误: VirtuosoClient 没有 skill.eval 方法！
result = client.skill.eval(skill_code)  # AttributeError

# ✅ 正确: 用 execute_operations()
result = client.execute_operations([skill_code])
```

### 3. **错误: `sch._run_skill()` - 私有方法不要用**
```python
# ❌ 错误: SchematicEditor 没有这个方法！
with client.schematic.edit(LIB, CELL) as sch:
    result = sch._run_skill(skill_code)  # AttributeError

# ✅ 正确: 直接用 client.execute_operations() 或 sch.add()
# 只读查询: 直接 client.execute_operations()
# 编辑操作: sch.add(skill_command)
```

### 4. **错误: `procedure` 嵌套在 `let` 里面**
```skill
; ❌ 错误: procedure 不能嵌套定义！
let((cv)
  procedure(foo() ...)  ; 语法错误！SKILL 不支持嵌套函数
)

; ✅ 正确: procedure 在顶层定义，let 里只放执行逻辑
procedure(foo() ...)

let((cv)
  foo()
)
```

### 5. **错误: MOSFET Terminal 名称大小写错误**
```skill
; ❌ 错误: 小写 g/d/s/b 不存在！
schAddInstTerm(inst "g" "VINP")  ; Terminal 'g' not found

; ✅ 正确: 必须是大写 G/D/S/B
schAddInstTerm(inst "G" "VINP")   ; Gate
schAddInstTerm(inst "D" "net")    ; Drain
schAddInstTerm(inst "S" "VSS")    ; Source
schAddInstTerm(inst "B" "VSS")    ; Bulk
```

### 6. **错误: 设置实例参数用 `cdfSetParam`**
```skill
; ❌ 错误: cdfSetParam 是 CDF 参数编辑，不是实例属性
cdfSetParam(inst "l" 300e-9)  ; 可能不生效

; ✅ 正确: 用 dbReplaceProp 设置实例属性
dbReplaceProp(inst "l" "float" 300e-9)
dbReplaceProp(inst "nfin" "float" 48)
```

### 7. **错误: `dbOpenCellViewByType` 只传 4 个参数**
```skill
; ❌ 错误: 少了 view type 参数！
cv = dbOpenCellViewByType("work_ai" "inv" "schematic" "w")  ; 返回 nil

; ✅ 正确: 必须传 5 个参数！
cv = dbOpenCellViewByType("work_ai" "inv" "schematic" "schematic" "w")
;                              lib      cell   view       view_type    mode
```

---

## 📌 核心原则

### 1. **`dbOpenCellViewByType` 需要 5 个参数！**
```skill
; ✅ 正确：5个参数
cv = dbOpenCellViewByType("work_ai" "inv" "layout" "maskLayout" "a")  ; 编辑模式
cv = dbOpenCellViewByType("work_ai" "inv" "layout" "maskLayout" "r")  ; 只读模式

; ❌ 错误：只给4个参数 (之前一直犯的错)
cv = dbOpenCellViewByType("work_ai" "inv" "layout" "a")  ; 返回 nil！
```

| 参数 | 说明 |
|------|------|
| 1 | library name |
| 2 | cell name |
| 3 | view name |
| 4 | **view type** (schematic/maskLayout/...) |
| 5 | mode ("a"=append/edit, "r"=read) |

### 2. **永远不要用 `printf` 调试**
`execute_skill()` 只返回表达式的**最终返回值**，不捕获标准输出。

### 3. **判断空值的正确方式**
```python
result = client.execute_skill('dbOpenCellViewByType("work_ai" "inv" "schematic" "maskLayout" "r")')
if 'nil' not in str(result.output) and result.output:
    print("✅ 存在")
else:
    print("❌ 不存在")
```

---

## 📋 Schematic 原理图绘制指南 (两级运放实战总结)

### ⚠️ 核心注意事项：Terminal 名称！

**这是最容易踩的坑！不同器件的 terminal 名称完全不同！**

| 器件类型 | Terminal 名称 | 说明 |
|----------|--------------|------|
| **MOSFET** (n18_ckt/p18_ckt) | **G, D, S, B** | Gate, Drain, Source, Bulk |
| **电容** (analogLib/cap) | **PLUS, MINUS** | 正负极 |
| **电阻** (analogLib/res) | **PLUS, MINUS** | 两端 |

❌ **错误示范**：用 PLUS/MINUS 连接 MOSFET 端口
```python
# ❌ 错误！MOSFET 没有 PLUS/MINUS terminal！
sch.add(schematic_label_instance_term("M1", "PLUS", "VINP"))  # 报错！

# ✅ 正确！MOSFET terminal 是 G/D/S/B
sch.add(schematic_label_instance_term("M1", "G", "VINP"))   # Gate
sch.add(schematic_label_instance_term("M1", "D", "net_d3")) # Drain
sch.add(schematic_label_instance_term("M1", "S", "net_s"))  # Source
sch.add(schematic_label_instance_term("M1", "B", "VSS"))    # Bulk
```

---

### 📝 两级运算放大器完整连接模板

#### 1. 器件放置
```python
from virtuoso_bridge.virtuoso.schematic import (
    schematic_create_inst_by_master_name as inst,
    schematic_create_pin,
    schematic_label_instance_term,
)

# 差分输入对 (NMOS)
sch.add(inst("smic12sf", "n18_ckt", "symbol", "M1", -4.0,  1.0, "R0"))
sch.add(inst("smic12sf", "n18_ckt", "symbol", "M2", -4.0,  0.0, "R0"))

# 电流镜负载 (PMOS)
sch.add(inst("smic12sf", "p18_ckt", "symbol", "M3", -2.0,  1.0, "MY"))
sch.add(inst("smic12sf", "p18_ckt", "symbol", "M4", -2.0,  0.0, "MY"))

# 尾电流源 (NMOS)
sch.add(inst("smic12sf", "n18_ckt", "symbol", "M5", -4.0, -1.0, "R0"))

# 第二级放大管 (NMOS)
sch.add(inst("smic12sf", "n18_ckt", "symbol", "M6",  0.0,  0.5, "R0"))

# 第二级有源负载 (PMOS)
sch.add(inst("smic12sf", "p18_ckt", "symbol", "M7",  0.0,  1.5, "MY"))

# 偏置电路 (PMOS 电流镜)
sch.add(inst("smic12sf", "p18_ckt", "symbol", "M8", -6.0,  1.0, "MY"))
sch.add(inst("smic12sf", "p18_ckt", "symbol", "M9", -6.0,  0.0, "MY"))

# 偏置 NMOS 二极管
sch.add(inst("smic12sf", "n18_ckt", "symbol", "M10", -6.0, -1.0, "R0"))

# Miller 补偿电容
sch.add(inst("analogLib", "cap", "symbol", "Cc",  2.0,  1.0, "R0"))
```

#### 2. 电源连接 (含 Bulk!)
```python
# ========== VDD ==========
# PMOS Source -> VDD
sch.add(schematic_label_instance_term("M3", "S", "VDD"))
sch.add(schematic_label_instance_term("M4", "S", "VDD"))
sch.add(schematic_label_instance_term("M7", "S", "VDD"))
sch.add(schematic_label_instance_term("M8", "S", "VDD"))
sch.add(schematic_label_instance_term("M9", "S", "VDD"))

# PMOS Bulk (B) -> VDD 【重要！不要忘记！】
sch.add(schematic_label_instance_term("M3", "B", "VDD"))
sch.add(schematic_label_instance_term("M4", "B", "VDD"))
sch.add(schematic_label_instance_term("M7", "B", "VDD"))
sch.add(schematic_label_instance_term("M8", "B", "VDD"))
sch.add(schematic_label_instance_term("M9", "B", "VDD"))

# ========== VSS ==========
# NMOS Source -> VSS
sch.add(schematic_label_instance_term("M5", "S", "VSS"))
sch.add(schematic_label_instance_term("M6", "S", "VSS"))
sch.add(schematic_label_instance_term("M10", "S", "VSS"))

# NMOS Bulk (B) -> VSS 【重要！不要忘记！】
sch.add(schematic_label_instance_term("M1", "B", "VSS"))
sch.add(schematic_label_instance_term("M2", "B", "VSS"))
sch.add(schematic_label_instance_term("M5", "B", "VSS"))
sch.add(schematic_label_instance_term("M6", "B", "VSS"))
sch.add(schematic_label_instance_term("M10", "B", "VSS"))
```

#### 3. 信号连接
```python
# 差分输入
sch.add(schematic_label_instance_term("M1", "G", "VINP"))
sch.add(schematic_label_instance_term("M2", "G", "VINN"))

# M1/M2 Source 连接到 M5 Drain
sch.add(schematic_label_instance_term("M1", "S", "net_s"))
sch.add(schematic_label_instance_term("M2", "S", "net_s"))
sch.add(schematic_label_instance_term("M5", "D", "net_s"))

# M3 Drain-Gate 二极管连接
sch.add(schematic_label_instance_term("M3", "D", "net_d3"))
sch.add(schematic_label_instance_term("M3", "G", "net_d3"))

# M3 Gate 连接到 M4 Gate (电流镜)
sch.add(schematic_label_instance_term("M4", "G", "net_d3"))

# M1 Drain 到 M3 Drain
sch.add(schematic_label_instance_term("M1", "D", "net_d3"))

# M2 Drain 到 M4 Drain (Node X)
sch.add(schematic_label_instance_term("M2", "D", "net_x"))
sch.add(schematic_label_instance_term("M4", "D", "net_x"))

# Node X 到 M6 Gate (第二级输入)
sch.add(schematic_label_instance_term("M6", "G", "net_x"))

# 第二级输出：M6 Drain 到 M7 Drain
sch.add(schematic_label_instance_term("M6", "D", "VOUT"))
sch.add(schematic_label_instance_term("M7", "D", "VOUT"))

# M7 Gate 连接到偏置 【⚠️ 最容易忘记！不要 floating！】
sch.add(schematic_label_instance_term("M7", "G", "net_bias"))

# Miller 补偿电容
sch.add(schematic_label_instance_term("Cc", "PLUS", "net_x"))
sch.add(schematic_label_instance_term("Cc", "MINUS", "VOUT"))
```

#### 4. 偏置电路连接
```python
# M8 D-G 二极管连接 (偏置参考)
sch.add(schematic_label_instance_term("M8", "D", "net_bias"))
sch.add(schematic_label_instance_term("M8", "G", "net_bias"))

# M8 G 连接到 M9 G (电流镜)
sch.add(schematic_label_instance_term("M9", "G", "net_bias"))

# M8 D 连接到 M10 D
sch.add(schematic_label_instance_term("M10", "D", "net_bias"))

# M10 G-D 二极管连接
sch.add(schematic_label_instance_term("M10", "G", "net_bias"))

# M9 D 连接到 M5 G (尾电流偏置输出)
sch.add(schematic_label_instance_term("M9", "D", "net_vb"))
sch.add(schematic_label_instance_term("M5", "G", "net_vb"))
```

#### 5. 创建 Pins
```python
sch.add(schematic_create_pin("VINP", -5.0,  1.0, "R0", direction="input"))
sch.add(schematic_create_pin("VINN", -5.0,  0.0, "R0", direction="input"))
sch.add(schematic_create_pin("VOUT",  3.0,  1.0, "R0", direction="output"))
sch.add(schematic_create_pin("VDD",  -6.0,  2.5, "R0", direction="inputOutput"))
sch.add(schematic_create_pin("VSS",  -6.0, -2.0, "R0", direction="inputOutput"))
```

---

### 🚨 原理图绘制常见坑 & 解决方案

#### ❌ 问题 1: MOSFET Terminal 用 PLUS/MINUS
```
RuntimeError: schematic edit failed: ("load" 0 t nil ("*Error* load: error while loading file - ..."))
```
**原因**：MOSFET 的 terminal 不是 PLUS/MINUS，而是 **G, D, S, B**
**解决**：
```python
# ❌ 错误
sch.add(label_term("M1", "PLUS", "VINP"))

# ✅ 正确
sch.add(label_term("M1", "G", "VINP"))  # Gate
sch.add(label_term("M1", "D", "net"))   # Drain
sch.add(label_term("M1", "S", "VSS"))   # Source
sch.add(label_term("M1", "B", "VSS"))   # Bulk
```

---

#### ❌ 问题 2: 忘记连接 Bulk (B) 端口
```
*Warning* Terminal 'B' of instance 'M1' is floating
```
**原因**：衬底没有连接到电源/地
**解决**：
```python
# NMOS Bulk -> VSS
sch.add(label_term("M1", "B", "VSS"))
sch.add(label_term("M2", "B", "VSS"))

# PMOS Bulk -> VDD
sch.add(label_term("M3", "B", "VDD"))
sch.add(label_term("M4", "B", "VDD"))
```

---

#### ❌ 问题 3: 有源负载 Gate floating (M7 Gate)
```
*Warning* Terminal 'G' of instance 'M7' is floating
```
**原因**：M7 是第二级 PMOS 有源负载，Gate 必须连接到偏置网络
**解决**：
```python
# M7 Gate 连接到偏置网络 net_bias
sch.add(label_term("M7", "G", "net_bias"))
```

---

#### ❌ 问题 4: 电容 Terminal 用 G/D/S
**原因**：电容的 terminal 是 PLUS/MINUS，不是 G/D/S
**解决**：
```python
# ✅ 正确：电容用 PLUS/MINUS
sch.add(label_term("Cc", "PLUS", "net_x"))
sch.add(label_term("Cc", "MINUS", "VOUT"))
```

---

#### ❌ 问题 5: 坐标格式错误
```python
# ❌ 错误
dbCreateInst(cv master "M1" list(-4:1.5) "R0" 1)  # list 里不能用冒号！

# ✅ 正确
dbCreateInst(cv master "M1" list(-4 1.5) "R0" 1)  # 空格分隔
```

---

### ✅ 原理图连接检查清单

创建完成后，检查以下项目：

- [ ] **所有 MOSFET 的 4 个端口都连接了 (G, D, S, B)**
- [ ] **NMOS 的 B 端口全部连接到 VSS**
- [ ] **PMOS 的 B 端口全部连接到 VDD**
- [ ] **电流镜的 Gate 都正确连接 (M3 G=M4 G, M8 G=M9 G)**
- [ ] **M7 的 Gate 没有 floating (连接到 net_bias)**
- [ ] **Miller 电容两端正确连接**
- [ ] **5 个 Pins 都创建了 (VINP, VINN, VOUT, VDD, VSS)**
- [ ] **没有任何 floating terminal 警告**

---

### 🔌 连线函数对比

| 函数 | 作用 | 特点 |
|------|------|------|
| `schematic_label_instance_term` | 在 terminal 放带标签的连线 stub | ✅ **推荐！自动实现电气连接，有标签可见** |
| `schematic_create_wire_between_instance_terms` | 在两个 terminal 之间画物理连线 | 只有视觉效果，需要另外设置网络名 |
| `schematic_create_wire` | 通过坐标画任意折线 | 适合电源轨等长连线 |

**最佳实践**：优先用 `schematic_label_instance_term` 实现电气连接，网络名相同就会自动连通！

---

## 📂 Layout 完整绘制流程 (反相器示例)

### Step 1: 器件放置
```skill
cv = dbOpenCellViewByType("work_ai" "inv" "layout" "maskLayout" "w")

; NMOS (n18_ckt) - MX orientation (mirrored X, source at bottom)
dbCreateParamInstByMasterName(cv "smic12sf" "n18_ckt" "layout" "NM0" list(1.203 0.384) "MX")

; PMOS (p18_ckt) - R0 orientation (source at top)
dbCreateParamInstByMasterName(cv "smic12sf" "p18_ckt" "layout" "PM0" list(1.203 1.008) "R0")
```

### Step 2: 设置 Pcell 参数
```skill
nm = dbFindAnyInstByName(cv "NM0")
pm = dbFindAnyInstByName(cv "PM0")

; 匹配 schematic: nfin=4, l=134n, fingers=1
cdfSetParam(nm "nfin" 4)
cdfSetParam(nm "l" 0.134)
cdfSetParam(nm "fingers" 1)

cdfSetParam(pm "nfin" 4)
cdfSetParam(pm "l" 0.134)
cdfSetParam(pm "fingers" 1)
```

### Step 3: M0 垂直访问条 (器件终端到电源轨)
```skill
; NMOS source → VSS rail
dbCreatePath(cv list("M0" "drawing") list(list(1.144 0.017) list(1.144 0.265)) 0.054)

; PMOS source → VDD rail
dbCreatePath(cv list("M0" "drawing") list(list(1.144 1.15) list(1.144 1.594)) 0.054)
```

### Step 4: M1 水平电源轨 + Gate 连接
```skill
; VSS rail (bottom, full width)
dbCreatePath(cv list("M1" "drawing") list(list(0.5 0.017) list(2.04 0.017)) 0.032)

; VDD rail (top, full width)
dbCreatePath(cv list("M1" "drawing") list(list(0.5 1.594) list(2.04 1.594)) 0.