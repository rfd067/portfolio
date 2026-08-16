import glob
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
old_id = 'G-DPYXTL3ZSN'
new_id = 'G-DPYXTL3ZSN'

# Find all HTML and python scripts
patterns = [
    os.path.join(base_dir, '*.html'),
    os.path.join(base_dir, 'blog', '*.html'),
    os.path.join(base_dir, 'classic', '*.html'),
    os.path.join(base_dir, 'version-b', '*.html'),
    os.path.join(base_dir, 'version-b', 'blog', '*.html'),
    os.path.join(base_dir, 'scripts', '*.py')
]

updated_count = 0
for pat in patterns:
    for fpath in glob.glob(pat):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_id in content:
            content = content.replace(old_id, new_id)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated: {fpath}')
            updated_count += 1

print(f'Total files updated with new Google Analytics ID ({new_id}): {updated_count}')
