import glob
import re
import os
import sys

# Ensure UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

html_files = [
    'index.html',
    'blog/index.html',
    'blog/hubspot-ai-enrichment-agent.html',
    'blog/b2b-event-lead-operations.html',
    'blog/modern-revops-lifecycle-architecture.html'
]

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('=== VALIDATING PORTFOLIO & BLOG SEO & ASSETS ===')

all_good = True
for hf in html_files:
    full_path = os.path.join(base_dir, hf)
    if not os.path.exists(full_path):
        print(f'[FAIL] Missing file: {hf}')
        all_good = False
        continue
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else 'MISSING TITLE'
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    desc = desc_match.group(1) if desc_match else 'MISSING DESCRIPTION'
    canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    canonical = canonical_match.group(1) if canonical_match else 'MISSING CANONICAL'
    ga_present = 'G-DPYXTL3ZSN' in content
    h1_count = len(re.findall(r'<h1[^>]*>', content, re.IGNORECASE))
    h2_count = len(re.findall(r'<h2[^>]*>', content, re.IGNORECASE))
    json_ld_present = 'application/ld+json' in content

    print(f'\nFile: {hf}')
    print(f'   Title: {title}')
    print(f'   Desc ({len(desc)} chars): {desc[:75]}...')
    print(f'   Canonical: {canonical}')
    print(f'   GA Tag: {"[OK] Present" if ga_present else "[FAIL] Missing"}')
    print(f'   H1 Count: {h1_count} ({"[OK] Single H1" if h1_count == 1 else "[FAIL] Check H1"})')
    print(f'   H2 Count: {h2_count}')
    print(f'   Schema.org JSON-LD: {"[OK] Present" if json_ld_present else "[FAIL] Missing"}')

print('\n=== ASSET VERIFICATION ===')
photo_path = os.path.join(base_dir, 'images', 'renzo-francesqui.jpg')
cv_path = os.path.join(base_dir, 'RenzoFrancesquiCV2026.pdf')
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
robots_path = os.path.join(base_dir, 'robots.txt')
vercel_path = os.path.join(base_dir, 'vercel.json')

print(f'Photo exists: {os.path.exists(photo_path)} ({os.path.getsize(photo_path)} bytes)')
print(f'CV PDF exists: {os.path.exists(cv_path)} ({os.path.getsize(cv_path)} bytes)')
print(f'sitemap.xml exists: {os.path.exists(sitemap_path)}')
print(f'robots.txt exists: {os.path.exists(robots_path)}')
print(f'vercel.json exists: {os.path.exists(vercel_path)}')
print('\nALL CHECKS FINISHED!')
