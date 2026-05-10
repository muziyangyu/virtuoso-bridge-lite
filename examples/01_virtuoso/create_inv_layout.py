#!/usr/bin/env python3
"""Create layout for work_ai/inv inverter."""

from virtuoso_bridge import VirtuosoClient
from virtuoso_bridge.layout import LayerMap
from virtuoso_bridge.layout.editor import LayoutEditor
import sys


def create_inv_layout(client, lib_name: str = "work_ai", cell_name: str = "inv"):
    """Create inverter layout with standard-cell style."""

    print(f"Creating layout for {lib_name}/{cell_name}...")

    # Open or create layout view
    result = client.execute_skill(f'''
    let((cv lib cell)
      lib = ddGetObj("{lib_name}")
      when(!lib error("Library {lib_name} not found!"))

      cell = ddGetObj(lib "{cell_name}")
      when(!cell error("Cell {cell_name} not found!"))

      ; Open/create layout view
      cv = dbOpenCellViewByType(lib "{cell_name}" "layout" "a")
      when(!cv error("Cannot open layout view!"))

      ; Clear existing layout
      foreach(obj cv~>shapes
        dbDeleteObject(obj)
      foreach(obj cv~>instances
        dbDeleteObject(obj)
      foreach(obj cv~>vias
        dbDeleteObject(obj)

      printf("Layout view opened: %L\\n" cv)
      cv
    )
    ''')
    print(f"Open result: {result.output}")

    with LayoutEditor(client, lib_name, cell_name, "layout") as le:
        print("Creating inverter layout...")

        # Layer definitions (SMIC 12nm)
        l = LayerMap()
        l.add("NW", 1, 23)    # N-well
        l.add("DNW", 2, 23)       # Deep N-well
        l.add("AA", 3, 23)        # Active area
        l.add("FP", 4, 23)         # Field Poly
        l.add("GT", 5, 23)         # Gate
        l.add("SBLK", 6, 23)     # Source/Drain Block
        l.add("CTM", 7, 23)       # Contact Metal
        l.add("M1", 8, 23)          # Metal 1
        l.add("V1", 9, 23)         # Via 1
        l.add("M2", 10, 23)        # Metal 2
        l.add("M3", 11, 23)        # Metal 3
        l.add("TXT", 63, 23)       # Text
        l.add("PR", 64, 23)         # Pin/Label
        l.add("BBOX", 25, 23)      # Boundary

        # Dimensions
        track_height = 270  # Standard cell height 270nm
        cell_width = 1000  # Cell width

        # Create P-tube
        # ============
        #   VDD rail at top, VSS rail at bottom

        # 1. Create N-well for PMOS (covers top half of cell)
        le.create_rect(l.NW, [(0, track_height//2), (cell_width, track_height)])

        # 2. PMOS transistor (top)
        pmos_width = 200
        pmos_l = 30
        le.create_rect(l.AA, [(100, 150), (300, 210)])  # Active
        le.create_rect(l.GT, [(200, 140), (230, 220)])  # Gate

        # 3. NMOS transistor (bottom)
        nmos_width = 100
        le.create_rect(l.AA, [(100, 60), (200, 120)])  # Active
        le.create_rect(l.GT, [(200, 50), (230, 130)])   # Gate (extends between PMOS and NMOS)

        # 4. Power rails (M1)
        rail_height = 40
        le.create_rect(l.M1, [(0, track_height - rail_height), (cell_width, track_height)])  # VDD
        le.create_rect(l.M1, [(0, 0), (cell_width, rail_height)])  # VSS

        # 5. Create pins
        le.create_pin("VDD", l.PR, [(0, track_height - rail_height), (cell_width, track_height)], "inputOutput")
        le.create_pin("VSS", l.PR, [(0, 0), (cell_width, rail_height)], "inputOutput")
        le.create_pin("VIN", l.PR, [(450, 100), (500, 150)], "input")
        le.create_pin("VOUT", l.PR, [(600, 100), (650, 150)], "output")

        print("Layout created successfully!")


if __name__ == "__main__":
    client = VirtuosoClient.from_env()
    create_inv_layout(client)
