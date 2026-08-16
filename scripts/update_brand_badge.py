import glob
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files_to_update = glob.glob(os.path.join(base_dir, 'blog', '*.html')) + [
    os.path.join(base_dir, 'version-b', 'index.html')
]

for fpath in files_to_update:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            txt = f.read()
        txt = txt.replace(
            '<span class="brand-tag-badge">AI Marketing Automation, CRM and Operations</span>',
            '<span class="brand-tag-badge">Digital Marketing | AI Marketing Automation, CRM and Operations</span>'
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(txt)
        print(f'Updated {fpath}')
