#!/usr/bin/env python3
"""
Automated SEO Sitemap & Robots Synchronizer
Run this script whenever new blog articles or pages are added to the portfolio:
    python scripts/update_seo.py
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PUBLIC_DIR = BASE_DIR / "public"
BLOG_DIR = BASE_DIR / "blog"

BASE_URL = "https://renzo-francesqui.vercel.app"
BRAND_TITLE = "Marketing Operations Specialist | CRM & RevOps Architect | Automation & AI Workflows"
PERSON_NAME = "Renzo Francesqui"

def generate_sitemap():
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
        '  ',
        '  <!-- Core Landing Pages -->',
        '  <url>',
        f'    <loc>{BASE_URL}/</loc>',
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}/" />',
        f'    <xhtml:link rel="alternate" hreflang="it" href="{BASE_URL}/it/" />',
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/" />',
        '    <changefreq>weekly</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>',
        '',
        '  <!-- Service Pages -->',
        '  <url>',
        f'    <loc>{BASE_URL}/services/hubspot-crm-optimization-startups</loc>',
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}/services/hubspot-crm-optimization-startups" />',
        f'    <xhtml:link rel="alternate" hreflang="it" href="{BASE_URL}/it/services/hubspot-crm-optimization-startups" />',
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/services/hubspot-crm-optimization-startups" />',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.9</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/services/paid-media-management</loc>',
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}/services/paid-media-management" />',
        f'    <xhtml:link rel="alternate" hreflang="it" href="{BASE_URL}/it/services/paid-media-management" />',
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/services/paid-media-management" />',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.9</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/services/seo-and-geo-optimization</loc>',
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}/services/seo-and-geo-optimization" />',
        f'    <xhtml:link rel="alternate" hreflang="it" href="{BASE_URL}/it/services/seo-and-geo-optimization" />',
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/services/seo-and-geo-optimization" />',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.9</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/services/marketing-data-reporting</loc>',
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}/services/marketing-data-reporting" />',
        f'    <xhtml:link rel="alternate" hreflang="it" href="{BASE_URL}/it/services/marketing-data-reporting" />',
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/services/marketing-data-reporting" />',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.9</priority>',
        '  </url>',
        '',
        '  <!-- Interactive Utility Tools -->',
        '  <url>',
        f'    <loc>{BASE_URL}/tools/mql-to-sql-sla-lead-leakage-calculator</loc>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.8</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/tools/b2b-campaign-utm-crm-builder</loc>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.8</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/tools/b2b-trade-show-roi-calculator</loc>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.8</priority>',
        '  </url>',
        '',
        '  <!-- Blog & Insights Articles -->',
        '  <url>',
        f'    <loc>{BASE_URL}/blog/hubspot-ai-enrichment-agent</loc>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.7</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/blog/b2b-event-lead-operations</loc>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.7</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/blog/modern-revops-lifecycle-architecture</loc>',
        '    <changefreq>monthly</changefreq>',
        '    <priority>0.7</priority>',
        '  </url>',
        '</urlset>'
    ]
    return '\n'.join(xml_lines) + '\n'

def generate_robots_txt():
    return f"""User-agent: *
Allow: /
Disallow: /version-1.5/
Disallow: /api/

# AI & Answer Engine Crawlers (Generative Engine Optimization)
User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""

def main():
    print(f"Synchronizing SEO configuration for: {BASE_URL}")
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Generate sitemap.xml
    sitemap_content = generate_sitemap()
    sitemap_root = BASE_DIR / "sitemap.xml"
    sitemap_public = PUBLIC_DIR / "sitemap.xml"
    with open(sitemap_root, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    with open(sitemap_public, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"[OK] Successfully updated {sitemap_root} and {sitemap_public}")

    # 2. Generate robots.txt
    robots_content = generate_robots_txt()
    robots_root = BASE_DIR / "robots.txt"
    robots_public = PUBLIC_DIR / "robots.txt"
    with open(robots_root, "w", encoding="utf-8") as f:
        f.write(robots_content)
    with open(robots_public, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"[OK] Successfully updated {robots_root} and {robots_public}")

    # Synchronize to it/ and version-3/it/
    for it_sub in [BASE_DIR / "it", BASE_DIR / "version-3" / "it"]:
        if it_sub.exists():
            with open(it_sub / "robots.txt", "w", encoding="utf-8") as f:
                f.write(robots_content)

    print("SEO synchronization complete.")

if __name__ == "__main__":
    main()
