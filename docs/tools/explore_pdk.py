#!/usr/bin/env python3
"""探索 smic12sf PDK 的器件库结构"""

from virtuoso_bridge import VirtuosoClient
import re

def main():
    client = VirtuosoClient.from_env()
    print("=" * 80)
    print("Virtuoso 连接成功")
    print("=" * 80)
    
    lib_name = "smic12sf"
    print(f"\n目标库: {lib_name}")
    
    # 1. 获取库中的所有 cells
    print("\n" + "=" * 80)
    print("步骤 1: 获取库中所有单元")
    print("=" * 80)
    
    skill_code = '''
    let((lib cells cell_names)
        lib = ddGetObj("smic12sf")
        if(lib then
            cells = ddGetObjCells(lib)
            cell_names = foreach(mapcar cell cells
                ddGetObjName(cell)
            )
            sort(cell_names 'alphalessp)
        )
    )
    '''
    result = client.execute_skill(skill_code)
    cells_output = result.output
    print(f"原始输出长度: {len(cells_output) if cells_output else 0}")
    
    # 解析 cell 列表
    cell_names = []
    if isinstance(cells_output, str):
        match = re.findall(r'"([^"]+)"', cells_output)
        if match:
            cell_names = match
    
    print(f"\n找到 {len(cell_names)} 个单元")
    
    # 2. 按类别分类器件
    print("\n" + "=" * 80)
    print("步骤 2: 器件分类")
    print("=" * 80)
    
    mos_cells = []
    passive_cells = []
    via_cells = []
    dio_cells = []
    bjt_cells = []
    other_cells = []
    
    for cell in cell_names:
        cell_lower = cell.lower()
        if any(x in cell_lower for x in ['nch', 'pch', 'nmos', 'pmos', 'mos']):
            mos_cells.append(cell)
        elif any(x in cell_lower for x in ['res', 'r_', 'cap', 'c_', 'mim', 'mom']):
            passive_cells.append(cell)
        elif any(x in cell_lower for x in ['via', 'm1m2', 'm2m3', 'm3m4', 'm4m5', 'cont', 'ct', 'bl1']):
            via_cells.append(cell)
        elif any(x in cell_lower for x in ['diode', 'dio', 'd_']):
            dio_cells.append(cell)
        elif any(x in cell_lower for x in ['npn', 'pnp', 'bjt']):
            bjt_cells.append(cell)
        else:
            other_cells.append(cell)
    
    print(f"\n【MOS 晶体管】({len(mos_cells)} 个)")
    for cell in sorted(mos_cells):
        print(f"  - {cell}")
    
    print(f"\n【无源器件】({len(passive_cells)} 个)")
    for cell in sorted(passive_cells):
        print(f"  - {cell}")
    
    print(f"\n【通孔】({len(via_cells)} 个)")
    for cell in sorted(via_cells):
        print(f"  - {cell}")
    
    print(f"\n【二极管】({len(dio_cells)} 个)")
    for cell in sorted(dio_cells):
        print(f"  - {cell}")
    
    print(f"\n【BJT】({len(bjt_cells)} 个)")
    for cell in sorted(bjt_cells):
        print(f"  - {cell}")
    
    print(f"\n【其他器件】({len(other_cells)} 个)")
    for cell in sorted(other_cells)[:50]:  # 只显示前50个
        print(f"  - {cell}")
    if len(other_cells) > 50:
        print(f"  ... 还有 {len(other_cells) - 50} 个")
    
    # 3. 分析典型器件的参数
    print("\n" + "=" * 80)
    print("步骤 3: 典型器件参数分析")
    print("=" * 80)
    
    # 选择几个典型器件进行分析
    sample_cells = []
    if mos_cells:
        sample_cells.extend(mos_cells[:3])
    if passive_cells:
        sample_cells.extend(passive_cells[:2])
    if via_cells:
        sample_cells.extend(via_cells[:2])
    
    for cell_name in sample_cells[:6]:  # 最多分析6个
        print(f"\n--- 器件: {cell_name} ---")
        
        # 获取器件的 CDF 参数
        skill_code = f'''
        let((cdf params param_info_list)
            when(cdf = cdfGetDataBase("smic12sf" "{cell_name}" "symbol")
                params = cdf->parameters
                param_info_list = foreach(mapcar param params
                    list(
                        param->name
                        param->type
                        param->defValue
                        param->range
                    )
                )
                param_info_list
            )
        )
        '''
        result = client.execute_skill(skill_code)
        params_output = result.output
        print(f"CDF 参数: {params_output}")
        
        # 尝试获取器件属性
        if not params_output or params_output == 'nil':
            skill_code = f'''
            let((cell cell_view prop_names)
                cell = ddGetObj("smic12sf" "{cell_name}")
                if(cell then
                    cell_view = car(ddGetObjViews(cell "symbol"))
                    if(cell_view then
                        prop_names = ddGetPropNames(cell_view)
                        prop_names
                    )
                )
            )
            '''
            result = client.execute_skill(skill_code)
            print(f"器件属性名: {result.output}")
    
    # 4. 获取层定义
    print("\n" + "=" * 80)
    print("步骤 4: 层定义信息")
    print("=" * 80)
    
    skill_code = '''
    let((tech layers layer_names)
        tech = car(geGetTechList())
        if(tech then
            layers = leGetAllLayers(tech)
            layer_names = foreach(mapcar layer layers
                list(car(layer) cadr(layer))
            )
            list("总层数" length(layer_names) "层列表" layer_names)
        )
    )
    '''
    result = client.execute_skill(skill_code)
    print(f"层信息: {result.output[:1000] if result.output else '无'}")
    
    # 获取层号
    skill_code = '''
    let((tech layers layer_info)
        tech = car(geGetTechList())
        if(tech then
            layers = leGetAllLayers(tech)
            layer_info = foreach(mapcar layer layers
                lpp = car(layer)
                purpose = cadr(layer)
                list(lpp purpose leGetLayerNum(tech lpp purpose))
            )
            car(nthcdr 0 layer_info 30)
        )
    )
    '''
    result = client.execute_skill(skill_code)
    print(f"\n前30层详细信息 (层名 用途 层号): {result.output}")
    
    # 5. 查找 techfile
    print("\n" + "=" * 80)
    print("步骤 5: 技术文件信息")
    print("=" * 80)
    
    skill_code = '''
    let((tech tf_path)
        tech = car(geGetTechList())
        if(tech then
            tf_path = tech->techFilePath
            list(
                "技术名" tech->name
                "路径" tf_path
                "版本" tech->version
            )
        )
    )
    '''
    result = client.execute_skill(skill_code)
    print(f"技术文件信息: {result.output}")
    
    # 6. 获取 PCell 信息
    print("\n" + "=" * 80)
    print("步骤 6: PCell 信息")
    print("=" * 80)
    
    skill_code = '''
    let((lib cells pcell_names)
        lib = ddGetObj("smic12sf")
        if(lib then
            cells = ddGetObjCells(lib)
            pcell_names = foreach(mapcar cell cells
                when(ddIsPCellMaster(cell)
                    ddGetObjName(cell)
                )
            )
            sort(pcell_names 'alphalessp)
        )
    )
    '''
    result = client.execute_skill(skill_code)
    pcell_output = result.output
    pcell_names = []
    if isinstance(pcell_output, str):
        match = re.findall(r'"([^"]+)"', pcell_output)
        if match:
            pcell_names = match
    print(f"PCell 数量: {len(pcell_names)}")
    print(f"前20个 PCell: {pcell_names[:20]}")
    
    print("\n" + "=" * 80)
    print("PDK 探索完成!")
    print("=" * 80)

if __name__ == "__main__":
    main()
