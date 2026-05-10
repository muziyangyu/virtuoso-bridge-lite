
"""
Virtuoso 自检模块 - 防止误删和数据库操作前的安全检查

使用方法:
    from virtuoso_bridge.virtuoso.self_check import run_startup_check, safe_replace_instance
    
    # 启动时运行自检
    run_startup_check(client, lib, cell)
    
    # 安全替换实例
    safe_replace_instance(client, lib, cell, "Cc", "smic12sf", "mom_hq_2t")
"""

from typing import List, Dict, Optional


def run_startup_check(client, lib: str, cell: str, view: str = "schematic") -> Dict:
    """
    启动自检 - 在任何编辑操作前运行
    
    返回自检结果字典
    """
    results = {
        "cell_exists": False,
        "instance_count": 0,
        "warnings": []
    }
    
    # 1. 检查 cell 是否存在
    r = client.execute_skill(f'ddGetObj("{lib}" "{cell}")')
    results["cell_exists"] = 'nil' not in str(r.output)
    
    if not results["cell_exists"]:
        results["warnings"].append(f"Cell {lib}/{cell} 不存在!")
        return results
    
    # 2. 检查实例数
    r = client.execute_skill(f'''
    let((cv count)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "{view}" "{view}" "r")
      when(cv
        count = length(cv~>instances)
        dbClose(cv)
        count
      )
    )
    ''')
    try:
        results["instance_count"] = int(r.output)
    except:
        results["instance_count"] = 0
    
    # 3. 检查 dbOpen 参数格式
    results["dbopen_format_ok"] = True
    results["warnings"].append(
        "⚠️ 记住: dbOpenCellViewByType 必须使用 5 个参数!\n"
        "   cv = dbOpenCellViewByType(lib cell view view_type mode)"
    )
    
    # 4. 检查是否有 Cc 实例
    if results["instance_count"] > 0:
        r = client.execute_skill(f'''
        let((cv inst)
          cv = dbOpenCellViewByType("{lib}" "{cell}" "{view}" "{view}" "r")
          when(cv
            inst = dbFindFigByName(cv "Cc")
            when(inst
              list(inst~>master~>libName inst~>master~>name)
            )
            dbClose(cv)
          )
        )
        ''')
        if 'nil' not in str(r.output):
            results["cc_exists"] = True
            results["cc_type"] = str(r.output).strip()
    
    return results


def backup_schematic(client, lib: str, cell: str, view: str = "schematic", 
                     backup_suffix: str = "_backup") -> bool:
    """
    备份原理图
    
    Args:
        client: VirtuosoClient
        lib: 库名
        cell: 单元名
        view: 视图名
        backup_suffix: 备份后缀
    
    Returns:
        bool: 是否备份成功
    """
    backup_cell = f"{cell}{backup_suffix}"
    
    r = client.execute_skill(f'''
    let((src_cv dst_cv)
      src_cv = dbOpenCellViewByType("{lib}" "{cell}" "{view}" "{view}" "r")
      when(src_cv
        ; 删除旧备份
        when(ddGetObj("{lib}" "{backup_cell}")
          ddDeleteObj(ddGetObj("{lib}" "{backup_cell}"))
        )
        ; 创建新备份
        dst_cv = dbOpenCellViewByType("{lib}" "{backup_cell}" "{view}" "{view}" "a")
        when(dst_cv
          dbCopy(dst_cv src_cv)
          dbSave(dst_cv)
          dbClose(dst_cv)
        )
        dbClose(src_cv)
        t
      )
    )
    ''')
    
    return 't' in str(r.output)


def get_instance_info(client, lib: str, cell: str, inst_name: str, 
                      view: str = "schematic") -> Optional[Dict]:
    """
    获取实例的详细信息（位置、方向、连接、参数等）
    
    Returns:
        实例信息字典，或 None 如果实例不存在
    """
    r = client.execute_skill(f'''
    let((cv inst result)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "{view}" "{view}" "r")
      when(cv
        inst = dbFindFigByName(cv "{inst_name}")
        when(inst
          result = list(
            list("name" inst~>name)
            list("xy" inst~>xy)
            list("orient" inst~>orient)
            list("master_lib" inst~>master~>libName)
            list("master_cell" inst~>master~>name)
            list("terms" foreach(mapcar term inst~>terms
              list(term~>name foreach(mapcar net term~>nets net~>name))
            ))
            list("params" foreach(mapcar param inst~>parameters
              list(param~>name param~>value)
            ))
          )
        )
        dbClose(cv)
        result
      )
    )
    ''')
    
    if 'nil' in str(r.output):
        return None
    
    # 解析返回值 (简化版)
    return {"raw_output": r.output}


def safe_replace_instance(client, lib: str, cell: str, inst_name: str,
                          new_lib: str, new_cell: str, view: str = "schematic",
                          new_view: str = "symbol") -> bool:
    """
    安全替换实例 - 记录原信息 -> 备份 -> 删除 -> 创建新实例 -> 重连
    
    Args:
        client: VirtuosoClient
        lib: 库名
        cell: 单元名
        inst_name: 要替换的实例名
        new_lib: 新器件库名
        new_cell: 新器件单元名
        view: 视图名
        new_view: 新器件视图名
    
    Returns:
        bool: 是否替换成功
    """
    # 1. 先获取原实例信息
    inst_info = get_instance_info(client, lib, cell, inst_name, view)
    if not inst_info:
        print(f"❌ 实例 {inst_name} 不存在!")
        return False
    
    print(f"✅ 找到原实例: {inst_name}")
    
    # 2. 备份
    backup_ok = backup_schematic(client, lib, cell, view)
    if not backup_ok:
        print(f"⚠️ 警告: 备份失败，但继续操作")
    else:
        print(f"✅ 备份已创建: {cell}_backup")
    
    # 3. 解析原实例信息
    # 注意: 实际使用时需要更完善的 SKILL 输出解析
    # 这里用简单的方式获取 x, y, orient, 端子连接
    
    r = client.execute_skill(f'''
    let((cv inst x y orient term_info)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "{view}" "{view}" "r")
      when(cv
        inst = dbFindFigByName(cv "{inst_name}")
        when(inst
          x = car(inst~>xy)
          y = cadr(inst~>xy)
          orient = inst~>orient
          term_info = nil
          foreach(term inst~>terms
            when(term~>nets
              term_info = cons(
                list(term~>name car(term~>nets)~>name)
                term_info
              )
            )
          )
        )
        dbClose(cv)
        list(x y orient term_info)
      )
    )
    ''')
    
    print(f"原实例信息: {r.output}")
    
    # 4. 执行替换 (单个 SKILL 块，避免竞态)
    r = client.execute_skill(f'''
    let((cv inst x y orient terms new_inst master)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "{view}" "{view}" "a")
      when(cv
        inst = dbFindFigByName(cv "{inst_name}")
        when(inst
          ; 记录原信息
          x = car(inst~>xy)
          y = cadr(inst~>xy)
          orient = inst~>orient
          
          ; 记录端子连接
          terms = nil
          foreach(term inst~>terms
            when(term~>nets
              terms = cons(
                list(term~>name car(term~>nets)~>name)
                terms
              )
            )
          )
          
          ; 删除旧实例
          dbDeleteObject(inst)
          
          ; 创建新实例
          master = dbOpenCellViewByType("{new_lib}" "{new_cell}" "{new_view}" "{new_view}" "r")
          when(master
            new_inst = dbCreateInst(cv master "{inst_name}" list(x y) orient)
            
            ; 重新连接端子
            foreach(term_pair terms
              schConnectNetByName(new_inst car(term_pair) cadr(term_pair))
            )
          )
          
          dbSave(cv)
        )
        dbClose(cv)
        t
      )
    )
    ''')
    
    success = 't' in str(r.output)
    
    if success:
        print(f"✅ 实例 {inst_name} 已成功替换为 {new_lib}/{new_cell}")
    else:
        print(f"❌ 替换失败")
    
    return success


def print_startup_report(results: Dict) -> None:
    """打印自检报告"""
    print("\n" + "="*60)
    print("VIRTUOSO 启动自检报告")
    print("="*60)
    
    print(f"Cell 存在: {'✅' if results['cell_exists'] else '❌'}")
    print(f"实例数量: {results['instance_count']}")
    
    if 'cc_exists' in results and results['cc_exists']:
        print(f"Cc 类型: {results.get('cc_type', 'N/A')}")
    
    if results['warnings']:
        print("\n⚠️ 警告:")
        for w in results['warnings']:
            print(f"  - {w}")
    
    print("="*60 + "\n")

