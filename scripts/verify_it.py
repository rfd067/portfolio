#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IT_FILE = BASE_DIR / "it" / "index.html"

with open(IT_FILE, "r", encoding="utf-8") as f:
    c = f.read()

modals = re.findall(r'id="(modal[A-Za-z0-9]+)"', c)
dock_btns = re.findall(r'onclick="activateOrbNode\(\'([^\']+)\'\)"', c)
nodes = re.findall(r"id:\s*'([^']+)',\s*label:", c)

print("Modals found in it/index.html:", modals)
print("Dock buttons found in it/index.html:", dock_btns)
print("Nodes found in it/index.html:", nodes)

assert len(dock_btns) == 7, "Expected 7 dock buttons"
assert len(nodes) == 7, "Expected 7 canvas nodes"
assert dock_btns == nodes, "Dock buttons and canvas nodes must match"

lang_btns = re.findall(r'class="lang-btn[^"]*"', c)
assert len(lang_btns) == 2, f"Expected 2 lang buttons, got {len(lang_btns)}"

assert '<html lang="it"' in c
assert 'https://renzo-francesqui.vercel.app/it/' in c
assert 'hreflang="en"' in c
assert 'hreflang="it"' in c
assert 'hreflang="x-default"' in c
assert 'Specialista in Marketing Operations & RevOps' in c

print("\n[OK] it/index.html is completely verified and valid!")
