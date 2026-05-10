"""SMIC 12nm SFE PDK 层定义"""
from typing import Tuple

class SMIC12SFLayers:
    """SMIC 12nm FinFET PDK 层定义"""
    
    # 基本工艺层
    AA = "AA"                    # 有源区
    FIN = "FIN"                  # FinFET 鳍
    GT = "GT"                    # 栅极
    DG = "DG"                    # 双栅
    P2 = "P2"                    # 第二多晶
    SN = "SN"                    # N型源漏注入
    SP = "SP"                    # P型源漏注入
    NW = "NW"                    # N阱
    DNW = "DNW"                  # 深N阱
    NPAA = "NPAA"                # N型AA注入
    PPAA = "PPAA"                # P型AA注入
    
    # 金属互连层
    M0 = "M0"                    # 第0层金属
    M0C = "M0C"                  # M0切割层
    M1 = "M1"                    # 第1层金属
    M2 = "M2"                    # 第2层金属
    M3 = "M3"                    # 第3层金属
    M4 = "M4n"                   # 第4层金属
    M5 = "M5n"                   # 第5层金属
    M6 = "M6n"                   # 第6层金属
    M7 = "M7n"                   # 第7层金属
    TM1 = "TM1"                  # 顶层金属1
    TM2 = "TM2"                  # 顶层金属2
    ALPA = "ALPA"                # 铝焊盘层
    PA = "PA"                    # 钝化层开口
    BUMP = "BUMP"                # 凸块层
    
    # 通孔层
    V0 = "V0"                    # M0-M1 通孔
    V1 = "V1"                    # M1-M2 通孔
    V2 = "V2"                    # M2-M3 通孔
    V3 = "V3"                    # M3-M4 通孔
    V4 = "V4"                    # M4-M5 通孔
    V5 = "V5"                    # M5-M6 通孔
    V6 = "V6"                    # M6-M7 通孔
    TV1 = "TV1"                  # M7-TM1 通孔
    TV2 = "TV2"                  # TM1-TM2 通孔
    BV1 = "BV1"                  # TM2-ALPA 通孔
    
    # 用途定义
    DRAWING = "drawing"          # 绘图用途
    PIN = "pin"                  # 引脚用途
    LABEL = "label"              # 标签用途
    NET = "net"                  # 网络用途
    
    @classmethod
    def lpp(cls, layer: str, purpose: str = DRAWING) -> Tuple[str, str]:
        """获取 (layer, purpose) 元组"""
        return (layer, purpose)

# 便捷实例
SMIC12SF = SMIC12SFLayers()
