import re
from pathlib import Path

def test_no_trailing_slashes_or_index_html():
    base_dir = Path(__file__).resolve().parent.parent
    bad_trailing = []
    bad_index = []
    
    for f in base_dir.rglob("*.html"):
        if ".git" in f.parts or "node_modules" in f.parts:
            continue
        txt = f.read_text(encoding="utf-8")
        
        # Check trailing slashes in service and tool links
        for m in re.finditer(r'href="((?:/it)?/(?:services|tools)/[^"#\? ]+/)"', txt):
            bad_trailing.append((str(f.relative_to(base_dir)), m.group(1)))
            
        # Check index.html anchor links
        for m in re.finditer(r'<a\s+[^>]*href="([^"]*index\.html[^"]*)"', txt):
            href = m.group(1)
            # Ignore external URLs if any
            if not href.startswith("http"):
                bad_index.append((str(f.relative_to(base_dir)), href))

    print(f"Bad trailing service/tool links found: {len(bad_trailing)}")
    for file, link in bad_trailing:
        print(f"  [TRAILING SLASH] {file}: {link}")
        
    print(f"Bad legacy index.html links found: {len(bad_index)}")
    for file, link in bad_index:
        print(f"  [INDEX.HTML] {file}: {link}")

    assert len(bad_trailing) == 0, f"Found {len(bad_trailing)} trailing slash links"
    assert len(bad_index) == 0, f"Found {len(bad_index)} legacy index.html links"
    print("\n[ALL CLEAN] Zero trailing slashes and zero legacy index.html links across entire repository!")

if __name__ == "__main__":
    test_no_trailing_slashes_or_index_html()
