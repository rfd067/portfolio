import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fpath = os.path.join(base_dir, 'version-1.5', 'index.html')

with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

ga_present = 'G-DPYXTL3ZSN' in content
modals = re.findall(r'id=["\'](modal\w+)["\']', content)
nodes = re.findall(r'id:\s*[\'"](\w+)[\'"]', content)
pills = re.findall(r'activateOrbNode\([\'"](\w+)[\'"]\)', content)

print('=== VERSION 1.5 VERIFICATION ===')
print('GA Tag Present:', ga_present)
print('Modals Detected:', modals)
print('Orbit Nodes in Canvas:', nodes)
print('Dock Menu Buttons:', pills)
print('File size:', len(content), 'bytes')

# Verify matching
for p in pills:
    assert p in nodes, f"Pill {p} not in nodes!"
print('[OK] All 7 dock pill buttons match 3D orbit nodes perfectly!')
