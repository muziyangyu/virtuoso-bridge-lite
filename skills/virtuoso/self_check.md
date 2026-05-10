
# Virtuoso 自检技能 (Self-Check)

## ⚠️ **本技能用于防止误删和数据库操作前的安全检查

## 启动自检

在执行任何编辑操作前，必须先运行自检：

```python
from virtuoso_bridge import VirtuosoClient

client = VirtuosoClient.from_env()

# === 自检 1: 检查 cell 是否存在
def check_cell_exists(client, lib, cell):
    """检查 cell 是否存在"""
    r = client.execute_skill(f'ddGetObj("{lib}" "{cell}")')
    return 'nil' not in str(r.output)

# === 自检 2: 检查当前原理图实例数
def check_schematic_instances(client, lib, cell):
    """检查原理图实例数"""
    r = client.execute_skill(f'''
    let((cv count)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "schematic" "schematic" "r")
      when(cv
        count = length(cv~>instances)
        dbClose(cv)
        count
      )
    )
    ''')
    try:
        return int(r.output)
    except:
        return 0

# === 自检 3: 安全删除前备份
def backup_schematic(client, lib, cell, backup_suffix="_backup"):
    """备份原理图到另一个 cell"""
    backup_cell = f"{cell}{backup_suffix}"
    r = client.execute_skill(f'''
    let((src_cv dst_cv)
      src_cv = dbOpenCellViewByType("{lib}" "{cell}" "schematic" "schematic" "r")
      when(src_cv
        ; 删除旧备份
        when(ddGetObj("{lib}" "{backup_cell}")
          ddDeleteObj(ddGetObj("{lib}" "{backup_cell}"))
        )
        ; 创建新备份
        dst_cv = dbOpenCellViewByType("{lib}" "{backup_cell}" "schematic" "schematic" "a")
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

# === 自检 4: 安全删除实例 - 只删除指定实例，不要全删
def safe_delete_instance(client, lib, cell, instance_names):
    """安全删除指定实例，而不是全删"""
    # 先备份
    backup_ok = backup_schematic(client, lib, cell)
    if not backup_ok:
        print(f"⚠️ 警告: 备份失败，继续操作")
        return False
    
    # 检查实例
    instances_str = ' '.join([f'"{name}"' for name in instance_names])
    r = client.execute_skill(f'''
    let((cv inst)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "schematic" "schematic" "a")
      when(cv
        foreach(name list({instances_str})
          inst = dbFindFigByName(cv name)
          when(inst
            dbDeleteObject(inst))
          )
        )
        dbSave(cv)
        dbClose(cv)
        t
      )
    )
    ''')
    return 't' in str(r.output)

# === 自检 5: 替换实例前验证
def verify_instance_replacement(client, lib, cell, old_inst_name, new_lib, new_cell):
    """验证替换操作：记录原实例信息"""
    r = client.execute_skill(f'''
    let((cv inst result)
      cv = dbOpenCellViewByType("{lib}" "{cell}" "schematic" "schematic" "r")
      when(cv
        inst = dbFindFigByName(cv "{old_inst_name}")
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
          )
        )
        dbClose(cv)
        result
      )
    )
    ''')
    return r.output

# === 自检 6: 检查 dbOpenCellViewByType 参数是否正确
def check_dbopen_params():
    """检查 dbOpenCellViewByType 的正确参数格式"""
    print("✅ dbOpenCellViewByType 必须使用 5 个参数!")
    print("   cv = dbOpenCellViewByType(lib cell view view_type mode)")
    print("   例如: cv = dbOpenCellViewByType(\"work_ai\" \"opamp_two_stage\" \"schematic\" \"schematic\" \"a\")")
    print()
    print("❌ 常见错误: 只传 4 个参数")
    print("   cv = dbOpenCellViewByType(\"work_ai\" \"opamp_two_stage\" \"schematic\" \"a\")")
    print("   返回 nil，导致后续操作全部失败!")

