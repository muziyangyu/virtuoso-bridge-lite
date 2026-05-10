#!/usr/bin/env python3
"""Apply the optimal opamp parameters (GBW=2.77 GHz) to the schematic.

Optimal config (from 09_opamp_optimize_168n.py):
    All MOS: l=168n, nfin=6
    M1/M2: m=64  |  M3/M4: m=64  |  M5: m=128
    M6: m=10  |  M7: m=14
    Cc: 0.08p
    → GBW=2.77 GHz, PM=154.7°, Gain=53.6 dB, Power=3.71 mW

Saves to work_ai/opamp_two_stage.

Follows SKILL_QUICK_REFERENCE.md "正确方法 1":
    Parameter modification via execute_operations, NOT inside edit().
    Uses dbReplaceProp for direct instance attribute changes.
"""

from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)

from virtuoso_bridge import VirtuosoClient

LIB = "work_ai"
CELL = "opamp_two_stage"

# ── Optimal parameters ──
MOS_DEVICES = {
    "M1":  {"m": 64},
    "M2":  {"m": 64},
    "M3":  {"m": 64},
    "M4":  {"m": 64},
    "M5":  {"m": 128},
    "M6":  {"m": 10},
    "M7":  {"m": 14},
    "M8":  {"m": 1},
    "M9":  {"m": 1},
    "M10": {"m": 1},
}

# 0.08p = 8e-14 Farads
CC_VALUE = 8e-14


def build_mos_skill(name: str, m: int) -> str:
    """Build SKILL let-block to update one MOS device."""
    return (
        f'let((i) '
        f'i=car(setof(x cv~>instances x~>name=="{name}")) '
        f'when(i '
        f'  dbReplaceProp(i "nfin" "float" 6) '
        f'  dbReplaceProp(i "l" "float" 1.68e-7) '
        f'  dbReplaceProp(i "m" "float" {m})'
        f'))'
    )


def main() -> int:
    print("=" * 60)
    print("  Apply Optimal Opamp Parameters to Schematic")
    print("=" * 60)

    client = VirtuosoClient.from_env()
    r = client.execute_skill("1+2")
    print(f"\nConnected: {r.output}")

    # ═══════════════════════════════════════════════════
    # Method from SKILL_QUICK_REFERENCE.md "正确方法 1"
    # Standalone SKILL: open → modify → save → close
    # NEVER mix with edit() context
    # ═══════════════════════════════════════════════════

    # Build all SKILL commands
    commands: list[str] = []

    # 1) Open schematic for editing
    commands.append(
        f'cv = dbOpenCellViewByType("{LIB}" "{CELL}" "schematic" "schematic" "a")'
    )
    commands.append('unless(cv error("could not open schematic"))')

    # 2) Update MOS devices
    print("\nUpdating MOS devices:")
    for name, p in MOS_DEVICES.items():
        m_val = p["m"]
        print(f"  {name}: nfin=6, l=168n, m={m_val}", end=" -> ")
        commands.append(build_mos_skill(name, m_val))
        print("OK")

    # 3) Update compensation capacitor
    print(f"\nUpdating Cc: c=0.08p ({CC_VALUE} F)")
    commands.append(
        'let((i) i=car(setof(x cv~>instances x~>name=="Cc")) '
        f'when(i dbReplaceProp(i "c" "float" {CC_VALUE}))'
    )
    print("OK")

    # 4) Run schCheck, save, and close
    commands.append("schCheck(cv)")
    commands.append("dbSave(cv)")
    commands.append("dbClose(cv)")
    commands.append('"done"')

    # 5) Execute all at once
    print("\nExecuting SKILL commands...")
    r = client.execute_operations(commands, timeout=60)

    output = str(r.output).strip().strip('"')
    if r.errors:
        print(f"  Errors: {r.errors[:3]}")
        return 1
    if "done" in output or "t" in output:
        print(f"\n  Result: {output}")
    else:
        print(f"\n  Output: {output}")

    print("\n" + "=" * 60)
    print("  Done! Parameters saved to schematic.")
    print("  Run verify_opamp_params.py to confirm, then run simulation.")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
