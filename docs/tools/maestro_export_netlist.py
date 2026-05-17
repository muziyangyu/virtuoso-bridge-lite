#!/usr/bin/env python3
"""
Maestro 仿真配置 + 网表导出 模板

用法:
    python3 docs/tools/maestro_export_netlist.py

流程:
    1. 打开 Maestro session (背景模式)
    2. 创建 Test, 配置 AC/TRAN/DC 分析
    3. 设置 Design Variables (开关参数等)
    4. 添加 Outputs
    5. 导出 Spectre netlist → netlist/netlist/input.scs
    6. (可选) 运行 Spectre 仿真

依赖:
    - virtuoso-bridge 已安装, SSH tunnel 已连接
    - 目标 cell 的 schematic 已存在

注意事项:
    - Maestro netlister 会优化掉零值 DC 源 (如 dc=0 的 VTOP)
      如需 AC 激励, 原理图中 VTOP 的 dc 不可为 0, 或用 port 元件
    - set_analysis 的 options 参数名需与 Spectre 一致:
        TRAN: "stop" 非 "stopTime"
        AC:   "start" "stop" "dec"
"""

import sys
import time
import shutil
from pathlib import Path

# ── 项目路径 ──
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.maestro import (
    open_session,
    close_session,
    create_test,
    set_analysis,
    set_var,
    set_sim_option,
    add_output,
    save_setup,
    create_netlist_for_corner,
    set_corner,
)
from virtuoso_bridge.spectre.runner import SpectreSimulator

# ═══════════════════════════════════════════════════════════════
#  用户配置区
# ═══════════════════════════════════════════════════════════════
LIB = "work_ai_iter"          # Library 名称
CELL = "mom_12b_array_8b_tb"  # Testbench cell 名称
TEST_NAME = "AC_TRAN"         # Maestro Test 名称
CORNER = "default"            # Corner 名称
OUTPUT_DIR = PROJECT_ROOT / "output" / "maestro_export_demo"

# Design Variables (原理图中的参数化变量)
DESIGN_VARS = {
    f"sw_msb{i}": "0" for i in range(4)
} | {
    f"sw_lsb{i}": "0" for i in range(4)
}

# Analysis 配置
AC_OPTIONS = """(("start" "1") ("stop" "10G")
                  ("incrType" "Logarithmic")
                  ("stepTypeLog" "Points Per Decade")
                  ("dec" "20"))"""

TRAN_OPTIONS = """(("stop" "20n") ("errpreset" "conservative"))"""

DC_OPTIONS = """(("saveOp" "selected"))"""

SIM_OPTIONS = """(("temp" "27") ("tnom" "27"))"""

# ═══════════════════════════════════════════════════════════════
#  执行
# ═══════════════════════════════════════════════════════════════

def maestro_configure_and_export(client: VirtuosoClient) -> Path | None:
    """通过 Maestro API 配置仿真并导出 netlist, 返回 netlist 路径."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    netlist_dir = OUTPUT_DIR / "netlist"

    print(f"[Maestro] Opening session for {LIB}/{CELL}...")
    session = open_session(client, LIB, CELL)

    try:
        # ── 1. 创建 Test ──
        print(f"[Maestro] Creating test '{TEST_NAME}'...")
        create_test(client, TEST_NAME, lib=LIB, cell=CELL, session=session)

        # ── 2. 配置 Analysis ──
        print("[Maestro] Setting AC analysis...")
        set_analysis(client, TEST_NAME, "ac", options=AC_OPTIONS, session=session)

        print("[Maestro] Setting TRAN analysis...")
        set_analysis(client, TEST_NAME, "tran", options=TRAN_OPTIONS, session=session)

        print("[Maestro] Setting DC analysis...")
        set_analysis(client, TEST_NAME, "dc", options=DC_OPTIONS, session=session)

        # ── 3. Simulator Options ──
        print("[Maestro] Setting simulator options...")
        set_sim_option(client, TEST_NAME, options=SIM_OPTIONS, session=session)

        # ── 4. Design Variables ──
        print("[Maestro] Setting design variables...")
        for name, value in DESIGN_VARS.items():
            set_var(client, name, value, session=session)

        # ── 5. Corner ──
        set_corner(client, CORNER, session=session)

        # ── 6. Outputs ──
        print("[Maestro] Adding outputs...")
        add_output(client, "VTOP_MSB", TEST_NAME,
                   output_type="net", signal_name="/TOP_MSB", session=session)

        # ── 7. 保存 ──
        save_setup(client, LIB, CELL, session=session)

        # ── 8. 导出 Netlist ──
        print(f"[Maestro] Exporting netlist to {netlist_dir}...")
        t0 = time.time()
        create_netlist_for_corner(client, TEST_NAME, CORNER, str(netlist_dir))
        print(f"  Done ({time.time()-t0:.1f}s)")

        netlist_files = list(netlist_dir.rglob("input.scs"))
        if netlist_files:
            return netlist_files[0]
        return None

    finally:
        close_session(client, session)
        print("[Maestro] Session closed.")


def run_spectre(netlist: Path):
    """对导出的 netlist 运行 Spectre 仿真."""
    sim_dir = OUTPUT_DIR / "sim"
    sim_dir.mkdir(exist_ok=True)

    # 复制 netlist 到 sim 目录 (避免修改原始导出)
    sim_netlist = sim_dir / "input.scs"
    shutil.copy2(netlist, sim_netlist)

    print(f"\n[Spectre] Running simulation...")
    t0 = time.time()
    sim = SpectreSimulator.local(
        spectre_cmd="/mnt/data/eda_tool/cadence/SPECTRE211/bin/spectre",
        timeout=600,
        work_dir=sim_dir,
    )
    result = sim.run_simulation(sim_netlist, {})
    elapsed = time.time() - t0

    print(f"  Status:  {result.status.value}")
    print(f"  Time:    {elapsed:.1f}s")
    if not result.ok:
        for e in result.errors[:5]:
            print(f"  ERROR:   {e}")
    else:
        print(f"  Output:  {result.metadata.get('output_dir')}")
    return result


def main():
    client = VirtuosoClient.from_env()
    client.test_connection(timeout=5)

    netlist = maestro_configure_and_export(client)

    if netlist:
        print(f"\nNetlist exported: {netlist}")
        print(f"Size:            {netlist.stat().st_size} bytes")

        # 可选: 运行 Spectre
        if "--run" in sys.argv:
            run_spectre(netlist)
    else:
        print("ERROR: No netlist exported.")


if __name__ == "__main__":
    main()
