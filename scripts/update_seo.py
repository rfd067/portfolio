#!/usr/bin/env python3
"""
Automated SEO Sitemap & Robots Synchronizer
Run this script whenever new blog articles or pages are added to the portfolio:
    python scripts/update_seo.py
"""

import os
import re
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BLOG_DIR = BASE_DIR / "blog"
CANONICAL_DOMAIN = "https://renzo-francesqui.vercel.app"

def get_articles_from_blog_dir():
    articles = []
    if not BLOG_DIR.exists():
        return articles

    for file_path in BLOG_DIR.glob("*.html"):
        if file_path.name == "index.html":
            continue
        
        slug = file_path.stem
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            title = title_match.group(1).split('|')[0].strip() if title_match else slug

            # Extract date if present
            date_match = re.search(r'content="(\d{4}-\d{2}-\d{2})', content)
            lastmod = date_match.group(1) if date_match else datetime.date.today().isoformat()

            articles.append({
                "slug": slug,
                "title": title,
                "file_name": file_path.name,
                "lastmod": lastmod,
                "priority": "0.85",
                "changefreq": "monthly"
            })
        except Exception as e:
            print(f"! Error reading {file_path}: {e}")

    # Sort articles by slug
    articles.sort(key=lambda x: x["slug"])
    return articles

def generate_sitemap(articles):
    today = datetime.date.today().isoformat()
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
        '  ',
        '  <!-- Primary Main Portfolio & Interactive AI Representative -->',
        '  <url>',
        f'    <loc>{CANONICAL_DOMAIN}/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>1.00</priority>',
        '  </url>',
        '',
        '  <!-- Dedicated Blog Hub -->',
        '  <url>',
        f'    <loc>{CANONICAL_DOMAIN}/blog/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.90</priority>',
        '  </url>',
        '',
        '  <!-- Version 1.5 (Categorized Skills & Mobile Optimized) -->',
        '  <url>',
        f'    <loc>{CANONICAL_DOMAIN}/version-1.5/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.95</priority>',
        '  </url>',
        '',
        '  <!-- Classic Version (Version A) -->',
        '  <url>',
        f'    <loc>{CANONICAL_DOMAIN}/classic/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.70</priority>',
        '  </url>',
        ''
    ]

    # Append all standalone blog posts
    for art in articles:
        xml_lines.extend([
            f'  <!-- Article: {art["title"]} -->',
            '  <url>',
            f'    <loc>{CANONICAL_DOMAIN}/blog/{art["file_name"]}</loc>',
            f'    <lastmod>{art["lastmod"]}</lastmod>',
            f'    <changefreq>{art["changefreq"]}</changefreq>',
            f'    <priority>{art["priority"]}</priority>',
            '  </url>',
            ''
        ])

    xml_lines.append('</urlset>')
    return '\n'.join(xml_lines)

def generate_robots_txt():
    return f"""User-agent: *
Allow: /

Sitemap: {CANONICAL_DOMAIN}/sitemap.xml
"""

def main():
    print(f"Synchronizing SEO configuration for: {CANONICAL_DOMAIN}")
    
    # 1. Discover all articles
    articles = get_articles_from_blog_dir()
    
    # 2. Write sitemap.xml
    sitemap_content = generate_sitemap(articles)
    sitemap_path = BASE_DIR / "sitemap.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"[OK] Successfully updated {sitemap_path} with {len(articles)} standalone blog posts.")

    # 3. Write robots.txt
    robots_content = generate_robots_txt()
    robots_path = BASE_DIR / "robots.txt"
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"[OK] Successfully updated {robots_path}")

    print("SEO synchronization complete.")

if __name__ == "__main__":
    main()
