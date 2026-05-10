"""SMIC 12nm SFE PDK 器件创建示例

演示如何使用 smic12sf PDK 专用的器件生成函数。
"""
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.layout import (
    smic12sf_create_nmos,
    smic12sf_create_pmos,
    smic12sf_create_mom_cap,
    smic12sf_create_resistor,
    smic12sf_nmos_svt,
    smic12sf_pmos_svt,
    SMIC12SF,
)
from virtuoso_bridge.virtuoso.layout.ops import layout_create_rect, layout_create_label


def main():
    # 连接到 Virtuoso
    client = VirtuosoClient.from_env()
    
    # 编辑一个测试 cell
    with client.layout.edit("test_lib", "smic12sf_demo", "layout") as editor:
        
        # ============================================
        # 示例 1: 使用便捷函数创建标准阈值 MOS
        # ============================================
        print("创建标准阈值 NMOS 和 PMOS...")
        
        # 创建反相器对
        editor.execute(smic12sf_nmos_svt("MN1", 0.0, 0.0, l=0.014, w=0.1, nf=2))
        editor.execute(smic12sf_pmos_svt("MP1", 0.0, 2.0, l=0.014, w=0.2, nf=2))
        
        # ============================================
        # 示例 2: 使用完整函数创建不同阈值的 MOS
        # ============================================
        print("创建不同阈值类型的 MOS...")
        
        # 低阈值 NMOS (速度快，漏电大)
        editor.execute(smic12sf_create_nmos(
            "MN_LVT", 2.0, 0.0,
            l=0.014, w=0.15, nf=4,
            vth="lvt", voltage="08"
        ))
        
        # 高阈值 PMOS (速度慢，漏电小)
        editor.execute(smic12sf_create_pmos(
            "MP_HVT", 2.0, 2.0,
            l=0.014, w=0.15, nf=4,
            vth="hvt", voltage="08"
        ))
        
        # 1.8V I/O 器件
        editor.execute(smic12sf_create_nmos(
            "MN_IO", 4.0, 0.0,
            l=0.028, w=0.5, nf=1,
            vth="svt", voltage="18"
        ))
        
        # 带深 N 阱的 NMOS
        editor.execute(smic12sf_create_nmos(
            "MN_DNW", 4.0, 2.0,
            l=0.014, w=0.1, nf=2,
            vth="svt", voltage="08", dnw=True
        ))
        
        # ============================================
        # 示例 3: 创建无源器件
        # ============================================
        print("创建无源器件...")
        
        # MOM 电容
        editor.execute(smic12sf_create_mom_cap(
            "C1", 6.0, 0.0,
            w=1.0, l=1.0, nf=2, ports=2
        ))
        
        # 高品质 MOM 电容
        editor.execute(smic12sf_create_mom_cap(
            "C2_HQ", 6.0, 2.0,
            w=2.0, l=2.0, nf=1, ports=2, high_quality=True
        ))
        
        # 电阻 (M1 金属电阻)
        editor.execute(smic12sf_create_resistor(
            "R1", 8.0, 0.0,
            w=0.1, l=5.0, m=1, res_type="rm1"
        ))
        
        # 顶层金属电阻
        editor.execute(smic12sf_create_resistor(
            "R2", 8.0, 2.0,
            w=0.2, l=10.0, m=1, res_type="rtm1"
        ))
        
        # ============================================
        # 示例 4: 使用层定义
        # ============================================
        print("使用层定义创建图形...")
        
        # 使用 SMIC12SF 层常量创建矩形
        editor.execute(layout_create_rect(
            SMIC12SF.lpp(SMIC12SF.M1, SMIC12SF.DRAWING),
            10.0, 0.0, 11.0, 0.5
        ))
        
        # 创建引脚
        editor.execute(layout_create_rect(
            SMIC12SF.lpp(SMIC12SF.M1, SMIC12SF.PIN),
            10.0, 1.0, 10.2, 1.2
        ))
        
        # 创建标签
        editor.execute(layout_create_label(
            SMIC12SF.lpp(SMIC12SF.M1, SMIC12SF.LABEL),
            10.0, 1.5, "VDD"
        ))
        
        # 使用不同金属层
        editor.execute(layout_create_rect(
            SMIC12SF.lpp(SMIC12SF.M2, SMIC12SF.DRAWING),
            10.0, 2.0, 11.0, 2.2
        ))
        
        editor.execute(layout_create_rect(
            SMIC12SF.lpp(SMIC12SF.TM1, SMIC12SF.DRAWING),
            10.0, 2.5, 12.0, 3.0
        ))
        
        # ============================================
        # 示例 5: 创建一个简单的运算放大器输入对
        # ============================================
        print("创建差分对...")
        
        # 差分输入对 (匹配的 NMOS)
        editor.execute(smic12sf_nmos_svt("MN_DIFF_P", 13.0, 0.0, l=0.014, w=0.2, nf=8))
        editor.execute(smic12sf_nmos_svt("MN_DIFF_N", 13.0, 1.0, l=0.014, w=0.2, nf=8))
        
        # 有源负载 (匹配的 PMOS)
        editor.execute(smic12sf_pmos_svt("MP_LOAD_P", 15.0, 0.0, l=0.014, w=0.3, nf=4))
        editor.execute(smic12sf_pmos_svt("MP_LOAD_N", 15.0, 1.0, l=0.014, w=0.3, nf=4))
        
        # 尾电流源
        editor.execute(smic12sf_create_nmos(
            "MN_TAIL", 13.0, -1.0,
            l=0.028, w=0.5, nf=16,
            vth="svt", voltage="08"
        ))
        
        print("\n器件创建完成!")
        print("已创建:")
        print("  - 反相器对 (NMOS + PMOS)")
        print("  - 不同阈值的 MOS (LVT, HVT)")
        print("  - 1.8V I/O 器件")
        print("  - 带 DNW 的 NMOS")
        print("  - MOM 电容 (标准和 HQ 版本)")
        print("  - 金属电阻")
        print("  - 各种金属层上的图形和标签")
        print("  - 差分对运算放大器输入级")


if __name__ == "__main__":
    main()
