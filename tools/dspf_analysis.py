#!/usr/bin/env python3
"""
DSPF 三款 RC 提取工具深度对比分析
工具: StarRC (golden), RCExplorer (rce), GloryEX RC (ref)
"""

import re
import json
from pathlib import Path
from collections import defaultdict


def parse_dspf(filepath):
    """解析 DSPF 文件，提取详细统计信息"""
    data = {
        'header': {},
        'total_cap': 0.0,
        'total_res': 0.0,
        'cap_count': 0,
        'res_count': 0,
        'cap_values': [],
        'res_values': [],
        'nets': set(),
        'cap_by_net': defaultdict(list),
        'res_by_net': defaultdict(list),
    }
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            
            # 解析头部
            if line.startswith('*|'):
                if '|DSPF' in line:
                    data['header']['format'] = line
                elif '|DATE' in line:
                    data['header']['date'] = line
                elif '|PROGRAM' in line:
                    data['header']['program'] = line.split('"')[1]
                elif '|VERSION' in line:
                    data['header']['version'] = line.split('"')[1]
            
            # 解析电容 - 兼容不同 DSPF 格式 (value 可能在最后或倒数第二个位置)
            elif line.startswith('C'):
                parts = line.split()
                if len(parts) >= 4:
                    cap_val = None
                    # 尝试从右往左找第一个可转换为浮点数的值
                    for i in range(len(parts) - 1, -1, -1):
                        try:
                            cap_val = float(parts[i])
                            break
                        except:
                            continue
                    if cap_val is not None:
                        data['cap_values'].append(cap_val)
                        data['total_cap'] += cap_val
                        data['cap_count'] += 1
                        net1 = parts[1].split(':')[0] if ':' in parts[1] else parts[1]
                        data['nets'].add(net1)
                        data['cap_by_net'][net1].append(cap_val)
            
            # 解析电阻 - 兼容不同 DSPF 格式
            elif line.startswith('R'):
                parts = line.split()
                if len(parts) >= 4:
                    res_val = None
                    for i in range(len(parts) - 1, -1, -1):
                        try:
                            res_val = float(parts[i])
                            break
                        except:
                            continue
                    if res_val is not None:
                        data['res_values'].append(res_val)
                        data['total_res'] += res_val
                        data['res_count'] += 1
                        net1 = parts[1].split(':')[0] if ':' in parts[1] else parts[1]
                        data['nets'].add(net1)
                        data['res_by_net'][net1].append(res_val)
    
    return data


def analyze_distribution(values):
    """分析数值分布"""
    if not values:
        return {}
    
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    
    return {
        'min': min(values),
        'max': max(values),
        'mean': sum(values) / len(values),
        'median': sorted_vals[n//2],
        'p10': sorted_vals[int(n*0.10)],
        'p25': sorted_vals[int(n*0.25)],
        'p75': sorted_vals[int(n*0.75)],
        'p90': sorted_vals[int(n*0.90)],
        'count': n,
    }


def main():
    dspf_dir = Path(r'D:\Users\admin\Desktop\work_path\virtuoso-bridge-lite\output\dspf')
    
    files = {
        'StarRC (Golden)': dspf_dir / 'output.golden.dspf',
        'RCExplorer (RCE)': dspf_dir / 'output.rce.dspf',
        'GloryEX RC (Ref)': dspf_dir / 'output.ref.dspf',
    }
    
    results = {}
    
    # 解析所有文件
    for name, path in files.items():
        print(f"\n{'='*60}")
        print(f"解析: {name}")
        print(f"文件: {path.name}")
        print(f"大小: {path.stat().st_size / 1024:.1f} KB")
        
        data = parse_dspf(path)
        results[name] = data
        
        # 输出基本统计
        print(f"\n📊 基本统计:")
        print(f"  工具版本: {data['header'].get('program', 'N/A')} {data['header'].get('version', 'N/A')}")
        print(f"  生成时间: {data['header'].get('date', 'N/A')}")
        print(f"  网络总数: {len(data['nets'])} 个")
        print(f"  电容数量: {data['cap_count']} 个")
        print(f"  电阻数量: {data['res_count']} 个")
        print(f"  总电容: {data['total_cap'] * 1e15:.4f} fF")
        print(f"  总电阻: {data['total_res']:.4f} Ω")
        
        # 分布分析
        cap_dist = analyze_distribution(data['cap_values'])
        res_dist = analyze_distribution(data['res_values'])
        
        print(f"\n📈 电容分布 (单位: fF):")
        print(f"  均值: {cap_dist.get('mean', 0) * 1e15:.4f} fF")
        print(f"  中值: {cap_dist.get('median', 0) * 1e15:.4f} fF")
        print(f"  范围: {cap_dist.get('min', 0) * 1e15:.6f} ~ {cap_dist.get('max', 0) * 1e15:.4f} fF")
        print(f"  P10-P90: {cap_dist.get('p10', 0) * 1e15:.6f} ~ {cap_dist.get('p90', 0) * 1e15:.4f} fF")
        
        print(f"\n📉 电阻分布 (单位: Ω):")
        print(f"  均值: {res_dist.get('mean', 0):.4f} Ω")
        print(f"  中值: {res_dist.get('median', 0):.4f} Ω")
        print(f"  范围: {res_dist.get('min', 0):.6f} ~ {res_dist.get('max', 0):.2f} Ω")
        print(f"  P10-P90: {res_dist.get('p10', 0):.6f} ~ {res_dist.get('p90', 0):.2f} Ω")
    
    # 生成对比表格
    print(f"\n{'='*60}")
    print("📋 三款工具综合对比")
    print(f"{'='*60}")
    
    # 表头
    print(f"\n{'项目':<25} {'StarRC (金标准)':<20} {'RCExplorer':<20} {'GloryEX RC':<20}")
    print(f"{'-'*85}")
    
    # 基本信息
    g_data = results['StarRC (Golden)']
    r_data = results['RCExplorer (RCE)']
    f_data = results['GloryEX RC (Ref)']
    
    print(f"{'电容总数':<25} {g_data['cap_count']:<20,} {r_data['cap_count']:<20,} {f_data['cap_count']:<20,}")
    print(f"{'电阻总数':<25} {g_data['res_count']:<20,} {r_data['res_count']:<20,} {f_data['res_count']:<20,}")
    print(f"{'网络总数':<25} {len(g_data['nets']):<20} {len(r_data['nets']):<20} {len(f_data['nets']):<20}")
    print()
    print(f"{'总电容 (fF)':<25} {g_data['total_cap']*1e15:<20.2f} {r_data['total_cap']*1e15:<20.2f} {f_data['total_cap']*1e15:<20.2f}")
    print(f"{'总电阻 (Ω)':<25} {g_data['total_res']:<20.2f} {r_data['total_res']:<20.2f} {f_data['total_res']:<20.2f}")
    print()
    
    # 相对差异 (以 StarRC 为基准 100%)
    cap_diff_r = (r_data['total_cap'] - g_data['total_cap']) / g_data['total_cap'] * 100
    cap_diff_f = (f_data['total_cap'] - g_data['total_cap']) / g_data['total_cap'] * 100
    res_diff_r = (r_data['total_res'] - g_data['total_res']) / g_data['total_res'] * 100
    res_diff_f = (f_data['total_res'] - g_data['total_res']) / g_data['total_res'] * 100
    
    print(f"{'电容相对差异':<25} {'基准 (100%)':<20} {cap_diff_r:+6.2f}%{'':<13} {cap_diff_f:+6.2f}%{'':<13}")
    print(f"{'电阻相对差异':<25} {'基准 (100%)':<20} {res_diff_r:+6.2f}%{'':<13} {res_diff_f:+6.2f}%{'':<13}")
    print()
    print(f"{'平均电容 (aF)':<25} {(g_data['total_cap']/g_data['cap_count']*1e18):<20.1f} {(r_data['total_cap']/r_data['cap_count']*1e18):<20.1f} {(f_data['total_cap']/f_data['cap_count']*1e18):<20.1f}")
    print(f"{'平均电阻 (mΩ)':<25} {(g_data['total_res']/g_data['res_count']*1e3):<20.1f} {(r_data['total_res']/r_data['res_count']*1e3):<20.1f} {(f_data['total_res']/f_data['res_count']*1e3):<20.1f}")
    
    # 电容分布对比
    g_cap_dist = analyze_distribution(g_data['cap_values'])
    r_cap_dist = analyze_distribution(r_data['cap_values'])
    f_cap_dist = analyze_distribution(f_data['cap_values'])
    
    print(f"\n{'='*60}")
    print("📊 电容分布对比 (单位: fF)")
    print(f"{'='*60}")
    print(f"{'分布指标':<20} {'StarRC':<15} {'RCExplorer':<15} {'GloryEX':<15}")
    print(f"{'-'*65}")
    print(f"{'Min':<20} {g_cap_dist['min']*1e15:<15.4f} {r_cap_dist['min']*1e15:<15.4f} {f_cap_dist['min']*1e15:<15.4f}")
    print(f"{'P10':<20} {g_cap_dist['p10']*1e15:<15.4f} {r_cap_dist['p10']*1e15:<15.4f} {f_cap_dist['p10']*1e15:<15.4f}")
    print(f"{'Median':<20} {g_cap_dist['median']*1e15:<15.4f} {r_cap_dist['median']*1e15:<15.4f} {f_cap_dist['median']*1e15:<15.4f}")
    print(f"{'P75':<20} {g_cap_dist['p75']*1e15:<15.4f} {r_cap_dist['p75']*1e15:<15.4f} {f_cap_dist['p75']*1e15:<15.4f}")
    print(f"{'P90':<20} {g_cap_dist['p90']*1e15:<15.4f} {r_cap_dist['p90']*1e15:<15.4f} {f_cap_dist['p90']*1e15:<15.4f}")
    print(f"{'Max':<20} {g_cap_dist['max']*1e15:<15.4f} {r_cap_dist['max']*1e15:<15.4f} {f_cap_dist['max']*1e15:<15.4f}")
    
    # 电阻分布对比
    g_res_dist = analyze_distribution(g_data['res_values'])
    r_res_dist = analyze_distribution(r_data['res_values'])
    f_res_dist = analyze_distribution(f_data['res_values'])
    
    print(f"\n{'='*60}")
    print("📊 电阻分布对比 (单位: Ω)")
    print(f"{'='*60}")
    print(f"{'分布指标':<20} {'StarRC':<15} {'RCExplorer':<15} {'GloryEX':<15}")
    print(f"{'-'*65}")
    print(f"{'Min':<20} {g_res_dist['min']:<15.6f} {r_res_dist['min']:<15.6f} {f_res_dist['min']:<15.6f}")
    print(f"{'P10':<20} {g_res_dist['p10']:<15.4f} {r_res_dist['p10']:<15.4f} {f_res_dist['p10']:<15.4f}")
    print(f"{'Median':<20} {g_res_dist['median']:<15.4f} {r_res_dist['median']:<15.4f} {f_res_dist['median']:<15.4f}")
    print(f"{'P75':<20} {g_res_dist['p75']:<15.4f} {r_res_dist['p75']:<15.4f} {f_res_dist['p75']:<15.4f}")
    print(f"{'P90':<20} {g_res_dist['p90']:<15.2f} {r_res_dist['p90']:<15.2f} {f_res_dist['p90']:<15.2f}")
    print(f"{'Max':<20} {g_res_dist['max']:<15.2f} {r_res_dist['max']:<15.2f} {f_res_dist['max']:<15.2f}")
    
    # 总结分析
    print(f"\n{'='*60}")
    print("🎯 关键发现总结")
    print(f"{'='*60}")
    
    print(f"\n1. 🔌 电容提取差异:")
    print(f"   - StarRC: {g_data['cap_count']:,} 个电容, 总容量 {g_data['total_cap']*1e15:.2f} fF")
    print(f"   - RCExplorer: 电容数量少 {g_data['cap_count'] - r_data['cap_count']:,} 个 ({(1 - r_data['cap_count']/g_data['cap_count'])*100:.1f}%), 总容量差 {cap_diff_r:+.2f}%")
    print(f"   - GloryEX: 电容数量少 {g_data['cap_count'] - f_data['cap_count']:,} 个 ({(1 - f_data['cap_count']/g_data['cap_count'])*100:.1f}%), 总容量差 {cap_diff_f:+.2f}%")
    
    print(f"\n2. ⚡ 电阻提取差异:")
    print(f"   - StarRC: {g_data['res_count']:,} 个电阻, 总阻值 {g_data['total_res']:.2f} Ω")
    print(f"   - RCExplorer: 电阻数量少 {g_data['res_count'] - r_data['res_count']:,} 个 ({(1 - r_data['res_count']/g_data['res_count'])*100:.1f}%), 总阻值差 {res_diff_r:+.2f}%")
    print(f"   - GloryEX: 电阻数量少 {g_data['res_count'] - f_data['res_count']:,} 个 ({(1 - f_data['res_count']/g_data['res_count'])*100:.1f}%), 总阻值差 {res_diff_f:+.2f}%")
    
    print(f"\n3. 📐 精度评估 (以 StarRC 为金标准):")
    cap_rmse_r = abs(cap_diff_r)
    res_rmse_r = abs(res_diff_r)
    cap_rmse_f = abs(cap_diff_f)
    res_rmse_f = abs(res_diff_f)
    print(f"   - RCExplorer: 电容偏差 ±{cap_rmse_r:.2f}%, 电阻偏差 ±{res_rmse_r:.2f}%")
    print(f"   - GloryEX: 电容偏差 ±{cap_rmse_f:.2f}%, 电阻偏差 ±{res_rmse_f:.2f}%")
    
    if cap_rmse_f < cap_rmse_r and res_rmse_f < res_rmse_r:
        print(f"   - 结论: GloryEX RC 整体更接近 StarRC 金标准")
    elif cap_rmse_r < cap_rmse_f and res_rmse_r < res_rmse_f:
        print(f"   - 结论: RCExplorer 整体更接近 StarRC 金标准")
    else:
        print(f"   - 结论: 两款工具各有优劣，需结合具体场景")
    
    print(f"\n4. 📦 提取粒度差异:")
    print(f"   - StarRC 平均每电容: {g_data['total_cap']/g_data['cap_count']*1e18:.1f} aF")
    print(f"   - RCExplorer 平均每电容: {r_data['total_cap']/r_data['cap_count']*1e18:.1f} aF")
    print(f"   - GloryEX 平均每电容: {f_data['total_cap']/f_data['cap_count']*1e18:.1f} aF")
    print(f"   - StarRC 平均每电阻: {g_data['total_res']/g_data['res_count']*1e3:.1f} mΩ")
    print(f"   - RCExplorer 平均每电阻: {r_data['total_res']/r_data['res_count']*1e3:.1f} mΩ")
    print(f"   - GloryEX 平均每电阻: {f_data['total_res']/f_data['res_count']*1e3:.1f} mΩ")

    # 保存详细结果
    summary = {
        'StarRC': {
            'tool': 'StarRC',
            'version': g_data['header'].get('version', ''),
            'cap_count': g_data['cap_count'],
            'res_count': g_data['res_count'],
            'total_cap_fF': g_data['total_cap'] * 1e15,
            'total_res_Ohm': g_data['total_res'],
            'cap_dist_fF': {k: v*1e15 for k, v in g_cap_dist.items()},
            'res_dist_Ohm': g_res_dist,
        },
        'RCExplorer': {
            'tool': 'RCExplorer',
            'version': r_data['header'].get('version', ''),
            'cap_count': r_data['cap_count'],
            'res_count': r_data['res_count'],
            'total_cap_fF': r_data['total_cap'] * 1e15,
            'total_res_Ohm': r_data['total_res'],
            'cap_dist_fF': {k: v*1e15 for k, v in r_cap_dist.items()},
            'res_dist_Ohm': r_res_dist,
        },
        'GloryEX': {
            'tool': 'GloryEX RC',
            'version': f_data['header'].get('version', ''),
            'cap_count': f_data['cap_count'],
            'res_count': f_data['res_count'],
            'total_cap_fF': f_data['total_cap'] * 1e15,
            'total_res_Ohm': f_data['total_res'],
            'cap_dist_fF': {k: v*1e15 for k, v in f_cap_dist.items()},
            'res_dist_Ohm': f_res_dist,
        },
        'comparison': {
            'rce_vs_golden_cap_diff_pct': cap_diff_r,
            'rce_vs_golden_res_diff_pct': res_diff_r,
            'glory_vs_golden_cap_diff_pct': cap_diff_f,
            'glory_vs_golden_res_diff_pct': res_diff_f,
        },
        'generated_at': '2026-05-08',
    }
    
    with open(dspf_dir / 'dspf_comparison_summary.json', 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 详细分析结果已保存到: {dspf_dir / 'dspf_comparison_summary.json'}")


if __name__ == '__main__':
    main()
