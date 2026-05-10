/* Create inverter layout for work_ai/inv
 * SMIC 12nm standard cell style
 */

procedure( create_inv_layout(lib_name cell_name)
  let((cv tech_lib lpp_nw lpp_aa lpp_gt lpp_ct lpp_m1 lpp_pr
        cell_height cell_width pmos_width nmos_width
        pmos_l nmos_l rail_height vdd_y1 vdd_y2 vss_y1 vss_y2)

    printf("Creating layout for %s/%s...\n" lib_name cell_name)

    ; Get technology layers
    tech_lib = car(ddGetLibList())
    lpp_nw = list("NW" "drawing")
    lpp_aa = list("AA" "drawing")
    lpp_gt = list("GT" "drawing")
    lpp_ct = list("CT" "drawing")
    lpp_m1 = list("M1" "drawing")
    lpp_v1 = list("V1" "drawing")
    lpp_m2 = list("M2" "drawing")
    lpp_pr = list("PR" "drawing")

    ; Standard cell dimensions (nanometers)
    cell_height = 270    ; Standard cell height: 270nm
    cell_width = 1000    ; Cell width: 1um
    pmos_width = 200     ; PMOS width
    nmos_width = 100     ; NMOS width (ratio 2:1 for rise/fall balance)
    pmos_l = 30          ; PMOS length
    nmos_l = 30          ; NMOS length
    rail_height = 40     ; Power rail height

    ; Calculate positions
    vdd_y1 = cell_height - rail_height
    vdd_y2 = cell_height
    vss_y1 = 0
    vss_y2 = rail_height

    ; Open or create cellview
    cv = dbOpenCellViewByType(lib_name cell_name "layout" "a")
    when(!cv
      error("Cannot open layout view for %s/%s" lib_name cell_name)
    )

    ; Clear existing shapes
    foreach(obj cv~>shapes
      dbDeleteObject(obj)
    )
    foreach(obj cv~>instances
      dbDeleteObject(obj)
    )
    foreach(obj cv~>vias
      dbDeleteObject(obj)
    )

    printf("Layout view opened: %L\n" cv)

    ; 1. N-well for PMOS (top half of cell)
    dbCreateRect(cv lpp_nw list(0:cell_height/2 cell_width:cell_height))

    ; 2. PMOS transistor (top region)
    ; Active area for PMOS
    dbCreateRect(cv lpp_aa list(100:150 300:210))
    ; Gate for PMOS
    dbCreateRect(cv lpp_gt list(200:140 230:220))

    ; 3. NMOS transistor (bottom region)
    ; Active area for NMOS
    dbCreateRect(cv lpp_aa list(100:60 200:120))
    ; Gate for NMOS (connects to PMOS gate = input)
    dbCreateRect(cv lpp_gt list(200:50 230:130))

    ; 4. Power rails (M1)
    ; VDD rail (top)
    dbCreateRect(cv lpp_m1 list(0:vdd_y1 cell_width:vdd_y2))
    ; VSS rail (bottom)
    dbCreateRect(cv lpp_m1 list(0:vss_y1 cell_width:vss_y2))

    ; 5. Input gate connection (poly strap)
    dbCreateRect(cv lpp_m1 list(200:125 230:145))

    ; 6. Create pins
    ; VDD pin
    dbCreatePin(cv "VDD" list(list(list(0:vdd_y1 cell_width:vdd_y2) "M1")) "inputOutput")
    ; VSS pin
    dbCreatePin(cv "VSS" list(list(list(0:vss_y1 cell_width:vss_y2) "M1")) "inputOutput")
    ; VIN pin (input)
    dbCreatePin(cv "VIN" list(list(list(450:100 500:150) "M1")) "input")
    ; VOUT pin (output)
    dbCreatePin(cv "VOUT" list(list(list(600:100 650:150) "M1")) "output")

    printf("Inverter layout created successfully!\n")
    printf("Cell size: %.1fnm x %.1fnm\n" cell_width cell_height)

    ; Save and close
    dbSave(cv)
    dbCheck(cv)
    dbClose(cv)

    t
  )
)

; Execute
create_inv_layout("work_ai" "inv")
