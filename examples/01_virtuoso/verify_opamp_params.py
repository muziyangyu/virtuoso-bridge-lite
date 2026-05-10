#!/usr/bin/env python3
"""Verify that schematic parameters were updated by reading them back from Virtuoso."""

from __future__ import annotations
import math
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.virtuoso.schematic.reader import read_schematic

LIB = "work_ai"
CELL = "opamp_two_stage"

# Expected optimal values
EXPECTED_MOS = {
    "M1":  {"nfin": 6, "l": "168n", "m": 64},
    "M2":  {"nfin": 6, "l": "168n", "m": 64},
    "M3":  {"nfin": 6, "l": "168n", "m": 64},
    "M4":  {"nfin": 6, "l": "168n", "m": 64},
    "M5":  {"nfin": 6, "l": "168n", "m": 128},
    "M6":  {"nfin": 6, "l": "168n", "m": 10},
    "M7":  {"nfin": 6, "l": "168n", "m": 14},
    "M8":  {"nfin": 6, "l": "168n", "m": 1},
    "M9":  {"nfin": 6, "l": "168n", "m": 1},
    "M10": {"nfin": 6, "l": "168n", "m": 1},
}
EXPECTED_CC = "0.08p"


def parse_sci_num(val, default_unit: str = "") -> float:
    """Convert SKILL value string to float in base units (meters, farads, etc.).

    Handles: '168n' -> 168e-9, '0.3p' -> 0.3e-12, '300f' -> 300e-15
    For suffixless values like '0.168', uses default_unit: 'u' (microns) for length,
    '' for bare numbers.
    """
    if val is None:
        return 0.0
    val = str(val)
    suffixes = {"f": 1e-15, "p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3, "k": 1e3, "M": 1e6, "G": 1e9}
    for s, mult in suffixes.items():
        if val.endswith(s):
            return float(val[:-1]) * mult
    # No suffix: apply default unit
    if default_unit in suffixes:
        return float(val) * suffixes[default_unit]
    return float(val)


def main() -> int:
    print("=" * 60)
    print("  Verify Schematic Parameters from Virtuoso")
    print("=" * 60)

    client = VirtuosoClient.from_env()
    r = client.execute_skill("1+2")
    print(f"\nConnected: {r.output}")

    print(f"\nReading {LIB}/{CELL} schematic...")
    data = read_schematic(client, LIB, CELL)

    instances = {inst["name"]: inst for inst in data["instances"]}

    all_pass = True

    # ── Check MOS devices ──
    print("\n── MOS Devices ──")
    hdr = f"  {'Name':<5s}  {'nfin':>5s}  {'l':>8s}  {'m':>5s}  {'Status':<6s}"
    sep = f"  {'-'*5}  {'-'*5}  {'-'*8}  {'-'*5}  {'-'*6}"
    print(hdr)
    print(sep)

    for name, exp in EXPECTED_MOS.items():
        inst = instances.get(name)
        if not inst:
            print(f"  {name:<5s}  {'?':>5s}  {'?':>8s}  {'?':>5s}  {'MISSING':<6s}")
            all_pass = False
            continue

        params = inst.get("params", {})
        nfin = params.get("nfin")
        l_val = params.get("l")
        m_val = params.get("m")

        nfin_ok = int(nfin) == exp["nfin"] if nfin else False
        # Virtuoso stores l in microns (0.168 um = 168 nm), so use 'u' as default
        l_actual = parse_sci_num(l_val) if l_val else 0
        l_expected = parse_sci_num(exp["l"])
        # Use relative tolerance for float comparison
        l_ok = math.isclose(l_actual, l_expected, rel_tol=1e-9) if l_val else False
        m_ok = int(m_val) == exp["m"] if m_val else False

        status = "OK" if (nfin_ok and l_ok and m_ok) else "FAIL"
        if status == "FAIL":
            all_pass = False

        detail = ""
        if status == "FAIL":
            reasons = []
            if not nfin_ok: reasons.append(f"nfin={nfin}")
            if not l_ok: reasons.append(f"l={l_val}(parsed={l_actual})")
            if not m_ok: reasons.append(f"m={m_val}")
            detail = f"  (expect nfin={exp['nfin']} l={exp['l']} m={exp['m']}, got {'; '.join(reasons)})"

        print(f"  {name:<5s}  {str(nfin) if nfin else '?':>5s}  {l_val if l_val else '?':>8s}  "
              f"{str(m_val) if m_val else '?':>5s}  {status:<6s}{detail}")

    # ── Check Cc ──
    print("\n── Capacitors ──")
    cc_inst = instances.get("Cc")
    if cc_inst:
        c_val = cc_inst.get("params", {}).get("c")
        c_ok = math.isclose(parse_sci_num(c_val), parse_sci_num(EXPECTED_CC), rel_tol=1e-9) if c_val else False
        status = "OK" if c_ok else "FAIL"
        if not c_ok:
            all_pass = False
        print(f"  Cc: {c_val if c_val else '?'}  {status}"
              + (f"  (expect {EXPECTED_CC})" if status == "FAIL" else ""))
    else:
        print("  Cc: MISSING")
        all_pass = False

    # ── Summary ──
    print("\n" + "=" * 60)
    if all_pass:
        print("  PASS: All parameters match expected optimal values!")
    else:
        print("  FAIL: Some parameters do not match. Check above.")
    print("=" * 60)

    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
