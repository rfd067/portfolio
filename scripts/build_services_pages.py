#!/usr/bin/env python3
"""
Build SpaceX Starshield Freelance Service Pages (EN & IT).
Rebuilds the 4 standalone B2B Service Pages linked from #modalServices:
1. /services/hubspot-crm-optimization-startups/index.html (and alias /services/small-startup-business-crm-setup-optimization/)
2. /services/paid-media-management/index.html
3. /services/seo-and-geo-optimization/index.html
4. /services/marketing-data-reporting/index.html

Strict SpaceX Starshield Design Laws:
- ZERO EMOJIS: Pure numeric codes (01, 02, 03, 04) and 1px SVG crosshairs/vectors.
- ZERO ROUNDED BUBBLES: All border-radius: 0px and exposed 1px solid rgba(255, 255, 255, 0.2) grid lines.
- STARK HIGH-CONTRAST PALETTE: Pure #000000 background, #FFFFFF headlines, #9499A1 muted copy, #d4a863 metallic gold telemetry.
- SIGNATURE SPACEX SLIDING-FILL BUTTONS: Rectangular 1px solid #FFFFFF with sliding bottom-to-top white fill.
- ORBITAL HORIZON / CAD WIREFRAME BACKGROUND: Fixed HTML5 canvas glowing planetary horizon limb arc + rotating CAD wireframe schematic (opacity 0.15) + starfield parallax.
- CALENDLY URL: http://calendly.com/renzo-francesqui
- Full SEO metadata, canonicals, bidirectional hreflang, Open Graph, Twitter Cards, Schema.org JSON-LD.
"""

from pathlib import Path
import json
import urllib.parse

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. MANDATORY SPACEX STARSHIELD MASTER CSS
SPACEX_MASTER_CSS = """@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root {
    --bg-black: #000000;
    --bg-panel: rgba(8, 8, 10, 0.82);
    --text-white: #FFFFFF;
    --text-Silver: #A7AEB8;
    --text-dim: #5E6570;
    --accent-gold: #D4A863;
    --line-faint: rgba(255, 255, 255, 0.16);
    --line-bright: rgba(255, 255, 255, 0.45);
    
    --font-display: 'Barlow Condensed', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', 'SF Mono', Consolas, Monaco, monospace;
    --ease-spacex: cubic-bezier(0.19, 1, 0.22, 1);
}

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    border-radius: 0 !important;
}

html {
    background-color: var(--bg-black);
    color: var(--text-white);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-black);
    overflow-x: hidden;
    line-height: 1.6;
}

main {
    position: relative;
    z-index: 1;
}

/* Fixed Deep-Space Aerospace Backdrop */
.sx-fixed-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
}

.sx-fixed-backdrop-img {
    position: absolute;
    top: -12%;
    right: -5%;
    width: 110%;
    height: 124%;
    background-size: cover;
    background-position: center right;
    background-repeat: no-repeat;
    opacity: 0.38;
    will-change: transform;
    filter: saturate(1.1) brightness(0.95);
}

.sx-fixed-backdrop-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 65% 50%, rgba(0, 0, 0, 0.15) 0%, rgba(0, 0, 0, 0.82) 70%, #000000 100%);
}

/* Fixed Orbital Horizon & Telemetry Canvas */
#starshieldCanvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
    pointer-events: none;
}

/* Fixed Left Scroll Progress Telemetry Rail */
.telemetry-rail {
    position: fixed;
    left: 2rem;
    top: 50%;
    transform: translateY(-50%);
    height: 220px;
    width: 1px;
    background: var(--line-faint);
    z-index: 50;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.telemetry-rail-fill {
    position: absolute;
    top: 0;
    left: 0;
    width: 1px;
    height: 0%;
    background: var(--text-white);
    box-shadow: 0 0 10px var(--text-white);
}

.telemetry-readout {
    position: fixed;
    left: 2.75rem;
    bottom: 2rem;
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-dim);
    text-transform: uppercase;
    z-index: 50;
    pointer-events: none;
}

/* Top SpaceX Navigation Bar */
.sx-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 80px;
    z-index: 100;
    background: rgba(0, 0, 0, 0.88);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--line-faint);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 4rem;
    transition: background 0.3s ease;
}

.sx-brand {
    font-family: var(--font-display);
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--text-white);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.sx-brand span.sub {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: var(--accent-gold);
    border-left: 1px solid var(--line-bright);
    padding-left: 1rem;
}

.sx-nav {
    display: flex;
    align-items: center;
    gap: 2.25rem;
}

.sx-nav-link {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-Silver);
    text-decoration: none;
    position: relative;
    padding: 0.4rem 0;
    transition: color 0.3s;
}

.sx-nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    width: 0%;
    height: 1px;
    background: var(--text-white);
    transition: width 0.35s var(--ease-spacex);
}

.sx-nav-link:hover,
.sx-nav-link.active {
    color: var(--text-white);
}

.sx-nav-link:hover::after,
.sx-nav-link.active::after {
    left: 0;
    right: auto;
    width: 100%;
}

/* Sharp SpaceX Language Switcher */
.sx-lang-switcher {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    border: 1px solid var(--line-faint);
    padding: 0.35rem 0.65rem;
    margin-left: 0.5rem;
}

.sx-lang-divider {
    color: var(--text-dim);
}

.sx-lang-btn {
    color: var(--text-Silver);
    text-decoration: none;
    transition: color 0.25s;
}

.sx-lang-btn:hover,
.sx-lang-btn.active {
    color: var(--text-white);
    font-weight: 700;
}

.sx-lang-btn.active {
    color: var(--accent-gold);
}

/* Signature SpaceX Sliding-Fill Button */
.sx-btn {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 1rem 2.4rem;
    border: 1px solid var(--text-white);
    background: transparent;
    color: var(--text-white);
    font-family: var(--font-mono);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    text-decoration: none;
    overflow: hidden;
    cursor: pointer;
    transition: color 0.4s var(--ease-spacex);
}

.sx-btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--text-white);
    transform: scaleY(0);
    transform-origin: bottom center;
    transition: transform 0.4s var(--ease-spacex);
    z-index: 0;
}

.sx-btn:hover {
    color: var(--bg-black);
}

.sx-btn:hover::before {
    transform: scaleY(1);
    transform-origin: top center;
}

.sx-btn span {
    position: relative;
    z-index: 1;
}

.sx-btn-subtle {
    border-color: var(--line-bright);
    color: var(--text-Silver);
}

.sx-btn-gold {
    border-color: var(--accent-gold);
    color: var(--accent-gold);
}
.sx-btn-gold::before {
    background: var(--accent-gold);
}
.sx-btn-gold:hover {
    color: var(--bg-black);
}

/* Page Sections */
main {
    position: relative;
    z-index: 10;
}

.sx-container {
    max-width: 1320px;
    margin: 0 auto;
    padding: 0 5rem;
    width: 100%;
}

/* SECTION 1: 100VH STARSHIELD HERO */
.sx-hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-top: 100px;
    padding-bottom: 6rem;
    position: relative;
    border-bottom: 1px solid var(--line-faint);
    overflow: hidden;
    background-color: var(--bg-black);
}

.sx-hero-backdrop {
    position: absolute;
    inset: 0;
    z-index: 1;
    overflow: hidden;
    pointer-events: none;
}

.sx-hero-img {
    position: absolute;
    top: -12%;
    right: 0;
    width: 100%;
    height: 124%;
    object-fit: cover;
    object-position: center right;
    will-change: transform;
    filter: saturate(1.15) contrast(1.08);
}

.sx-hero-overlay {
    position: absolute;
    inset: 0;
    background: 
        linear-gradient(180deg, rgba(0, 0, 0, 0.95) 0%, rgba(0, 0, 0, 0.45) 16%, rgba(0, 0, 0, 0) 32%),
        linear-gradient(0deg, #000000 0%, rgba(0, 0, 0, 0.9) 14%, rgba(0, 0, 0, 0.3) 30%, rgba(0, 0, 0, 0) 50%),
        linear-gradient(90deg, #000000 0%, rgba(0, 0, 0, 0.94) 35%, rgba(0, 0, 0, 0.72) 52%, rgba(0, 0, 0, 0.15) 75%, rgba(0, 0, 0, 0) 100%),
        radial-gradient(ellipse at 85% 45%, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.25) 60%, rgba(0, 0, 0, 0.8) 100%);
}

.sx-hero .sx-container {
    position: relative;
    z-index: 4;
}

.sx-eyebrow {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-bottom: 1.25rem;
    display: block;
}

.sx-hero-title {
    font-family: var(--font-display);
    font-size: clamp(2.8rem, 6.2vw, 5.8rem);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    line-height: 0.98;
    margin-bottom: 1.75rem;
    max-width: 800px;
}

.sx-hero-lead {
    font-size: 1.05rem;
    color: var(--text-Silver);
    max-width: 720px;
    font-weight: 300;
    margin-bottom: 2.75rem;
    line-height: 1.75;
}

.sx-hero-actions {
    display: flex;
    gap: 1.25rem;
    flex-wrap: wrap;
    align-items: center;
}

/* Scroll Down Indicator */
.sx-scroll-cue {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 30px;
    opacity: 0.6;
    animation: bounceDown 2s infinite;
}

@keyframes bounceDown {
    0%, 100% { transform: translate(-50%, 0); opacity: 0.3; }
    50% { transform: translate(-50%, 8px); opacity: 0.9; }
}

/* SECTION 2: OVERSIZED TELEMETRY COUNTERS (SPACEX STATS BAR) */
.sx-stats-section {
    border-bottom: 1px solid var(--line-faint);
    background: rgba(4, 4, 6, 0.88);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    position: relative;
    z-index: 2;
}

.sx-stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    max-width: 1320px;
    margin: 0 auto;
}

.sx-stat-cell {
    padding: 4.5rem 3rem;
    text-align: center;
    border-right: 1px solid var(--line-faint);
}

.sx-stat-cell:last-child {
    border-right: none;
}

.sx-stat-number {
    font-family: var(--font-display);
    font-size: clamp(3rem, 5.5vw, 5.2rem);
    font-weight: 600;
    line-height: 1;
    letter-spacing: 0.02em;
    color: var(--text-white);
    margin-bottom: 0.75rem;
}

.sx-stat-label {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-Silver);
}

/* SECTION 3: STARSHIELD 3-PILLAR ARCHITECTURAL GRID */
.sx-pillars-section {
    padding: 8rem 0;
    border-bottom: 1px solid var(--line-faint);
    position: relative;
    z-index: 2;
    background: rgba(0, 0, 0, 0.72);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

.sx-section-header {
    margin-bottom: 4rem;
}

.sx-section-title {
    font-family: var(--font-display);
    font-size: clamp(2.2rem, 4.5vw, 3.6rem);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    line-height: 1.05;
}

.sx-pillars-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border: 1px solid var(--line-faint);
    background: var(--bg-panel);
}

.sx-pillar-card {
    padding: 3.5rem 2.75rem;
    border-right: 1px solid var(--line-faint);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 420px;
    position: relative;
    transition: background 0.4s;
}

.sx-pillar-card:last-child {
    border-right: none;
}

.sx-pillar-card:hover {
    background: rgba(255, 255, 255, 0.03);
}

.sx-pillar-num {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    color: var(--accent-gold);
    margin-bottom: 2rem;
    display: block;
}

.sx-pillar-title {
    font-family: var(--font-display);
    font-size: 1.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 1.25rem;
    color: var(--text-white);
}

.sx-pillar-desc {
    font-size: 0.92rem;
    color: var(--text-Silver);
    line-height: 1.7;
}

.sx-pillar-foot {
    margin-top: 2.5rem;
    padding-top: 1.25rem;
    border-top: 1px solid var(--line-faint);
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-dim);
}

/* SECTION 4: FALCON-9 STYLE TECHNICAL SPECIFICATION TABLE + CAD SCHEMATIC */
.sx-specs-section {
    padding: 8rem 0;
    border-bottom: 1px solid var(--line-faint);
    position: relative;
    z-index: 2;
    background: rgba(2, 2, 5, 0.84);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.sx-specs-layout {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 5rem;
    align-items: center;
}

.sx-spec-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 2rem;
}

.sx-spec-table tr {
    border-bottom: 1px solid var(--line-faint);
}

.sx-spec-table td {
    padding: 1.35rem 0;
    font-size: 0.85rem;
}

.sx-spec-table td:first-child {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-Silver);
}

.sx-spec-table td:last-child {
    font-family: var(--font-mono);
    font-weight: 600;
    color: var(--text-white);
    text-align: right;
}

.sx-spec-table td span.gold {
    color: var(--accent-gold);
}

/* Architectural Wireframe Box (Right Column) */
.sx-wireframe-box {
    border: 1px solid var(--line-faint);
    background: rgba(5, 5, 7, 0.9);
    aspect-ratio: 1 / 1;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2.5rem;
}

.sx-wireframe-box::before,
.sx-wireframe-box::after {
    content: '+';
    position: absolute;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--text-dim);
}
.sx-wireframe-box::before { top: 12px; left: 14px; }
.sx-wireframe-box::after { bottom: 12px; right: 14px; }

.sx-wireframe-label {
    position: absolute;
    top: 16px;
    right: 18px;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.16em;
    color: var(--accent-gold);
}

/* SECTION 5: 4-STAGE LAUNCH SEQUENCE + PROVEN FLIGHT HERITAGE */
.sx-sequence-section {
    padding: 8rem 0;
    border-bottom: 1px solid var(--line-faint);
    position: relative;
    z-index: 2;
    background: rgba(0, 0, 0, 0.72);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

.sx-sequence-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-top: 1px solid var(--line-bright);
    margin-top: 3rem;
}

.sx-seq-step {
    padding: 2.5rem 2rem 0 0;
    position: relative;
}

.sx-seq-step::before {
    content: '';
    position: absolute;
    top: -5px;
    left: 0;
    width: 9px;
    height: 9px;
    background: var(--bg-black);
    border: 2px solid var(--text-white);
}

.sx-seq-step:hover::before {
    background: var(--accent-gold);
    border-color: var(--accent-gold);
    box-shadow: 0 0 12px var(--accent-gold);
}

.sx-seq-code {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    color: var(--accent-gold);
    margin-bottom: 0.75rem;
}

.sx-seq-title {
    font-family: var(--font-display);
    font-size: 1.45rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.75rem;
}

.sx-seq-text {
    font-size: 0.86rem;
    color: var(--text-Silver);
    line-height: 1.65;
}

/* Flight Heritage Callout Bar with subtle aerospace backdrop */
.sx-heritage-bar {
    margin-top: 5rem;
    border: 1px solid var(--line-bright);
    border-left: 3px solid var(--accent-gold);
    padding: 2.75rem 3.25rem;
    background-color: var(--bg-panel);
    background-image: 
        linear-gradient(90deg, rgba(6, 6, 9, 0.96) 0%, rgba(6, 6, 9, 0.90) 55%, rgba(6, 6, 9, 0.75) 100%),
        var(--heritage-bg, none);
    background-size: cover;
    background-position: center right;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 3rem;
    position: relative;
    overflow: hidden;
}

.sx-heritage-bar .sx-btn-gold {
    background: rgba(0, 0, 0, 0.82);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

/* SECTION 6: SPACEX STARSHIELD VERTICAL-LINE FOOTER */
.sx-footer {
    padding: 7rem 2rem 5rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 2;
    background: linear-gradient(180deg, rgba(0, 0, 0, 0.7) 0%, #000000 100%);
}

.sx-vertical-line {
    width: 1px;
    height: 90px;
    background: linear-gradient(180deg, transparent, var(--text-white));
    margin-bottom: 2.5rem;
}

.sx-footer-title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 4vw, 3.2rem);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 1rem;
}

.sx-footer-sub {
    font-size: 0.92rem;
    color: var(--text-Silver);
    max-width: 580px;
    margin-bottom: 2.5rem;
}

.sx-copyright {
    margin-top: 5rem;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    color: var(--text-dim);
    text-transform: uppercase;
}

/* Robust Progressive Scroll Reveal Utility (Content is always fully visible by default) */
.reveal-up {
    opacity: 1;
    transform: none;
    transition: opacity 0.6s var(--ease-spacex), transform 0.6s var(--ease-spacex);
}

.js-ready .reveal-up.visible {
    opacity: 1;
    transform: none;
}

@media (max-width: 960px) {
    .sx-header { padding: 0 1.5rem; }
    .sx-nav { display: none; }
    .sx-container { padding: 0 1.75rem; }
    .telemetry-rail, .telemetry-readout { display: none; }
    .sx-stats-grid, .sx-pillars-grid, .sx-specs-layout, .sx-sequence-grid {
        grid-template-columns: 1fr;
    }
    .sx-stat-cell, .sx-pillar-card {
        border-right: none;
        border-bottom: 1px solid var(--line-faint);
        min-height: auto;
    }
    .sx-heritage-bar { flex-direction: column; align-items: flex-start; padding: 2rem 1.5rem; }
    .sx-hero { padding-top: 110px; padding-bottom: 4rem; }
    .sx-hero-title { max-width: 100%; font-size: clamp(2.4rem, 8.5vw, 3.8rem); }
    .sx-hero-img { 
        object-position: center center; 
        opacity: 0.74; 
        top: -5%; 
        height: 110%; 
    }
    .sx-hero-overlay {
        background: 
            linear-gradient(180deg, rgba(0, 0, 0, 0.88) 0%, rgba(0, 0, 0, 0.45) 45%, rgba(0, 0, 0, 0.92) 100%),
            linear-gradient(90deg, rgba(0, 0, 0, 0.85) 0%, rgba(0, 0, 0, 0.5) 100%);
    }
}
"""

# 2. GLOBAL BACKGROUND CANVAS & SCROLL TELEMETRY SCRIPT
# Pure clean JS string without f-string backslash mangling
SPACEX_MASTER_JS = """document.addEventListener('DOMContentLoaded', function() {
    document.body.classList.add('js-ready');
    const canvas = document.getElementById('starshieldCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let w, h, scrollY = window.scrollY;

    const stars = Array.from({ length: 180 }, function() {
        return {
            x: Math.random(),
            y: Math.random(),
            r: Math.random() * 1.2 + 0.3,
            a: Math.random() * 0.65 + 0.15
        };
    });

    function resize() {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    function render(time) {
        ctx.clearRect(0, 0, w, h);

        // Subtle deep-space stars with smooth twinkling
        stars.forEach(function(s) {
            const py = ((s.y * h - scrollY * 0.1) % h + h) % h;
            const px = s.x * w;
            const alpha = s.a * (0.8 + 0.2 * Math.sin((time || 0) * 0.002 + s.x * 12));
            ctx.fillStyle = 'rgba(255, 255, 255, ' + alpha.toFixed(2) + ')';
            ctx.beginPath();
            ctx.arc(px, py, s.r, 0, Math.PI * 2);
            ctx.fill();
        });

        requestAnimationFrame(render);
    }
    requestAnimationFrame(render);

    // Scroll Telemetry & High-Performance Parallax Observer
    const railFill = document.querySelector('.telemetry-rail-fill');
    const readout = document.querySelector('.telemetry-readout');
    const heroImg = document.querySelector('.sx-hero-img');
    const fixedBgImg = document.querySelector('.sx-fixed-backdrop-img');

    let ticking = false;
    window.addEventListener('scroll', function() {
        scrollY = window.scrollY;
        if (!ticking) {
            window.requestAnimationFrame(function() {
                const maxScroll = Math.max(1, document.body.scrollHeight - window.innerHeight);
                const pct = Math.min(100, Math.round((scrollY / maxScroll) * 100));
                if (railFill) railFill.style.height = pct + '%';
                if (readout) {
                    readout.textContent = 'ORBITAL TELEMETRY // ALT: ' + (pct * 4.2).toFixed(1) + ' KM // TRAJECTORY: NOMINAL';
                    readout.style.opacity = Math.max(0, 1 - (scrollY / 450));
                }
                if (heroImg && scrollY < window.innerHeight * 1.5) {
                    heroImg.style.transform = 'translate3d(0, ' + (scrollY * 0.16).toFixed(1) + 'px, 0)';
                }
                if (fixedBgImg) {
                    fixedBgImg.style.transform = 'translate3d(0, ' + (-scrollY * 0.05).toFixed(1) + 'px, 0)';
                }
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
            if (e.isIntersecting) e.target.classList.add('visible');
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-up').forEach(function(el) {
        observer.observe(el);
    });

    // Protocol fallback for file:// protocol so local file browsing works without web server
    if (window.location.protocol === 'file:') {
        const isCurrentIt = document.documentElement.lang === 'it' || window.location.pathname.toLowerCase().indexOf('/it/') !== -1;
        const cleanPath = window.location.pathname.replace(/\\\\/g, '/');
        const parts = cleanPath.split('/');
        const sIdx = parts.indexOf('services');
        const sSlug = (sIdx !== -1 && parts[sIdx + 1]) ? parts[sIdx + 1] : '';

        document.querySelectorAll('.sx-lang-switcher .sx-lang-btn').forEach(function(btn) {
            const isItBtn = btn.textContent.trim().toUpperCase() === 'IT';
            if (isItBtn) {
                btn.href = isCurrentIt ? 'index.html' : ('../../it/services/' + sSlug + '/index.html');
            } else {
                btn.href = isCurrentIt ? ('../../../services/' + sSlug + '/index.html') : 'index.html';
            }
        });

        document.querySelectorAll('.sx-nav .sx-nav-link').forEach(function(link) {
            const href = link.getAttribute('href');
            if (href && href.startsWith('/')) {
                const cleanHref = href.endsWith('/') ? href.slice(0, -1) : href;
                const targetSlug = cleanHref.split('/').pop();
                link.href = '../' + targetSlug + '/index.html';
            }
        });

        document.querySelectorAll('a[href^="/"]').forEach(function(link) {
            const href = link.getAttribute('href');
            if (href === '/' || href === '/index.html') {
                link.href = isCurrentIt ? '../../../index.html' : '../../index.html';
            } else if (href === '/it/' || href === '/it/index.html') {
                link.href = isCurrentIt ? '../../index.html' : '../../it/index.html';
            }
        });

        document.addEventListener('click', function(e) {
            const a = e.target.closest('a');
            if (!a) return;
            const href = a.getAttribute('href');
            if (href && href.startsWith('/')) {
                e.preventDefault();
                if (href === '/' || href === '/index.html') {
                    window.location.href = isCurrentIt ? '../../../index.html' : '../../index.html';
                } else if (href === '/it/' || href === '/it/index.html') {
                    window.location.href = isCurrentIt ? '../../index.html' : '../../it/index.html';
                } else if (href.startsWith('/services/') || href.startsWith('/it/services/')) {
                    const cleanHref = href.endsWith('/') ? href.slice(0, -1) : href;
                    const targetSlug = cleanHref.split('/').pop();
                    const isItTarget = href.startsWith('/it/services/');
                    if (isCurrentIt) {
                        window.location.href = isItTarget ? ('../' + targetSlug + '/index.html') : ('../../../services/' + targetSlug + '/index.html');
                    } else {
                        window.location.href = isItTarget ? ('../../it/services/' + targetSlug + '/index.html') : ('../' + targetSlug + '/index.html');
                    }
                }
            }
        }, true);
    }
});"""

# 3. 1PX SVG CAD SCHEMATICS FOR EACH SECTOR
CAD_SCHEMATICS = {
    "crm": """<svg width="100%" height="100%" viewBox="0 0 460 460" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Concentric Orbital Telemetry Rings -->
    <circle cx="230" cy="230" r="190" stroke="rgba(255,255,255,0.12)" stroke-width="1" stroke-dasharray="3 3"/>
    <circle cx="230" cy="230" r="140" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
    <circle cx="230" cy="230" r="85" stroke="rgba(212,168,99,0.3)" stroke-width="1" stroke-dasharray="4 2"/>
    <circle cx="230" cy="230" r="28" stroke="#FFFFFF" stroke-width="1"/>
    <circle cx="230" cy="230" r="4" fill="#D4A863"/>

    <!-- Central Crosshairs -->
    <line x1="230" y1="20" x2="230" y2="440" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <line x1="20" y1="230" x2="440" y2="230" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>

    <!-- Node 1: INGEST (Top) -->
    <rect x="180" y="70" width="100" height="34" fill="#050507" stroke="#FFFFFF" stroke-width="1"/>
    <text x="230" y="91" font-family="'JetBrains Mono', monospace" font-size="9" fill="#FFFFFF" font-weight="700" letter-spacing="0.1em" text-anchor="middle">01 // INGEST</text>

    <!-- Node 2: SCORE (Right) -->
    <rect x="320" y="213" width="100" height="34" fill="#050507" stroke="#D4A863" stroke-width="1"/>
    <text x="370" y="234" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D4A863" font-weight="700" letter-spacing="0.1em" text-anchor="middle">02 // SCORE</text>

    <!-- Node 3: ROUTE (Bottom) -->
    <rect x="180" y="356" width="100" height="34" fill="#050507" stroke="#FFFFFF" stroke-width="1"/>
    <text x="230" y="377" font-family="'JetBrains Mono', monospace" font-size="9" fill="#FFFFFF" font-weight="700" letter-spacing="0.1em" text-anchor="middle">03 // ROUTE</text>

    <!-- Node 4: DEAL (Left) -->
    <rect x="40" y="213" width="100" height="34" fill="#050507" stroke="#D4A863" stroke-width="1"/>
    <text x="90" y="234" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D4A863" font-weight="700" letter-spacing="0.1em" text-anchor="middle">04 // DEAL</text>

    <!-- Telemetry Flow Vectors -->
    <path d="M 280 87 L 370 87 L 370 213" stroke="#D4A863" stroke-width="1" stroke-dasharray="2 2"/>
    <path d="M 370 247 L 370 373 L 280 373" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="2 2"/>
    <path d="M 180 373 L 90 373 L 90 247" stroke="#D4A863" stroke-width="1" stroke-dasharray="2 2"/>
    <path d="M 90 213 L 90 87 L 180 87" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="2 2"/>

    <!-- Technical Readouts -->
    <text x="24" y="432" font-family="'JetBrains Mono', monospace" font-size="8" fill="#5E6570" letter-spacing="0.15em">CAD: REVOPS_STATE_MACHINE_V4</text>
    <text x="436" y="432" font-family="'JetBrains Mono', monospace" font-size="8" fill="#D4A863" letter-spacing="0.15em" text-anchor="end">SLA: &lt; 30S</text>
</svg>""",

    "paid_media": """<svg width="100%" height="100%" viewBox="0 0 460 460" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Targeting Range Reticle -->
    <circle cx="230" cy="230" r="195" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
    <circle cx="230" cy="230" r="145" stroke="rgba(255,255,255,0.25)" stroke-width="1" stroke-dasharray="4 4"/>
    <circle cx="230" cy="230" r="95" stroke="rgba(212,168,99,0.35)" stroke-width="1"/>
    <circle cx="230" cy="230" r="45" stroke="#FFFFFF" stroke-width="1"/>
    <circle cx="230" cy="230" r="3" fill="#D4A863"/>

    <!-- Angular Reticle Crosshairs with Degree Ticks -->
    <line x1="230" y1="15" x2="230" y2="445" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="15" y1="230" x2="445" y2="230" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="92" y1="92" x2="368" y2="368" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
    <line x1="92" y1="368" x2="368" y2="92" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

    <!-- Acquisition Quadrant Markers -->
    <rect x="250" y="40" width="165" height="26" fill="#050507" stroke="#FFFFFF" stroke-width="1"/>
    <text x="332" y="57" font-family="'JetBrains Mono', monospace" font-size="8" fill="#FFFFFF" letter-spacing="0.14em" text-anchor="middle">GOOGLE SEARCH // INTENT</text>

    <rect x="250" y="394" width="165" height="26" fill="#050507" stroke="#D4A863" stroke-width="1"/>
    <text x="332" y="411" font-family="'JetBrains Mono', monospace" font-size="8" fill="#D4A863" letter-spacing="0.14em" text-anchor="middle">LINKEDIN // FIRMOGRAPHIC ABM</text>

    <rect x="45" y="40" width="165" height="26" fill="#050507" stroke="#D4A863" stroke-width="1"/>
    <text x="127" y="57" font-family="'JetBrains Mono', monospace" font-size="8" fill="#D4A863" letter-spacing="0.14em" text-anchor="middle">OFFLINE CRM SQL SYNC</text>

    <rect x="45" y="394" width="165" height="26" fill="#050507" stroke="#FFFFFF" stroke-width="1"/>
    <text x="127" y="411" font-family="'JetBrains Mono', monospace" font-size="8" fill="#FFFFFF" letter-spacing="0.14em" text-anchor="middle">SERVER-SIDE GA4 / GTM</text>

    <!-- Converging Ingestion Vectors -->
    <path d="M 230 45 L 230 185" stroke="#D4A863" stroke-width="1" stroke-dasharray="3 3"/>
    <path d="M 45 230 L 185 230" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="3 3"/>
    <path d="M 415 230 L 275 230" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="3 3"/>
    <path d="M 230 415 L 230 275" stroke="#D4A863" stroke-width="1" stroke-dasharray="3 3"/>

    <!-- Target Coordinates -->
    <text x="24" y="222" font-family="'JetBrains Mono', monospace" font-size="8" fill="#5E6570">AZ: 142.8°</text>
    <text x="400" y="222" font-family="'JetBrains Mono', monospace" font-size="8" fill="#5E6570">EL: 48.2°</text>
</svg>""",

    "seo_geo": """<svg width="100%" height="100%" viewBox="0 0 460 460" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Global Latitude & Longitude Wireframe Sphere -->
    <circle cx="230" cy="230" r="185" stroke="#FFFFFF" stroke-width="1"/>
    <circle cx="230" cy="230" r="140" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>

    <!-- Latitude Parallels -->
    <ellipse cx="230" cy="230" rx="185" ry="125" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
    <ellipse cx="230" cy="230" rx="185" ry="60" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
    <ellipse cx="230" cy="140" rx="155" ry="40" stroke="rgba(212,168,99,0.35)" stroke-width="1" stroke-dasharray="3 3"/>
    <ellipse cx="230" cy="320" rx="155" ry="40" stroke="rgba(212,168,99,0.35)" stroke-width="1" stroke-dasharray="3 3"/>

    <!-- Longitude Meridians -->
    <ellipse cx="230" cy="230" rx="125" ry="185" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
    <ellipse cx="230" cy="230" rx="60" ry="185" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
    <line x1="230" y1="45" x2="230" y2="415" stroke="#D4A863" stroke-width="1"/>
    <line x1="45" y1="230" x2="415" y2="230" stroke="#FFFFFF" stroke-width="1"/>

    <!-- Semantic Entity Graph Nodes -->
    <circle cx="230" cy="140" r="5" fill="#D4A863"/>
    <circle cx="160" cy="210" r="4" fill="#FFFFFF"/>
    <circle cx="300" cy="250" r="4" fill="#FFFFFF"/>
    <circle cx="230" cy="320" r="5" fill="#D4A863"/>

    <line x1="230" y1="140" x2="160" y2="210" stroke="#D4A863" stroke-width="1" stroke-dasharray="2 2"/>
    <line x1="160" y1="210" x2="300" y2="250" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="2 2"/>
    <line x1="300" y1="250" x2="230" y2="320" stroke="#D4A863" stroke-width="1" stroke-dasharray="2 2"/>

    <!-- LLM RAG Projection Beam -->
    <path d="M 230 45 L 290 18 M 230 45 L 170 18" stroke="#D4A863" stroke-width="1"/>

    <!-- Labels -->
    <text x="230" y="24" font-family="'JetBrains Mono', monospace" font-size="8" fill="#D4A863" letter-spacing="0.16em" text-anchor="middle">LLM RAG ANSWER CITATION</text>
    <text x="24" y="434" font-family="'JetBrains Mono', monospace" font-size="8" fill="#5E6570" letter-spacing="0.14em">GRID: WGS-84 // JSON-LD GRAPH</text>
</svg>""",

    "marketing_data": """<svg width="100%" height="100%" viewBox="0 0 460 460" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Markov Transition Matrix Nodes -->
    <rect x="50" y="60" width="80" height="40" fill="#050507" stroke="#FFFFFF" stroke-width="1"/>
    <text x="90" y="85" font-family="'JetBrains Mono', monospace" font-size="9" fill="#FFFFFF" font-weight="700" text-anchor="middle">S0 // IMPR</text>

    <rect x="190" y="60" width="80" height="40" fill="#050507" stroke="#D4A863" stroke-width="1"/>
    <text x="230" y="85" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D4A863" font-weight="700" text-anchor="middle">S1 // CLICK</text>

    <rect x="330" y="60" width="80" height="40" fill="#050507" stroke="#FFFFFF" stroke-width="1"/>
    <text x="370" y="85" font-family="'JetBrains Mono', monospace" font-size="9" fill="#FFFFFF" font-weight="700" text-anchor="middle">S2 // SQL</text>

    <rect x="190" y="160" width="80" height="40" fill="#050507" stroke="#D4A863" stroke-width="1"/>
    <text x="230" y="185" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D4A863" font-weight="700" text-anchor="middle">S3 // WON</text>

    <!-- Directed Markov Vectors -->
    <path d="M 130 80 L 190 80" stroke="#FFFFFF" stroke-width="1"/>
    <path d="M 270 80 L 330 80" stroke="#D4A863" stroke-width="1"/>
    <path d="M 230 100 L 230 160" stroke="#D4A863" stroke-width="1"/>
    <path d="M 370 100 L 370 180 L 270 180" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="3 3"/>
    <path d="M 90 100 L 90 180 L 190 180" stroke="rgba(255,255,255,0.3)" stroke-width="1" stroke-dasharray="2 2"/>

    <text x="160" y="74" font-family="'JetBrains Mono', monospace" font-size="7" fill="#5E6570">P: 0.38</text>
    <text x="300" y="74" font-family="'JetBrains Mono', monospace" font-size="7" fill="#5E6570">P: 0.24</text>
    <text x="238" y="135" font-family="'JetBrains Mono', monospace" font-size="7" fill="#D4A863">P: 0.65</text>

    <!-- Telemetry Waveform Section (Lower Half) -->
    <line x1="40" y1="260" x2="420" y2="260" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="40" y1="330" x2="420" y2="330" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <line x1="40" y1="400" x2="420" y2="400" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>

    <path d="M 40 370 L 80 350 L 120 380 L 160 310 L 200 330 L 240 280 L 280 300 L 320 270 L 360 290 L 400 265 L 420 270" stroke="#FFFFFF" stroke-width="1.5"/>
    <path d="M 40 380 L 100 365 L 180 345 L 260 320 L 340 295 L 420 280" stroke="#D4A863" stroke-width="1" stroke-dasharray="4 2"/>

    <text x="40" y="425" font-family="'JetBrains Mono', monospace" font-size="8" fill="#5E6570" letter-spacing="0.14em">SQL TELEMETRY // REAL-TIME ATTRIBUTION WAVEFORM</text>
</svg>"""
}

# 4. STRUCTURED DATA FOR THE 4 PAGES
SERVICES_DATA = [
    {
        "id": "crm",
        "slug": "hubspot-crm-optimization-startups",
        "aliases": ["small-startup-business-crm-setup-optimization"],
        "bg_image": "starshield-crm-revops",
        "num": "01",
        "nav_label_en": "01 CRM ARCHITECTURE",
        "nav_label_it": "01 ARCHITETTURA CRM",

        # SEO Metadata (<60 chars title, <160 chars desc)
        "meta_title_en": "HubSpot CRM & RevOps Architecture | Francesqui",
        "meta_title_it": "Architettura CRM & RevOps HubSpot | Francesqui",
        "meta_desc_en": "HubSpot & Salesforce CRM architecture for B2B startups. Eliminate lead leakage, automate MQL routing, and scale pipeline velocity.",
        "meta_desc_it": "Architettura CRM HubSpot & Salesforce per startup B2B. Elimina la dispersione di lead, automatizza il routing MQL e scala la pipeline.",

        # Section 1: Hero
        "eyebrow_en": "SECTOR 01 // REVOPS & CRM ARCHITECTURE",
        "eyebrow_it": "SETTORE 01 // ARCHITETTURA CRM & REVOPS",
        "hero_title_en": "HUBSPOT & SALESFORCE ARCHITECTURE FOR B2B REVENUE TEAMS",
        "hero_title_it": "ARCHITETTURA HUBSPOT & SALESFORCE PER TEAM REVENUE B2B",
        "hero_lead_en": "Eliminate lead leakage, manual data entry, and broken pipeline visibility. Mission-critical lifecycle modeling, automated MQL-to-SQL routing SLAs, and strict deal governance engineered for scaling B2B startups.",
        "hero_lead_it": "Elimina la dispersione dei lead, l'inserimento manuale dei dati e la visibilità frammentata della pipeline. Modellazione del lifecycle mission-critical, SLA di routing MQL-to-SQL automatizzati e rigorosa deal governance per startup B2B.",
        "cad_label": "SCHEMATIC // REV-OP STATE MACHINE",

        # Section 2: Oversized Stats (SpaceX Stats Bar)
        "stats_en": [
            ("100%", "CAPTURED LEAD SYNCHRONIZATION"),
            ("< 5 MIN", "AUTOMATED MQL-TO-SQL ROUTING SLA"),
            ("0", "UNASSIGNED / STAGNANT PIPELINE DEALS")
        ],
        "stats_it": [
            ("100%", "SINCRONIZZAZIONE LEAD ACQUISITI"),
            ("< 5 MIN", "SLA ROUTING MQL-TO-SQL AUTOMATIZZATO"),
            ("0", "TRATTATIVE DI PIPELINE NON ASSEGNATE")
        ],

        # Section 3: 3 Starshield Capability Pillars
        "section3_title_en": "SYSTEM CAPABILITIES",
        "section3_title_it": "CAPACITÀ DEL SISTEMA",
        "pillars_en": [
            ("01", "LIFECYCLE MODELING & GOVERNANCE", "Standardized Contact, Company, and Deal object schemas. Mandatory stage-gate validation rules to enforce pipeline hygiene and eliminate premature stage skips.", "SPEC: ZERO STAGE BYPASS"),
            ("02", "ZERO-LATENCY ROUTING & SLA ESCALATION", "Instant webhook-driven lead ingestion with automated territory assignment. Automated Slack and Email alerts triggered when high-intent leads stagnate.", "SPEC: AUTOMATED HANDOFF"),
            ("03", "ATTRIBUTION TAXONOMY & REPORTING", "Unified UTM tracking and custom property governance. Real-time executive dashboards connecting marketing campaign sources directly to closed-won revenue.", "SPEC: SINGLE SOURCE OF TRUTH")
        ],
        "pillars_it": [
            ("01", "MODELLAZIONE LIFECYCLE & GOVERNANCE", "Schemi standardizzati per Contatti, Aziende e Trattative. Regole di validazione stage-gate obbligatorie per garantire l'igiene di pipeline ed eliminare salti di fase prematuri.", "SPEC: ZERO BYPASS DELLE FASI"),
            ("02", "ROUTING A ZERO LATENZA & ESCALATION SLA", "Ingestione istantanea dei lead via webhook con assegnazione territoriale automatizzata. Notifiche automatiche su Slack ed Email quando i lead ad alta intenzione ristagnano.", "SPEC: HANDOFF AUTOMATIZZATO"),
            ("03", "TASSONOMIA ATTRIBUZIONE & REPORTISTICA", "Tracciamento UTM unificato e governance delle proprietà personalizzate. Dashboard executive in tempo reale che collegano le campagne marketing direttamente al fatturato vinto.", "SPEC: UNICA FONTE DI VERITÀ")
        ],

        # Section 4: Falcon-9 Style Technical Spec Table
        "section4_title_en": "TECHNICAL SPECIFICATIONS",
        "section4_title_it": "SPECIFICHE TECNICHE",
        "specs_en": [
            ("SUPPORTED PLATFORMS", "HUBSPOT ENTERPRISE / SALESFORCE"),
            ("LIFECYCLE MODEL", "LEAD → MQL → SQL → OPPORTUNITY → WON"),
            ("LEAD ROUTING LATENCY", "< 30 SECONDS (WEBHOOK / API)"),
            ("DATA HYGIENE ENFORCEMENT", "MANDATORY STAGE-GATE VALIDATION RULES"),
            ("SCORING METHODOLOGY", "COMPOSITE ICP FIT + BEHAVIORAL INTENT"),
            ("SLA MONITORING", "REAL-TIME SLACK & EMAIL ESCALATION")
        ],
        "specs_it": [
            ("PIATTAFORME SUPPORTATE", "HUBSPOT ENTERPRISE / SALESFORCE"),
            ("MODELLO LIFECYCLE", "LEAD → MQL → SQL → OPPORTUNITY → WON"),
            ("LATENZA ROUTING LEAD", "< 30 SECONDI (WEBHOOK / API)"),
            ("IGIENE DEI DATI", "REGOLE DI VALIDAZIONE STAGE-GATE OBBLIGATORIE"),
            ("METODOLOGIA SCORING", "FIT ICP COMPOSITO + INTENTO COMPORTAMENTALE"),
            ("MONITORAGGIO SLA", "ESCALATION IN TEMPO REALE VIA SLACK ED EMAIL")
        ],

        # Section 5: 4-Stage Launch Sequence + Flight Heritage
        "section5_title_en": "DEPLOYMENT SEQUENCE",
        "section5_title_it": "SEQUENZA DI DEPLOYMENT",
        "stages_en": [
            ("STAGE 01", "AUDIT & DATA TAXONOMY", "Full diagnostic of existing CRM properties, duplicate leakage, and broken workflows."),
            ("STAGE 02", "LIFECYCLE & DEAL GATING", "Deployment of custom objects, lifecycle stages, and deal-stage validation gates."),
            ("STAGE 03", "AUTOMATION & ROUTING SLA", "Activation of lead scoring, territory routing, and SLA breach notifications."),
            ("STAGE 04", "EXECUTIVE BI & GOVERNANCE", "Sales rep playbooks, executive pipeline velocity dashboards, and sandbox QA.")
        ],
        "stages_it": [
            ("STAGE 01", "AUDIT & TASSONOMIA DATI", "Diagnosi completa delle proprietà CRM esistenti, dispersione duplicati e workflow interrotti."),
            ("STAGE 02", "LIFECYCLE & DEAL GATING", "Rilascio di oggetti personalizzati, fasi di lifecycle e regole di validazione deal-gate."),
            ("STAGE 03", "AUTOMAZIONE & SLA DI ROUTING", "Attivazione di lead scoring, routing per territorio e notifiche di violazione SLA."),
            ("STAGE 04", "EXECUTIVE BI & GOVERNANCE", "Playbook commerciali, dashboard di velocità pipeline e test in ambiente sandbox.")
        ],
        "heritage_title_en": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // TOMRA — MARKETING EVENTS & CRM OPERATIONS",
        "heritage_title_it": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // TOMRA — OPERAZIONI MARKETING EVENTI & CRM",
        "heritage_quote_en": "Co-led HubSpot CRM operational adoption across 15–20 annual global exhibitions (IFAT, PRS Europe), syncing 100% of captured leads for a 30–50 rep EMEA & Americas sales force and cutting handoff from 7+ days to same-week execution.",
        "heritage_quote_it": "Co-guidato l'adozione operativa di HubSpot CRM in 15–20 fiere globali annuali (IFAT, PRS Europe), sincronizzando il 100% dei lead acquisiti per una forza vendita di 30–50 commerciali EMEA e Americhe, riducendo l'handoff da 7+ giorni a esecuzione entro la settimana.",

        "service_name_en": "HubSpot & Salesforce Architecture",
        "service_name_it": "Architettura HubSpot & Salesforce"
    },

    {
        "id": "paid_media",
        "slug": "paid-media-management",
        "aliases": [],
        "bg_image": "starshield-paid-media",
        "num": "02",
        "nav_label_en": "02 PAID MEDIA",
        "nav_label_it": "02 PAID MEDIA",

        "meta_title_en": "Pipeline-Driven Paid Media | Francesqui",
        "meta_title_it": "Paid Media Guidati da Pipeline | Francesqui",
        "meta_desc_en": "Pipeline-driven Google Search, LinkedIn ABM, and Meta demand generation wired to CRM closed-won revenue data via offline conversion tracking loops.",
        "meta_desc_it": "Demand generation Google Search, LinkedIn ABM e Meta collegata al fatturato vinto nel CRM tramite loop di tracciamento conversioni offline.",

        "eyebrow_en": "SECTOR 02 // B2B PERFORMANCE & DEMAND GENERATION",
        "eyebrow_it": "SETTORE 02 // PERFORMANCE B2B & DEMAND GENERATION",
        "hero_title_en": "PIPELINE-DRIVEN PAID MEDIA FOR TECHNICAL & B2B MARKETS",
        "hero_title_it": "PAID MEDIA GUIDATI DALLA PIPELINE PER MERCATI TECNICI & B2B",
        "hero_lead_en": "Stop burning budget on vanity clicks. Full-funnel Google Search, LinkedIn ABM, and Meta demand generation wired directly to your CRM's closed-won revenue data via offline conversion tracking loops.",
        "hero_lead_it": "Basta bruciare budget su click di vanità. Acquisizione full-funnel su Google Search, LinkedIn ABM e Meta collegata direttamente al fatturato vinto nel CRM tramite loop di conversioni offline.",
        "cad_label": "SCHEMATIC // ACQUISITION RETICLE",

        "stats_en": [
            ("+33%", "VERIFIED PAID CONVERSION RATE LIFT"),
            ("10+", "INTERNATIONAL MARKETS SCALED"),
            ("SQL-SYNCED", "OFFLINE CONVERSION IMPORT LOOP")
        ],
        "stats_it": [
            ("+33%", "INCREMENTO CONVERSIONE PAID VERIFICATO"),
            ("10+", "MERCATI INTERNAZIONALI SCALATI"),
            ("SQL-SYNCED", "LOOP IMPORT CONVERSIONI OFFLINE")
        ],

        "section3_title_en": "SYSTEM CAPABILITIES",
        "section3_title_it": "CAPACITÀ DEL SISTEMA",
        "pillars_en": [
            ("01", "OFFLINE CONVERSION CRM LOOP", "Bi-directional CRM sync feeding verified SQL milestones and closed deal values back to ad bidding algorithms for maximum ROAS efficiency.", "SPEC: CLOSED-LOOP ROAS"),
            ("02", "HIGH-INTENT SEARCH ARCHITECTURE", "Exact and phrase-match Google Search campaigns capturing bottom-of-funnel commercial intent with aggressive negative keyword filtering.", "SPEC: INTENT HARVESTING"),
            ("03", "ACCOUNT-BASED MARKETING (ABM)", "Precision LinkedIn and Meta campaigns targeting specific enterprise decision-makers, buying committees, and ideal customer profiles.", "SPEC: ACCOUNT PENETRATION")
        ],
        "pillars_it": [
            ("01", "LOOP CONVERSIONI OFFLINE CRM", "Sincronizzazione CRM bidirezionale che reinvia milestone SQL verificate e valori di deal vinti agli algoritmi pubblicitari per il massimo ROAS.", "SPEC: ROAS CLOSED-LOOP"),
            ("02", "ARCHITETTURA SEARCH AD ALTA INTENZIONE", "Campagne Google Search a corrispondenza esatta e a frase per intercettare l'intento commerciale bottom-of-funnel con filtri negativi rigorosi.", "SPEC: CATTURA INTENTO"),
            ("03", "ACCOUNT-BASED MARKETING (ABM)", "Campagne di precisione su LinkedIn e Meta mirate a decisori aziendali specifici, buying committee e profili cliente ideali (ICP).", "SPEC: PENETRAZIONE ACCOUNT")
        ],

        "section4_title_en": "TECHNICAL SPECIFICATIONS",
        "section4_title_it": "SPECIFICHE TECNICHE",
        "specs_en": [
            ("ACQUISITION CHANNELS", "GOOGLE ADS / LINKEDIN ABM / META"),
            ("BIDDING OPTIMIZATION SIGNAL", "OFFLINE CRM SQL & DEAL VALUE IMPORT"),
            ("TRACKING INFRASTRUCTURE", "GA4 + SERVER-SIDE GTM + ENHANCED CONVERSIONS"),
            ("LEAD CAPTURE ARCHITECTURE", "CONVERSATIONAL FORMS + INSTANT CRM ROUTING"),
            ("NEGATIVE KEYWORD MATRIX", "1,500+ B2B EXCLUSIONS ACTIVATED"),
            ("ATTRIBUTION HORIZON", "90-DAY FIRST-TOUCH TO CLOSED-WON")
        ],
        "specs_it": [
            ("CANALI DI ACQUISIZIONE", "GOOGLE ADS / LINKEDIN ABM / META"),
            ("SEGNALE DI OTTIMIZZAZIONE", "IMPORT OFFLINE CRM DI SQL & VALORE DEAL"),
            ("INFRASTRUTTURA TRACCIAMENTO", "GA4 + GTM SERVER-SIDE + ENHANCED CONVERSIONS"),
            ("ARCHITETTURA LEAD CAPTURE", "MODULI CONVERSAZIONALI + ROUTING CRM ISTANTANEO"),
            ("MATRICE PAROLE NEGATIVE", "1.500+ ESCLUSIONI B2B ATTIVATE"),
            ("ORIZZONTE DI ATTRIBUZIONE", "90 GIORNI DAL PRIMO TOUCH AL CLOSED-WON")
        ],

        "section5_title_en": "DEPLOYMENT SEQUENCE",
        "section5_title_it": "SEQUENZA DI DEPLOYMENT",
        "stages_en": [
            ("STAGE 01", "ICP & TRACKING AUDIT", "Auditing tracking pixels, server-side GA4, and defining tier-1 ICP account lists."),
            ("STAGE 02", "HIGH-INTENT SEARCH DEPLOYMENT", "Launching exact-match intent search structures and comprehensive negative matrices."),
            ("STAGE 03", "LINKEDIN ABM & PAID SOCIAL", "Deploying firmographic-matched ABM campaigns for buying committee air cover."),
            ("STAGE 04", "OFFLINE CONVERSION ENGINE", "Automating daily CRM closed-won deal value imports into Google and LinkedIn bidding.")
        ],
        "stages_it": [
            ("STAGE 01", "AUDIT ICP & TRACCIAMENTO", "Audit pixel di tracciamento, GA4 server-side e definizione liste account ICP tier-1."),
            ("STAGE 02", "DEPLOYMENT SEARCH AD ALTA INTENZIONE", "Lancio strutture search a corrispondenza esatta e matrici negative esaustive."),
            ("STAGE 03", "LINKEDIN ABM & PAID SOCIAL", "Rilascio campagne ABM profilate per copertura completa del buying committee."),
            ("STAGE 04", "MOTORE CONVERSIONI OFFLINE", "Automazione dell'import giornaliero di trattative vinte dal CRM al bidding.")
        ],
        "heritage_title_en": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // IMBAREX & THE PISONAY COMPANY",
        "heritage_title_it": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // IMBAREX & THE PISONAY COMPANY",
        "heritage_quote_en": "Engineered multi-channel paid acquisition funnels across 10+ international markets, driving a verified +33% increase in qualified pipeline conversion while reducing wasted spend through offline CRM feedback loops.",
        "heritage_quote_it": "Ingegnerizzato funnel di acquisizione multicanale in oltre 10 mercati internazionali, registrando un incremento verificato del +33% nella conversione di pipeline qualificata e riducendo gli sprechi con loop di feedback CRM offline.",

        "service_name_en": "Pipeline-Driven Paid Media",
        "service_name_it": "Paid Media Guidati da Pipeline"
    },

    {
        "id": "seo_geo",
        "slug": "seo-and-geo-optimization",
        "aliases": [],
        "bg_image": "starshield-seo-geo",
        "num": "03",
        "nav_label_en": "03 TECHNICAL SEO & GEO",
        "nav_label_it": "03 SEO TECNICA & GEO",

        "meta_title_en": "Dual-Engine SEO & GEO Architecture | Francesqui",
        "meta_title_it": "Architettura SEO & GEO Dual-Engine | Francesqui",
        "meta_desc_en": "Dual-engine SEO and Generative Engine Optimization (GEO). Technical search architecture and Schema entity graphs to rank in Google and get cited by AI.",
        "meta_desc_it": "SEO dual-engine e Generative Engine Optimization (GEO). Architettura di ricerca tecnica ed entity graph Schema per ranking Google e citazioni AI.",

        "eyebrow_en": "SECTOR 03 // TECHNICAL SEO & GENERATIVE AI VISIBILITY",
        "eyebrow_it": "SETTORE 03 // SEO TECNICA & VISIBILITÀ SU MOTORI GENERATIVI AI",
        "hero_title_en": "DUAL-ENGINE ORGANIC SEARCH & GENERATIVE ENGINE OPTIMIZATION",
        "hero_title_it": "OTTIMIZZAZIONE DUAL-ENGINE: RICERCA ORGANICA & GENERATIVE ENGINE",
        "hero_lead_en": "B2B buyers research vendors across both Google Search and AI answer engines. Technical search architecture, Schema.org entity graphs, and high-authority content systems engineered to rank in SERPs and get cited by ChatGPT, Perplexity, and Gemini.",
        "hero_lead_it": "I buyer B2B ricercano fornitori sia su Google Search sia su motori di risposta AI. Architettura di ricerca tecnica, entity graph Schema.org e contenuti autorevoli ingegnerizzati per posizionarsi nelle SERP ed essere citati da ChatGPT, Perplexity e Gemini.",
        "cad_label": "SCHEMATIC // LLM RAG PROJECTION",

        "stats_en": [
            ("+40%", "ORGANIC TRAFFIC GROWTH IN 6 MONTHS"),
            ("DUAL-ENGINE", "GOOGLE SERP + AI ANSWER CITATION"),
            ("JSON-LD", "STRUCTURED ENTITY KNOWLEDGE GRAPH")
        ],
        "stats_it": [
            ("+40%", "CRESCITA TRAFFICO ORGANICO IN 6 MESI"),
            ("DUAL-ENGINE", "GOOGLE SERP + CITAZIONE RISPOSTE AI"),
            ("JSON-LD", "KNOWLEDGE GRAPH ENTITÀ STRUTTURATO")
        ],

        "section3_title_en": "SYSTEM CAPABILITIES",
        "section3_title_it": "CAPACITÀ DEL SISTEMA",
        "pillars_en": [
            ("01", "TECHNICAL CRAWL & HREFLANG ARCHITECTURE", "Flawless site architecture, Core Web Vitals optimization, and bidirectional hreflang implementations for seamless international crawling.", "SPEC: ZERO CRAWL LEAKAGE"),
            ("02", "SCHEMA.ORG ENTITY GRAPH MODELING", "Rich JSON-LD schemas connecting Organization, Service, WebPage, and Person entities to establish definitive authority across search algorithms.", "SPEC: KNOWLEDGE GRAPH INJECTION"),
            ("03", "GENERATIVE ENGINE OPTIMIZATION (GEO)", "Information architecture and authoritative knowledge formatting designed specifically to be ingested and cited as canonical sources by LLM RAG pipelines.", "SPEC: AI ANSWER CITATION")
        ],
        "pillars_it": [
            ("01", "ARCHITETTURA CRAWL TECNICO & HREFLANG", "Architettura di sito impeccabile, ottimizzazione Core Web Vitals e implementazioni hreflang bidirezionali per un crawling internazionale privo di errori.", "SPEC: ZERO DISPERSIONE CRAWL"),
            ("02", "MODELLAZIONE ENTITY GRAPH SCHEMA.ORG", "Schemi JSON-LD avanzati che collegano entità Organization, Service, WebPage e Person per stabilire un'autorevolezza chiara per gli algoritmi di ricerca.", "SPEC: INIEZIONE KNOWLEDGE GRAPH"),
            ("03", "GENERATIVE ENGINE OPTIMIZATION (GEO)", "Architettura informativa e formattazione della conoscenza progettate appositamente per essere assimilate e citate come fonti autorevoli dalle pipeline RAG degli LLM.", "SPEC: CITAZIONE RISPOSTE AI")
        ],

        "section4_title_en": "TECHNICAL SPECIFICATIONS",
        "section4_title_it": "SPECIFICHE TECNICHE",
        "specs_en": [
            ("TARGET ENGINES", "GOOGLE / CHATGPT / PERPLEXITY / GEMINI"),
            ("STRUCTURED DATA", "NESTED SCHEMA.ORG JSON-LD ENTITY GRAPH"),
            ("INTERNATIONALIZATION", "BIDIRECTIONAL HREFLANG & REGIONAL ROUTING"),
            ("CORE WEB VITALS TARGET", "95+ PERFORMANCE / ACCESSIBILITY / SEO"),
            ("CRAWL ARCHITECTURE", "XML SITEMAPS + STRICT CANONICAL TAXONOMY"),
            ("CONTENT AUTHORITY MODEL", "HIGH-DENSITY TECHNICAL SPECIFICATIONS")
        ],
        "specs_it": [
            ("MOTORI TARGET", "GOOGLE / CHATGPT / PERPLEXITY / GEMINI"),
            ("DATI STRUTTURATI", "ENTITY GRAPH NIDIFICATO SCHEMA.ORG JSON-LD"),
            ("INTERNAZIONALIZZAZIONE", "HREFLANG BIDIREZIONALE & ROUTING REGIONALE"),
            ("OBIETTIVO CORE WEB VITALS", "95+ PERFORMANCE / ACCESSIBILITÀ / SEO"),
            ("ARCHITETTURA CRAWL", "SITEMAP XML + TASSONOMIA CANONICAL RIGOROSA"),
            ("MODELLO AUTOREVOLEZZA CONTENUTI", "SPECIFICHE TECNICHE AD ALTA DENSITÀ")
        ],

        "section5_title_en": "DEPLOYMENT SEQUENCE",
        "section5_title_it": "SEQUENZA DI DEPLOYMENT",
        "stages_en": [
            ("STAGE 01", "TECHNICAL & CRAWL DIAGNOSTIC", "Full audit of indexation, Core Web Vitals, canonical hygiene, and international hreflang."),
            ("STAGE 02", "SCHEMA ENTITY GRAPH INJECTION", "Deployment of nested JSON-LD schema graphs tying Brand, Services, and Knowledge bases."),
            ("STAGE 03", "CONTENT CLUSTER ARCHITECTURE", "High-authority technical topic clusters built for commercial intent dominance."),
            ("STAGE 04", "AI ENGINE CITATION BENCHMARKING", "Validating brand inclusion across Perplexity, ChatGPT, and Gemini query outputs.")
        ],
        "stages_it": [
            ("STAGE 01", "DIAGNOSI TECNICA & CRAWLING", "Audit completo di indicizzazione, Core Web Vitals, igiene canonical e hreflang internazionale."),
            ("STAGE 02", "INIEZIONE SCHEMA ENTITY GRAPH", "Rilascio di schemi JSON-LD nidificati che collegano Brand, Servizi e Basi di conoscenza."),
            ("STAGE 03", "ARCHITETTURA TOPIC CLUSTER", "Topic cluster tecnici ad alta autorevolezza costruiti per dominare l'intento commerciale."),
            ("STAGE 04", "BENCHMARK CITAZIONI MOTORI AI", "Validazione della presenza del brand nelle risposte di Perplexity, ChatGPT e Gemini.")
        ],
        "heritage_title_en": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // IMBAREX — INTERNATIONAL DIGITAL STRATEGY",
        "heritage_title_it": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // IMBAREX — STRATEGIA DIGITALE INTERNAZIONALE",
        "heritage_quote_en": "Achieved a verified +40% increase in organic B2B search visibility within 6 months through rigorous technical crawling audits, Schema entity modeling, and international multi-lingual SEO deployment.",
        "heritage_quote_it": "Raggiunto un incremento verificato del +40% nella visibilità di ricerca organica B2B in 6 mesi tramite audit di crawling tecnico, modellazione di entità Schema e implementazione SEO multilingua internazionale.",

        "service_name_en": "Dual-Engine SEO & GEO Architecture",
        "service_name_it": "Architettura SEO & GEO Dual-Engine"
    },

    {
        "id": "marketing_data",
        "slug": "marketing-data-reporting",
        "aliases": [],
        "bg_image": "starshield-data-bi",
        "num": "04",
        "nav_label_en": "04 DATA & BI",
        "nav_label_it": "04 DATI & BI",

        "meta_title_en": "Marketing Data & Executive BI | Francesqui",
        "meta_title_it": "Dati Marketing & BI Direzionale | Francesqui",
        "meta_desc_en": "Replace conflicting platform numbers with automated marketing data modeling, multi-touch Markov attribution, and real-time Looker Studio executive BI.",
        "meta_desc_it": "Sostituisci numeri contrastanti con data modeling marketing automatizzato, attribuzione multi-touch Markov e dashboard executive Looker Studio in tempo reale.",

        "eyebrow_en": "SECTOR 04 // ANALYTICS, ATTRIBUTION & EXECUTIVE BI",
        "eyebrow_it": "SETTORE 04 // ANALYTICS, ATTRIBUZIONE & EXECUTIVE BI",
        "hero_title_en": "MARKETING DATA MODELING & AUTOMATED EXECUTIVE REPORTING",
        "hero_title_it": "MODELLAZIONE DATI MARKETING & REPORTISTICA EXECUTIVE AUTOMATIZZATA",
        "hero_lead_en": "Replace conflicting platform numbers and manual spreadsheets with an automated analytics infrastructure. Unify CRM, paid media, and web telemetry into real-time executive dashboards and multi-touch attribution models.",
        "hero_lead_it": "Sostituisci numeri di piattaforma contrastanti e fogli di calcolo manuali con un'infrastruttura analitica automatizzata. Unifica CRM, paid media e telemetria web in dashboard executive in tempo reale e modelli di attribuzione multi-touch.",
        "cad_label": "SCHEMATIC // MARKOV REVENUE MATRIX",

        "stats_en": [
            ("SINGLE TRUTH", "UNIFIED AD SPEND + CRM PIPELINE"),
            ("MULTI-TOUCH", "MARKOV & FULL-FUNNEL ATTRIBUTION"),
            ("AUTOMATED", "REAL-TIME BI & SLACK KPI DELIVERY")
        ],
        "stats_it": [
            ("UNICA FONTE", "SPESA ADV UNIFICATA + PIPELINE CRM"),
            ("MULTI-TOUCH", "ATTRIBUZIONE MARKOV & FULL-FUNNEL"),
            ("AUTOMATIZZATA", "DELIVERY KPI BI & SLACK IN TEMPO REALE")
        ],

        "section3_title_en": "SYSTEM CAPABILITIES",
        "section3_title_it": "CAPACITÀ DEL SISTEMA",
        "pillars_en": [
            ("01", "DATA WAREHOUSE & ETL PIPELINES", "Automated data extraction from ad networks, analytics engines, and CRM systems into clean, queryable SQL data warehouses.", "SPEC: AUTOMATED ETL"),
            ("02", "ALGORITHMIC MULTI-TOUCH ATTRIBUTION", "Moving beyond flawed first/last click models with Markov Chain removal effects to accurately assign revenue credit across all digital touchpoints.", "SPEC: MARKOV REMOVAL EFFECT"),
            ("03", "EXECUTIVE BI & AUTOMATED BRIEFINGS", "Custom Looker Studio and Power BI executive dashboards paired with automated Slack alerts for immediate visibility into CAC, pipeline velocity, and LTV.", "SPEC: 24/7 BOARD VISIBILITY")
        ],
        "pillars_it": [
            ("01", "DATA WAREHOUSE & PIPELINE ETL", "Estrazione automatizzata dei dati da piattaforme ad, motori di analytics e sistemi CRM in data warehouse SQL puliti e interrogabili.", "SPEC: ETL AUTOMATIZZATO"),
            ("02", "ATTRIBUZIONE ALGORITMICA MULTI-TOUCH", "Superamento dei modelli primo/ultimo click con catene di Markov basate sull'effetto rimozione per assegnare con precisione il credito di fatturato a ciascun touchpoint.", "SPEC: EFFETTO RIMOZIONE MARKOV"),
            ("03", "EXECUTIVE BI & BRIEFING AUTOMATIZZATI", "Dashboard executive Looker Studio e Power BI integrate con alert Slack automatici per una visibilità istantanea su CAC, velocità di pipeline e LTV.", "SPEC: VISIBILITÀ CDA 24/7")
        ],

        "section4_title_en": "TECHNICAL SPECIFICATIONS",
        "section4_title_it": "SPECIFICHE TECNICHE",
        "specs_en": [
            ("DATA SOURCES", "HUBSPOT / SALESFORCE / GA4 / AD NETWORKS"),
            ("QUERY & TRANSFORMATION", "SQL (BIGQUERY / POSTGRESQL / ORACLE)"),
            ("ATTRIBUTION METHODOLOGY", "MULTI-TOUCH & MARKOV CHAIN REMOVAL EFFECT"),
            ("VISUALIZATION LAYER", "LOOKER STUDIO / POWER BI EXECUTIVE VIEWS"),
            ("AUTOMATED ALERTS", "SCHEDULED SLACK & EMAIL KPI PAYLOADS"),
            ("CORE METRICS TRACKED", "BLENDED CAC / LTV:CAC / PIPELINE VELOCITY")
        ],
        "specs_it": [
            ("FONTI DATI", "HUBSPOT / SALESFORCE / GA4 / RETI ADV"),
            ("QUERY & TRASFORMAZIONE", "SQL (BIGQUERY / POSTGRESQL / ORACLE)"),
            ("METODOLOGIA ATTRIBUZIONE", "MULTI-TOUCH & EFFETTO RIMOZIONE MARKOV CHAIN"),
            ("LIVELLO DI VISUALIZZAZIONE", "VISTE EXECUTIVE LOOKER STUDIO / POWER BI"),
            ("ALERT AUTOMATIZZATI", "PAYLOAD KPI PROGRAMMATI SU SLACK ED EMAIL"),
            ("METRICHE MONITORATE", "CAC AGGREGATO / LTV:CAC / VELOCITÀ PIPELINE")
        ],

        "section5_title_en": "DEPLOYMENT SEQUENCE",
        "section5_title_it": "SEQUENZA DI DEPLOYMENT",
        "stages_en": [
            ("STAGE 01", "TAXONOMY & UTM AUDIT", "Auditing and standardizing UTM parameters, GA4 events, and CRM properties."),
            ("STAGE 02", "ETL PIPELINE & SQL WAREHOUSE", "Connecting APIs and writing SQL transformations to unify spend and revenue."),
            ("STAGE 03", "MARKOV ATTRIBUTION MODELING", "Deploying multi-touch weighting across online campaigns and field events."),
            ("STAGE 04", "EXECUTIVE DASHBOARD IGNITION", "Delivering live executive BI dashboards and automated weekly Slack briefings.")
        ],
        "stages_it": [
            ("STAGE 01", "AUDIT TASSONOMIA & UTM", "Audit e standardizzazione dei parametri UTM, eventi GA4 e proprietà di tracciamento CRM."),
            ("STAGE 02", "PIPELINE ETL & DATA WAREHOUSE", "Integrazione API e scritture di trasformazioni SQL per unificare spesa e fatturato."),
            ("STAGE 03", "MODELLAZIONE ATTRIBUZIONE MARKOV", "Distribuzione di pesi multi-touch tra campagne online ed eventi sul campo."),
            ("STAGE 04", "AVVIO CRUSCOTTI EXECUTIVE", "Consegna di cruscotti BI per il CDA e briefing settimanali automatizzati su Slack.")
        ],
        "heritage_title_en": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // REVOPS & BI ENGINEERING",
        "heritage_title_it": "FLIGHT HERITAGE // VERIFIED MISSION HERITAGE // INGEGNERIA REVOPS & BI",
        "heritage_quote_en": "Built executive board-level KPI & ROI attribution systems at IMBAREX and engineered automated Python + HubSpot API enrichment architectures and Markov Chain attribution models.",
        "heritage_quote_it": "Creato sistemi di attribuzione ROI e KPI per il Consiglio di Amministrazione in IMBAREX e sviluppato architetture automatizzate di arricchimento Python + API HubSpot e modelli di attribuzione con catene di Markov.",

        "service_name_en": "Marketing Data & Executive BI",
        "service_name_it": "Dati Marketing & BI Direzionale"
    }
]

def render_spacex_page(service, lang="en", current_slug=None):
    is_it = (lang == "it")
    slug = current_slug or service["slug"]
    canonical_slug = service["slug"]

    # URLs
    site_url = "https://renzo-francesqui.vercel.app"
    en_canonical_url = f"{site_url}/services/{canonical_slug}/"
    it_canonical_url = f"{site_url}/it/services/{canonical_slug}/"
    page_canonical = it_canonical_url if is_it else en_canonical_url
    page_url = f"{site_url}/it/services/{slug}/" if is_it else f"{site_url}/services/{slug}/"

    # Language toggles
    en_toggle_href = f"/services/{canonical_slug}/"
    it_toggle_href = f"/it/services/{canonical_slug}/"

    # Navigation Links
    brand_sub = "MISSION CONTROL"
    home_link = "../../index.html"
    solar_matrix_link = "../../index.html"
    solar_matrix_text = "RITORNO ALLA MATRICE SOLARE" if is_it else "RETURN TO SOLAR MATRIX"
    favicon_svg = "../../../favicon.svg" if is_it else "../../favicon.svg"
    favicon_ico = "../../../favicon.ico" if is_it else "../../favicon.ico"

    # Aerospace Background Image Assets
    root_prefix = "../../.." if is_it else "../.."
    bg_image_name = service.get("bg_image", "starshield-crm-revops")
    hero_bg_webp = f"{root_prefix}/images/services/{bg_image_name}.webp"
    hero_bg_jpg = f"{root_prefix}/images/services/{bg_image_name}.jpg"

    # Text fields based on language
    meta_title = service["meta_title_it"] if is_it else service["meta_title_en"]
    meta_desc = service["meta_desc_it"] if is_it else service["meta_desc_en"]
    eyebrow = service["eyebrow_it"] if is_it else service["eyebrow_en"]
    hero_title = service["hero_title_it"] if is_it else service["hero_title_en"]
    hero_lead = service["hero_lead_it"] if is_it else service["hero_lead_en"]
    cad_label = service["cad_label"]
    stats = service["stats_it"] if is_it else service["stats_en"]
    section3_title = service["section3_title_it"] if is_it else service["section3_title_en"]
    pillars = service["pillars_it"] if is_it else service["pillars_en"]
    section4_title = service["section4_title_it"] if is_it else service["section4_title_en"]
    specs = service["specs_it"] if is_it else service["specs_en"]
    section5_title = service["section5_title_it"] if is_it else service["section5_title_en"]
    stages = service["stages_it"] if is_it else service["stages_en"]
    heritage_title = service["heritage_title_it"] if is_it else service["heritage_title_en"]
    heritage_quote = service["heritage_quote_it"] if is_it else service["heritage_quote_en"]
    service_name = service["service_name_it"] if is_it else service["service_name_en"]

    # Calendly URL (Law 7)
    calendly_url = "http://calendly.com/renzo-francesqui"

    # Buttons
    cta_primary_label = "PRENOTA BRIEFING (CALENDLY)" if is_it else "SCHEDULE MISSION BRIEFING"
    cta_secondary_label = "SPECIFICHE TECNICHE" if is_it else "TECHNICAL SPECIFICATIONS"
    cta_inquire_label = "AVVIA TRASMISSIONE" if is_it else "INITIATE TRANSMISSION"
    footer_title = "PRONTO A DISTRIBUIRE QUESTA ARCHITETTURA?" if is_it else "READY TO DEPLOY THIS ARCHITECTURE?"
    footer_sub = "Disponibile per ingegneria freelance strategica e consulenza RevOps per mercati EMEA e globali. Prenota direttamente su Calendly o trasmetti i parametri di progetto." if is_it else "Available for strategic freelance engineering and RevOps consulting across EMEA and global markets. Reserve time via Calendly or transmit project scope."
    footer_return = "RITORNA IN ORBITA" if is_it else "RETURN TO ORBIT"

    mail_subject = f"Richiesta Missione — {service_name}" if is_it else f"Mission Inquiry — {service_name}"
    encoded_subject = urllib.parse.quote(mail_subject)

    # Nav links across 4 sectors
    nav_links_html = []
    for s in SERVICES_DATA:
        s_slug = s["slug"]
        s_href = f"/it/services/{s_slug}/" if is_it else f"/services/{s_slug}/"
        s_label = s["nav_label_it"] if is_it else s["nav_label_en"]
        active_class = " active" if s["id"] == service["id"] else ""
        nav_links_html.append(f'<a href="{s_href}" class="sx-nav-link{active_class}">{s_label}</a>')
    nav_links_str = "\n            ".join(nav_links_html)

    # Stats HTML
    stats_cells = []
    for num, label in stats:
        stats_cells.append(f"""            <div class="sx-stat-cell">
                <div class="sx-stat-number">{num}</div>
                <div class="sx-stat-label">{label}</div>
            </div>""")
    stats_html = "\n".join(stats_cells)

    # Pillars HTML
    pillars_cells = []
    for p_num, p_title, p_desc, p_foot in pillars:
        pillars_cells.append(f"""            <div class="sx-pillar-card">
                <div>
                    <span class="sx-pillar-num">{p_num} // CAPABILITY</span>
                    <h3 class="sx-pillar-title">{p_title}</h3>
                    <p class="sx-pillar-desc">{p_desc}</p>
                </div>
                <div class="sx-pillar-foot">{p_foot}</div>
            </div>""")
    pillars_html = "\n".join(pillars_cells)

    # Specs HTML
    specs_rows = []
    for label, val in specs:
        specs_rows.append(f"""                    <tr>
                        <td>{label}</td>
                        <td>{val}</td>
                    </tr>""")
    specs_html = "\n".join(specs_rows)

    # Stages HTML
    stages_cells = []
    for code, title, text in stages:
        stages_cells.append(f"""            <div class="sx-seq-step">
                <div class="sx-seq-code">{code}</div>
                <h4 class="sx-seq-title">{title}</h4>
                <p class="sx-seq-text">{text}</p>
            </div>""")
    stages_html = "\n".join(stages_cells)

    # CAD Schematic SVG
    cad_svg = CAD_SCHEMATICS.get(service["id"], "")

    # JSON-LD Schema
    schema_graph = [
        {
            "@type": "WebPage",
            "@id": f"{page_canonical}#webpage",
            "url": page_canonical,
            "name": meta_title,
            "description": meta_desc,
            "inLanguage": lang,
            "isPartOf": {
                "@type": "WebSite",
                "@id": f"{site_url}/#website",
                "url": f"{site_url}/",
                "name": "Renzo Francesqui — Portfolio & Systems"
            }
        },
        {
            "@type": "Service",
            "@id": f"{page_canonical}#service",
            "name": hero_title,
            "serviceType": service_name,
            "description": meta_desc,
            "provider": {
                "@type": "Person",
                "@id": f"{site_url}/#person",
                "name": "Renzo Francesqui",
                "jobTitle": "Specialista Marketing Operations, Architetture CRM & RevOps" if is_it else "Marketing Operations & RevOps Specialist",
                "url": site_url
            },
            "audience": {
                "@type": "BusinessAudience",
                "audienceType": "B2B Startups, Scaleups & Mid-Market Enterprises"
            },
            "areaServed": ["EMEA", "Americas", "Global"]
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{page_canonical}#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Mission Control",
                    "item": f"{site_url}/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Services",
                    "item": f"{site_url}/#modalServices"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": hero_title,
                    "item": page_canonical
                }
            ]
        }
    ]

    if is_it:
        schema_graph.append({
            "@type": "Organization",
            "@id": f"{site_url}/it/#organization",
            "name": "Renzo Francesqui — Consulenza RevOps & Architetture CRM",
            "url": f"{site_url}/it/",
            "logo": f"{site_url}/images/renzo-francesqui.jpg",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Milano",
                "addressRegion": "Lombardy",
                "addressCountry": "IT"
            },
            "areaServed": ["Milano, Italy", "Lombardy", "EMEA", "Globale"]
        })

    schema_json_str = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-DPYXTL3ZSN"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-DPYXTL3ZSN');
    </script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{meta_title}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="author" content="Renzo Francesqui">
    <meta name="robots" content="index, follow">

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="{favicon_svg}">
    <link rel="alternate icon" href="{favicon_ico}">

    <!-- Canonical & Language Alternates -->
    <link rel="canonical" href="{page_canonical}">
    <link rel="alternate" hreflang="en" href="{en_canonical_url}">
    <link rel="alternate" hreflang="it" href="{it_canonical_url}">
    <link rel="alternate" hreflang="x-default" href="{en_canonical_url}">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_url}">
    <meta property="og:title" content="{meta_title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:image" content="https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{page_url}">
    <meta name="twitter:title" content="{meta_title}">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
{schema_json_str}
    </script>

    <style>
{SPACEX_MASTER_CSS}
    </style>
</head>
<body>
    <!-- Fixed Deep-Space Aerospace Backdrop -->
    <div class="sx-fixed-backdrop">
        <div class="sx-fixed-backdrop-img" style="background-image: url('{hero_bg_webp}');"></div>
        <div class="sx-fixed-backdrop-overlay"></div>
    </div>

    <!-- Fixed Left Scroll Progress Telemetry Rail -->
    <div class="telemetry-rail">
        <div class="telemetry-rail-fill"></div>
    </div>
    <div class="telemetry-readout">ORBITAL TELEMETRY // ALT: 0.0 KM // TRAJECTORY: NOMINAL</div>

    <!-- Top SpaceX Navigation Bar -->
    <header class="sx-header">
        <a href="{home_link}" class="sx-brand">
            RENZO FRANCESQUI
            <span class="sub">{brand_sub}</span>
        </a>

        <div style="display: flex; align-items: center; gap: 2rem;">
            <nav class="sx-nav">
                {nav_links_str}
                <a href="{solar_matrix_link}" class="sx-nav-link">{solar_matrix_text}</a>
            </nav>
            <div class="sx-lang-switcher">
                <a href="{en_toggle_href}" class="sx-lang-btn{' active' if not is_it else ''}">EN</a>
                <span class="sx-lang-divider">/</span>
                <a href="{it_toggle_href}" class="sx-lang-btn{' active' if is_it else ''}">IT</a>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main>
        <!-- SECTION 1: 100VH STARSHIELD HERO -->
        <section class="sx-hero">
            <!-- Starshield Photorealistic Aerospace Hero Backdrop -->
            <div class="sx-hero-backdrop">
                <picture>
                    <source srcset="{hero_bg_webp}" type="image/webp">
                    <img src="{hero_bg_jpg}" alt="{hero_title}" class="sx-hero-img" loading="eager" fetchpriority="high">
                </picture>
                <canvas id="starshieldCanvas"></canvas>
                <div class="sx-hero-overlay"></div>
            </div>

            <div class="sx-container">
                <span class="sx-eyebrow">{eyebrow}</span>
                <h1 class="sx-hero-title">{hero_title}</h1>
                <p class="sx-hero-lead">{hero_lead}</p>
                <div class="sx-hero-actions">
                    <a href="{calendly_url}" target="_blank" rel="noopener noreferrer" class="sx-btn sx-btn-gold">
                        <span>{cta_primary_label}</span>
                    </a>
                    <a href="#specifications" class="sx-btn sx-btn-subtle">
                        <span>{cta_secondary_label}</span>
                    </a>
                    <a href="mailto:renzo.francesqui@gmail.com?subject={encoded_subject}" class="sx-btn sx-btn-subtle">
                        <span>{cta_inquire_label}</span>
                    </a>
                </div>
            </div>
            <div class="sx-scroll-cue">
                <svg width="20" height="30" viewBox="0 0 20 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M 3 10 L 10 17 L 17 10" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
            </div>
        </section>

        <!-- SECTION 2: OVERSIZED TELEMETRY COUNTERS (SPACEX STATS BAR) -->
        <section class="sx-stats-section">
            <div class="sx-stats-grid">
{stats_html}
            </div>
        </section>

        <!-- SECTION 3: STARSHIELD 3-PILLAR ARCHITECTURAL GRID -->
        <section class="sx-pillars-section" id="capabilities">
            <div class="sx-container">
                <div class="sx-section-header reveal-up">
                    <span class="sx-eyebrow">SECTOR {service['num']} // ARCHITECTURE</span>
                    <h2 class="sx-section-title">{section3_title}</h2>
                </div>
                <div class="sx-pillars-grid reveal-up">
{pillars_html}
                </div>
            </div>
        </section>

        <!-- SECTION 4: FALCON-9 STYLE TECHNICAL SPECIFICATION TABLE + CAD SCHEMATIC -->
        <section class="sx-specs-section" id="specifications">
            <div class="sx-container">
                <div class="sx-section-header reveal-up">
                    <span class="sx-eyebrow">TELEMETRY MATRIX // SPECIFICATION</span>
                    <h2 class="sx-section-title">{section4_title}</h2>
                </div>
                <div class="sx-specs-layout reveal-up">
                    <div>
                        <table class="sx-spec-table">
                            <tbody>
{specs_html}
                            </tbody>
                        </table>
                    </div>
                    <div class="sx-wireframe-box">
                        <span class="sx-wireframe-label">{cad_label}</span>
                        {cad_svg}
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 5: 4-STAGE LAUNCH SEQUENCE + PROVEN FLIGHT HERITAGE -->
        <section class="sx-sequence-section" id="sequence">
            <div class="sx-container">
                <div class="sx-section-header reveal-up">
                    <span class="sx-eyebrow">FLIGHT PROTOCOL // 4 PHASES</span>
                    <h2 class="sx-section-title">{section5_title}</h2>
                </div>
                <div class="sx-sequence-grid reveal-up">
{stages_html}
                </div>
                <div class="sx-heritage-bar reveal-up" style="--heritage-bg: url('{hero_bg_webp}');">
                    <div>
                        <span class="sx-eyebrow" style="margin-bottom: 0.5rem;">{heritage_title}</span>
                        <p style="font-size: 0.95rem; color: var(--text-white); font-weight: 400; line-height: 1.7; max-width: 820px;">
                            "{heritage_quote}"
                        </p>
                    </div>
                    <a href="{calendly_url}" target="_blank" rel="noopener noreferrer" class="sx-btn sx-btn-gold" style="flex-shrink: 0;">
                        <span>{cta_primary_label}</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- SECTION 6: SPACEX STARSHIELD VERTICAL-LINE FOOTER -->
        <footer class="sx-footer">
            <div class="sx-vertical-line"></div>
            <h2 class="sx-footer-title">{footer_title}</h2>
            <p class="sx-footer-sub">{footer_sub}</p>
            <div style="display: flex; gap: 1.25rem; flex-wrap: wrap; justify-content: center;">
                <a href="{calendly_url}" target="_blank" rel="noopener noreferrer" class="sx-btn sx-btn-gold">
                    <span>{cta_primary_label}</span>
                </a>
                <a href="mailto:renzo.francesqui@gmail.com?subject={encoded_subject}" class="sx-btn">
                    <span>{cta_inquire_label}</span>
                </a>
                <a href="{home_link}" class="sx-btn sx-btn-subtle">
                    <span>{footer_return}</span>
                </a>
            </div>
            <div class="sx-copyright">RENZO FRANCESQUI // ORBITAL REVOPS &amp; ARCHITECTURE SYSTEMS // ALL RIGHTS RESERVED</div>
        </footer>
    </main>

    <!-- Global Background Canvas & Scroll Telemetry Script -->
    <script>
{SPACEX_MASTER_JS}
    </script>
</body>
</html>"""

def build_all_services():
    count = 0
    for service in SERVICES_DATA:
        # 1. English page: services/<slug>/index.html
        en_dir = BASE_DIR / "services" / service['slug']
        en_dir.mkdir(parents=True, exist_ok=True)
        en_file = en_dir / "index.html"
        en_html = render_spacex_page(service, lang="en")
        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_html)
        count += 1

        # 2. Italian page: it/services/<slug>/index.html
        it_dir = BASE_DIR / "it" / "services" / service['slug']
        it_dir.mkdir(parents=True, exist_ok=True)
        it_file = it_dir / "index.html"
        it_html = render_spacex_page(service, lang="it")
        with open(it_file, "w", encoding="utf-8") as f:
            f.write(it_html)
        count += 1

        # 3. Aliases (if any)
        for alias_slug in service.get("aliases", []):
            alias_en_dir = BASE_DIR / "services" / alias_slug
            alias_en_dir.mkdir(parents=True, exist_ok=True)
            alias_en_file = alias_en_dir / "index.html"
            alias_en_html = render_spacex_page(service, lang="en", current_slug=alias_slug)
            with open(alias_en_file, "w", encoding="utf-8") as f:
                f.write(alias_en_html)
            count += 1

            alias_it_dir = BASE_DIR / "it" / "services" / alias_slug
            alias_it_dir.mkdir(parents=True, exist_ok=True)
            alias_it_file = alias_it_dir / "index.html"
            alias_it_html = render_spacex_page(service, lang="it", current_slug=alias_slug)
            with open(alias_it_file, "w", encoding="utf-8") as f:
                f.write(alias_it_html)
            count += 1

    # 4. Sync aerospace background assets across all required asset mirrors
    import shutil
    src_images_services = BASE_DIR / "images" / "services"
    if src_images_services.exists():
        target_dirs = [
            BASE_DIR / "assets" / "images" / "services",
            BASE_DIR / "assets" / "services",
            BASE_DIR / "it" / "images" / "services",
            BASE_DIR / "version-3" / "images" / "services",
            BASE_DIR / "version-3" / "it" / "images" / "services",
            BASE_DIR / "version-3" / "assets" / "images" / "services",
        ]
        for td in target_dirs:
            td.mkdir(parents=True, exist_ok=True)
            for f in src_images_services.glob("*.*"):
                shutil.copy2(f, td / f.name)
        print(f"[OK] Synced {len(list(src_images_services.glob('*.*')))} aerospace assets across mirrors.")

    print(f"[OK] Generated {count} SpaceX Starshield standalone service landing pages (EN and IT).")

if __name__ == "__main__":
    build_all_services()

