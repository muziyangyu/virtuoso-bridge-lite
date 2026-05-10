"""SMIC 12nm SFE PDK 器件生成器"""
from typing import Optional, Tuple
from .ops import (
    layout_create_param_inst,
    layout_create_simple_mosaic,
    layout_create_rect,
    layout_create_label,
)

# PDK 库名常量
SMIC12SF_LIB = "smic12sf"
DEFAULT_VIEW = "layout"


def _cdf_param_set(inst_name: str, **params: str) -> str:
    """构建通过 CDF 设置 pcell 参数的 SKILL 代码。

    处理 ``instData`` 类型的 CDF 参数（所有值存为字符串）。
    优先使用 ``cv``（编辑器上下文变量），回退到 ``geGetEditCellView()``。
    """
    pairs = " ".join(
        f'p = get(cdf "{k}") when(p p~>value = "{v}")'
        for k, v in params.items()
    )
    return (
        f'let((ci) '
        f'ci = dbFindInst(geGetEditCellView() "{inst_name}") '
        f'unless(ci ci = car(setof(x cv~>instances x~>name == "{inst_name}"))) '
        f'when(ci let((cdf) cdf = cdfGetInstCDF(ci) when(cdf {pairs})))'
        f')'
    )


# ============================================
# MOS 器件生成函数
# ============================================

def smic12sf_create_nmos(
    instance_name: str,
    x: float,
    y: float,
    orientation: str = "R0",
    *,
    l: float = 0.014,
    w: float = 0.1,
    nf: int = 1,
    m: int = 1,
    vth: str = "svt",
    voltage: str = "08",
    dnw: bool = False,
) -> str:
    """创建 SMIC 12nm NMOS 器件

    Args:
        instance_name: 实例名称
        x, y: 放置坐标
        orientation: 方向 (R0, R90, R180, R270, MY, MX)
        l: 栅长 (um), 默认 0.014
        w: 栅宽 (um) per finger, 默认 0.1
        nf: 指状数, 默认 1
        m: 并联倍数, 默认 1
        vth: 阈值类型 "ulvt", "lvt", "svt", "hvt", 默认 "svt"
        voltage: 电压等级 "08" (0.8V), "18" (1.8V), 默认 "08"
        dnw: 是否使用深N阱, 默认 False
    """
    vth_map = {
        "ulvt": "nulvt",
        "lvt": "nlvt",
        "svt": "n",
        "hvt": "nhvt",
    }

    dnw_suffix = "_dnw" if dnw else ""
    cell_name = f"{vth_map[vth]}{voltage}{dnw_suffix}_ckt"

    cmd = layout_create_param_inst(
        SMIC12SF_LIB,
        cell_name,
        DEFAULT_VIEW,
        instance_name,
        x,
        y,
        orientation,
    )

    param_cmd = _cdf_param_set(instance_name, l=str(l), w=str(w), nf=str(nf), m=str(m))
    return cmd + " " + param_cmd


def smic12sf_create_pmos(
    instance_name: str,
    x: float,
    y: float,
    orientation: str = "R0",
    *,
    l: float = 0.014,
    w: float = 0.1,
    nf: int = 1,
    m: int = 1,
    vth: str = "svt",
    voltage: str = "08",
) -> str:
    """创建 SMIC 12nm PMOS 器件

    Args:
        instance_name: 实例名称
        x, y: 放置坐标
        orientation: 方向
        l: 栅长 (um)
        w: 栅宽 (um) per finger
        nf: 指状数
        m: 并联倍数
        vth: 阈值类型 "ulvt", "lvt", "svt", "hvt"
        voltage: 电压等级 "08" (0.8V), "18" (1.8V)
    """
    vth_map = {
        "ulvt": "pulvt",
        "lvt": "plvt",
        "svt": "p",
        "hvt": "phvt",
    }

    cell_name = f"{vth_map[vth]}{voltage}_ckt"

    cmd = layout_create_param_inst(
        SMIC12SF_LIB,
        cell_name,
        DEFAULT_VIEW,
        instance_name,
        x,
        y,
        orientation,
    )

    param_cmd = _cdf_param_set(instance_name, l=str(l), w=str(w), nf=str(nf), m=str(m))
    return cmd + " " + param_cmd


# ============================================
# 无源器件生成函数
# ============================================

def smic12sf_create_mom_cap(
    instance_name: str,
    x: float,
    y: float,
    orientation: str = "R0",
    *,
    w: float = 1.0,
    l: float = 1.0,
    nf: int = 1,
    ports: int = 2,
    high_quality: bool = False,
    ultra_low: bool = False,
) -> str:
    """创建 MOM 电容

    Args:
        instance_name: 实例名称
        x, y: 放置坐标
        orientation: 方向
        w: 电容宽度 (um)
        l: 电容长度 (um)
        nf: 指状数
        ports: 端口数 2,3,4,5
        high_quality: 高品质版本
        ultra_low: 超低电容版本
    """
    if high_quality:
        quality = "hq_"
    elif ultra_low:
        quality = "ulc_"
    else:
        quality = ""

    cell_name = f"mom_{quality}{ports}t_1p25"

    cmd = layout_create_param_inst(
        SMIC12SF_LIB,
        cell_name,
        DEFAULT_VIEW,
        instance_name,
        x,
        y,
        orientation,
    )

    param_cmd = _cdf_param_set(instance_name, w=str(w), l=str(l), nf=str(nf))
    return cmd + " " + param_cmd


def smic12sf_create_resistor(
    instance_name: str,
    x: float,
    y: float,
    orientation: str = "R0",
    *,
    w: float = 0.1,
    l: float = 1.0,
    m: int = 1,
    res_type: str = "rm1",
) -> str:
    """创建电阻

    Args:
        instance_name: 实例名称
        x, y: 放置坐标
        orientation: 方向
        w: 电阻宽度 (um)
        l: 电阻长度 (um)
        m: 并联倍数
        res_type: 电阻类型 "rm1"~"rm7", "rtm1", "rtm2", "ralpa", "rhrpo", "rnwsti"
    """
    cell_name = f"{res_type}_ckt"

    cmd = layout_create_param_inst(
        SMIC12SF_LIB,
        cell_name,
        DEFAULT_VIEW,
        instance_name,
        x,
        y,
        orientation,
    )

    param_cmd = _cdf_param_set(instance_name, w=str(w), l=str(l), m=str(m))
    return cmd + " " + param_cmd


def smic12sf_create_diode(
    instance_name: str,
    x: float,
    y: float,
    orientation: str = "R0",
    *,
    diode_type: str = "ndio08",
    w: float = 0.5,
    l: float = 0.5,
) -> str:
    """创建二极管

    Args:
        instance_name: 实例名称
        x, y: 放置坐标
        orientation: 方向
        diode_type: "ndio08", "ndio18", "pdio08", "pdio18", "dnwdio", "nwdio", "rwdio"
        w: 宽度 (um)
        l: 长度 (um)
    """
    cell_name = f"{diode_type}_ckt"

    cmd = layout_create_param_inst(
        SMIC12SF_LIB,
        cell_name,
        DEFAULT_VIEW,
        instance_name,
        x,
        y,
        orientation,
    )

    param_cmd = _cdf_param_set(instance_name, w=str(w), l=str(l))
    return cmd + " " + param_cmd


# ============================================
# 标准单元快捷函数
# ============================================

def smic12sf_nmos_svt(
    name: str, x: float, y: float, *, l: float = 0.014, w: float = 0.1, nf: int = 1
) -> str:
    """便捷函数: 创建标准阈值 0.8V NMOS"""
    return smic12sf_create_nmos(name, x, y, l=l, w=w, nf=nf, vth="svt", voltage="08")


def smic12sf_pmos_svt(
    name: str, x: float, y: float, *, l: float = 0.014, w: float = 0.1, nf: int = 1
) -> str:
    """便捷函数: 创建标准阈值 0.8V PMOS"""
    return smic12sf_create_pmos(name, x, y, l=l, w=w, nf=nf, vth="svt", voltage="08")


def smic12sf_nmos_lvt(
    name: str, x: float, y: float, *, l: float = 0.014, w: float = 0.1, nf: int = 1
) -> str:
    """便捷函数: 创建低阈值 0.8V NMOS"""
    return smic12sf_create_nmos(name, x, y, l=l, w=w, nf=nf, vth="lvt", voltage="08")


def smic12sf_pmos_lvt(
    name: str, x: float, y: float, *, l: float = 0.014, w: float = 0.1, nf: int = 1
) -> str:
    """便捷函数: 创建低阈值 0.8V PMOS"""
    return smic12sf_create_pmos(name, x, y, l=l, w=w, nf=nf, vth="lvt", voltage="08")
