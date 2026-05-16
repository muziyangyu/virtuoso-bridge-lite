;==============================================================================
; new_p18.il — SMIC 12nm 1.8V PMOS 参数化单元
;
; 基于 ROD (Relative Object Design) 框架的 PCell 实现。
; 创建完整的 PMOS 版图：AA 有源区、GT 栅极、SP 注入、M1 金属、V0 通孔、Pin。
;
; 参数:
;   w  - 栅宽 (um), 每指宽度
;   l  - 栅长 (um), 栅极长度
;   nf - 指状数 (fingers)
;   m  - 并联倍数 (multiplier)
;
; 安装:
;   load("new_p18_load.il")
;==============================================================================

;------------------------------------------------------------------------------
; newP18Create — 生成 new_p18 版图
;------------------------------------------------------------------------------
procedure(newP18Create(cv @key (w 0.2) (l 0.03) (nf 1) (m 1))
  let((snapGrid halfW halfL totalW inst rect)

    ;--- 工艺常量 (SMIC 12nm FinFET, 单位 um) ---
    snapGrid = 0.001             ; 工艺网格

    ;--- 计算几何参数 ---
    halfW = w / 2.0              ; 半宽
    halfL = l / 2.0              ; 半长
    totalW = w * nf              ; 总宽度 (多指)

    ;--- 删除旧几何 (用于 CDF 回调时的再生) ---
    foreach(shape cv~>shapes dbDeleteObject(shape))
    foreach(inst cv~>instances dbDeleteObject(inst))

    ;--- 1. P+ 注入 (SP) ---
    rect = dbCreateRect(cv list("SP" "drawing")
      list(list(-halfW - 0.05 -1.0) list(totalW + halfW + 0.05 1.0)))

    ;--- 2. N 阱 (NW) ---
    rect = dbCreateRect(cv list("NW" "drawing")
      list(list(-halfW - 0.1 -1.5) list(totalW + halfW + 0.1 1.5)))

    ;--- 3. 有源区 (AA) ---
    rect = dbCreateRect(cv list("AA" "drawing")
      list(list(-halfW - 0.02 -0.5) list(totalW + halfW + 0.02 0.5)))

    ;--- 4. GT 栅极 (多晶硅) ---
    for(i 0 nf - 1
      ; 栅极位置: 从 x=0 开始, 间距 = w
      gateX = i * w
      dbCreateRect(cv list("GT" "drawing")
        list(list(gateX - halfL  -0.6) list(gateX + halfL 0.6)))
    )

    ;--- 5. M1 金属 (S/D 连接) ---
    ; 源极 (Source) — 左侧
    dbCreateRect(cv list("M1" "drawing")
      list(list(-halfW - 0.1 -0.15) list(-0.02 0.15)))

    ; 漏极 (Drain) — 右侧 (单指) 或交替 (多指)
    if(nf == 1 then
      dbCreateRect(cv list("M1" "drawing")
        list(list(0.02 -0.15) list(totalW + halfW + 0.1 0.15)))
    else
      ; 多指: 每对指中间画漏极金属
      for(i 0 nf - 2
        dbCreateRect(cv list("M1" "drawing")
          list(list(i * w + halfL + 0.02 -0.15) list((i + 1) * w - halfL - 0.02 0.15)))
      )
    )

    ;--- 6. Pin 标签 ---
    ; 源极 S (左侧)
    dbCreateLabel(cv list("M1" "pin") list(-halfW - 0.3 0) "S"
      "centerCenter" "R0" "roman" 0.1)

    ; 漏极 D (右侧)
    dbCreateLabel(cv list("M1" "pin") list(totalW + halfW + 0.3 0) "D"
      "centerCenter" "R0" "roman" 0.1)

    ; 栅极 G (上方)
    dbCreateLabel(cv list("M1" "pin") list(totalW / 2 0.8) "G"
      "centerCenter" "R0" "roman" 0.1)

    ; 体极 B (下方)
    dbCreateLabel(cv list("M1" "pin") list(totalW / 2 -0.8) "B"
      "centerCenter" "R0" "roman" 0.1)

    t   ; 返回成功
  )
)

;------------------------------------------------------------------------------
; newP18CB — CDF 回调函数
; 当用户在属性表单中修改参数时自动调用
;------------------------------------------------------------------------------
procedure(newP18CB()
  let((cv inst)
    cv = geGetEditCellView()
    unless(cv return(nil))

    ; 读取 CDF 参数值
    newP18Create(cv
      ?w  cdfGetFloat(cdfgData "w")
      ?l  cdfGetFloat(cdfgData "l")
      ?nf cdfGetInt(cdfgData "nf")
      ?m  cdfGetInt(cdfgData "m")
    )

    dbSave(cv)
  )
)

;------------------------------------------------------------------------------
; newP18Init — CDF formInitProc
; 首次创建实例时自动调用
;------------------------------------------------------------------------------
procedure(newP18Init()
  let((cv)
    cv = geGetEditCellView()
    unless(cv return(nil))

    ; 用默认参数生成初始版图
    newP18Create(cv ?w 0.2 ?l 0.03 ?nf 1 ?m 1)
    dbSave(cv)
  )
)

;==============================================================================
; new_p18 PCell 安装
;==============================================================================
procedure(newP18Install(libName)
  let((cellId cdfId tfId)

    ; 获取或创建 cell
    unless(cellId = ddGetObj(libName "new_p18")
      error("Cannot find cell %s/new_p18" libName)
    )

    ; 删除旧 CDF
    when(cdfId = cdfGetBaseCellCDF(cellId)
      cdfDeleteCDF(cdfId)
    )

    ; 创建新 CDF
    cdfId = cdfCreateBaseCellCDF(cellId)
    tfId = techGetTechFile(cellId)

    ;--- 参数定义 ---
    ; w - 栅宽
    cdfCreateParam(cdfId
      ?name      "w"
      ?prompt    "Gate Width (um)"
      ?type      "string"
      ?defValue  "0.2"
      ?parseAsNumber "yes"
      ?units     "lengthMetric"
      ?callback  "newP18CB()"
    )

    ; l - 栅长
    cdfCreateParam(cdfId
      ?name      "l"
      ?prompt    "Gate Length (um)"
      ?type      "string"
      ?defValue  "0.03"
      ?parseAsNumber "yes"
      ?units     "lengthMetric"
      ?callback  "newP18CB()"
    )

    ; nf - 指状数
    cdfCreateParam(cdfId
      ?name      "nf"
      ?prompt    "Number of Fingers"
      ?type      "int"
      ?defValue  1
      ?callback  "newP18CB()"
    )

    ; m - 并联倍数
    cdfCreateParam(cdfId
      ?name      "m"
      ?prompt    "Multiplier (m)"
      ?type      "int"
      ?defValue  1
    )

    ;--- 仿真信息 ---
    cdfId->simInfo = list(nil)
    cdfId->simInfo->spectreS = '(nil
      netlistProcedure  ansSpectreSDevPrim
      instParameters    (w l m)
      termOrder         (D G S B)
      termMapping       (nil D d G g S s B b)
      namePrefix        "M"
      componentName     pmos
    )
    cdfId->simInfo->auLvs = '(nil
      netlistProcedure  ansLvsCompPrim
      instParameters    (m l w)
      componentName     "p18_ckt"
      termOrder         (D G S B)
      deviceTerminals   "D G S B"
    )

    ;--- CDF 属性 ---
    cdfId->formInitProc  = "newP18Init()"
    cdfId->doneProc      = ""
    cdfSaveCDF(cdfId)

    printf("new_p18 PCell installed in %s\n" libName)
    t
  )
)

printf("new_p18 PCell SKILL code loaded.\n")
printf("  Run: newP18Install(\"work_ai\") to install.\n")
