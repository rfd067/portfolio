#!/usr/bin/env python3
"""
Comprehensive Verification Suite for it/index.html (Italian Localized Edition).
Validates 3D Solar Matrix nodes, modals, dock buttons, technical SEO, Milan/Lombardy schema, and Calendly integration.
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IT_FILE = BASE_DIR / "it" / "index.html"

with open(IT_FILE, "r", encoding="utf-8") as f:
    c = f.read()

modals = re.findall(r'id="(modal[A-Za-z0-9]+)"', c)
dock_btns = re.findall(r'onclick="(?:focusOnPlanet|activateOrbNode)\(\'([^\']+)\'(?:,\s*true)?\)"', c)
nodes = re.findall(r"id:\s*'([^']+)',\s*(?:name|label):", c)

print("Modals found in it/index.html:", modals)
print("Dock buttons found in it/index.html:", dock_btns)
print("Nodes found in it/index.html:", nodes)

assert len(dock_btns) >= 7, f"Expected at least 7 dock buttons, got {len(dock_btns)}"
assert len(nodes) >= 7, f"Expected at least 7 celestial nodes, got {len(nodes)}"
assert dock_btns == nodes, "Dock buttons and canvas/planet nodes must match"

assert "modalServices" in modals, "Missing modalServices in it/index.html"
assert "modalTools" in modals, "Missing modalTools in it/index.html"
assert "modalExperience" in modals, "Missing modalExperience in it/index.html"
assert "modalProjects" in modals, "Missing modalProjects in it/index.html"
assert "modalContact" in modals, "Missing modalContact in it/index.html"

lang_btns = re.findall(r'class="lang-btn[^"]*"', c)
assert len(lang_btns) == 2, f"Expected 2 lang buttons, got {len(lang_btns)}"

assert '<html lang="it"' in c, "Missing <html lang=\"it\">"
assert 'https://renzo-francesqui.vercel.app/it/' in c, "Missing canonical URL"
assert 'hreflang="en"' in c, "Missing hreflang en"
assert 'hreflang="it"' in c, "Missing hreflang it"
assert 'hreflang="x-default"' in c, "Missing hreflang x-default"

assert 'Specialista' in c and 'Marketing Operations' in c, "Missing Italian Job Title"
assert 'Milano, Italy' in c and 'Lombardy' in c, "Missing Milan & Lombardy geographic schema"
assert 'https://calendly.com/renzo-francesqui' in c, "Missing Calendly URL"
assert 'Prenota una Call su Calendly' in c, "Missing Italian Calendly CTA button"
assert 'Motore di Attribuzione Algoritmica con Catene di Markov' in c, "Missing Italian translation for Markov Chain Attribution"

print("\n[OK] it/index.html is completely verified and valid!")
