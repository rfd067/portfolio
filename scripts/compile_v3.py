#!/usr/bin/env python3
"""
Compile script to generate:
1. version-3/index.html (English Edition)
2. version-3/it/index.html (Italian Edition)

Features implemented:
- Celestial Realism (Photorealistic Sun with convective granulation, turbulent flares, sunspots, chromosphere prominence shell, dynamic corona; high-fidelity PBR planets with procedural albedo, bump, roughness, and emissive maps; authentic impact cratering; fine concentric Saturn rings with Cassini division & Encke gap and non-wobbling celestial tilt; Rayleigh atmospheric scattering).
- Mobile Experience & Responsiveness (multi-pointer 1-finger rotate, 2-finger pinch-to-zoom, tap-to-focus on planets, background tap dismiss, 60 FPS pixel ratio capping, ergonomic 360px-430px mobile styling, mobile-visible hint box with 5s timer).
- Black hole realistic relativistic accretion flow, gravitational lensing, and Doppler beaming shader.
- Full Italian (IT) edition with complete B2B translations, hreflang, and Italian service landing links (/it/services/...).
"""

import os
import re
import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
V3_DIR = BASE_DIR / "version-3"
V3_INDEX = V3_DIR / "index.html"
V3_IT_DIR = V3_DIR / "it"
V3_IT_INDEX = V3_IT_DIR / "index.html"
ROOT_INDEX = BASE_DIR / "index.html"
ROOT_IT_DIR = BASE_DIR / "it"
ROOT_IT_INDEX = ROOT_IT_DIR / "index.html"

with open(BASE_DIR / "images" / "renzo-francesqui.jpg", "rb") as _f_av:
    _avatar_b64 = base64.b64encode(_f_av.read()).decode("utf-8")
RENZO_AVATAR_DATA_URI = f"data:image/jpeg;base64,{_avatar_b64}"

def read_source_html():
    with open(V3_INDEX, "r", encoding="utf-8") as f:
        return f.read()

# ========================================================
# 1. UPGRADED CSS (Mobile 360px-430px viewports & Ergonomics)
# ========================================================
UPGRADED_MOBILE_CSS = '''        /* ======================================================== */
        /* PULSE LIVE ANIMATION & STATUS INDICATORS                 */
        /* ======================================================== */
        @keyframes pulseLive {
            0%, 100% { transform: scale(1); opacity: 1; box-shadow: 0 0 8px var(--accent-emerald); }
            50% { transform: scale(1.35); opacity: 0.55; box-shadow: 0 0 16px var(--accent-emerald); }
        }

        /* ======================================================== */
        /* MISSION CONTROL WELCOME HUD (#orbitFloatingHint)         */
        /* ======================================================== */
        .orbit-floating-hint {
            position: absolute;
            top: 4.8rem;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(10, 8, 14, 0.82);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(212, 168, 99, 0.35);
            border-radius: 18px;
            padding: 0.9rem 1.4rem 1rem;
            font-family: var(--font-sans);
            color: var(--text-secondary);
            margin: 0 auto;
            text-align: center;
            max-width: 620px;
            width: 92vw;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7), 0 0 25px rgba(212, 168, 99, 0.1);
            pointer-events: auto;
            z-index: 95;
            transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .orbit-floating-hint.fade-out {
            opacity: 0;
            pointer-events: none;
            transform: translate(-50%, -14px);
        }

        .hint-close-btn {
            position: absolute;
            top: 0.65rem;
            right: 0.75rem;
            width: 24px;
            height: 24px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-glass);
            border-radius: 50%;
            color: var(--text-secondary);
            font-size: 0.72rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }

        .hint-close-btn:hover {
            background: rgba(251, 113, 133, 0.2);
            border-color: #fb7185;
            color: #ffffff;
            transform: scale(1.1);
        }

        .hint-eyebrow {
            font-family: var(--font-mono);
            font-size: 0.64rem;
            color: var(--accent-gold);
            letter-spacing: 0.08em;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 0.35rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.45rem;
        }

        .hint-pulse-dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #10b981;
            animation: pulseLive 2s infinite;
        }

        .hint-headline {
            font-size: 0.98rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.01em;
            margin-bottom: 0.35rem;
            line-height: 1.35;
        }

        .hint-subtext {
            font-size: 0.72rem;
            color: var(--text-secondary);
            line-height: 1.45;
            margin-bottom: 0.75rem;
        }

        .hint-actions {
            display: flex;
            gap: 0.6rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .hint-pill-btn {
            background: rgba(212, 168, 99, 0.12);
            border: 1px solid rgba(212, 168, 99, 0.35);
            border-radius: 9999px;
            color: #f8fafc;
            font-size: 0.7rem;
            font-weight: 600;
            padding: 0.35rem 0.85rem;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }

        .hint-pill-btn:hover {
            background: rgba(212, 168, 99, 0.25);
            border-color: var(--accent-gold);
            transform: translateY(-1px);
            box-shadow: 0 4px 14px rgba(212, 168, 99, 0.25);
        }

        /* ======================================================== */
        /* INTERACTIVE TOOLS SUITE STYLES (#modalTools)             */
        /* ======================================================== */
        #modalTools {
            width: 94vw;
            max-width: 980px;
            max-height: 90vh;
        }

        .tools-suite-header {
            text-align: center;
            margin-bottom: 1.25rem;
        }

        .tools-suite-title {
            font-size: 1.15rem;
            color: #06b6d4;
            margin-bottom: 0.4rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }

        .tools-suite-subtitle {
            font-size: 0.82rem;
            color: var(--text-secondary);
            max-width: 580px;
            margin: 0 auto;
            line-height: 1.5;
        }

        .tools-tab-switcher {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 1.4rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 0.75rem;
            flex-wrap: wrap;
        }

        .tools-tab-btn {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-glass);
            border-radius: 9999px;
            padding: 0.45rem 1rem;
            color: var(--text-secondary);
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }

        .tools-tab-btn:hover {
            color: #ffffff;
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.2);
        }

        .tools-tab-btn.active {
            color: #06b6d4;
            background: rgba(6, 182, 212, 0.12);
            border-color: rgba(6, 182, 212, 0.45);
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
        }

        .tool-pane {
            animation: fadeInTool 0.25s ease-out;
        }

        @keyframes fadeInTool {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .tool-intro-box {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-glass);
            border-radius: 14px;
            padding: 0.85rem 1.15rem;
            margin-bottom: 1.25rem;
        }

        .tool-pane-title {
            font-size: 0.98rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }

        .tool-pane-desc {
            font-size: 0.78rem;
            color: var(--text-secondary);
            line-height: 1.5;
            margin: 0;
        }

        .tool-dedicated-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.42rem 0.9rem;
            font-family: var(--font-mono);
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--accent-gold);
            background: rgba(212, 168, 99, 0.1);
            border: 1px solid rgba(212, 168, 99, 0.4);
            border-radius: 9999px;
            text-decoration: none;
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .tool-dedicated-btn:hover {
            background: rgba(212, 168, 99, 0.22) !important;
            border-color: var(--accent-gold) !important;
            color: #ffffff !important;
            transform: translateY(-1px);
        }

        .tool-grid-layout {
            display: grid;
            grid-template-columns: 1.1fr 1fr;
            gap: 1.25rem;
            align-items: start;
        }

        .tool-inputs-card, .tool-results-card {
            background: rgba(255, 255, 255, 0.025);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 1.25rem;
        }

        .tool-input-group {
            margin-bottom: 1.1rem;
        }

        .tool-input-group:last-child {
            margin-bottom: 0;
        }

        .tool-label-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.45rem;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        .tool-input-label {
            display: block;
            margin-bottom: 0.45rem;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        .tool-val-display {
            font-family: var(--font-mono);
            font-size: 0.8rem;
            color: var(--accent-gold);
            font-weight: 700;
        }

        .tool-range-slider {
            width: 100%;
            height: 6px;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.1);
            outline: none;
            -webkit-appearance: none;
            cursor: pointer;
        }

        .tool-range-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--accent-gold);
            box-shadow: 0 0 10px rgba(212, 168, 99, 0.6);
            cursor: pointer;
            transition: transform 0.1s;
        }

        .tool-range-slider::-webkit-slider-thumb:hover {
            transform: scale(1.15);
        }

        .tool-pills-row {
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
        }

        .tool-pill-option {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            color: var(--text-secondary);
            font-size: 0.72rem;
            font-weight: 600;
            padding: 0.35rem 0.65rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .tool-pill-option:hover {
            color: #ffffff;
            background: rgba(255, 255, 255, 0.08);
        }

        .tool-pill-option.active {
            color: #06b6d4;
            background: rgba(6, 182, 212, 0.12);
            border-color: #06b6d4;
            box-shadow: 0 0 8px rgba(6, 182, 212, 0.25);
        }

        .tool-text-input {
            width: 100%;
            background: rgba(0, 0, 0, 0.35);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            padding: 0.5rem 0.75rem;
            color: #ffffff;
            font-family: var(--font-sans);
            font-size: 0.76rem;
            outline: none;
            transition: border-color 0.2s;
            box-sizing: border-box;
        }

        .tool-text-input:focus {
            border-color: #06b6d4;
            box-shadow: 0 0 8px rgba(6, 182, 212, 0.25);
        }

        .tool-kpis-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 0.85rem;
            margin-bottom: 1.15rem;
        }

        .tool-kpi-card {
            border-radius: 14px;
            padding: 1rem 1.15rem;
            border: 1px solid;
            transition: transform 0.2s ease;
        }

        .tool-kpi-card:hover {
            transform: translateY(-2px);
        }

        .tool-kpi-label {
            font-family: var(--font-mono);
            font-size: 0.65rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.3rem;
        }

        .tool-kpi-num {
            font-family: var(--font-mono);
            font-size: 1.35rem;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 0.25rem;
        }

        .tool-kpi-sub {
            font-size: 0.72rem;
            color: var(--text-secondary);
            line-height: 1.35;
        }

        .tool-cta-wrapper {
            margin-top: 1rem;
        }

        .tool-cta-btn {
            width: 100%;
            background: linear-gradient(135deg, rgba(212, 168, 99, 0.2), rgba(6, 182, 212, 0.15));
            border: 1px solid var(--accent-gold);
            border-radius: 10px;
            color: #ffffff;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.65rem 1rem;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }

        .tool-cta-btn:hover {
            background: linear-gradient(135deg, rgba(212, 168, 99, 0.35), rgba(6, 182, 212, 0.3));
            box-shadow: 0 4px 18px rgba(212, 168, 99, 0.3);
            transform: translateY(-1px);
        }

        .terminal-block {
            background: rgba(0, 0, 0, 0.45);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            overflow: hidden;
        }

        .terminal-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.5rem 0.85rem;
            background: rgba(255, 255, 255, 0.03);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }

        .terminal-tag {
            font-family: var(--font-mono);
            font-size: 0.64rem;
            color: #06b6d4;
            font-weight: 700;
            letter-spacing: 0.05em;
        }

        .terminal-copy-btn {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-glass);
            border-radius: 6px;
            color: var(--text-secondary);
            font-size: 0.68rem;
            padding: 0.2rem 0.55rem;
            cursor: pointer;
            transition: all 0.2s;
        }

        .terminal-copy-btn:hover {
            color: #ffffff;
            background: rgba(255, 255, 255, 0.12);
        }

        /* Mobile Adjustments & Small Screen Ergonomics (360px - 430px) */
        @media (max-width: 900px) {
            .hud-matrix {
                padding: max(0.6rem, calc(env(safe-area-inset-top) + 0.25rem)) 0.65rem max(0.6rem, calc(env(safe-area-inset-bottom) + 0.25rem)) 0.65rem;
            }

            .hud-header {
                padding: 0.4rem 0.75rem;
                gap: 0.5rem;
            }

            .brand-name { font-size: 0.92rem; }

            .brand-tag-badge {
                max-width: 28vw;
                font-size: 0.52rem;
            }

            .orbit-floating-hint {
                display: block !important;
                top: 4.5rem;
                left: 50%;
                transform: translateX(-50%);
                width: 94vw;
                max-width: 480px;
                padding: 0.75rem 1rem 0.85rem;
                border-radius: 16px;
            }

            .orbit-floating-hint.fade-out {
                opacity: 0;
                pointer-events: none;
                transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1);
                transform: translate(-50%, -10px);
            }

            .spatial-modal-card {
                width: 96vw;
                max-height: 86vh;
                border-radius: 20px;
            }

            #modalServices, #modalTools {
                width: 95vw;
                max-height: 88vh;
                border-radius: 24px;
            }

            #modalServices .modal-body-scroll, #modalTools .modal-body-scroll {
                padding: 1.35rem 1.3rem 1.85rem;
                gap: 1.15rem;
            }

            .services-cards-grid, .tool-grid-layout {
                grid-template-columns: 1fr;
                gap: 1.15rem;
            }

            .tool-kpis-grid {
                grid-template-columns: 1fr !important;
            }

            .service-feature-card {
                padding: 1.35rem 1.35rem 1.25rem;
            }

            .services-cta-banner {
                flex-direction: column;
                align-items: stretch;
                padding: 1.3rem;
                gap: 1rem;
            }

            .services-cta-banner-actions {
                width: 100%;
            }

            .services-cta-banner-actions button,
            .services-cta-banner-actions a {
                flex: 1;
                text-align: center;
                justify-content: center;
            }

            .hud-dock-bottom {
                bottom: max(0.4rem, env(safe-area-inset-bottom));
            }

            .dock-pill-bar {
                max-width: 96vw;
                padding: 0.35rem 0.5rem;
                gap: 0.3rem;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }

            .dock-pill-btn {
                flex-shrink: 0;
                padding: 0.35rem 0.65rem;
                font-size: 0.72rem;
                white-space: nowrap;
            }

            .spatial-chat-dock {
                width: 95vw;
                max-width: 420px;
                height: 82vh;
                top: 50%;
                left: 50%;
                bottom: auto;
                right: auto;
                transform: translate(-50%, -50%) scale(0.92);
                border-radius: 20px;
                z-index: 1001;
            }

            .spatial-chat-dock.active {
                transform: translate(-50%, -50%) scale(1);
            }

            .floating-chat-trigger {
                bottom: 4.8rem;
                right: 0.75rem;
                padding: 4px 10px 4px 5px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
            }

            #planetInspectHUD {
                top: auto;
                bottom: 4.8rem;
                left: 0.75rem;
                right: 0.75rem;
                max-width: none;
                padding: 0.9rem 1.1rem;
                border-radius: 16px;
            }

            .inspect-title { font-size: 1.12rem; }
            .inspect-desc { font-size: 0.78rem; margin-bottom: 0.75rem; }

            .pipeline-nodes-track {
                grid-template-columns: 1fr;
            }

            .planet-screen-label {
                font-size: 0.62rem;
                padding: 2px 7px;
            }
        }

        /* Narrow viewports (360px - 430px iPhone & Android devices) */
        @media (max-width: 480px) {
            .hud-header {
                padding: 0.3rem 0.55rem;
                gap: 0.35rem;
            }

            .brand-name {
                font-size: 0.84rem;
            }

            .brand-tag-badge {
                display: none; /* Hide badge on narrowest mobile screens so controls never overflow */
            }

            .hud-header-actions {
                gap: 0.35rem;
            }

            .hud-action-pill {
                padding: 0.28rem 0.55rem;
                font-size: 0.60rem;
                gap: 0.25rem;
            }

            .lang-switcher {
                padding: 1px 3px;
                gap: 1px;
            }

            .lang-btn {
                padding: 2px 6px;
                font-size: 0.60rem;
            }

            .dock-pill-bar {
                padding: 0.3rem 0.4rem;
                gap: 0.25rem;
            }

            .dock-pill-btn {
                flex-shrink: 0;
                padding: 0.3rem 0.55rem;
                font-size: 0.68rem;
                gap: 0.25rem;
            }

            .orbit-floating-hint {
                top: 4.2rem;
                padding: 0.65rem 0.85rem 0.75rem;
            }

            .hint-headline {
                font-size: 0.88rem;
            }

            .hint-subtext {
                font-size: 0.66rem;
            }

            .hint-pill-btn {
                padding: 0.28rem 0.6rem;
                font-size: 0.64rem;
            }

            .floating-chat-trigger {
                bottom: 4.4rem;
                right: 0.5rem;
            }

            #planetInspectHUD {
                bottom: 4.4rem;
                left: 0.5rem;
                right: 0.5rem;
                padding: 0.8rem;
            }

            .inspect-btn, .inspect-btn-secondary {
                padding: 0.4rem 0.75rem;
                font-size: 0.64rem;
            }

            #modalServices, #modalTools {
                width: 96vw;
                max-height: 90vh;
                border-radius: 20px;
            }

            #modalServices .modal-top-bar, #modalTools .modal-top-bar {
                padding: 1rem 1.15rem;
            }

            .modal-title-text {
                font-size: 1.02rem;
            }

            #modalServices .modal-body-scroll, #modalTools .modal-body-scroll {
                padding: 1rem 0.85rem 1.5rem;
                gap: 1rem;
            }

            .tools-tab-btn {
                padding: 0.35rem 0.7rem;
                font-size: 0.7rem;
            }

            .tool-inputs-card, .tool-results-card {
                padding: 0.95rem;
            }

            .service-feature-card {
                padding: 1.2rem 1.05rem;
            }

            .service-card-title {
                font-size: 1.02rem;
            }

            .service-btn-primary,
            .service-btn-secondary {
                flex: 1 1 100%;
                width: 100%;
            }
        }

        /* Ultra-narrow viewports (320px - 375px small screens) */
        @media (max-width: 375px) {
            .hud-header {
                padding: 0.25rem 0.4rem;
                gap: 0.25rem;
            }
            .brand-name {
                font-size: 0.78rem;
            }
            .hud-action-pill {
                padding: 0.22rem 0.4rem;
                font-size: 0.56rem;
            }
            .lang-btn {
                padding: 1px 4px;
                font-size: 0.56rem;
            }
        }
    </style>'''

# ========================================================
# 2. UPGRADED PROCEDURAL TEXTURES & SHADERS (Sun & Planets)
# ========================================================
UPGRADED_TEXTURE_AND_SHADER_ENGINE = '''        // ========================================================
        // 3. PHOTOREALISTIC SOLAR & PLANETARY PROCEDURAL TEXTURE ENGINE
        // ========================================================

        // --- THE SUN: Photorealistic Star Shaders ---
        const sunVertexShader = `
            varying vec2 vUv;
            varying vec3 vNormal;
            varying vec3 vPosition;
            varying vec3 vWorldNormal;
            varying vec3 vWorldPosition;

            void main() {
                vUv = uv;
                vNormal = normalize(normalMatrix * normal);
                vPosition = position;
                vec4 worldPos = modelMatrix * vec4(position, 1.0);
                vWorldPosition = worldPos.xyz;
                vWorldNormal = normalize((modelMatrix * vec4(normal, 0.0)).xyz);
                gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
            }
        `;

        const sunFragmentShader = `
            precision highp float;

            uniform float uTime;
            varying vec2 vUv;
            varying vec3 vNormal;
            varying vec3 vPosition;
            varying vec3 vWorldNormal;
            varying vec3 vWorldPosition;

            // Ultra-fast analytical 3D hash & value noise for 60 FPS mobile rendering
            float sunHash(vec3 p) {
                p = fract(p * vec3(443.897, 441.423, 437.195));
                p += dot(p, p.yzx + 19.19);
                return fract((p.x + p.y) * p.z);
            }

            float sunNoise(vec3 p) {
                vec3 i = floor(p);
                vec3 f = fract(p);
                vec3 u = f * f * (3.0 - 2.0 * f);
                float n000 = sunHash(i + vec3(0.0, 0.0, 0.0));
                float n100 = sunHash(i + vec3(1.0, 0.0, 0.0));
                float n010 = sunHash(i + vec3(0.0, 1.0, 0.0));
                float n110 = sunHash(i + vec3(1.0, 1.0, 0.0));
                float n001 = sunHash(i + vec3(0.0, 0.0, 1.0));
                float n101 = sunHash(i + vec3(1.0, 0.0, 1.0));
                float n011 = sunHash(i + vec3(0.0, 1.0, 1.0));
                float n111 = sunHash(i + vec3(1.0, 1.0, 1.0));
                return mix(
                    mix(mix(n000, n100, u.x), mix(n010, n110, u.x), u.y),
                    mix(mix(n001, n101, u.x), mix(n011, n111, u.x), u.y),
                    u.z
                );
            }

            float sunFbm(vec3 p) {
                float v = 0.0;
                v += 0.5000 * sunNoise(p); p = p * 2.02 + vec3(0.12, 0.23, 0.34);
                v += 0.2500 * sunNoise(p); p = p * 2.03 + vec3(0.34, 0.45, 0.56);
                v += 0.1250 * sunNoise(p); p = p * 2.01 + vec3(0.56, 0.67, 0.78);
                v += 0.0625 * sunNoise(p);
                return v;
            }

            void main() {
                vec3 normPos = normalize(vPosition);
                vec3 viewDir = normalize(cameraPosition - vWorldPosition);
                float NdotV = max(0.0, dot(vWorldNormal, viewDir));

                // 1. Limb Darkening (Eddington-Barbier physical solar photosphere model)
                float limbDarkening = pow(NdotV, 0.52);

                // 2. Chromosphere Fresnel Rim Flare at grazing angle
                float fresnel = pow(1.0 - NdotV, 3.2);

                // 3. Multi-Octave Convective Solar Granulation
                // Differential solar rotation
                float rot = uTime * 0.04;
                mat2 rotMat = mat2(cos(rot), -sin(rot), sin(rot), cos(rot));
                vec3 rotPos = vec3(rotMat * normPos.xz, normPos.y).xzy;

                // Domain-warped turbulent magnetic plasma flow
                vec3 warp = vec3(
                    sunFbm(rotPos * 3.5 + vec3(0.0, uTime * 0.06, 0.0)),
                    sunFbm(rotPos * 3.5 + vec3(4.3, 1.7, uTime * 0.05)),
                    sunFbm(rotPos * 3.5 + vec3(1.9, uTime * 0.07, 3.1))
                );

                // High-frequency convective cellular granulation
                float gran1 = sunNoise(rotPos * 22.0 + warp * 2.2 + vec3(uTime * 0.08));
                float gran2 = sunNoise(rotPos * 44.0 - warp * 1.8 - vec3(uTime * 0.12));
                float granulation = smoothstep(0.32, 0.78, gran1 * 0.65 + gran2 * 0.35);

                // 4. Turbulent Solar Magnetic Flares & Prominence Filaments
                float flareField1 = sunFbm(rotPos * 2.8 + vec3(uTime * 0.05, -uTime * 0.03, uTime * 0.06));
                float flareField2 = sunFbm(rotPos * 5.6 - vec3(uTime * 0.08, uTime * 0.06, -uTime * 0.07));
                float flareFilaments = pow(abs(flareField1 * 0.7 + flareField2 * 0.3), 1.7);
                float flareSurge = smoothstep(0.42, 0.72, flareFilaments);

                // 5. Equatorial Sunspots (cooler magnetic flux tubes)
                float spotLatMask = smoothstep(0.55, 0.20, abs(normPos.y));
                float spotNoise = sunNoise(rotPos * 3.8 + vec3(8.5, 0.0, 3.2));
                float sunspots = smoothstep(0.70, 0.85, spotNoise) * spotLatMask;

                // 6. Deep Incandescent Blackbody Spectrum Color Grading
                vec3 colCoreWhite  = vec3(1.00, 0.98, 0.92);
                vec3 colHotGold    = vec3(1.00, 0.80, 0.22);
                vec3 colOrange     = vec3(0.96, 0.44, 0.06);
                vec3 colDarkRed    = vec3(0.62, 0.11, 0.02);
                vec3 colSunspot    = vec3(0.18, 0.03, 0.01);
                vec3 colChromRim   = vec3(1.00, 0.88, 0.60);

                // Base convective granulation mix
                vec3 starColor = mix(colDarkRed, colOrange, granulation);
                starColor = mix(starColor, colHotGold, smoothstep(0.45, 0.85, granulation + flareFilaments * 0.35));

                // Flare surges (thermonuclear white-hot surges)
                starColor = mix(starColor, colCoreWhite, flareSurge * 0.90);

                // Sunspots (cool dark magnetic umbra)
                starColor = mix(starColor, colSunspot, sunspots * 0.88);

                // Physical Limb Darkening & Chromospheric Rim Flare
                starColor *= mix(0.58, 1.0, limbDarkening);
                starColor += colChromRim * fresnel * 1.55;

                // Subtle thermal oscillation
                starColor *= (1.0 + 0.03 * sin(uTime * 2.2));

                gl_FragColor = vec4(starColor, 1.0);
            }
        `;

        const chromosphereVertexShader = `
            varying vec3 vNormal;
            varying vec3 vPosition;
            void main() {
                vNormal = normalize(normalMatrix * normal);
                vPosition = (modelViewMatrix * vec4(position, 1.0)).xyz;
                gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
            }
        `;

        const chromosphereFragmentShader = `
            precision highp float;
            uniform float uTime;
            varying vec3 vNormal;
            varying vec3 vPosition;

            void main() {
                vec3 viewDir = normalize(-vPosition);
                float rim = pow(1.0 - max(0.0, dot(vNormal, viewDir)), 2.6);
                float pulse = 0.85 + 0.15 * sin(uTime * 2.8 + vPosition.x * 0.2);
                vec3 chromoColor = vec3(1.0, 0.65, 0.18) * rim * 1.8 * pulse;
                gl_FragColor = vec4(chromoColor, rim * 0.95);
            }
        `;

        function createCoronaTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            const cGrad = ctx.createRadialGradient(256, 256, 0, 256, 256, 256);
            cGrad.addColorStop(0, 'rgba(255, 250, 230, 0.98)');
            cGrad.addColorStop(0.12, 'rgba(254, 220, 150, 0.75)');
            cGrad.addColorStop(0.25, 'rgba(245, 158, 11, 0.45)');
            cGrad.addColorStop(0.50, 'rgba(217, 119, 6, 0.18)');
            cGrad.addColorStop(0.75, 'rgba(180, 83, 9, 0.05)');
            cGrad.addColorStop(1, 'transparent');
            ctx.fillStyle = cGrad;
            ctx.fillRect(0, 0, 512, 512);

            // Subtle radial coronal streamers
            ctx.strokeStyle = 'rgba(255, 230, 160, 0.12)';
            ctx.lineWidth = 1.5;
            for (let i = 0; i < 48; i++) {
                const angle = (i / 48) * Math.PI * 2;
                const len = 140 + Math.sin(i * 1.7) * 90;
                ctx.beginPath();
                ctx.moveTo(256 + Math.cos(angle) * 35, 256 + Math.sin(angle) * 35);
                ctx.lineTo(256 + Math.cos(angle) * len, 256 + Math.sin(angle) * len);
                ctx.stroke();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createSunTexture() {
            // High-resolution canvas texture kept for fallback compatibility
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 0, 512);
            grad.addColorStop(0, '#fef08a');
            grad.addColorStop(0.3, '#f59e0b');
            grad.addColorStop(0.7, '#d97706');
            grad.addColorStop(1, '#fef08a');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 1024, 512);
            return new THREE.CanvasTexture(canvas);
        }

        // --- PROCEDURAL IMPACT CRATER GENERATOR ---
        function drawImpactCrater(ctx, x, y, radius, isBump) {
            ctx.save();
            if (isBump) {
                // Exterior ejecta blanket (slight rise above surface)
                const ejecta = ctx.createRadialGradient(x, y, radius * 0.9, x, y, radius * 1.45);
                ejecta.addColorStop(0, '#707070');
                ejecta.addColorStop(1, 'transparent');
                ctx.fillStyle = ejecta;
                ctx.beginPath(); ctx.arc(x, y, radius * 1.45, 0, Math.PI * 2); ctx.fill();

                // Elevated circular crater rim wall (high bump)
                const rim = ctx.createRadialGradient(x, y, radius * 0.75, x, y, radius);
                rim.addColorStop(0, '#505050');
                rim.addColorStop(0.85, '#e0e0e0');
                rim.addColorStop(1, '#606060');
                ctx.fillStyle = rim;
                ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();

                // Deep excavated cavity depression floor (dark cavity)
                const floor = ctx.createRadialGradient(x, y, 0, x, y, radius * 0.75);
                floor.addColorStop(0, '#101010');
                floor.addColorStop(0.7, '#151515');
                floor.addColorStop(1, '#505050');
                ctx.fillStyle = floor;
                ctx.beginPath(); ctx.arc(x, y, radius * 0.75, 0, Math.PI * 2); ctx.fill();

                // Central rebound peak for larger craters
                if (radius > 16) {
                    const peak = ctx.createRadialGradient(x, y, 0, x, y, radius * 0.22);
                    peak.addColorStop(0, '#c0c0c0');
                    peak.addColorStop(1, 'transparent');
                    ctx.fillStyle = peak;
                    ctx.beginPath(); ctx.arc(x, y, radius * 0.22, 0, Math.PI * 2); ctx.fill();
                }
            } else {
                // Albedo / Visual Crater
                ctx.strokeStyle = '#991b1b';
                ctx.lineWidth = Math.max(1.5, radius * 0.15);
                ctx.beginPath(); ctx.arc(x, y, radius * 0.9, 0, Math.PI * 2); ctx.stroke();

                const floor = ctx.createRadialGradient(x - radius * 0.2, y - radius * 0.2, 0, x, y, radius * 0.85);
                floor.addColorStop(0, '#1c0709');
                floor.addColorStop(0.8, '#2e0a0e');
                floor.addColorStop(1, '#450a0a');
                ctx.fillStyle = floor;
                ctx.beginPath(); ctx.arc(x, y, radius * 0.85, 0, Math.PI * 2); ctx.fill();

                if (radius > 16) {
                    ctx.fillStyle = '#7f1d1d';
                    ctx.beginPath(); ctx.arc(x, y, radius * 0.2, 0, Math.PI * 2); ctx.fill();
                }

                // Subtle radial ejecta rays
                ctx.strokeStyle = 'rgba(127, 29, 29, 0.25)';
                ctx.lineWidth = 1.0;
                for (let r = 0; r < 8; r++) {
                    const ang = (r / 8) * Math.PI * 2 + (x * 0.01);
                    ctx.beginPath();
                    ctx.moveTo(x + Math.cos(ang) * radius, y + Math.sin(ang) * radius);
                    ctx.lineTo(x + Math.cos(ang) * radius * 1.8, y + Math.sin(ang) * radius * 1.8);
                    ctx.stroke();
                }
            }
            ctx.restore();
        }

        // --- CONCENTRIC RING GEOMETRY HELPER ---
        function createConcentricRingGeometry(innerRadius, outerRadius, thetaSegments) {
            const geo = new THREE.RingGeometry(innerRadius, outerRadius, thetaSegments);
            const pos = geo.attributes.position;
            const uvs = geo.attributes.uv;
            for (let i = 0; i < pos.count; i++) {
                const x = pos.getX(i);
                const y = pos.getY(i);
                const dist = Math.sqrt(x * x + y * y);
                const u = (dist - innerRadius) / (outerRadius - innerRadius);
                uvs.setXY(i, u, 0.5);
            }
            return geo;
        }

        // --- 1. GAS GIANT TEXTURE (AI Dialogue) ---
        function createGasGiantTexture(colorHex1, colorHex2, colorHex3, stormColor) {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            // 1. Zonal atmospheric jet stream bands
            for (let y = 0; y < 512; y++) {
                const n = Math.sin(y * 0.08) * 0.45 + Math.sin(y * 0.18 + Math.cos(y * 0.03) * 2.2) * 0.35 + Math.sin(y * 0.02) * 0.20;
                let c = colorHex1;
                if (n > 0.25) c = colorHex2;
                else if (n < -0.2) c = colorHex3;
                ctx.fillStyle = c;
                ctx.fillRect(0, y, 1024, 1);
            }

            // 2. Micro-shear turbulence along zonal boundaries
            for (let i = 0; i < 40; i++) {
                const by = Math.floor(Math.random() * 480) + 16;
                ctx.fillStyle = i % 2 === 0 ? colorHex2 : colorHex3;
                ctx.globalAlpha = 0.45;
                ctx.beginPath();
                ctx.moveTo(0, by);
                for (let x = 0; x <= 1024; x += 16) {
                    const wy = by + Math.sin(x * 0.05 + i) * 6 + Math.cos(x * 0.02) * 4;
                    ctx.lineTo(x, wy);
                }
                ctx.lineTo(1024, by + 12);
                ctx.lineTo(0, by + 12);
                ctx.closePath();
                ctx.fill();
            }
            ctx.globalAlpha = 1.0;

            // 3. The Great Storm Oval Vortex
            const stormX = 640;
            const stormY = 320;
            const stormW = 85;
            const stormH = 40;

            const sg = ctx.createRadialGradient(stormX, stormY, 0, stormX, stormY, stormW);
            sg.addColorStop(0, '#ffffff');
            sg.addColorStop(0.3, stormColor || colorHex3);
            sg.addColorStop(0.7, colorHex2);
            sg.addColorStop(1, 'transparent');
            ctx.fillStyle = sg;
            ctx.beginPath();
            ctx.ellipse(stormX, stormY, stormW, stormH, 0.08, 0, Math.PI * 2);
            ctx.fill();

            // Storm spiral arms
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
            ctx.lineWidth = 2.0;
            for (let r = 8; r <= 32; r += 8) {
                ctx.beginPath();
                ctx.ellipse(stormX + (r % 16 - 8), stormY, r * 1.8, r * 0.9, 0.12, 0, Math.PI * 2);
                ctx.stroke();
            }

            // 4. White anticyclonic storm ovals
            for (let j = 0; j < 8; j++) {
                const ox = (j * 140 + 75) % 1024;
                const oy = 120 + (j * 43) % 280;
                const ow = 14 + (j % 4) * 6;
                const oh = 6 + (j % 3) * 3;
                const og = ctx.createRadialGradient(ox, oy, 0, ox, oy, ow);
                og.addColorStop(0, 'rgba(255, 255, 255, 0.85)');
                og.addColorStop(0.6, 'rgba(255, 255, 255, 0.25)');
                og.addColorStop(1, 'transparent');
                ctx.fillStyle = og;
                ctx.beginPath();
                ctx.ellipse(ox, oy, ow, oh, 0, 0, Math.PI * 2);
                ctx.fill();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createGasGiantBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#808080';
            ctx.fillRect(0, 0, 1024, 512);

            for (let y = 0; y < 512; y++) {
                const n = Math.sin(y * 0.08) * 0.5 + Math.sin(y * 0.18) * 0.3;
                const val = Math.floor(128 + n * 40);
                ctx.fillStyle = `rgb(${val},${val},${val})`;
                ctx.fillRect(0, y, 1024, 1);
            }
            return new THREE.CanvasTexture(canvas);
        }

        // --- 2. SERVICES NEXUS TEXTURE (Services) ---
        function createServicesNexusTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#022c22';
            ctx.fillRect(0, 0, 1024, 512);

            // Tectonic cyber plates
            ctx.fillStyle = '#064e3b';
            for (let i = 0; i < 22; i++) {
                const px = (i * 120 + 30) % 1024;
                const py = 60 + (i * 55) % 400;
                const pr = 45 + (i % 5) * 20;
                ctx.beginPath();
                ctx.arc(px, py, pr, 0, Math.PI * 2);
                ctx.fill();
            }

            // Neural circuit network
            ctx.strokeStyle = 'rgba(52, 211, 153, 0.45)';
            ctx.lineWidth = 1.4;
            for (let x = 0; x < 1024; x += 32) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
            }
            for (let y = 0; y < 512; y += 32) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(1024, y); ctx.stroke();
            }

            // Arterial data highways
            ctx.strokeStyle = '#10b981';
            ctx.lineWidth = 2.8;
            for (let h = 0; h < 6; h++) {
                const hy = 80 + h * 65;
                ctx.beginPath();
                ctx.moveTo(0, hy);
                ctx.lineTo(300, hy);
                ctx.lineTo(380, hy + 40);
                ctx.lineTo(750, hy + 40);
                ctx.lineTo(820, hy);
                ctx.lineTo(1024, hy);
                ctx.stroke();
            }

            // 4 Primary Freelance Service Nexus Core Nodes
            const hubs = [
                { x: 220, y: 180, label: 'CRM', col: '#f59e0b' },
                { x: 480, y: 310, label: 'ADS', col: '#10b981' },
                { x: 740, y: 200, label: 'SEO', col: '#34d399' },
                { x: 890, y: 360, label: 'BI',  col: '#fbbf24' }
            ];
            hubs.forEach(hub => {
                const hg = ctx.createRadialGradient(hub.x, hub.y, 0, hub.x, hub.y, 28);
                hg.addColorStop(0, '#ffffff');
                hg.addColorStop(0.3, hub.col);
                hg.addColorStop(0.7, '#064e3b');
                hg.addColorStop(1, 'transparent');
                ctx.fillStyle = hg;
                ctx.beginPath();
                ctx.arc(hub.x, hub.y, 26, 0, Math.PI * 2);
                ctx.fill();

                // Concentric beacon pulses
                for (let r = 8; r <= 36; r += 10) {
                    ctx.strokeStyle = hub.col;
                    ctx.lineWidth = 1.2;
                    ctx.beginPath();
                    ctx.arc(hub.x, hub.y, r, 0, Math.PI * 2);
                    ctx.stroke();
                }
            });

            // Secondary synaptic nodes
            for (let k = 0; k < 60; k++) {
                const nx = Math.floor(Math.random() * 32) * 32;
                const ny = Math.floor(Math.random() * 16) * 32;
                const ng = ctx.createRadialGradient(nx, ny, 0, nx, ny, 8);
                ng.addColorStop(0, '#ffffff');
                ng.addColorStop(0.4, '#34d399');
                ng.addColorStop(1, 'transparent');
                ctx.fillStyle = ng;
                ctx.beginPath();
                ctx.arc(nx, ny, 7, 0, Math.PI * 2);
                ctx.fill();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createServicesNexusEmissiveTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.strokeStyle = '#059669';
            ctx.lineWidth = 2.0;
            for (let h = 0; h < 6; h++) {
                const hy = 80 + h * 65;
                ctx.beginPath();
                ctx.moveTo(0, hy);
                ctx.lineTo(300, hy);
                ctx.lineTo(380, hy + 40);
                ctx.lineTo(750, hy + 40);
                ctx.lineTo(820, hy);
                ctx.lineTo(1024, hy);
                ctx.stroke();
            }

            const hubs = [
                { x: 220, y: 180, col: '#f59e0b' },
                { x: 480, y: 310, col: '#10b981' },
                { x: 740, y: 200, col: '#34d399' },
                { x: 890, y: 360, col: '#fbbf24' }
            ];
            hubs.forEach(hub => {
                const hg = ctx.createRadialGradient(hub.x, hub.y, 0, hub.x, hub.y, 24);
                hg.addColorStop(0, '#ffffff');
                hg.addColorStop(0.5, hub.col);
                hg.addColorStop(1, 'transparent');
                ctx.fillStyle = hg;
                ctx.beginPath();
                ctx.arc(hub.x, hub.y, 22, 0, Math.PI * 2);
                ctx.fill();
            });

            for (let k = 0; k < 60; k++) {
                const nx = Math.floor(Math.random() * 32) * 32;
                const ny = Math.floor(Math.random() * 16) * 32;
                ctx.fillStyle = '#34d399';
                ctx.beginPath();
                ctx.arc(nx, ny, 3.5, 0, Math.PI * 2);
                ctx.fill();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createServicesNexusBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#404040';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.fillStyle = '#808080';
            for (let i = 0; i < 22; i++) {
                const px = (i * 120 + 30) % 1024;
                const py = 60 + (i * 55) % 400;
                const pr = 45 + (i % 5) * 20;
                ctx.beginPath();
                ctx.arc(px, py, pr, 0, Math.PI * 2);
                ctx.fill();
            }

            ctx.strokeStyle = '#c0c0c0';
            ctx.lineWidth = 3.0;
            for (let h = 0; h < 6; h++) {
                const hy = 80 + h * 65;
                ctx.beginPath();
                ctx.moveTo(0, hy);
                ctx.lineTo(300, hy);
                ctx.lineTo(380, hy + 40);
                ctx.lineTo(750, hy + 40);
                ctx.lineTo(820, hy);
                ctx.lineTo(1024, hy);
                ctx.stroke();
            }
            return new THREE.CanvasTexture(canvas);
        }

        // --- 3. TERRESTRIAL TEXTURES (Experience) ---
        function createEarthTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            // 1. Deep Ocean Base
            ctx.fillStyle = '#023e8a';
            ctx.fillRect(0, 0, 1024, 512);

            // 2. Continental Shelf / Shallow Turquoise Seas
            const landmasses = [
                { x: 220, y: 190, r: 85 },
                { x: 300, y: 310, r: 65 },
                { x: 580, y: 180, r: 105 },
                { x: 680, y: 220, r: 90 },
                { x: 740, y: 340, r: 55 },
                { x: 450, y: 200, r: 50 },
                { x: 140, y: 140, r: 45 }
            ];

            landmasses.forEach(lm => {
                const shelfG = ctx.createRadialGradient(lm.x, lm.y, lm.r * 0.8, lm.x, lm.y, lm.r * 1.35);
                shelfG.addColorStop(0, '#00b4d8');
                shelfG.addColorStop(0.6, '#0077b6');
                shelfG.addColorStop(1, 'transparent');
                ctx.fillStyle = shelfG;
                ctx.beginPath();
                ctx.arc(lm.x, lm.y, lm.r * 1.35, 0, Math.PI * 2);
                ctx.fill();
            });

            // 3. Continents & Biomes
            landmasses.forEach(lm => {
                ctx.fillStyle = '#1b4332';
                ctx.beginPath(); ctx.arc(lm.x, lm.y, lm.r, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = '#2d6a4f';
                ctx.beginPath(); ctx.arc(lm.x + 10, lm.y - 12, lm.r * 0.75, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = '#d4a373';
                ctx.beginPath(); ctx.arc(lm.x - 8, lm.y + 10, lm.r * 0.45, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = '#6c757d';
                ctx.beginPath(); ctx.ellipse(lm.x + 5, lm.y - 5, lm.r * 0.4, lm.r * 0.15, 0.45, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = '#ffffff';
                ctx.beginPath(); ctx.ellipse(lm.x + 5, lm.y - 5, lm.r * 0.22, lm.r * 0.08, 0.45, 0, Math.PI * 2); ctx.fill();
            });

            // 4. Polar Ice Caps with Glacial Fractures
            ctx.fillStyle = '#f8fafc';
            ctx.fillRect(0, 0, 1024, 42);
            ctx.fillRect(0, 470, 1024, 42);

            ctx.strokeStyle = '#cbd5e1';
            ctx.lineWidth = 1.2;
            for (let x = 0; x < 1024; x += 40) {
                ctx.beginPath(); ctx.moveTo(x, 42); ctx.lineTo(x + 15, 52); ctx.lineTo(x + 35, 42); ctx.stroke();
                ctx.beginPath(); ctx.moveTo(x, 470); ctx.lineTo(x + 20, 460); ctx.lineTo(x + 40, 470); ctx.stroke();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createEarthBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#202020';
            ctx.fillRect(0, 0, 1024, 512);

            const landmasses = [
                { x: 220, y: 190, r: 85 },
                { x: 300, y: 310, r: 65 },
                { x: 580, y: 180, r: 105 },
                { x: 680, y: 220, r: 90 },
                { x: 740, y: 340, r: 55 },
                { x: 450, y: 200, r: 50 },
                { x: 140, y: 140, r: 45 }
            ];

            landmasses.forEach(lm => {
                ctx.fillStyle = '#606060';
                ctx.beginPath(); ctx.arc(lm.x, lm.y, lm.r, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = '#b0b0b0';
                ctx.beginPath(); ctx.ellipse(lm.x + 5, lm.y - 5, lm.r * 0.45, lm.r * 0.18, 0.45, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = '#ffffff';
                ctx.beginPath(); ctx.ellipse(lm.x + 5, lm.y - 5, lm.r * 0.22, lm.r * 0.08, 0.45, 0, Math.PI * 2); ctx.fill();
            });

            ctx.fillStyle = '#909090';
            ctx.fillRect(0, 0, 1024, 42);
            ctx.fillRect(0, 470, 1024, 42);

            return new THREE.CanvasTexture(canvas);
        }

        function createEarthRoughnessTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#101010'; // Oceans ultra-glossy / low roughness for brilliant sun specular glint
            ctx.fillRect(0, 0, 1024, 512);

            const landmasses = [
                { x: 220, y: 190, r: 85 },
                { x: 300, y: 310, r: 65 },
                { x: 580, y: 180, r: 105 },
                { x: 680, y: 220, r: 90 },
                { x: 740, y: 340, r: 55 },
                { x: 450, y: 200, r: 50 },
                { x: 140, y: 140, r: 45 }
            ];

            landmasses.forEach(lm => {
                ctx.fillStyle = '#c0c0c0'; // Land diffuse / high roughness
                ctx.beginPath(); ctx.arc(lm.x, lm.y, lm.r, 0, Math.PI * 2); ctx.fill();
            });

            ctx.fillStyle = '#606060';
            ctx.fillRect(0, 0, 1024, 42);
            ctx.fillRect(0, 470, 1024, 42);

            return new THREE.CanvasTexture(canvas);
        }

        function createEarthLightsTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, 1024, 512);

            const cityClusters = [
                { x: 220, y: 180 }, { x: 240, y: 200 }, { x: 200, y: 190 },
                { x: 560, y: 170 }, { x: 590, y: 190 }, { x: 610, y: 160 },
                { x: 670, y: 210 }, { x: 700, y: 230 }, { x: 720, y: 200 },
                { x: 300, y: 300 }, { x: 320, y: 320 }, { x: 740, y: 330 }
            ];

            cityClusters.forEach(c => {
                for (let i = 0; i < 20; i++) {
                    const cx = c.x + (Math.random() - 0.5) * 55;
                    const cy = c.y + (Math.random() - 0.5) * 45;
                    const cg = ctx.createRadialGradient(cx, cy, 0, cx, cy, 5);
                    cg.addColorStop(0, '#fef08a');
                    cg.addColorStop(0.5, '#f59e0b');
                    cg.addColorStop(1, 'transparent');
                    ctx.fillStyle = cg;
                    ctx.beginPath();
                    ctx.arc(cx, cy, 4, 0, Math.PI * 2);
                    ctx.fill();
                }
            });

            return new THREE.CanvasTexture(canvas);
        }

        function createEarthCloudsTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, 1024, 512);

            ctx.fillStyle = 'rgba(255, 255, 255, 0.42)';
            for (let i = 0; i < 160; i++) {
                const x = Math.random() * 1024;
                const y = 50 + Math.random() * 412;
                const rw = 30 + Math.random() * 85;
                const rh = 8 + Math.random() * 22;
                ctx.beginPath();
                ctx.ellipse(x, y, rw, rh, (Math.random() - 0.5) * 0.35, 0, Math.PI * 2);
                ctx.fill();
            }

            // Swirling cyclone storm vortices
            const storms = [{ x: 380, y: 160 }, { x: 800, y: 280 }];
            storms.forEach(st => {
                for (let a = 0; a < 14; a++) {
                    const ang = a * 0.5;
                    const dist = a * 4;
                    const sx = st.x + Math.cos(ang) * dist;
                    const sy = st.y + Math.sin(ang) * dist * 0.55;
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.75)';
                    ctx.beginPath();
                    ctx.ellipse(sx, sy, 16 + a * 1.5, 7 + a * 0.8, ang, 0, Math.PI * 2);
                    ctx.fill();
                }
            });

            return new THREE.CanvasTexture(canvas);
        }

        // --- 4. CYBERNETIC MATRIX TEXTURES (Projects) ---
        function createCyberGridTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#080d1a';
            ctx.fillRect(0, 0, 1024, 512);

            // Integrated processor die blocks
            ctx.fillStyle = '#0f172a';
            for (let i = 0; i < 16; i++) {
                const bx = (i % 4) * 256 + 28;
                const by = Math.floor(i / 4) * 128 + 16;
                ctx.fillRect(bx, by, 200, 96);
                ctx.strokeStyle = '#1e293b';
                ctx.lineWidth = 1.5;
                ctx.strokeRect(bx, by, 200, 96);
            }

            // High-density circuit bus lines
            ctx.strokeStyle = '#10b981';
            ctx.lineWidth = 1.5;
            for (let x = 0; x < 1024; x += 32) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
            }
            for (let y = 0; y < 512; y += 32) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(1024, y); ctx.stroke();
            }

            // Glowing optical data channels
            ctx.strokeStyle = '#06b6d4';
            ctx.lineWidth = 2.4;
            for (let y = 32; y < 512; y += 96) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(240, y);
                ctx.lineTo(300, y + 24);
                ctx.lineTo(700, y + 24);
                ctx.lineTo(760, y);
                ctx.lineTo(1024, y);
                ctx.stroke();
            }

            // Server telemetry clusters
            for (let i = 0; i < 90; i++) {
                const nx = Math.floor(Math.random() * 32) * 32;
                const ny = Math.floor(Math.random() * 16) * 32;
                const g = ctx.createRadialGradient(nx, ny, 0, nx, ny, 10);
                g.addColorStop(0, '#ffffff');
                g.addColorStop(0.35, '#34d399');
                g.addColorStop(0.7, '#06b6d4');
                g.addColorStop(1, 'transparent');
                ctx.fillStyle = g;
                ctx.beginPath();
                ctx.arc(nx, ny, 9, 0, Math.PI * 2);
                ctx.fill();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createCyberGridBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#303030';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.fillStyle = '#909090';
            for (let i = 0; i < 16; i++) {
                const bx = (i % 4) * 256 + 28;
                const by = Math.floor(i / 4) * 128 + 16;
                ctx.fillRect(bx, by, 200, 96);
            }

            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2.0;
            for (let x = 0; x < 1024; x += 32) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createCyberGridEmissiveTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.strokeStyle = '#06b6d4';
            ctx.lineWidth = 2.4;
            for (let y = 32; y < 512; y += 96) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(240, y);
                ctx.lineTo(300, y + 24);
                ctx.lineTo(700, y + 24);
                ctx.lineTo(760, y);
                ctx.lineTo(1024, y);
                ctx.stroke();
            }

            for (let i = 0; i < 90; i++) {
                const nx = Math.floor(Math.random() * 32) * 32;
                const ny = Math.floor(Math.random() * 16) * 32;
                ctx.fillStyle = '#34d399';
                ctx.beginPath();
                ctx.arc(nx, ny, 4, 0, Math.PI * 2);
                ctx.fill();
            }

            return new THREE.CanvasTexture(canvas);
        }

        // --- 5. SATURNIAN GAS GIANT & CONCENTRIC RINGS (Skills) ---
        function createSaturnTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            const bands = [
                '#78350f', '#92400e', '#b45309', '#d97706',
                '#f59e0b', '#fbbf24', '#fde68a', '#fef3c7',
                '#f59e0b', '#d97706', '#b45309', '#78350f'
            ];

            for (let y = 0; y < 512; y++) {
                const idx = Math.floor((y / 512) * bands.length);
                const nextIdx = Math.min(bands.length - 1, idx + 1);
                const t = (y % (512 / bands.length)) / (512 / bands.length);
                const ripple = Math.sin(y * 0.15) * 0.15;
                ctx.fillStyle = t + ripple > 0.5 ? bands[nextIdx] : bands[idx];
                ctx.fillRect(0, y, 1024, 1);
            }

            // Great North Polar Hexagon Storm
            const hexY = 55;
            ctx.strokeStyle = 'rgba(254, 243, 199, 0.65)';
            ctx.lineWidth = 3.2;
            for (let a = 0; a < 6; a++) {
                const x1 = a * (1024 / 6);
                const x2 = (a + 1) * (1024 / 6);
                ctx.beginPath();
                ctx.moveTo(x1, hexY);
                ctx.lineTo((x1 + x2) * 0.5, hexY + 12);
                ctx.lineTo(x2, hexY);
                ctx.stroke();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createSaturnRingTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 64;
            const ctx = canvas.getContext('2d');

            const g = ctx.createLinearGradient(0, 0, 1024, 0);
            g.addColorStop(0, 'rgba(0,0,0,0)');
            g.addColorStop(0.06, 'rgba(0,0,0,0)');
            // D Ring (faint inner ring)
            g.addColorStop(0.08, 'rgba(180, 140, 90, 0.18)');
            g.addColorStop(0.18, 'rgba(195, 155, 95, 0.38)');
            // C Ring (Crepe Ring)
            g.addColorStop(0.20, 'rgba(210, 168, 100, 0.52)');
            g.addColorStop(0.38, 'rgba(215, 172, 105, 0.78)');
            // B Ring (Dense, brightest main ring)
            g.addColorStop(0.40, 'rgba(250, 220, 150, 0.98)');
            g.addColorStop(0.52, 'rgba(235, 195, 130, 0.99)');
            g.addColorStop(0.65, 'rgba(245, 210, 140, 0.95)');
            // Cassini Division (famous major gap)
            g.addColorStop(0.66, 'rgba(0,0,0,0.01)');
            g.addColorStop(0.72, 'rgba(0,0,0,0.01)');
            // A Ring with Encke gap
            g.addColorStop(0.73, 'rgba(220, 180, 120, 0.88)');
            g.addColorStop(0.83, 'rgba(225, 185, 125, 0.82)');
            // Encke gap (narrow outer division)
            g.addColorStop(0.84, 'rgba(0,0,0,0.08)');
            g.addColorStop(0.85, 'rgba(225, 185, 125, 0.78)');
            g.addColorStop(0.92, 'rgba(190, 150, 95, 0.68)');
            // F Ring (thin outermost shepherd ring)
            g.addColorStop(0.95, 'rgba(170, 130, 80, 0.40)');
            g.addColorStop(0.98, 'rgba(140, 100, 60, 0.18)');
            g.addColorStop(1, 'rgba(0,0,0,0)');

            ctx.fillStyle = g;
            ctx.fillRect(0, 0, 1024, 64);
            return new THREE.CanvasTexture(canvas);
        }

        // --- 6. VOLCANIC & MARTIAN CRATER WORLD (Blog) ---
        function createVolcanicTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#1c0709';
            ctx.fillRect(0, 0, 1024, 512);

            // Martian iron oxide terrain plates
            ctx.fillStyle = '#450a0a';
            for (let i = 0; i < 28; i++) {
                const cx = (i * 110 + 40) % 1024;
                const cy = 70 + (i * 45) % 380;
                const cr = 40 + (i % 6) * 18;
                ctx.beginPath(); ctx.arc(cx, cy, cr, 0, Math.PI * 2); ctx.fill();
            }

            // Realistic Martian / Lunar Impact Craters
            const craters = [
                { x: 180, y: 150, r: 38 },
                { x: 340, y: 280, r: 24 },
                { x: 520, y: 130, r: 32 },
                { x: 670, y: 340, r: 42 },
                { x: 830, y: 210, r: 20 },
                { x: 910, y: 390, r: 28 },
                { x: 120, y: 360, r: 18 },
                { x: 440, y: 410, r: 22 }
            ];
            craters.forEach(c => drawImpactCrater(ctx, c.x, c.y, c.r, false));

            // Magma ridges & volcanic canyons
            for (let i = 0; i < 40; i++) {
                const x1 = Math.random() * 1024;
                const y1 = Math.random() * 512;
                const x2 = x1 + (Math.random() - 0.5) * 220;
                const y2 = y1 + (Math.random() - 0.5) * 170;

                const g = ctx.createLinearGradient(x1, y1, x2, y2);
                g.addColorStop(0, '#f97316');
                g.addColorStop(0.5, '#ef4444');
                g.addColorStop(1, '#7f1d1d');

                ctx.strokeStyle = g;
                ctx.lineWidth = 2 + Math.random() * 5;
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.stroke();
            }

            // Glowing volcanic calderas & lava lakes
            for (let i = 0; i < 25; i++) {
                const cx = Math.random() * 1024;
                const cy = Math.random() * 512;
                const cr = 8 + Math.random() * 20;
                const cg = ctx.createRadialGradient(cx, cy, 0, cx, cy, cr);
                cg.addColorStop(0, '#fef08a');
                cg.addColorStop(0.3, '#f97316');
                cg.addColorStop(0.7, '#991b1b');
                cg.addColorStop(1, 'transparent');
                ctx.fillStyle = cg;
                ctx.beginPath();
                ctx.arc(cx, cy, cr, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createVolcanicBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#404040';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.fillStyle = '#909090';
            for (let i = 0; i < 28; i++) {
                const cx = (i * 110 + 40) % 1024;
                const cy = 70 + (i * 45) % 380;
                const cr = 40 + (i % 6) * 18;
                ctx.beginPath(); ctx.arc(cx, cy, cr, 0, Math.PI * 2); ctx.fill();
            }

            // Craters on Bump Map (realistic elevation cavity and rim wall)
            const craters = [
                { x: 180, y: 150, r: 38 },
                { x: 340, y: 280, r: 24 },
                { x: 520, y: 130, r: 32 },
                { x: 670, y: 340, r: 42 },
                { x: 830, y: 210, r: 20 },
                { x: 910, y: 390, r: 28 },
                { x: 120, y: 360, r: 18 },
                { x: 440, y: 410, r: 22 }
            ];
            craters.forEach(c => drawImpactCrater(ctx, c.x, c.y, c.r, true));

            ctx.strokeStyle = '#101010'; // Deep rift trenches
            ctx.lineWidth = 5.0;
            for (let i = 0; i < 40; i++) {
                const x1 = Math.random() * 1024;
                const y1 = Math.random() * 512;
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x1 + (Math.random() - 0.5) * 200, y1 + (Math.random() - 0.5) * 150);
                ctx.stroke();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createVolcanicEmissiveTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, 1024, 512);

            for (let i = 0; i < 40; i++) {
                const x1 = Math.random() * 1024;
                const y1 = Math.random() * 512;
                ctx.strokeStyle = '#ef4444';
                ctx.lineWidth = 2.5;
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x1 + (Math.random() - 0.5) * 200, y1 + (Math.random() - 0.5) * 150);
                ctx.stroke();
            }

            for (let i = 0; i < 25; i++) {
                const cx = Math.random() * 1024;
                const cy = Math.random() * 512;
                const cr = 8 + Math.random() * 20;
                const cg = ctx.createRadialGradient(cx, cy, 0, cx, cy, cr);
                cg.addColorStop(0, '#fef08a');
                cg.addColorStop(0.4, '#f97316');
                cg.addColorStop(1, 'transparent');
                ctx.fillStyle = cg;
                ctx.beginPath();
                ctx.arc(cx, cy, cr, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        // --- 7. CRYSTAL WORLD TEXTURES (Certifications) ---
        function createCrystalTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#291103';
            ctx.fillRect(0, 0, 1024, 512);

            // Interlocking crystalline quartz facets
            for (let i = 0; i < 95; i++) {
                const x = Math.random() * 1024;
                const y = Math.random() * 512;
                const w = 35 + Math.random() * 85;
                const h = 25 + Math.random() * 65;

                ctx.save();
                ctx.translate(x, y);
                ctx.rotate(Math.random() * Math.PI);

                const fg = ctx.createLinearGradient(-w/2, -h/2, w/2, h/2);
                fg.addColorStop(0, 'rgba(254, 215, 170, 0.55)');
                fg.addColorStop(0.5, 'rgba(245, 158, 11, 0.35)');
                fg.addColorStop(1, 'rgba(120, 53, 15, 0.7)');

                ctx.fillStyle = fg;
                ctx.strokeStyle = 'rgba(251, 191, 36, 0.65)';
                ctx.lineWidth = 1.2;
                ctx.beginPath();
                ctx.moveTo(-w/2, 0);
                ctx.lineTo(0, -h/2);
                ctx.lineTo(w/2, 0);
                ctx.lineTo(0, h/2);
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
                ctx.restore();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createCrystalBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#404040';
            ctx.fillRect(0, 0, 1024, 512);

            for (let i = 0; i < 95; i++) {
                const x = Math.random() * 1024;
                const y = Math.random() * 512;
                const w = 35 + Math.random() * 85;
                const h = 25 + Math.random() * 65;

                ctx.save();
                ctx.translate(x, y);
                ctx.rotate(Math.random() * Math.PI);
                const bg = ctx.createLinearGradient(-w/2, -h/2, w/2, h/2);
                bg.addColorStop(0, '#ffffff');
                bg.addColorStop(1, '#202020');
                ctx.fillStyle = bg;
                ctx.beginPath();
                ctx.moveTo(-w/2, 0); ctx.lineTo(0, -h/2); ctx.lineTo(w/2, 0); ctx.lineTo(0, h/2);
                ctx.closePath();
                ctx.fill();
                ctx.restore();
            }
            return new THREE.CanvasTexture(canvas);
        }

        // --- 8. QUANTUM BEACON TEXTURES (Get in Touch) ---
        function createBeaconTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#08142c';
            ctx.fillRect(0, 0, 1024, 512);

            // Nitrogen ice fractures
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
            ctx.lineWidth = 1.2;
            for (let x = 0; x < 1024; x += 64) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
            }
            for (let y = 0; y < 512; y += 42) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(1024, y); ctx.stroke();
            }

            // Quantum transmission arrays
            for (let i = 0; i < 8; i++) {
                const cx = (i * 130 + 100) % 1024;
                const cy = (i * 80 + 120) % 512;
                for (let r = 10; r <= 50; r += 12) {
                    ctx.strokeStyle = `rgba(147, 197, 253, ${0.5 - r * 0.007})`;
                    ctx.beginPath();
                    ctx.arc(cx, cy, r, 0, Math.PI * 2);
                    ctx.stroke();
                }
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createBeaconEmissiveTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, 1024, 512);

            for (let i = 0; i < 8; i++) {
                const cx = (i * 130 + 100) % 1024;
                const cy = (i * 80 + 120) % 512;
                for (let r = 10; r <= 45; r += 14) {
                    ctx.strokeStyle = 'rgba(96, 165, 250, 0.8)';
                    ctx.lineWidth = 2.0;
                    ctx.beginPath();
                    ctx.arc(cx, cy, r, 0, Math.PI * 2);
                    ctx.fill();
                }
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createBeaconBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#303030';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.strokeStyle = '#a0a0a0';
            ctx.lineWidth = 2.0;
            for (let x = 0; x < 1024; x += 64) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 512); ctx.stroke();
            }
            return new THREE.CanvasTexture(canvas);
        }

        // --- 8. TOOLS WORLD TEXTURES (Interactive Utilities & MarTech Tooling) ---
        function createToolsTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#0f172a';
            ctx.fillRect(0, 0, 1024, 512);

            // Hexagonal modular panel pattern & tooling telemetry rails
            ctx.strokeStyle = 'rgba(6, 182, 212, 0.45)';
            ctx.lineWidth = 1.4;
            const hexR = 32;
            const hDist = hexR * Math.sqrt(3);
            for (let y = 0; y < 512 + hexR; y += hexR * 1.5) {
                for (let x = 0; x < 1024 + hexR; x += hDist) {
                    const cx = (Math.floor(y / (hexR * 1.5)) % 2 === 0) ? x : x + hDist / 2;
                    ctx.beginPath();
                    for (let a = 0; a < 6; a++) {
                        const angle = Math.PI / 3 * a + Math.PI / 6;
                        const px = cx + hexR * 0.7 * Math.cos(angle);
                        const py = y + hexR * 0.7 * Math.sin(angle);
                        if (a === 0) ctx.moveTo(px, py);
                        else ctx.lineTo(px, py);
                    }
                    ctx.closePath();
                    ctx.stroke();
                }
            }

            // Energy telemetry circuits
            ctx.strokeStyle = 'rgba(34, 211, 238, 0.75)';
            ctx.lineWidth = 2.0;
            for (let i = 0; i < 12; i++) {
                const py = (i * 44 + 20) % 512;
                ctx.beginPath();
                ctx.moveTo(0, py);
                ctx.lineTo(260 + (i * 40) % 300, py);
                ctx.lineTo(310 + (i * 40) % 300, py + 20);
                ctx.lineTo(1024, py + 20);
                ctx.stroke();
            }

            return new THREE.CanvasTexture(canvas);
        }

        function createToolsEmissiveTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.strokeStyle = 'rgba(6, 182, 212, 0.9)';
            ctx.lineWidth = 2.2;
            for (let i = 0; i < 12; i++) {
                const py = (i * 44 + 20) % 512;
                ctx.beginPath();
                ctx.moveTo(0, py);
                ctx.lineTo(260 + (i * 40) % 300, py);
                ctx.lineTo(310 + (i * 40) % 300, py + 20);
                ctx.lineTo(1024, py + 20);
                ctx.stroke();

                // Luminous node dots
                ctx.fillStyle = '#22d3ee';
                ctx.beginPath();
                ctx.arc(260 + (i * 40) % 300, py, 3.5, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createToolsBumpTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#404040';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.strokeStyle = '#c0c0c0';
            ctx.lineWidth = 2.0;
            const hexR = 32;
            const hDist = hexR * Math.sqrt(3);
            for (let y = 0; y < 512 + hexR; y += hexR * 1.5) {
                for (let x = 0; x < 1024 + hexR; x += hDist) {
                    const cx = (Math.floor(y / (hexR * 1.5)) % 2 === 0) ? x : x + hDist / 2;
                    ctx.beginPath();
                    for (let a = 0; a < 6; a++) {
                        const angle = Math.PI / 3 * a + Math.PI / 6;
                        const px = cx + hexR * 0.7 * Math.cos(angle);
                        const py = y + hexR * 0.7 * Math.sin(angle);
                        if (a === 0) ctx.moveTo(px, py);
                        else ctx.lineTo(px, py);
                    }
                    ctx.closePath();
                    ctx.stroke();
                }
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createRingTexture(colorHex) {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 64;
            const ctx = canvas.getContext('2d');

            const g = ctx.createLinearGradient(0, 0, 1024, 0);
            g.addColorStop(0, 'rgba(0,0,0,0)');
            g.addColorStop(0.12, colorHex + '33');
            g.addColorStop(0.35, colorHex + 'cc');
            g.addColorStop(0.55, 'rgba(0,0,0,0.05)');
            g.addColorStop(0.58, colorHex + 'dd');
            g.addColorStop(0.88, colorHex + '77');
            g.addColorStop(1, 'rgba(0,0,0,0)');

            ctx.fillStyle = g;
            ctx.fillRect(0, 0, 1024, 64);
            return new THREE.CanvasTexture(canvas);
        }'''

# ========================================================
# 3. UPGRADED SUN MESH & DYNAMIC CORONA
# ========================================================
UPGRADED_SUN_MESH_CODE = '''        // Central Photorealistic Star (Multi-octave granulation, turbulent flares, sunspots & limb darkening)
        const sunGeo = new THREE.SphereGeometry(22, 64, 64);
        const sunMat = new THREE.ShaderMaterial({
            uniforms: {
                uTime: { value: 0 }
            },
            vertexShader: sunVertexShader,
            fragmentShader: sunFragmentShader
        });
        const sunMesh = new THREE.Mesh(sunGeo, sunMat);
        scene.add(sunMesh);

        // Dynamic Chromosphere Prominence Shell
        const chromosphereGeo = new THREE.SphereGeometry(22 * 1.08, 48, 48);
        const chromosphereMat = new THREE.ShaderMaterial({
            uniforms: {
                uTime: { value: 0 }
            },
            vertexShader: chromosphereVertexShader,
            fragmentShader: chromosphereFragmentShader,
            transparent: true,
            blending: THREE.AdditiveBlending,
            side: THREE.FrontSide,
            depthWrite: false
        });
        const chromosphereMesh = new THREE.Mesh(chromosphereGeo, chromosphereMat);
        scene.add(chromosphereMesh);

        // Dynamic Volumetric Corona Halo Sprite
        const coronaTexture = createCoronaTexture();
        const coronaMat = new THREE.SpriteMaterial({
            map: coronaTexture,
            color: 0xffffff,
            blending: THREE.AdditiveBlending,
            transparent: true
        });
        const coronaSprite = new THREE.Sprite(coronaMat);
        coronaSprite.scale.set(175, 175, 1);
        scene.add(coronaSprite);'''

# ========================================================
# 4. UPGRADED PLANET CONFIGS (Full PBR maps & properties)
# ========================================================
UPGRADED_PLANET_CONFIGS = '''        const planetConfigs = [
            {
                id: 'ai_dialogue',
                name: 'AI Dialogue',
                icon: '💬',
                sector: 'ALPHA-ORBIT // SECTOR 01',
                desc: 'Amethyst storm colossus housing Renzo\\\'s interactive zero-latency AI Representative.',
                orbitRadius: 95,
                orbitSpeed: 0.012,
                radius: 6.8,
                colorHex: '#c084fc',
                type: 'gas_giant',
                texture: () => createGasGiantTexture('#2e1065', '#9333ea', '#c084fc', '#e9d5ff'),
                bumpMap: () => createGasGiantBumpTexture(),
                bumpScale: 0.12,
                roughness: 0.36,
                metalness: 0.08,
                atmScale: 1.18,
                atmIntensity: 0.90,
                hasRing: true,
                ringColor: '#a855f7'
            },
            {
                id: 'services',
                name: 'Services',
                icon: '⚡',
                sector: 'BETA-ORBIT // SECTOR 02',
                desc: 'Radiant emerald neural matrix detailing specialized freelance solutions across CRM, Ads, SEO/GEO & BI.',
                orbitRadius: 140,
                orbitSpeed: 0.0095,
                radius: 8.6,
                colorHex: '#10b981',
                type: 'emerald_nexus',
                texture: () => createServicesNexusTexture(),
                emissiveMap: () => createServicesNexusEmissiveTexture(),
                emissiveColor: '#10b981',
                emissiveIntensity: 0.85,
                bumpMap: () => createServicesNexusBumpTexture(),
                bumpScale: 0.18,
                roughness: 0.30,
                metalness: 0.38,
                atmScale: 1.15,
                atmIntensity: 0.80
            },
            {
                id: 'experience',
                name: 'Experience',
                icon: '🏛️',
                sector: 'GAMMA-ORBIT // SECTOR 03',
                desc: 'Earth-like oceanic oasis charting career leadership across TOMRA, IMBAREX & The Pisonay Co.',
                orbitRadius: 190,
                orbitSpeed: 0.0078,
                radius: 8.2,
                colorHex: '#38bdf8',
                type: 'terrestrial',
                texture: () => createEarthTexture(),
                bumpMap: () => createEarthBumpTexture(),
                bumpScale: 0.24,
                roughnessMap: () => createEarthRoughnessTexture(),
                roughness: 0.45,
                metalness: 0.06,
                emissiveMap: () => createEarthLightsTexture(),
                emissiveColor: '#fef08a',
                emissiveIntensity: 0.55,
                atmScale: 1.18,
                atmIntensity: 0.95,
                hasClouds: true
            },
            {
                id: 'projects',
                name: 'Projects',
                icon: '🚀',
                sector: 'DELTA-ORBIT // SECTOR 04',
                desc: 'Cybernetic matrix world executing autonomous AI CRM enrichment pipelines & live simulators.',
                orbitRadius: 240,
                orbitSpeed: 0.0062,
                radius: 7.8,
                colorHex: '#34d399',
                type: 'cyber',
                texture: () => createCyberGridTexture(),
                bumpMap: () => createCyberGridBumpTexture(),
                bumpScale: 0.22,
                emissiveMap: () => createCyberGridEmissiveTexture(),
                emissiveColor: '#34d399',
                emissiveIntensity: 0.95,
                roughness: 0.26,
                metalness: 0.52,
                atmScale: 1.12,
                atmIntensity: 0.75
            },
            {
                id: 'skills',
                name: 'Skills',
                icon: '🛠️',
                sector: 'EPSILON-ORBIT // SECTOR 05',
                desc: 'Ringed golden colossus detailing 6 strategic pillars across CRM, RevOps, AI & Performance.',
                orbitRadius: 290,
                orbitSpeed: 0.0050,
                radius: 10.5,
                colorHex: '#d4a863',
                type: 'saturn',
                texture: () => createSaturnTexture(),
                bumpMap: () => createGasGiantBumpTexture(),
                bumpScale: 0.14,
                roughness: 0.38,
                metalness: 0.10,
                atmScale: 1.18,
                atmIntensity: 0.85,
                hasBigRing: true,
                ringColor: '#d4a863'
            },
            {
                id: 'tools',
                name: 'Tools',
                icon: '🧰',
                sector: 'ZETA-ORBIT // SECTOR 06',
                desc: 'Titanium cyber-forge matrix housing operational MarTech utilities, automation tooling, and revenue calculators.',
                orbitRadius: 340,
                orbitSpeed: 0.0042,
                radius: 7.5,
                colorHex: '#06b6d4',
                type: 'forge',
                texture: () => createToolsTexture(),
                bumpMap: () => createToolsBumpTexture(),
                bumpScale: 0.22,
                emissiveMap: () => createToolsEmissiveTexture(),
                emissiveColor: '#06b6d4',
                emissiveIntensity: 0.75,
                roughness: 0.32,
                metalness: 0.48,
                atmScale: 1.14,
                atmIntensity: 0.80,
                hasRing: true,
                ringColor: '#06b6d4'
            },
            {
                id: 'blog',
                name: 'Blog',
                icon: '📰',
                sector: 'ETA-ORBIT // SECTOR 07',
                desc: 'Volcanic crimson world publishing operational field notes & technical RevOps playbooks.',
                orbitRadius: 390,
                orbitSpeed: 0.0035,
                radius: 7.2,
                colorHex: '#fb7185',
                type: 'volcanic',
                texture: () => createVolcanicTexture(),
                bumpMap: () => createVolcanicBumpTexture(),
                bumpScale: 0.30,
                emissiveMap: () => createVolcanicEmissiveTexture(),
                emissiveColor: '#ef4444',
                emissiveIntensity: 0.95,
                roughness: 0.72,
                metalness: 0.14,
                atmScale: 1.10,
                atmIntensity: 0.65
            },
            {
                id: 'credentials',
                name: 'Certifications',
                icon: '🎓',
                sector: 'THETA-ORBIT // SECTOR 08',
                desc: 'Radiant crystalline planet showcasing completed HubSpot/Google certs & Salesforce prep.',
                orbitRadius: 440,
                orbitSpeed: 0.0028,
                radius: 8.0,
                colorHex: '#f59e0b',
                type: 'crystal',
                texture: () => createCrystalTexture(),
                bumpMap: () => createCrystalBumpTexture(),
                bumpScale: 0.28,
                emissiveColor: '#f59e0b',
                emissiveIntensity: 0.25,
                roughness: 0.22,
                metalness: 0.35,
                atmScale: 1.12,
                atmIntensity: 0.70
            },
            {
                id: 'contact',
                name: 'Get in Touch',
                icon: '✉️',
                sector: 'IOTA-ORBIT // SECTOR 09',
                desc: 'Quantum beacon hyper-core routing senior inquiries for EMEA & global RevOps roles.',
                orbitRadius: 490,
                orbitSpeed: 0.0022,
                radius: 7.6,
                colorHex: '#60a5fa',
                type: 'beacon',
                texture: () => createBeaconTexture(),
                bumpMap: () => createBeaconBumpTexture(),
                bumpScale: 0.22,
                emissiveMap: () => createBeaconEmissiveTexture(),
                emissiveColor: '#60a5fa',
                emissiveIntensity: 0.90,
                roughness: 0.25,
                metalness: 0.38,
                atmScale: 1.14,
                atmIntensity: 0.85
            }
        ];'''

# ========================================================
# 5. UPGRADED PLANET MESH CREATION LOOP (PBR & Non-Wobbling Rings)
# ========================================================
UPGRADED_PLANET_CREATION_LOOP = '''        const planets = [];

        planetConfigs.forEach((cfg) => {
            // Planet Group
            const pivot = new THREE.Group();
            scene.add(pivot);

            // Orbit line
            const orbitCurve = new THREE.EllipseCurve(0, 0, cfg.orbitRadius, cfg.orbitRadius, 0, 2 * Math.PI, false, 0);
            const orbitPoints = orbitCurve.getPoints(128);
            const orbitGeo = new THREE.BufferGeometry().setFromPoints(orbitPoints.map(p => new THREE.Vector3(p.x, 0, p.y)));
            const orbitMat = new THREE.LineBasicMaterial({ color: 0xd4a863, transparent: true, opacity: 0.12 });
            const orbitLine = new THREE.LineLoop(orbitGeo, orbitMat);
            scene.add(orbitLine);

            // Planet Core Mesh with PBR Materials & Relief Bump/Emissive Maps
            const pGeo = new THREE.SphereGeometry(cfg.radius, 48, 48);
            const pMat = new THREE.MeshStandardMaterial({
                map: cfg.texture(),
                roughness: cfg.roughness !== undefined ? cfg.roughness : 0.55,
                metalness: cfg.metalness !== undefined ? cfg.metalness : 0.15,
                bumpMap: cfg.bumpMap ? cfg.bumpMap() : null,
                bumpScale: cfg.bumpScale !== undefined ? cfg.bumpScale : 0.1,
                roughnessMap: cfg.roughnessMap ? cfg.roughnessMap() : null,
                emissive: cfg.emissiveColor ? new THREE.Color(cfg.emissiveColor) : new THREE.Color(0x000000),
                emissiveMap: cfg.emissiveMap ? cfg.emissiveMap() : null,
                emissiveIntensity: cfg.emissiveIntensity !== undefined ? cfg.emissiveIntensity : 0.0
            });
            const pMesh = new THREE.Mesh(pGeo, pMat);
            pMesh.castShadow = true;
            pMesh.receiveShadow = true;
            pMesh.userData = { id: cfg.id, config: cfg };

            // Clouds for Earth-like (Experience)
            let cloudsMesh = null;
            if (cfg.hasClouds) {
                const cGeo = new THREE.SphereGeometry(cfg.radius * 1.025, 48, 48);
                const cMat = new THREE.MeshStandardMaterial({
                    map: createEarthCloudsTexture(),
                    transparent: true,
                    opacity: 0.82,
                    blending: THREE.AdditiveBlending
                });
                cloudsMesh = new THREE.Mesh(cGeo, cMat);
                pMesh.add(cloudsMesh);
            }

            // Atmosphere Rayleigh Glow Shell (FrontSide with delicate limb halo)
            const atmGeo = new THREE.SphereGeometry(cfg.radius * (cfg.atmScale || 1.15), 32, 32);
            const atmMat = new THREE.ShaderMaterial({
                vertexShader: `
                    varying vec3 vNormal;
                    varying vec3 vPosition;
                    void main() {
                        vNormal = normalize(normalMatrix * normal);
                        vPosition = (modelViewMatrix * vec4(position, 1.0)).xyz;
                        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                    }
                `,
                fragmentShader: `
                    varying vec3 vNormal;
                    varying vec3 vPosition;
                    uniform vec3 glowColor;
                    uniform float intensity;
                    void main() {
                        vec3 viewDir = normalize(-vPosition);
                        float rim = pow(1.0 - max(0.0, dot(vNormal, viewDir)), 2.6);
                        gl_FragColor = vec4(glowColor, rim * intensity);
                    }
                `,
                uniforms: {
                    glowColor: { value: new THREE.Color(cfg.colorHex) },
                    intensity: { value: cfg.atmIntensity !== undefined ? cfg.atmIntensity : 0.85 }
                },
                transparent: true,
                blending: THREE.AdditiveBlending,
                side: THREE.FrontSide,
                depthWrite: false
            });
            const atmMesh = new THREE.Mesh(atmGeo, atmMat);
            pMesh.add(atmMesh);

            // Planetary Rings (AI Dialogue & Skills / Saturn)
            // Kept in a ring tilt container so the ring maintains its fixed celestial plane while planet spins!
            let ringGroup = null;
            if (cfg.hasBigRing || cfg.hasRing) {
                const inR = cfg.radius * 1.45;
                const outR = cfg.radius * (cfg.hasBigRing ? 2.55 : 1.95);
                const rGeo = createConcentricRingGeometry(inR, outR, 128);
                const rMat = new THREE.MeshBasicMaterial({
                    map: cfg.hasBigRing ? createSaturnRingTexture() : createRingTexture(cfg.ringColor),
                    side: THREE.DoubleSide,
                    transparent: true,
                    opacity: 0.88,
                    depthWrite: false
                });
                const rMesh = new THREE.Mesh(rGeo, rMat);
                ringGroup = new THREE.Group();
                ringGroup.rotation.x = Math.PI * 0.44;
                ringGroup.rotation.y = Math.PI * 0.08;
                ringGroup.add(rMesh);
            }

            // Invisible Hit Proxy Sphere (1.55x radius for effortless touch/click target)
            const hitGeo = new THREE.SphereGeometry(cfg.radius * 1.55, 16, 16);
            const hitMat = new THREE.MeshBasicMaterial({ visible: false });
            const hitProxy = new THREE.Mesh(hitGeo, hitMat);
            hitProxy.userData = { id: cfg.id, config: cfg };
            pMesh.add(hitProxy);

            // Initial Angle
            const angle = Math.random() * Math.PI * 2;
            const initX = Math.cos(angle) * cfg.orbitRadius;
            const initZ = Math.sin(angle) * cfg.orbitRadius;
            pMesh.position.set(initX, 0, initZ);
            pivot.add(pMesh);
            if (ringGroup) {
                ringGroup.position.set(initX, 0, initZ);
                pivot.add(ringGroup);
            }

            // Screen Label
            const labelEl = document.createElement('div');
            labelEl.className = 'planet-screen-label';
            labelEl.innerHTML = `<span class="label-indicator" style="background: ${cfg.colorHex}; box-shadow: 0 0 8px ${cfg.colorHex}"></span>${cfg.icon} ${cfg.name}`;
            labelEl.onclick = () => focusOnPlanet(cfg.id);
            labelsContainer.appendChild(labelEl);

            planets.push({
                id: cfg.id,
                config: cfg,
                mesh: pMesh,
                ringGroup: ringGroup,
                hitProxy: hitProxy,
                clouds: cloudsMesh,
                pivot: pivot,
                angle: angle,
                speed: cfg.orbitSpeed,
                labelEl: labelEl
            });
        });'''

# ========================================================
# 6. UPGRADED TOUCH & MULTI-POINTER CONTROLLER (Pinch-to-zoom & Tap)
# ========================================================
UPGRADED_TOUCH_AND_CAMERA_CONTROLS = '''        // Multi-touch & Pointer Tracking for Mobile & Desktop (Smooth rotate, pinch-to-zoom, tap)
        const activePointers = new Map();
        let prevPinchDist = 0;
        let pointerMoved = false;
        let pointerDownTime = 0;

        window.addEventListener('pointerdown', (e) => {
            if (e.target.id === 'webglCanvas') {
                activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
                if (activePointers.size === 1) {
                    isPointerDown = true;
                    prevMouseX = e.clientX;
                    prevMouseY = e.clientY;
                    pointerStartX = e.clientX;
                    pointerStartY = e.clientY;
                    pointerMoved = false;
                    pointerDownTime = performance.now();
                } else if (activePointers.size === 2) {
                    const pts = Array.from(activePointers.values());
                    prevPinchDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
                    pointerMoved = true; // Pinching gesture is not a tap
                    if (typeof dismissFloatingHint === 'function') dismissFloatingHint();
                }
            }
        });

        window.addEventListener('pointermove', (e) => {
            if (!activePointers.has(e.pointerId)) return;
            activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

            if (activePointers.size === 1) {
                // Single-finger orbit rotation
                const deltaX = e.clientX - prevMouseX;
                const deltaY = e.clientY - prevMouseY;
                if (Math.hypot(e.clientX - pointerStartX, e.clientY - pointerStartY) > 8) {
                    pointerMoved = true;
                    if (typeof dismissFloatingHint === 'function') dismissFloatingHint();
                }
                prevMouseX = e.clientX;
                prevMouseY = e.clientY;

                camSpherical.theta -= deltaX * 0.0042;
                camSpherical.phi = Math.max(0.18, Math.min(Math.PI * 0.48, camSpherical.phi - deltaY * 0.0042));
            } else if (activePointers.size >= 2) {
                // Two-finger pinch-to-zoom
                const pts = Array.from(activePointers.values());
                const curPinchDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
                const deltaDist = curPinchDist - prevPinchDist;
                prevPinchDist = curPinchDist;

                if (viewMode === 'OVERVIEW' && Math.abs(deltaDist) > 0.5) {
                    camSpherical.radius = Math.max(160, Math.min(920, camSpherical.radius - deltaDist * 0.95));
                    pointerMoved = true;
                    if (typeof dismissFloatingHint === 'function') dismissFloatingHint();
                } else if (viewMode === 'INSPECT' && deltaDist < -20) {
                    // Pinching inward while inspecting resets back to overview
                    resetToOverview();
                    pointerMoved = true;
                    if (typeof dismissFloatingHint === 'function') dismissFloatingHint();
                }
            }
        });

        window.addEventListener('pointerup', (e) => {
            const wasTracking = activePointers.has(e.pointerId);
            activePointers.delete(e.pointerId);

            // Tap detection on canvas (single touch, short duration, minimal drag movement)
            if (wasTracking && activePointers.size === 0 && !pointerMoved && (performance.now() - pointerDownTime) < 450) {
                if (e.target.id === 'webglCanvas') {
                    // Check if an active modal is open: tapping background canvas dismisses it
                    const activeModal = document.querySelector('.spatial-modal-card.active');
                    if (activeModal) {
                        closeActiveModal();
                        if (viewMode === 'INSPECT') resetToOverview();
                    } else {
                        if (typeof dismissFloatingHint === 'function') dismissFloatingHint();
                        handlePointerClick(e.clientX, e.clientY);
                    }
                }
            }

            if (activePointers.size === 1) {
                // Transitioning from 2 fingers to 1 finger: update prev coords without camera jump
                const remaining = Array.from(activePointers.values())[0];
                prevMouseX = remaining.x;
                prevMouseY = remaining.y;
            } else if (activePointers.size === 0) {
                isPointerDown = false;
            }
        });

        window.addEventListener('pointercancel', (e) => {
            activePointers.delete(e.pointerId);
            if (activePointers.size === 0) isPointerDown = false;
        });

        // Wheel Zoom for Desktop
        window.addEventListener('wheel', (e) => {
            if (viewMode === 'OVERVIEW') {
                camSpherical.radius = Math.max(160, Math.min(920, camSpherical.radius + e.deltaY * 0.5));
                if (typeof dismissFloatingHint === 'function') dismissFloatingHint();
            }
        }, { passive: true });'''

# ========================================================
# 7. UPGRADED ANIMATE LOOP (Sun time uniform, thermal pulses)
# ========================================================
UPGRADED_ANIMATE_SUN_CODE = '''            // Update Photorealistic Sun, Chromosphere & Corona
            if (typeof sunMat !== 'undefined' && sunMat.uniforms && sunMat.uniforms.uTime) {
                sunMat.uniforms.uTime.value = animClock;
            }
            if (typeof chromosphereMat !== 'undefined' && chromosphereMat.uniforms && chromosphereMat.uniforms.uTime) {
                chromosphereMat.uniforms.uTime.value = animClock;
            }
            sunMesh.rotation.y += 0.0018;
            if (typeof chromosphereMesh !== 'undefined') {
                chromosphereMesh.rotation.y -= 0.0012;
            }
            if (typeof coronaSprite !== 'undefined') {
                coronaSprite.rotation.z += 0.0008;
                const cScale = 175 + Math.sin(animClock * 1.6) * 6;
                coronaSprite.scale.set(cScale, cScale, 1);
            }
            if (typeof sunLight !== 'undefined') {
                sunLight.intensity = 3.6 + Math.sin(animClock * 1.5) * 0.15;
            }'''

# ========================================================
# 8. UPGRADED SERVICES MODAL CSS & HTML (Spacious Glassmorphic Architecture)
# ========================================================
UPGRADED_SERVICES_CSS = '''        /* Services Cards Grid & Freelance Architecture */
        #modalServices {
            width: 92vw;
            max-width: 960px;
            height: 86vh;
            max-height: 840px;
            border-radius: 28px;
            box-shadow: 0 45px 100px rgba(0, 0, 0, 0.95), 0 0 50px rgba(212, 168, 99, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }

        #modalServices .modal-body-scroll {
            padding: 1.6rem 2rem 2.25rem;
            flex: 1;
            overflow-y: auto;
            overscroll-behavior: contain;
            -webkit-overflow-scrolling: touch;
            scroll-behavior: smooth;
            scrollbar-width: thin;
            scrollbar-color: rgba(212, 168, 99, 0.4) transparent;
            display: flex;
            flex-direction: column;
            gap: 1.35rem;
        }

        #modalServices .modal-body-scroll::-webkit-scrollbar {
            width: 6px;
        }

        #modalServices .modal-body-scroll::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.25);
            border-radius: 9999px;
        }

        #modalServices .modal-body-scroll::-webkit-scrollbar-thumb {
            background: rgba(212, 168, 99, 0.4);
            border-radius: 9999px;
        }

        #modalServices .modal-body-scroll::-webkit-scrollbar-thumb:hover {
            background: rgba(212, 168, 99, 0.65);
        }

        .services-modal-intro {
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
            padding-bottom: 0.15rem;
        }

        .services-status-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 5px 14px;
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.28);
            border-radius: 9999px;
            width: fit-content;
            font-family: var(--font-mono);
            font-size: 0.67rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            color: var(--accent-emerald);
            box-shadow: 0 2px 10px rgba(16, 185, 129, 0.12);
        }

        .status-pulse-dot {
            width: 7px;
            height: 7px;
            background: var(--accent-emerald);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--accent-emerald);
            animation: pulseLive 2s infinite;
        }

        .services-intro-desc {
            font-size: 0.94rem;
            color: #cbd5e1;
            line-height: 1.6;
            margin: 0;
            max-width: 880px;
        }

        .services-cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.35rem;
            margin: 0.1rem 0;
            align-items: stretch;
        }

        .service-feature-card {
            position: relative;
            background: linear-gradient(145deg, rgba(24, 19, 34, 0.82), rgba(13, 10, 19, 0.92));
            backdrop-filter: blur(30px) saturate(200%);
            -webkit-backdrop-filter: blur(30px) saturate(200%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 1.55rem 1.6rem 1.45rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 1rem;
            transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.48), inset 0 1px 0 rgba(255, 255, 255, 0.08);
            overflow: hidden;
        }

        .service-feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, rgba(212, 168, 99, 0.6), transparent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .service-feature-card:hover {
            background: linear-gradient(145deg, rgba(32, 25, 45, 0.92), rgba(18, 14, 26, 0.96));
            border-color: rgba(212, 168, 99, 0.45);
            transform: translateY(-3px);
            box-shadow: 0 22px 50px rgba(0, 0, 0, 0.65), 0 0 28px rgba(212, 168, 99, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.18);
        }

        .service-feature-card:hover::before {
            opacity: 1;
        }

        .service-feature-card.card-crm:hover {
            border-color: rgba(52, 211, 153, 0.45);
            box-shadow: 0 22px 50px rgba(0, 0, 0, 0.65), 0 0 28px rgba(52, 211, 153, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.18);
        }
        .service-feature-card.card-crm::before {
            background: linear-gradient(90deg, transparent, rgba(52, 211, 153, 0.75), transparent);
        }

        .service-feature-card.card-media:hover {
            border-color: rgba(212, 168, 99, 0.5);
            box-shadow: 0 22px 50px rgba(0, 0, 0, 0.65), 0 0 28px rgba(212, 168, 99, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.18);
        }
        .service-feature-card.card-media::before {
            background: linear-gradient(90deg, transparent, rgba(212, 168, 99, 0.8), transparent);
        }

        .service-feature-card.card-seo:hover {
            border-color: rgba(192, 132, 252, 0.45);
            box-shadow: 0 22px 50px rgba(0, 0, 0, 0.65), 0 0 28px rgba(192, 132, 252, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.18);
        }
        .service-feature-card.card-seo::before {
            background: linear-gradient(90deg, transparent, rgba(192, 132, 252, 0.75), transparent);
        }

        .service-feature-card.card-data:hover {
            border-color: rgba(56, 189, 248, 0.45);
            box-shadow: 0 22px 50px rgba(0, 0, 0, 0.65), 0 0 28px rgba(56, 189, 248, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.18);
        }
        .service-feature-card.card-data::before {
            background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.75), transparent);
        }

        .service-card-body {
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .service-card-tag {
            font-family: var(--font-mono);
            font-size: 0.64rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 3.5px 11px;
            border-radius: 9999px;
            width: fit-content;
            line-height: 1.2;
            margin-bottom: 0.45rem;
        }

        .service-tag-crm {
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #34d399;
        }

        .service-tag-media {
            background: rgba(212, 168, 99, 0.08);
            border: 1px solid rgba(212, 168, 99, 0.3);
            color: var(--accent-gold);
        }

        .service-tag-seo {
            background: rgba(192, 132, 252, 0.08);
            border: 1px solid rgba(192, 132, 252, 0.3);
            color: #c084fc;
        }

        .service-tag-data {
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.3);
            color: #38bdf8;
        }

        .service-card-title {
            font-size: 1.14rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.35;
            letter-spacing: -0.01em;
            margin: 0.2rem 0 0.45rem;
        }

        .service-card-desc {
            font-size: 0.86rem;
            color: #94a3b8;
            line-height: 1.58;
            margin: 0 0 0.85rem;
        }

        .service-bullets {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.55rem;
            font-size: 0.81rem;
            color: #e2e8f0;
            margin: auto 0 0;
            padding: 0;
        }

        .service-bullets li {
            display: flex;
            align-items: flex-start;
            gap: 0.55rem;
            line-height: 1.45;
        }

        .service-bullets li span.check {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 17px;
            height: 17px;
            border-radius: 50%;
            background: rgba(212, 168, 99, 0.12);
            border: 1px solid rgba(212, 168, 99, 0.32);
            color: var(--accent-gold);
            font-weight: 700;
            font-size: 0.64rem;
            flex-shrink: 0;
            margin-top: 1px;
        }

        .card-crm .service-bullets li span.check {
            background: rgba(16, 185, 129, 0.12);
            border-color: rgba(16, 185, 129, 0.32);
            color: #34d399;
        }

        .card-seo .service-bullets li span.check {
            background: rgba(192, 132, 252, 0.12);
            border-color: rgba(192, 132, 252, 0.32);
            color: #c084fc;
        }

        .card-data .service-bullets li span.check {
            background: rgba(56, 189, 248, 0.12);
            border-color: rgba(56, 189, 248, 0.32);
            color: #38bdf8;
        }

        .service-card-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            margin-top: 1.15rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.07);
        }

        .service-btn-primary,
        .service-btn-secondary {
            flex: 1 1 145px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.4rem;
            font-family: var(--font-sans);
            font-size: 0.77rem;
            font-weight: 700;
            padding: 0.58rem 0.8rem;
            border-radius: 9999px;
            text-decoration: none;
            text-align: center;
            white-space: nowrap;
            transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
            box-sizing: border-box;
            min-height: 38px;
        }

        .service-btn-primary {
            background: linear-gradient(135deg, #e5b974, #d4a863);
            color: #08060c;
            border: 1px solid rgba(212, 168, 99, 0.65);
            box-shadow: 0 4px 14px rgba(212, 168, 99, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.35);
        }

        .service-btn-primary:hover {
            background: linear-gradient(135deg, #f0ca8c, #e2ba78);
            border-color: #f0ca8c;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(212, 168, 99, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.45);
        }

        .service-btn-secondary {
            background: rgba(255, 255, 255, 0.05);
            color: #f8fafc;
            border: 1px solid rgba(255, 255, 255, 0.13);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        }

        .service-btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(212, 168, 99, 0.45);
            color: var(--accent-gold);
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4), 0 0 14px rgba(212, 168, 99, 0.2);
        }

        .services-cta-banner {
            background: linear-gradient(135deg, rgba(30, 24, 40, 0.82), rgba(18, 14, 25, 0.94));
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(212, 168, 99, 0.35);
            border-radius: 24px;
            padding: 1.45rem 1.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.25rem;
            margin-top: 0.25rem;
            box-shadow: 0 16px 38px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.12);
        }

        .services-cta-banner-text h4 {
            font-size: 1.1rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.3rem;
            letter-spacing: -0.01em;
        }

        .services-cta-banner-text p {
            font-size: 0.86rem;
            color: #94a3b8;
            line-height: 1.48;
            margin: 0;
        }

        .services-cta-banner-actions {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
        }

        .services-cta-banner-actions .inspect-btn,
        .services-cta-banner-actions .inspect-btn-secondary {
            padding: 0.58rem 1.2rem;
            font-size: 0.75rem;
            font-weight: 700;
        }'''

UPGRADED_MODAL_SERVICES_HTML = '''    <!-- MODAL: SERVICES (FREELANCE SOLUTIONS) -->
    <div class="spatial-modal-card" id="modalServices">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>⚡</span> High-Impact Freelance Services & Growth Systems</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <div class="services-modal-intro">
                <div class="services-status-badge">
                    <span class="status-pulse-dot"></span>
                    <span class="status-text">AVAILABLE FOR STRATEGIC FREELANCE & REVOPS CONSULTING</span>
                </div>
                <p class="services-intro-desc">
                    Specialized enterprise-grade freelance engineering across HubSpot/Salesforce CRM architecture, B2B paid demand generation, technical SEO/GEO, and executive revenue intelligence.
                </p>
            </div>

            <div class="services-cards-grid">

                <!-- Service 1 -->
                <div class="service-feature-card card-crm">
                    <div class="service-card-body">
                        <div class="service-card-tag service-tag-crm">🎯 REVOPS ARCHITECTURE & STARTUP CRM</div>
                        <h3 class="service-card-title">HubSpot CRM Setup & RevOps Architecture</h3>
                        <p class="service-card-desc">
                            Eliminate lead leakage and chaotic spreadsheets. Complete HubSpot/Salesforce lifecycle modeling, custom pipeline properties, and SLA automation.
                        </p>
                        <ul class="service-bullets">
                            <li><span class="check">✓</span> <span>Lifecycle stage modeling (Lead → MQL → SQL → Deal)</span></li>
                            <li><span class="check">✓</span> <span>Automated lead routing & 0-latency SLA notifications</span></li>
                            <li><span class="check">✓</span> <span>Mandatory deal-stage gating properties</span></li>
                        </ul>
                    </div>
                    <div class="service-card-actions">
                        <a href="mailto:renzo.francesqui@gmail.com?subject=Inquiry%20regarding%20HubSpot%20CRM%20Setup%20and%20RevOps" class="service-btn-primary">
                            <span>Inquire / Consult ✉️</span>
                        </a>
                        <a href="/services/hubspot-crm-optimization-startups/" target="_blank" class="service-btn-secondary">
                            <span>Explore Scope ↗</span>
                        </a>
                    </div>
                </div>

                <!-- Service 2 -->
                <div class="service-feature-card card-media">
                    <div class="service-card-body">
                        <div class="service-card-tag service-tag-media">📈 B2B PERFORMANCE & DEMAND GENERATION</div>
                        <h3 class="service-card-title">Paid Media Management for B2B & Tech</h3>
                        <p class="service-card-desc">
                            Stop wasting ad budgets. Full-funnel Google Search, LinkedIn ABM, and Meta campaigns acquiring qualified demo requests at profitable CAC.
                        </p>
                        <ul class="service-bullets">
                            <li><span class="check">✓</span> <span>High-intent Google Search keyword architecture</span></li>
                            <li><span class="check">✓</span> <span>LinkedIn Account-Based Marketing matching ICP firmographics</span></li>
                            <li><span class="check">✓</span> <span>Server-side tracking & GA4 offline conversion import</span></li>
                        </ul>
                    </div>
                    <div class="service-card-actions">
                        <a href="mailto:renzo.francesqui@gmail.com?subject=Inquiry%20regarding%20Paid%20Media%20Management" class="service-btn-primary">
                            <span>Inquire / Consult ✉️</span>
                        </a>
                        <a href="/services/paid-media-management/" target="_blank" class="service-btn-secondary">
                            <span>Explore Scope ↗</span>
                        </a>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="service-feature-card card-seo">
                    <div class="service-card-body">
                        <div class="service-card-tag service-tag-seo">🌐 ORGANIC SEARCH & GENERATIVE AI ENGINE VISIBILITY</div>
                        <h3 class="service-card-title">Technical SEO & Generative Engine Optimization (GEO)</h3>
                        <p class="service-card-desc">
                            Dual-engine organic dominance: rank in top Google SERPs while ensuring generative AI answer engines (ChatGPT, Perplexity, Gemini, Claude) cite your brand.
                        </p>
                        <ul class="service-bullets">
                            <li><span class="check">✓</span> <span>Core Web Vitals, crawl budget, and hreflang routing</span></li>
                            <li><span class="check">✓</span> <span>Generative Engine Optimization (GEO) brand entity modeling</span></li>
                            <li><span class="check">✓</span> <span>Advanced Schema.org JSON-LD microdata implementation</span></li>
                        </ul>
                    </div>
                    <div class="service-card-actions">
                        <a href="mailto:renzo.francesqui@gmail.com?subject=Inquiry%20regarding%20SEO%20and%20GEO%20Optimization" class="service-btn-primary">
                            <span>Inquire / Consult ✉️</span>
                        </a>
                        <a href="/services/seo-and-geo-optimization/" target="_blank" class="service-btn-secondary">
                            <span>Explore Scope ↗</span>
                        </a>
                    </div>
                </div>

                <!-- Service 4 -->
                <div class="service-feature-card card-data">
                    <div class="service-card-body">
                        <div class="service-card-tag service-tag-data">📊 ANALYTICS, ATTRIBUTION & EXECUTIVE INTELLIGENCE</div>
                        <h3 class="service-card-title">Marketing Data Modeling & Automated KPI Reporting</h3>
                        <p class="service-card-desc">
                            Connect your CRM, ads, and web analytics into executive dashboards with automated Slack/email revenue delivery. Single Source of Truth analytics.
                        </p>
                        <ul class="service-bullets">
                            <li><span class="check">✓</span> <span>End-to-end GA4 measurement & multi-touch attribution</span></li>
                            <li><span class="check">✓</span> <span>Custom SQL pipeline modeling (BigQuery, PostgreSQL)</span></li>
                            <li><span class="check">✓</span> <span>Real-time Looker Studio / Power BI executive dashboards</span></li>
                        </ul>
                    </div>
                    <div class="service-card-actions">
                        <a href="mailto:renzo.francesqui@gmail.com?subject=Inquiry%20regarding%20Marketing%20Data%20and%20KPI%20Reporting" class="service-btn-primary">
                            <span>Inquire / Consult ✉️</span>
                        </a>
                        <a href="/services/marketing-data-reporting/" target="_blank" class="service-btn-secondary">
                            <span>Explore Scope ↗</span>
                        </a>
                    </div>
                </div>

            </div>

            <!-- Direct Transmission Banner -->
            <div class="services-cta-banner">
                <div class="services-cta-banner-text">
                    <h4>Ready to scale your marketing engine?</h4>
                    <p>Get in touch directly or download verified CV for freelance engagement.</p>
                </div>
                <div class="services-cta-banner-actions">
                    <button onclick="openModalForPlanet('contact')" class="inspect-btn">
                        <span>✉️</span> Initiate Transmission
                    </button>
                    <a href="RenzoFrancesquiCV2026.pdf" target="_blank" download class="inspect-btn-secondary" style="text-decoration: none;">
                        <span>📄</span> Download CV (PDF)
                    </a>
                </div>
            </div>
        </div>
    </div>'''

UPGRADED_MODAL_TOOLS_HTML = '''    <!-- MODAL: TOOLS -->
    <div class="spatial-modal-card" id="modalTools">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>🧰</span> Tools</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <div class="tools-suite-header">
                <h3 class="tools-suite-title"><span>🧰</span> Interactive RevOps &amp; MarTech Utility Suite</h3>
                <p class="tools-suite-subtitle">Production-grade Revenue Operations calculators, campaign governance builders, and event lead modeling tools engineered by Renzo Francesqui.</p>
            </div>

            <div class="tools-tab-switcher">
                <button class="tools-tab-btn active" id="tabBtnSla" onclick="switchToolsTab('sla')">
                    <span>⚡</span> SLA &amp; Lead Leakage Calculator
                </button>
                <button class="tools-tab-btn" id="tabBtnUtm" onclick="switchToolsTab('utm')">
                    <span>🔗</span> B2B UTM Taxonomy Builder
                </button>
                <button class="tools-tab-btn" id="tabBtnTradeShow" onclick="switchToolsTab('tradeshow')">
                    <span>🎪</span> Trade Show ROI Modeler
                </button>
            </div>

            <!-- TAB 1: MQL-to-SQL SLA & Lead Leakage Calculator -->
            <div class="tool-pane" id="paneToolsSla">
                <div class="tool-intro-box" style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 260px;">
                        <h4 class="tool-pane-title">MQL-to-SQL SLA &amp; Lead Leakage Calculator</h4>
                        <p class="tool-pane-desc">Quantify how follow-up response latency degrades inbound pipeline conversion. Sub-5-minute routing consistently delivers up to 8x higher lead-to-opportunity velocity compared to manual spreadsheets.</p>
                    </div>
                    <a href="/tools/mql-to-sql-sla-lead-leakage-calculator/" target="_blank" rel="noopener noreferrer" class="tool-dedicated-btn">
                        <span>↗</span> Open Full Tool &amp; Guide
                    </a>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaLeadsInput">Monthly Inbound / Event Leads</label>
                                <span class="tool-val-display" id="slaLeadsVal">350 leads</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaLeadsInput" min="50" max="2500" step="25" value="350" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaAcvInput">Average B2B Deal Value (€)</label>
                                <span class="tool-val-display" id="slaAcvVal">€15,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaAcvInput" min="2000" max="100000" step="1000" value="15000" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Current Average Sales Follow-Up Time</label>
                            <div class="tool-pills-row" id="slaSpeedPills">
                                <button type="button" class="tool-pill-option active" data-speed="slow" onclick="setSlaFollowup('slow')">&gt; 48 Hours (Manual CSV)</button>
                                <button type="button" class="tool-pill-option" data-speed="medium" onclick="setSlaFollowup('medium')">24 Hours</button>
                                <button type="button" class="tool-pill-option" data-speed="fast" onclick="setSlaFollowup('fast')">&lt; 5 Minutes (Automated Webhook + HubSpot SLA)</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid">
                            <div class="tool-kpi-card" style="border-color: rgba(251, 113, 133, 0.4); background: rgba(251, 113, 133, 0.05);">
                                <div class="tool-kpi-label">Estimated Annual Pipeline Leaked (€)</div>
                                <div class="tool-kpi-num" id="slaLeakedVal" style="color: #fb7185;">€19,530,000</div>
                                <div class="tool-kpi-sub" id="slaLeakedSub">75% lead drop-off due to latency (&gt; 48h)</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">Recoverable Pipeline with 0-Latency Routing (€)</div>
                                <div class="tool-kpi-num" id="slaRecoverableVal" style="color: #34d399;">€13,671,000</div>
                                <div class="tool-kpi-sub" id="slaRecoverableSub">With sub-5min automated SLA</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Projected MQL-to-SQL Conversion Lift (%)</div>
                                <div class="tool-kpi-num" id="slaLiftVal" style="color: #d4a863;">+775%</div>
                                <div class="tool-kpi-sub" id="slaLiftSub">4% current → 35% SLA target</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('services');">
                                <span>⚡</span> Fix This Pipeline Leakage in Your CRM →
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: B2B Campaign UTM & CRM Governance Builder -->
            <div class="tool-pane" id="paneToolsUtm" style="display: none;">
                <div class="tool-intro-box" style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 260px;">
                        <h4 class="tool-pane-title">B2B Campaign UTM &amp; CRM Governance Builder</h4>
                        <p class="tool-pane-desc">Enforce standard tracking taxonomy across paid acquisition and map attribution keys into hidden HubSpot/Salesforce form properties.</p>
                    </div>
                    <a href="/tools/b2b-campaign-utm-crm-builder/" target="_blank" rel="noopener noreferrer" class="tool-dedicated-btn">
                        <span>↗</span> Open Full Tool &amp; Guide
                    </a>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <label for="utmUrlInput" class="tool-input-label">Landing Page URL</label>
                            <input type="url" class="tool-text-input" id="utmUrlInput" value="https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Channel / Source</label>
                            <div class="tool-pills-row" id="utmSourcePills">
                                <button type="button" class="tool-pill-option active" data-src="linkedin" onclick="setUtmSource('linkedin')">linkedin</button>
                                <button type="button" class="tool-pill-option" data-src="google" onclick="setUtmSource('google')">google</button>
                                <button type="button" class="tool-pill-option" data-src="meta" onclick="setUtmSource('meta')">meta</button>
                                <button type="button" class="tool-pill-option" data-src="tradeshow_qr" onclick="setUtmSource('tradeshow_qr')">tradeshow_qr</button>
                                <button type="button" class="tool-pill-option" data-src="email_nurture" onclick="setUtmSource('email_nurture')">email_nurture</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Medium</label>
                            <div class="tool-pills-row" id="utmMediumPills">
                                <button type="button" class="tool-pill-option active" data-med="cpc" onclick="setUtmMedium('cpc')">cpc</button>
                                <button type="button" class="tool-pill-option" data-med="abm_sponsored" onclick="setUtmMedium('abm_sponsored')">abm_sponsored</button>
                                <button type="button" class="tool-pill-option" data-med="offline_badge" onclick="setUtmMedium('offline_badge')">offline_badge</button>
                                <button type="button" class="tool-pill-option" data-med="automation" onclick="setUtmMedium('automation')">automation</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label for="utmCampaignInput" class="tool-input-label">Campaign Name (Auto-slugified to lowercase with underscores)</label>
                            <input type="text" class="tool-text-input" id="utmCampaignInput" value="2026_q2_enterprise_revops_scale" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">ICP Segment / Region</label>
                            <div class="tool-pills-row" id="utmRegionPills">
                                <button type="button" class="tool-pill-option active" data-reg="emea" onclick="setUtmRegion('emea')">emea</button>
                                <button type="button" class="tool-pill-option" data-reg="americas" onclick="setUtmRegion('americas')">americas</button>
                                <button type="button" class="tool-pill-option" data-reg="dach" onclick="setUtmRegion('dach')">dach</button>
                                <button type="button" class="tool-pill-option" data-reg="italy" onclick="setUtmRegion('italy')">italy</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="terminal-block">
                            <div class="terminal-bar">
                                <span class="terminal-tag">GOVERNED CAMPAIGN URL</span>
                                <button class="terminal-copy-btn" id="btnCopyUtm" onclick="copyGovernedUrl()">📋 Copy Governed URL</button>
                            </div>
                            <div class="terminal-content" id="utmOutputUrl" style="word-break: break-all; font-family: var(--font-mono); font-size: 0.72rem; color: #38bdf8; line-height: 1.5; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px;">
                                https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/?utm_source=linkedin&amp;utm_medium=cpc&amp;utm_campaign=2026_q2_enterprise_revops_scale&amp;custom_icp_region=emea
                            </div>
                        </div>

                        <div class="terminal-block" style="margin-top: 1rem;">
                            <div class="terminal-bar">
                                <span class="terminal-tag">HUBSPOT / SALESFORCE HIDDEN FORM FIELDS</span>
                                <span style="font-family: var(--font-mono); font-size: 0.62rem; color: var(--accent-gold);">INGESTION JSON</span>
                            </div>
                            <pre class="terminal-content" id="utmJsonPreview" style="font-family: var(--font-mono); font-size: 0.68rem; color: #a78bfa; line-height: 1.45; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px; margin: 0; overflow-x: auto;">{
  "utm_source": "linkedin",
  "utm_medium": "cpc",
  "utm_campaign": "2026_q2_enterprise_revops_scale",
  "custom_icp_region": "emea"
}</pre>
                        </div>
                        <div class="tool-cta-wrapper" style="margin-top: 1.15rem;">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('services');">
                                <span>🔗</span> Eliminate Attribution Drift in Your CRM →
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: B2B Trade Show & Exhibition ROI Calculator -->
            <div class="tool-pane" id="paneToolsTradeShow" style="display: none;">
                <div class="tool-intro-box" style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 260px;">
                        <h4 class="tool-pane-title">B2B Trade Show &amp; Exhibition ROI Calculator</h4>
                        <p class="tool-pane-desc">Modeled on real-world industrial exhibition operations (IFAT Munich, PRS Europe). Measure pipeline creation, qualified cost per opportunity, and automated sync hours saved.</p>
                    </div>
                    <a href="/tools/b2b-trade-show-roi-calculator/" target="_blank" rel="noopener noreferrer" class="tool-dedicated-btn">
                        <span>↗</span> Open Full Tool &amp; Guide
                    </a>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsCostInput">Total Booth &amp; Event Sponsorship Cost (€)</label>
                                <span class="tool-val-display" id="tsCostVal">€45,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsCostInput" min="5000" max="250000" step="2500" value="45000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsBadgesInput">Badges Scanned at Show</label>
                                <span class="tool-val-display" id="tsBadgesVal">320 badges</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsBadgesInput" min="20" max="2500" step="10" value="320" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsQualInput">Qualification Rate (% High-Intent ICP)</label>
                                <span class="tool-val-display" id="tsQualVal">45%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsQualInput" min="5" max="90" step="5" value="45" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsAcvInput">Average Contract Value (€)</label>
                                <span class="tool-val-display" id="tsAcvVal">€28,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsAcvInput" min="2000" max="150000" step="1000" value="28000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsWinRateInput">Close Rate (%)</label>
                                <span class="tool-val-display" id="tsWinRateVal">22%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsWinRateInput" min="2" max="60" step="1" value="22" oninput="updateTradeShowRoi()">
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid" style="grid-template-columns: repeat(2, 1fr);">
                            <div class="tool-kpi-card" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.05);">
                                <div class="tool-kpi-label">Cost Per Scanned Lead (€)</div>
                                <div class="tool-kpi-num" id="tsCplVal" style="color: #38bdf8;">€141</div>
                                <div class="tool-kpi-sub" id="tsCplSub">Cost per qualified SQL: €313</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Generated SQL Pipeline (€)</div>
                                <div class="tool-kpi-num" id="tsPipelineVal" style="color: #d4a863;">€4,032,000</div>
                                <div class="tool-kpi-sub" id="tsPipelineSub">Projected won: €887,040</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">Projected Event ROAS (x)</div>
                                <div class="tool-kpi-num" id="tsRoasVal" style="color: #34d399;">19.7x</div>
                                <div class="tool-kpi-sub" id="tsRoasSub">Return on event capital invested</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(167, 139, 250, 0.4); background: rgba(167, 139, 250, 0.05);">
                                <div class="tool-kpi-label">Time Saved via Automated Badge-to-HubSpot Sync (Hours)</div>
                                <div class="tool-kpi-num" id="tsHoursVal" style="color: #a78bfa;">43 hrs</div>
                                <div class="tool-kpi-sub" id="tsHoursSub">Via zero-latency CRM ingestion</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('services');">
                                <span>🎪</span> Model Your Trade Show Lead Engine in CRM →
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>'''

UPGRADED_MODAL_TOOLS_HTML_IT = '''    <!-- MODAL: TOOLS -->
    <div class="spatial-modal-card" id="modalTools">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>🧰</span> Strumenti</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <div class="tools-suite-header">
                <h3 class="tools-suite-title"><span>🧰</span> Suite Utility Interattive RevOps &amp; MarTech</h3>
                <p class="tools-suite-subtitle">Calcolatori Revenue Operations enterprise, costruttori di governance tracciamento campagne e modelli di acquisizione fieristica sviluppati da Renzo Francesqui.</p>
            </div>

            <div class="tools-tab-switcher">
                <button class="tools-tab-btn active" id="tabBtnSla" onclick="switchToolsTab('sla')">
                    <span>⚡</span> Calcolatore SLA &amp; Dispersione Lead
                </button>
                <button class="tools-tab-btn" id="tabBtnUtm" onclick="switchToolsTab('utm')">
                    <span>🔗</span> Builder Tassonomia UTM B2B
                </button>
                <button class="tools-tab-btn" id="tabBtnTradeShow" onclick="switchToolsTab('tradeshow')">
                    <span>🎪</span> Modello ROI Fiere B2B
                </button>
            </div>

            <!-- TAB 1: MQL-to-SQL SLA & Lead Leakage Calculator (IT) -->
            <div class="tool-pane" id="paneToolsSla">
                <div class="tool-intro-box" style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 260px;">
                        <h4 class="tool-pane-title">Calcolatore SLA MQL-to-SQL &amp; Dispersione Pipeline</h4>
                        <p class="tool-pane-desc">Quantifica come la latenza di risposta commerciale degrada la conversione della pipeline inbound. Il routing sotto i 5 minuti genera fino a 8 volte più conversioni rispetto ai tradizionali fogli di calcolo.</p>
                    </div>
                    <a href="/it/tools/mql-to-sql-sla-lead-leakage-calculator/" target="_blank" rel="noopener noreferrer" class="tool-dedicated-btn">
                        <span>↗</span> Apri Tool Dedicato
                    </a>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaLeadsInput">Lead Inbound / Eventi Mensili</label>
                                <span class="tool-val-display" id="slaLeadsVal">350 lead</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaLeadsInput" min="50" max="2500" step="25" value="350" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaAcvInput">Valore Medio Trattativa B2B (€)</label>
                                <span class="tool-val-display" id="slaAcvVal">€15,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaAcvInput" min="2000" max="100000" step="1000" value="15000" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Tempo Medio Attuale di Risposta Commerciale</label>
                            <div class="tool-pills-row" id="slaSpeedPills">
                                <button type="button" class="tool-pill-option active" data-speed="slow" onclick="setSlaFollowup('slow')">&gt; 48 Ore (CSV Manuale)</button>
                                <button type="button" class="tool-pill-option" data-speed="medium" onclick="setSlaFollowup('medium')">24 Ore</button>
                                <button type="button" class="tool-pill-option" data-speed="fast" onclick="setSlaFollowup('fast')">&lt; 5 Minuti (Webhook + SLA HubSpot)</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid">
                            <div class="tool-kpi-card" style="border-color: rgba(251, 113, 133, 0.4); background: rgba(251, 113, 133, 0.05);">
                                <div class="tool-kpi-label">Pipeline Annuale Dispersa (€)</div>
                                <div class="tool-kpi-num" id="slaLeakedVal" style="color: #fb7185;">€19,530,000</div>
                                <div class="tool-kpi-sub" id="slaLeakedSub">75% dispersione per latenza (&gt; 48h)</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">Pipeline Recuperabile con Routing a Latenza Zero (€)</div>
                                <div class="tool-kpi-num" id="slaRecoverableVal" style="color: #34d399;">€13,671,000</div>
                                <div class="tool-kpi-sub" id="slaRecoverableSub">Con routing automatizzato SLA &lt; 5 min</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Incremento Conversione MQL-to-SQL (%)</div>
                                <div class="tool-kpi-num" id="slaLiftVal" style="color: #d4a863;">+775%</div>
                                <div class="tool-kpi-sub" id="slaLiftSub">4% attuale → 35% target SLA</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('services');">
                                <span>⚡</span> Risolvi Questa Dispersione Pipeline nel Tuo CRM →
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: Governance UTM & CRM (IT) -->
            <div class="tool-pane" id="paneToolsUtm" style="display: none;">
                <div class="tool-intro-box" style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 260px;">
                        <h4 class="tool-pane-title">Builder UTM Campagne B2B &amp; Governance CRM</h4>
                        <p class="tool-pane-desc">Definisci convenzioni di tracciamento standard per l'acquisizione a pagamento e mappa i parametri nei campi modulo nascosti di HubSpot/Salesforce.</p>
                    </div>
                    <a href="/it/tools/b2b-campaign-utm-crm-builder/" target="_blank" rel="noopener noreferrer" class="tool-dedicated-btn">
                        <span>↗</span> Apri Tool Dedicato
                    </a>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <label for="utmUrlInput" class="tool-input-label">URL Landing Page di Destinazione</label>
                            <input type="url" class="tool-text-input" id="utmUrlInput" value="https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Canale / Sorgente</label>
                            <div class="tool-pills-row" id="utmSourcePills">
                                <button type="button" class="tool-pill-option active" data-src="linkedin" onclick="setUtmSource('linkedin')">linkedin</button>
                                <button type="button" class="tool-pill-option" data-src="google" onclick="setUtmSource('google')">google</button>
                                <button type="button" class="tool-pill-option" data-src="meta" onclick="setUtmSource('meta')">meta</button>
                                <button type="button" class="tool-pill-option" data-src="tradeshow_qr" onclick="setUtmSource('tradeshow_qr')">tradeshow_qr</button>
                                <button type="button" class="tool-pill-option" data-src="email_nurture" onclick="setUtmSource('email_nurture')">email_nurture</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Medium</label>
                            <div class="tool-pills-row" id="utmMediumPills">
                                <button type="button" class="tool-pill-option active" data-med="cpc" onclick="setUtmMedium('cpc')">cpc</button>
                                <button type="button" class="tool-pill-option" data-med="abm_sponsored" onclick="setUtmMedium('abm_sponsored')">abm_sponsored</button>
                                <button type="button" class="tool-pill-option" data-med="offline_badge" onclick="setUtmMedium('offline_badge')">offline_badge</button>
                                <button type="button" class="tool-pill-option" data-med="automation" onclick="setUtmMedium('automation')">automation</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label for="utmCampaignInput" class="tool-input-label">Nome Campagna (Auto-formattato in minuscolo con underscore)</label>
                            <input type="text" class="tool-text-input" id="utmCampaignInput" value="2026_q2_enterprise_revops_scale" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Segmento ICP / Regione</label>
                            <div class="tool-pills-row" id="utmRegionPills">
                                <button type="button" class="tool-pill-option active" data-reg="emea" onclick="setUtmRegion('emea')">emea</button>
                                <button type="button" class="tool-pill-option" data-reg="americas" onclick="setUtmRegion('americas')">americas</button>
                                <button type="button" class="tool-pill-option" data-reg="dach" onclick="setUtmRegion('dach')">dach</button>
                                <button type="button" class="tool-pill-option" data-reg="italy" onclick="setUtmRegion('italy')">italy</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="terminal-block">
                            <div class="terminal-bar">
                                <span class="terminal-tag">URL TRACCIAMENTO GOVERNATO</span>
                                <button class="terminal-copy-btn" id="btnCopyUtm" onclick="copyGovernedUrl()">📋 Copia URL con Governance</button>
                            </div>
                            <div class="terminal-content" id="utmOutputUrl" style="word-break: break-all; font-family: var(--font-mono); font-size: 0.72rem; color: #38bdf8; line-height: 1.5; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px;">
                                https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/?utm_source=linkedin&amp;utm_medium=cpc&amp;utm_campaign=2026_q2_enterprise_revops_scale&amp;custom_icp_region=emea
                            </div>
                        </div>

                        <div class="terminal-block" style="margin-top: 1rem;">
                            <div class="terminal-bar">
                                <span class="terminal-tag">CAMPI MODULO NASCOSTI HUBSPOT / SALESFORCE</span>
                                <span style="font-family: var(--font-mono); font-size: 0.62rem; color: var(--accent-gold);">SCHEMA JSON</span>
                            </div>
                            <pre class="terminal-content" id="utmJsonPreview" style="font-family: var(--font-mono); font-size: 0.68rem; color: #a78bfa; line-height: 1.45; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px; margin: 0; overflow-x: auto;">{
  "utm_source": "linkedin",
  "utm_medium": "cpc",
  "utm_campaign": "2026_q2_enterprise_revops_scale",
  "custom_icp_region": "emea"
}</pre>
                        </div>
                        <div class="tool-cta-wrapper" style="margin-top: 1.15rem;">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('services');">
                                <span>🔗</span> Elimina la Dispersione di Attribuzione nel CRM →
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: B2B Trade Show & Exhibition ROI Calculator (IT) -->
            <div class="tool-pane" id="paneToolsTradeShow" style="display: none;">
                <div class="tool-intro-box" style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 260px;">
                        <h4 class="tool-pane-title">Calcolatore ROI Fiere &amp; Stand B2B</h4>
                        <p class="tool-pane-desc">Modellato sulle reali dinamiche fieristiche industriali internazionali (IFAT Monaco, PRS Europe). Calcola la generazione di pipeline, il costo per opportunità e le ore risparmiate tramite automazione.</p>
                    </div>
                    <a href="/it/tools/b2b-trade-show-roi-calculator/" target="_blank" rel="noopener noreferrer" class="tool-dedicated-btn">
                        <span>↗</span> Apri Tool Dedicato
                    </a>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsCostInput">Costo Totale Stand &amp; Sponsorizzazione Fiera (€)</label>
                                <span class="tool-val-display" id="tsCostVal">€45,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsCostInput" min="5000" max="250000" step="2500" value="45000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsBadgesInput">Badge Scansionati in Fiera</label>
                                <span class="tool-val-display" id="tsBadgesVal">320 badge</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsBadgesInput" min="20" max="2500" step="10" value="320" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsQualInput">Tasso di Qualifica (% ICP ad Alto Intento)</label>
                                <span class="tool-val-display" id="tsQualVal">45%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsQualInput" min="5" max="90" step="5" value="45" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsAcvInput">Valore Medio Contratto (€)</label>
                                <span class="tool-val-display" id="tsAcvVal">€28,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsAcvInput" min="2000" max="150000" step="1000" value="28000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsWinRateInput">Tasso di Chiusura (%)</label>
                                <span class="tool-val-display" id="tsWinRateVal">22%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsWinRateInput" min="2" max="60" step="1" value="22" oninput="updateTradeShowRoi()">
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid" style="grid-template-columns: repeat(2, 1fr);">
                            <div class="tool-kpi-card" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.05);">
                                <div class="tool-kpi-label">Costo per Lead Scansionato (€)</div>
                                <div class="tool-kpi-num" id="tsCplVal" style="color: #38bdf8;">€141</div>
                                <div class="tool-kpi-sub" id="tsCplSub">Costo per SQL qualificato: €313</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Pipeline SQL Generata (€)</div>
                                <div class="tool-kpi-num" id="tsPipelineVal" style="color: #d4a863;">€4,032,000</div>
                                <div class="tool-kpi-sub" id="tsPipelineSub">Fatturato previsto vinto: €887,040</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">ROAS Previsto Evento (x)</div>
                                <div class="tool-kpi-num" id="tsRoasVal" style="color: #34d399;">19.7x</div>
                                <div class="tool-kpi-sub" id="tsRoasSub">Rendimento sul capitale investito</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(167, 139, 250, 0.4); background: rgba(167, 139, 250, 0.05);">
                                <div class="tool-kpi-label">Tempo Risparmiato con Sincronizzazione Badge-HubSpot (Ore)</div>
                                <div class="tool-kpi-num" id="tsHoursVal" style="color: #a78bfa;">43 ore</div>
                                <div class="tool-kpi-sub" id="tsHoursSub">Tramite sincronizzazione CRM a latenza zero</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('services');">
                                <span>🎪</span> Risolvi Questa Dispersione Pipeline nel Tuo CRM →
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>'''

PROJECTS_4_CARDS_EN = '''            <!-- Standalone Project Cards (4 Cards Grid) -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Automated CRM Enrichment Agent</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Google Antigravity + HubSpot API. Automatically scrapes corporate domains and classifies company firmographics against ICP in 30 seconds, saving 15+ hours weekly.</p>
                    <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7423816376298913792/" target="_blank" rel="noopener noreferrer" style="font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem;">View LinkedIn Post →</a>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Market Intelligence Pipeline</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Automated Workflow + Slack + HubSpot. Monitors competitor pricing shifts every 6 hours and logs intelligence summaries.</p>
                    <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7419768812691935233/" target="_blank" rel="noopener noreferrer" style="font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem;">View LinkedIn Post →</a>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Algorithmic Markov Chain Attribution Engine</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Python + SQL + BI. Technical B2B multi-touch attribution model calculating channel removal effects across Paid Search, LinkedIn ABM, Organic/GEO, and Offline Trade Shows to replace flawed last-click reporting.</p>
                    <button onclick="closeActiveModal(); openModalForPlanet('services');" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Explore Data Architecture →</button>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Enterprise HubSpot &amp; Salesforce RevOps Architecture</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">HubSpot Sandbox + Salesforce Dev Edition. End-to-end CRM governance featuring automated MQL-to-SQL assignment flows, mandatory deal-stage validation rules, custom objects, and SLA breach escalation webhooks.</p>
                    <button onclick="closeActiveModal(); openModalForPlanet('services');" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Explore RevOps Architecture →</button>
                </div>
            </div>'''

PROJECTS_4_CARDS_IT = '''            <!-- Standalone Project Cards (4 Cards Grid) -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Agente Automatico di Arricchimento CRM</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Google Antigravity + API HubSpot. Esegue lo scraping autonomo dei domini aziendali e classifica la firmografica rispetto all'ICP in 30 secondi, risparmiando oltre 15 ore settimanali.</p>
                    <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7423816376298913792/" target="_blank" rel="noopener noreferrer" style="font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem;">Visualizza Post LinkedIn →</a>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Pipeline di Market Intelligence</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Workflow Automatizzato + Slack + HubSpot. Monitora le variazioni di prezzo dei competitor ogni 6 ore e registra report di sintesi dell'intelligence.</p>
                    <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7419768812691935233/" target="_blank" rel="noopener noreferrer" style="font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem;">Visualizza Post LinkedIn →</a>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Motore di Attribuzione Algoritmica Markov Chain</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Python + SQL + BI. Modello di attribuzione multi-touch B2B tecnico che calcola gli effetti di rimozione del canale tra Ricerca a Pagamento, LinkedIn ABM, Organico/GEO e Fiere Offline per sostituire i modelli last-click.</p>
                    <button onclick="closeActiveModal(); openModalForPlanet('services');" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Esplora Architettura Dati →</button>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Architettura RevOps Enterprise HubSpot &amp; Salesforce</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">HubSpot Sandbox + Salesforce Dev Edition. Governance CRM end-to-end con flussi di assegnazione automatica MQL-to-SQL, regole di validazione deal-stage obbligatorie, oggetti personalizzati e webhook di escalation per violazioni SLA.</p>
                    <button onclick="closeActiveModal(); openModalForPlanet('services');" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Esplora Architettura RevOps →</button>
                </div>
            </div>'''

UPGRADED_MODAL_CONTACT_HTML = '''    <!-- MODAL 6: CONTACT -->
    <div class="spatial-modal-card" id="modalContact">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>✉️</span> Initiate Direct Transmission</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
                Available for high-impact opportunities in Marketing Operations, HubSpot CRM Architecture, and AI Marketing Automation workflows.
            </p>
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 18px; padding: 1.25rem; display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="font-size: 0.85rem; color: var(--text-secondary);">
                    📍 <strong>Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.</strong>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem;">
                <a href="https://calendly.com/renzo-francesqui" target="_blank" rel="noopener noreferrer" class="inspect-btn" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem; background: var(--accent-gold); color: #0a080e; font-weight: 700; border-color: var(--accent-gold);">
                    📅 Book a Call on Calendly
                </a>
                <a href="RenzoFrancesquiCV2026.pdf" target="_blank" download class="inspect-btn-secondary" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem;">
                    DOWNLOAD VERIFIED CV (PDF) ▹
                </a>
                <a href="mailto:renzo.francesqui@gmail.com" class="inspect-btn-secondary" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem; color: var(--text-primary);">
                    TRANSMIT EMAIL INQUIRY ✉
                </a>
                <a href="https://www.linkedin.com/in/renzofrancesqui/" target="_blank" rel="noopener noreferrer" class="inspect-btn-secondary" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem; color: var(--text-primary);">
                    CONNECT ON LINKEDIN 🔗
                </a>
            </div>
        </div>
    </div>'''

UPGRADED_MODAL_CONTACT_HTML_IT = '''    <!-- MODAL 6: CONTACT -->
    <div class="spatial-modal-card" id="modalContact">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>✉️</span> Avvia Trasmissione Diretta</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
                Disponibile per progetti freelance e collaborazioni ad alto impatto in Marketing Operations, Architetture HubSpot/Salesforce e Automazioni AI.
            </p>
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 18px; padding: 1.25rem; display: flex; flex-direction: column; gap: 0.75rem;">
                <div style="font-size: 0.85rem; color: var(--text-secondary);">
                    📍 <strong>Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA &amp; Globali.</strong>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem;">
                <a href="https://calendly.com/renzo-francesqui" target="_blank" rel="noopener noreferrer" class="inspect-btn" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem; background: var(--accent-gold); color: #0a080e; font-weight: 700; border-color: var(--accent-gold);">
                    📅 Prenota una Call su Calendly
                </a>
                <a href="RenzoFrancesquiCV2026.pdf" target="_blank" download class="inspect-btn-secondary" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem;">
                    SCARICA CV VERIFICATO (PDF) 📄
                </a>
                <a href="mailto:renzo.francesqui@gmail.com" class="inspect-btn-secondary" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem; color: var(--text-primary);">
                    INVIA EMAIL DIRETTA ✉️
                </a>
                <a href="https://www.linkedin.com/in/renzofrancesqui/" target="_blank" rel="noopener noreferrer" class="inspect-btn-secondary" style="text-align: center; text-decoration: none; padding: 0.8rem 1rem; color: var(--text-primary);">
                    CONNETTITI SU LINKEDIN 💼
                </a>
            </div>
        </div>
    </div>'''

UPGRADED_TOOLS_JS = '''        // ========================================================
        // INTERACTIVE TOOLS SUITE LOGIC (#modalTools)
        // ========================================================
        let currentSlaSpeed = 'slow';
        let currentUtmSource = 'linkedin';
        let currentUtmMedium = 'cpc';
        let currentUtmRegion = 'emea';

        function switchToolsTab(tabId) {
            ['sla', 'utm', 'tradeshow'].forEach(t => {
                const pane = document.getElementById(t === 'sla' ? 'paneToolsSla' : (t === 'utm' ? 'paneToolsUtm' : 'paneToolsTradeShow'));
                const btn = document.getElementById(t === 'sla' ? 'tabBtnSla' : (t === 'utm' ? 'tabBtnUtm' : 'tabBtnTradeShow'));
                if (pane) pane.style.display = (t === tabId) ? 'block' : 'none';
                if (btn) btn.classList.toggle('active', t === tabId);
            });
            if (tabId === 'sla') updateSlaCalculator();
            else if (tabId === 'utm') updateUtmBuilder();
            else if (tabId === 'tradeshow') updateTradeShowRoi();
            if (typeof playSynthTone === 'function') playSynthTone(520, 'sine', 0.06);
        }

        function setSlaFollowup(speed) {
            currentSlaSpeed = speed;
            const pills = document.querySelectorAll('#slaSpeedPills .tool-pill-option');
            pills.forEach(p => p.classList.toggle('active', p.getAttribute('data-speed') === speed));
            updateSlaCalculator();
        }

        function updateSlaCalculator() {
            const leadsInput = document.getElementById('slaLeadsInput');
            const acvInput = document.getElementById('slaAcvInput');
            if (!leadsInput || !acvInput) return;

            const leads = parseInt(leadsInput.value) || 350;
            const acv = parseInt(acvInput.value) || 15000;
            const isIt = document.documentElement.lang === 'it';

            const leadsVal = document.getElementById('slaLeadsVal');
            const acvVal = document.getElementById('slaAcvVal');
            if (leadsVal) leadsVal.innerText = `${leads.toLocaleString()} ${isIt ? 'lead' : 'leads'}`;
            if (acvVal) acvVal.innerText = `€${acv.toLocaleString()}`;

            let currentRate = 0.04;
            let leakageRate = 0.75;
            let speedLabel = '> 48h';
            if (currentSlaSpeed === 'slow') {
                currentRate = 0.04;
                leakageRate = 0.75;
                speedLabel = '> 48h';
            } else if (currentSlaSpeed === 'medium') {
                currentRate = 0.14;
                leakageRate = 0.40;
                speedLabel = '24h';
            } else {
                currentRate = 0.35;
                leakageRate = 0.05;
                speedLabel = '< 5m';
            }

            const optimalRate = 0.35;
            const currentSqls = leads * currentRate;
            const optimalSqls = leads * optimalRate;
            const lostSqls = Math.max(0, optimalSqls - currentSqls);

            // Annual calculations (12 months)
            const annualLeakedVal = lostSqls * acv * 12;
            const annualRecoverableVal = lostSqls * 0.70 * acv * 12;
            const liftPct = currentRate > 0 ? Math.round(((optimalRate - currentRate) / currentRate) * 100) : 0;

            const elLeaked = document.getElementById('slaLeakedVal');
            const elLeakedSub = document.getElementById('slaLeakedSub');
            const elRec = document.getElementById('slaRecoverableVal');
            const elRecSub = document.getElementById('slaRecoverableSub');
            const elLift = document.getElementById('slaLiftVal');
            const elLiftSub = document.getElementById('slaLiftSub');

            if (elLeaked) elLeaked.innerText = `€${Math.round(annualLeakedVal).toLocaleString()}`;
            if (elLeakedSub) {
                elLeakedSub.innerText = isIt
                    ? `${Math.round(leakageRate * 100)}% dispersione per latenza (${speedLabel})`
                    : `${Math.round(leakageRate * 100)}% lead drop-off due to latency (${speedLabel})`;
            }
            if (elRec) elRec.innerText = `€${Math.round(annualRecoverableVal).toLocaleString()}`;
            if (elRecSub) {
                elRecSub.innerText = isIt
                    ? 'Con routing automatizzato SLA < 5 min'
                    : 'With sub-5min automated SLA';
            }
            if (elLift) elLift.innerText = `+${liftPct}%`;
            if (elLiftSub) {
                elLiftSub.innerText = isIt
                    ? `${Math.round(currentRate * 100)}% attuale → 35% target SLA`
                    : `${Math.round(currentRate * 100)}% current → 35% SLA target`;
            }
        }

        function setUtmSource(src) {
            currentUtmSource = src;
            const pills = document.querySelectorAll('#utmSourcePills .tool-pill-option');
            pills.forEach(p => p.classList.toggle('active', p.getAttribute('data-src') === src || p.innerText.trim().toLowerCase() === src));
            updateUtmBuilder();
        }

        function setUtmMedium(med) {
            currentUtmMedium = med;
            const pills = document.querySelectorAll('#utmMediumPills .tool-pill-option');
            pills.forEach(p => p.classList.toggle('active', p.getAttribute('data-med') === med || p.innerText.trim().toLowerCase() === med));
            updateUtmBuilder();
        }

        function setUtmRegion(reg) {
            currentUtmRegion = reg;
            const pills = document.querySelectorAll('#utmRegionPills .tool-pill-option');
            pills.forEach(p => p.classList.toggle('active', p.getAttribute('data-reg') === reg || p.innerText.trim().toLowerCase() === reg));
            updateUtmBuilder();
        }

        function updateUtmBuilder() {
            const urlInput = document.getElementById('utmUrlInput');
            const campInput = document.getElementById('utmCampaignInput');
            if (!urlInput || !campInput) return;

            const isIt = document.documentElement.lang === 'it';
            let defaultBase = isIt ? 'https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/' : 'https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/';
            let rawUrl = urlInput.value.trim() || defaultBase;
            const hashIdx = rawUrl.indexOf('#');
            let hashPart = '';
            if (hashIdx !== -1) {
                hashPart = rawUrl.slice(hashIdx);
                rawUrl = rawUrl.slice(0, hashIdx);
            }
            let baseUrl = rawUrl.split('?')[0].trim();
            if (!baseUrl) baseUrl = defaultBase;

            const rawCamp = campInput.value.trim() || '2026_q2_enterprise_revops_scale';
            // Auto-slugified to lowercase with underscores
            const slugCamp = rawCamp.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');

            const finalUrl = `${baseUrl}?utm_source=${encodeURIComponent(currentUtmSource)}&utm_medium=${encodeURIComponent(currentUtmMedium)}&utm_campaign=${encodeURIComponent(slugCamp)}&custom_icp_region=${encodeURIComponent(currentUtmRegion)}${hashPart}`;

            const outEl = document.getElementById('utmOutputUrl');
            if (outEl) outEl.innerText = finalUrl;

            const jsonPreview = {
                "utm_source": currentUtmSource,
                "utm_medium": currentUtmMedium,
                "utm_campaign": slugCamp,
                "custom_icp_region": currentUtmRegion
            };

            const jsonEl = document.getElementById('utmJsonPreview');
            if (jsonEl) jsonEl.innerText = JSON.stringify(jsonPreview, null, 2);
        }

        function copyGovernedUrl() {
            const outEl = document.getElementById('utmOutputUrl');
            const btn = document.getElementById('btnCopyUtm');
            if (!outEl) return;
            const textToCopy = outEl.innerText.trim();
            const isIt = document.documentElement.lang === 'it';
            const originalText = isIt ? '📋 Copia URL con Governance' : '📋 Copy Governed URL';
            const showSuccess = () => {
                if (btn) {
                    btn.innerText = isIt ? 'Copiato! ✓' : 'Copied! ✓';
                    setTimeout(() => { if (btn) btn.innerText = originalText; }, 2000);
                }
            };
            const showError = () => {
                if (btn) {
                    btn.innerText = isIt ? 'Errore di copia' : 'Error copying';
                    setTimeout(() => { if (btn) btn.innerText = originalText; }, 2000);
                }
            };
            const fallbackCopy = (text) => {
                try {
                    const textArea = document.createElement('textarea');
                    textArea.value = text;
                    textArea.style.position = 'fixed';
                    textArea.style.top = '-9999px';
                    textArea.style.left = '-9999px';
                    textArea.setAttribute('readonly', '');
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    const successful = document.execCommand('copy');
                    document.body.removeChild(textArea);
                    if (successful) showSuccess();
                    else showError();
                } catch (e) {
                    showError();
                }
            };
            if (navigator.clipboard && window.isSecureContext) {
                navigator.clipboard.writeText(textToCopy).then(showSuccess).catch(() => {
                    fallbackCopy(textToCopy);
                });
            } else {
                fallbackCopy(textToCopy);
            }
        }

        function updateTradeShowRoi() {
            const costInput = document.getElementById('tsCostInput');
            const badgesInput = document.getElementById('tsBadgesInput');
            const qualInput = document.getElementById('tsQualInput');
            const acvInput = document.getElementById('tsAcvInput');
            const winRateInput = document.getElementById('tsWinRateInput');
            if (!costInput || !badgesInput || !qualInput || !acvInput || !winRateInput) return;

            const cost = parseInt(costInput.value) || 45000;
            const badges = parseInt(badgesInput.value) || 320;
            const qualPct = parseInt(qualInput.value) || 45;
            const acv = parseInt(acvInput.value) || 28000;
            const winRate = parseInt(winRateInput.value) || 22;
            const isIt = document.documentElement.lang === 'it';

            const elCost = document.getElementById('tsCostVal');
            const elBadges = document.getElementById('tsBadgesVal');
            const elQual = document.getElementById('tsQualVal');
            const elAcv = document.getElementById('tsAcvVal');
            const elWin = document.getElementById('tsWinRateVal');

            if (elCost) elCost.innerText = `€${cost.toLocaleString()}`;
            if (elBadges) elBadges.innerText = `${badges.toLocaleString()} ${isIt ? 'badge' : 'badges'}`;
            if (elQual) elQual.innerText = `${qualPct}%`;
            if (elAcv) elAcv.innerText = `€${acv.toLocaleString()}`;
            if (elWin) elWin.innerText = `${winRate}%`;

            const qualSqls = Math.round(badges * (qualPct / 100));
            const cpl = badges > 0 ? Math.round(cost / badges) : 0;
            const costPerSql = qualSqls > 0 ? Math.round(cost / qualSqls) : 0;
            const pipeline = qualSqls * acv;
            const wonRev = Math.round(pipeline * (winRate / 100));
            const roas = cost > 0 ? (wonRev / cost).toFixed(1) : '0';
            const hoursSaved = Math.round((badges * 8) / 60);

            const elCpl = document.getElementById('tsCplVal');
            const elCplSub = document.getElementById('tsCplSub');
            const elPipe = document.getElementById('tsPipelineVal');
            const elPipeSub = document.getElementById('tsPipelineSub');
            const elRoas = document.getElementById('tsRoasVal');
            const elHours = document.getElementById('tsHoursVal');

            if (elCpl) elCpl.innerText = `€${cpl}`;
            if (elCplSub) elCplSub.innerText = isIt ? `Costo per SQL qualificato: €${costPerSql}` : `Cost per qualified SQL: €${costPerSql}`;
            if (elPipe) elPipe.innerText = `€${pipeline.toLocaleString()}`;
            if (elPipeSub) elPipeSub.innerText = isIt ? `Fatturato previsto vinto: €${wonRev.toLocaleString()}` : `Projected won: €${wonRev.toLocaleString()}`;
            if (elRoas) elRoas.innerText = `${roas}x`;
            if (elHours) elHours.innerText = `${hoursSaved} ${isIt ? 'ore' : 'hrs'}`;
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                updateSlaCalculator();
                updateUtmBuilder();
                updateTradeShowRoi();
            });
        } else {
            updateSlaCalculator();
            updateUtmBuilder();
            updateTradeShowRoi();
        }'''

def build_en_html(src):
    html = src

    # 0.5. Mobile & PulseLive CSS (IDEMPOTENT REPLACEMENT)
    css_pattern = r'[ \t]*/\* ========================================================\s*\*/\s*/\* PULSE LIVE ANIMATION & STATUS INDICATORS[\s\S]*?</style>(?:\s*</style>)*'
    if re.search(css_pattern, html):
        html = re.sub(css_pattern, UPGRADED_MOBILE_CSS, html)

    # 1. Update Title and Meta Tags
    html = re.sub(
        r'<title>.*?</title>',
        '<title>Renzo Francesqui — Digital Marketing, CRM Architecture & Business Insights</title>',
        html
    )
    html = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="Photorealistic 3D WebGL Solar System Portfolio & Interactive AI Representative for Renzo Francesqui — Digital Marketing, CRM Architecture, RevOps & Freelance Solutions.">',
        html
    )
    html = re.sub(
        r'<meta property="og:title" content=".*?">',
        '<meta property="og:title" content="Renzo Francesqui — Digital Marketing, CRM Architecture & Business Insights">',
        html
    )
    html = re.sub(
        r'<meta property="og:description" content=".*?">',
        '<meta property="og:description" content="Photorealistic 3D WebGL Solar System Portfolio & Interactive AI Representative for Renzo Francesqui — Digital Marketing, CRM Architecture, RevOps & Freelance Solutions.">',
        html
    )
    html = re.sub(
        r'<meta name="twitter:title" content=".*?">',
        '<meta name="twitter:title" content="Renzo Francesqui — Digital Marketing, CRM Architecture & Business Insights">',
        html
    )
    html = re.sub(
        r'<meta name="twitter:description" content=".*?">',
        '<meta name="twitter:description" content="Photorealistic 3D WebGL Solar System Portfolio & Interactive AI Representative for Renzo Francesqui — Digital Marketing, CRM Architecture, RevOps & Freelance Solutions.">',
        html
    )

    # 2. Update Header Brand Badge
    html = re.sub(
        r'<span class="brand-tag-badge">.*?</span>',
        '<span class="brand-tag-badge">Digital Marketing · CRM Architecture · Business Insights</span>',
        html
    )

    # Remove Classic 1.5 AND Services button from Header (Keep services only on menu dock below!)
    extra_header_btns = r'(?:<a href="/" class="hud-action-pill"[^>]*>[\s\S]*?CLASSIC V1\.5[\s\S]*?</a>\s*|<button class="hud-action-pill" onclick="focusOnPlanet\(\'services\'\)"[^>]*>[\s\S]*?</button>\s*)'
    html = re.sub(extra_header_btns, '', html)

    # Language Switcher links for EN
    lang_switcher_pattern = r'<div class="lang-switcher" aria-label="Language selector">[\s\S]*?</div>'
    lang_switcher_en = '''<div class="lang-switcher" aria-label="Language selector">
                    <a href="index.html" class="lang-btn active" title="English">EN</a>
                    <span class="lang-divider">/</span>
                    <a href="it/index.html" class="lang-btn" title="Italiano">IT</a>
                </div>'''
    html = re.sub(lang_switcher_pattern, lang_switcher_en, html)

    # 3. Floating Orbit Hint: remove (v3.0), add ID, 5-second fade out timer
    hint_pattern = r'[ \t]*<div class="orbit-floating-hint"[^>]*>[\s\S]*?(?=<!-- Bottom Floating Spatial Menu Dock)'
    hint_replacement = '''<div class="orbit-floating-hint" id="orbitFloatingHint">
            <button class="hint-close-btn" onclick="dismissFloatingHint(event)" aria-label="Close welcome HUD">✕</button>
            <div class="hint-eyebrow"><span class="hint-pulse-dot"></span> ONLINE // MILAN &amp; PARMA, ITALY • EMEA &amp; GLOBAL</div>
            <div class="hint-headline">Renzo Francesqui — CRM Architecture, RevOps &amp; Digital Growth</div>
            <div class="hint-subtext">Drag to orbit the 3D Solar Matrix • Click any planet to inspect • Select a sector below</div>
            <div class="hint-actions">
                <button class="hint-pill-btn" onclick="dismissFloatingHint(); openModalForPlanet('services');"><span>⚡</span> Explore Freelance Services</button>
                <button class="hint-pill-btn" onclick="dismissFloatingHint(); openModalForPlanet('experience');"><span>📄</span> View Track Record</button>
            </div>
        </div>

        '''
    html = re.sub(hint_pattern, hint_replacement, html)

    # 4. Floating Action Pills / Bottom Dock
    dock_pattern = r'[ \t]*<nav class="dock-pill-bar">[\s\S]*?</nav>'
    dock_replacement = '''<nav class="dock-pill-bar">
                <button class="dock-pill-btn" onclick="focusOnPlanet('ai_dialogue', true)">
                    <span>💬</span> AI Dialogue
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('services', true)">
                    <span>⚡</span> Services
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('experience', true)">
                    <span>🏛️</span> Experience
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('projects', true)">
                    <span>🚀</span> Projects
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('skills', true)">
                    <span>🛠️</span> Skills
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('tools', true)">
                    <span>🧰</span> Tools
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('blog', true)">
                    <span>📰</span> Blog
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('credentials', true)">
                    <span>🎓</span> Certifications
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('contact', true)">
                    <span>✉️</span> Get in Touch
                </button>
            </nav>'''
    html = re.sub(dock_pattern, dock_replacement, html)

    # 6. #modalServices Modal Card (IDEMPOTENT REPLACEMENT)
    modal_services_pattern = r'[ \t]*<!-- MODAL: SERVICES \(FREELANCE SOLUTIONS\) -->[\s\S]*?(?=<!-- MODAL 1: EXPERIENCE -->)'
    if re.search(modal_services_pattern, html):
        html = re.sub(modal_services_pattern, UPGRADED_MODAL_SERVICES_HTML + '\n\n    ', html)
    else:
        html = html.replace('<!-- MODAL 1: EXPERIENCE -->', UPGRADED_MODAL_SERVICES_HTML + '\n\n    <!-- MODAL 1: EXPERIENCE -->')

    # 6.4. Projects 4 Cards Grid (IDEMPOTENT REPLACEMENT)
    projects_pattern = r'[ \t]*(?:<!-- Standalone Project Cards.*?-->\s*)?<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 1rem;(?:\s*margin-top: 1rem;)?"?>[\s\S]*?(?=</div>\s*</div>\s*<!-- MODAL 3: SKILLS)'
    if re.search(projects_pattern, html):
        html = re.sub(projects_pattern, PROJECTS_4_CARDS_EN + '\n        ', html)

    # 6.6. Contact Location Badge & Calendly Booking Button in EN (IDEMPOTENT REPLACEMENT)
    modal_contact_pattern = r'[ \t]*<!-- MODAL 6: CONTACT -->[\s\S]*?(?=<!-- THREE\.JS 3D ENGINE)'
    if re.search(modal_contact_pattern, html):
        html = re.sub(modal_contact_pattern, UPGRADED_MODAL_CONTACT_HTML + '\n\n    ', html)
    else:
        html = html.replace('Based in Milan, Italy.', 'Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.')
        html = html.replace('📍 <strong>Based in Milan, Italy.</strong>', '📍 <strong>Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.</strong>')

    # 6.5. #modalTools Modal Card (IDEMPOTENT REPLACEMENT)
    modal_tools_pattern = r'[ \t]*<!-- MODAL: TOOLS -->[\s\S]*?(?=<!-- MODAL 4: CREDENTIALS -->)'
    if re.search(modal_tools_pattern, html):
        html = re.sub(modal_tools_pattern, UPGRADED_MODAL_TOOLS_HTML + '\n\n    ', html)
    else:
        html = html.replace('<!-- MODAL 4: CREDENTIALS -->', UPGRADED_MODAL_TOOLS_HTML + '\n\n    <!-- MODAL 4: CREDENTIALS -->')

    # 7. Procedural Texture and Solar Shaders Engine (IDEMPOTENT REPLACEMENT)
    tex_pattern = r'[ \t]*(?:// ========================================================\s*// 3\. PHOTOREALISTIC SOLAR[\s\S]*?|function createServicesNexusTexture\(\) \{[\s\S]*?|function createSunTexture\(\) \{[\s\S]*?)[ \t]*(?:const RENZO_AVATAR_DATA_URI = "[^"]*";\s*)?(?=const GARGANTUA_DATA_URI)'
    html = re.sub(tex_pattern, UPGRADED_TEXTURE_AND_SHADER_ENGINE + f'\n\n        const RENZO_AVATAR_DATA_URI = "{RENZO_AVATAR_DATA_URI}";\n\n        ', html)

    # 8. Sun Mesh, Chromosphere, and Dynamic Corona (IDEMPOTENT REPLACEMENT)
    sun_mesh_pattern = r'[ \t]*(?:// Central Photorealistic Star[\s\S]*?|// Central Sun Mesh & Corona[\s\S]*?)scene\.add\(coronaSprite\);'
    html = re.sub(sun_mesh_pattern, UPGRADED_SUN_MESH_CODE, html)

    # 9. Planet Configs with full PBR properties (IDEMPOTENT REPLACEMENT)
    planet_configs_pattern = r'[ \t]*const planetConfigs = \[\s\S]*?\];'
    html = re.sub(planet_configs_pattern, UPGRADED_PLANET_CONFIGS, html)

    # 10. Planet Creation Loop with PBR Materials & Non-Wobbling Rings (IDEMPOTENT REPLACEMENT)
    creation_loop_pattern = r'[ \t]*const planets = \[\];\s*planetConfigs\.forEach\(\(cfg\) => \{[\s\S]*?\}\);\s*[ \t]*(?=// ========================================================\s*// 4\.5\. 3D COSMIC COMET)'
    html = re.sub(creation_loop_pattern, UPGRADED_PLANET_CREATION_LOOP + '\n\n        ', html)

    # 11. Multi-pointer touch & camera interaction (IDEMPOTENT REPLACEMENT)
    touch_controls_pattern = r'[ \t]*(?:// Multi-touch & Pointer Tracking[\s\S]*?|// Mouse & Touch Orbit Controls[\s\S]*?)[ \t]*(?=// Raycaster for Planet & Comet Clicking)'
    html = re.sub(touch_controls_pattern, UPGRADED_TOUCH_AND_CAMERA_CONTROLS + '\n\n        ', html)

    # 11.5. Planetary Animate Loop (Orbit & non-wobbling rings update)
    anim_planets_pattern = r'[ \t]*// Orbit Planets & Rotate[\s\S]*?(?:if \(p\.ringGroup\) \{[\s\S]*?\}\s*)?if \(p\.clouds\) \{\s*p\.clouds\.rotation\.y \+= 0\.022;\s*\}'
    anim_planets_replacement = '''// Orbit Planets & Rotate
            planets.forEach(p => {
                p.angle += p.speed * 0.45;
                const px = Math.cos(p.angle) * p.config.orbitRadius;
                const pz = Math.sin(p.angle) * p.config.orbitRadius;
                p.mesh.position.x = px;
                p.mesh.position.z = pz;
                p.mesh.rotation.y += 0.015;

                if (p.ringGroup) {
                    p.ringGroup.position.x = px;
                    p.ringGroup.position.z = pz;
                }

                if (p.clouds) {
                    p.clouds.rotation.y += 0.022;
                }'''
    html = re.sub(anim_planets_pattern, anim_planets_replacement, html)

    # 12. Modal Map
    modal_map_pattern = r'[ \t]*const modalMap = \{[\s\S]*?\};'
    modal_map_replacement = '''const modalMap = {
                'services': 'modalServices',
                'experience': 'modalExperience',
                'projects': 'modalProjects',
                'skills': 'modalSkills',
                'tools': 'modalTools',
                'credentials': 'modalCredentials',
                'blog': 'modalBlog',
                'contact': 'modalContact'
            };'''
    html = re.sub(modal_map_pattern, modal_map_replacement, html)

    # 13. AI Chat Services Handler
    services_ai_code = '''            // Services & Freelance Query
            if (query.includes('serviz') || query.includes('freelance') || query.includes('service') || query.includes('cost') || query.includes('prezz') || query.includes('offer') || query.includes('hire') || query.includes('consulenz')) {
                return "I offer **4 specialized freelance solutions** to help high-growth businesses scale predictable revenue:\\n\\n1. **HubSpot CRM Setup & RevOps Architecture (Startup & SMB CRM Architecture)**: HubSpot/Salesforce lifecycle setup, lead routing & SLA automation.\\n2. **Paid Media Management**: High-intent Google, LinkedIn & Meta Ads demand generation.\\n3. **SEO & GEO Optimization**: Dual search engine + generative AI engine (ChatGPT/Perplexity) visibility.\\n4. **Marketing Data & Automated KPI Reporting**: GA4 multi-touch attribution, SQL modeling & Looker Studio executive dashboards.\\n\\nExplore the **Services** orb or submit a transmission in **Get in Touch** to discuss your project!";
            }
'''
    if "query.includes('serviz')" not in html:
        html = html.replace("const query = q.toLowerCase();", "const query = q.toLowerCase();\n" + services_ai_code)

    # 13.5. Interactive Tools Suite Logic (IDEMPOTENT REPLACEMENT)
    tools_js_pattern = r'[ \t]*// ========================================================\s*// INTERACTIVE TOOLS SUITE LOGIC \(#modalTools\)[\s\S]*?(?=function dismissFloatingHint)'
    if re.search(tools_js_pattern, html):
        html = re.sub(tools_js_pattern, UPGRADED_TOOLS_JS + '\n\n        ', html)
    else:
        html = html.replace('function dismissFloatingHint(e) {', UPGRADED_TOOLS_JS + '\n\n        function dismissFloatingHint(e) {')

    # 14. Floating Hint 5-Second Dismiss Timer
    timer_pattern = r'[ \t]*// Auto-dismiss the floating hint box[\s\S]*?\s*(?=appendMessage\(\'ai\',)'
    timer_5s_code = (
        "// Auto-dismiss the floating hint box after 5 seconds\n"
        "        setTimeout(() => {\n"
        "            if (typeof dismissFloatingHint === 'function') dismissFloatingHint();\n"
        "        }, 5000);\n\n        "
    )
    if re.search(timer_pattern, html):
        html = re.sub(timer_pattern, timer_5s_code, html)
    else:
        welcome_marker = "appendMessage('ai', \"Greetings!"
        if welcome_marker in html:
            html = html.replace(welcome_marker, timer_5s_code + welcome_marker)

    # 15. Sun & Chromosphere Animation in animate() (IDEMPOTENT REPLACEMENT)
    anim_sun_pattern = r'[ \t]*(?:// Update Photorealistic Sun, Chromosphere & Corona[\s\S]*?sunLight\.intensity = 3\.6 \+ Math\.sin\(animClock \* 1\.5\) \* 0\.15;\s*\}|// Rotate Sun\s*sunMesh\.rotation\.y \+= 0\.003;\s*coronaSprite\.rotation\.z \+= 0\.001;)'
    html = re.sub(anim_sun_pattern, UPGRADED_ANIMATE_SUN_CODE, html)

    # 16. Pixel Ratio on Resize
    resize_pattern = r'[ \t]*window\.addEventListener\(\'resize\', \(\) => \{\s*camera\.aspect = window\.innerWidth / window\.innerHeight;\s*camera\.updateProjectionMatrix\(\);\s*renderer\.setSize\(window\.innerWidth, window\.innerHeight\);[\s\S]*?\}\);'
    resize_replacement = '''window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        });'''
    html = re.sub(resize_pattern, resize_replacement, html)

    return html

def build_it_html(en_html):
    it = en_html

    # 1. HTML lang attribute
    it = it.replace('<html lang="en" data-theme="dark">', '<html lang="it" data-theme="dark">')

    # 2. Page Title & Meta Tags
    it = re.sub(
        r'<title>.*?</title>',
        '<title>Renzo Francesqui — Marketing Digitale, Architetture CRM & Business Insights</title>',
        it
    )
    it = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="Matrice solare 3D WebGL fotorealistica e Rappresentante AI interattivo di Renzo Francesqui — Marketing Operations B2B, Architetture CRM HubSpot, Paid Media & Automazioni AI.">',
        it
    )
    it = it.replace('content="https://renzo-francesqui.vercel.app/version-3/"', 'content="https://renzo-francesqui.vercel.app/version-3/it/"')
    it = re.sub(
        r'<meta property="og:title" content=".*?">',
        '<meta property="og:title" content="Renzo Francesqui — Marketing Digitale, Architetture CRM & Business Insights">',
        it
    )
    it = re.sub(
        r'<meta property="og:description" content=".*?">',
        '<meta property="og:description" content="Matrice solare 3D WebGL fotorealistica e Rappresentante AI interattivo di Renzo Francesqui — Marketing Operations B2B, Architetture CRM HubSpot, Paid Media & Automazioni AI.">',
        it
    )
    it = re.sub(
        r'<meta name="twitter:title" content=".*?">',
        '<meta name="twitter:title" content="Renzo Francesqui — Marketing Digitale, Architetture CRM & Business Insights">',
        it
    )
    it = re.sub(
        r'<meta name="twitter:description" content=".*?">',
        '<meta name="twitter:description" content="Matrice solare 3D WebGL fotorealistica e Rappresentante AI interattivo di Renzo Francesqui — Marketing Operations B2B, Architetture CRM HubSpot, Paid Media & Automazioni AI.">',
        it
    )

    # Alternate Links
    it = it.replace('<link rel="canonical" href="https://renzo-francesqui.vercel.app/version-3/">', '<link rel="canonical" href="https://renzo-francesqui.vercel.app/version-3/it/">')
    it = it.replace('<link rel="alternate" hreflang="en" href="https://renzo-francesqui.vercel.app/">', '<link rel="alternate" hreflang="en" href="https://renzo-francesqui.vercel.app/version-3/">')
    it = it.replace('<link rel="alternate" hreflang="it" href="https://renzo-francesqui.vercel.app/it/">', '<link rel="alternate" hreflang="it" href="https://renzo-francesqui.vercel.app/version-3/it/">')

    # Schema JSON-LD Job Title, URL, and Geographic Milan/Lombardy Properties
    old_v3_schema = '''    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Person",
          "@id": "https://renzo-francesqui.vercel.app/version-3/#person",
          "name": "Renzo Francesqui",
          "jobTitle": "Marketing Operations & CRM Specialist",
          "url": "https://renzo-francesqui.vercel.app/version-3/",
          "image": "https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg",
          "alumniOf": "Università degli Studi di Parma",
          "worksFor": {
            "@id": "https://renzo-francesqui.vercel.app/version-3/#organization"
          },
          "knowsAbout": [
            "HubSpot CRM Architecture",
            "Revenue Operations (RevOps)",
            "AI Marketing Automation",
            "Lead Scoring & Lifecycle Management",
            "Go-To-Market (GTM) Strategy",
            "Performance Marketing",
            "Salesforce Administration",
            "Oracle SQL"
          ]
        },
        {
          "@type": "Organization",
          "@id": "https://renzo-francesqui.vercel.app/version-3/#organization",
          "name": "TOMRA",
          "url": "https://renzo-francesqui.vercel.app/version-3/"
        },
        {
          "@type": "WebSite",
          "@id": "https://renzo-francesqui.vercel.app/version-3/#website",
          "name": "Renzo Francesqui Portfolio",
          "url": "https://renzo-francesqui.vercel.app/version-3/",
          "description": "Photorealistic 3D WebGL Solar System Portfolio & Interactive AI Representative for Renzo Francesqui — Digital Marketing, CRM Architecture, RevOps & Freelance Solutions.",
          "publisher": {
            "@id": "https://renzo-francesqui.vercel.app/version-3/#person"
          }
        },
        {
          "@type": "BreadcrumbList",
          "@id": "https://renzo-francesqui.vercel.app/version-3/#breadcrumb",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://renzo-francesqui.vercel.app/"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Version 3.0",
              "item": "https://renzo-francesqui.vercel.app/version-3/"
            }
          ]
        }
      ]
    }
    </script>'''

    new_v3_schema = '''    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Person",
          "@id": "https://renzo-francesqui.vercel.app/version-3/it/#person",
          "name": "Renzo Francesqui",
          "jobTitle": "Specialista Marketing Operations, Architetture CRM & RevOps",
          "url": "https://renzo-francesqui.vercel.app/version-3/it/",
          "image": "https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg",
          "alumniOf": "Università degli Studi di Parma",
          "areaServed": [
            {
              "@type": "City",
              "name": "Milano, Italy"
            },
            {
              "@type": "AdministrativeArea",
              "name": "Lombardy"
            }
          ],
          "location": {
            "@type": "Place",
            "name": "Milano, Italy",
            "address": {
              "@type": "PostalAddress",
              "addressLocality": "Milano",
              "addressRegion": "Lombardy",
              "addressCountry": "IT"
            }
          },
          "worksFor": {
            "@id": "https://renzo-francesqui.vercel.app/version-3/it/#organization"
          },
          "knowsAbout": [
            "HubSpot CRM Architecture",
            "Revenue Operations (RevOps)",
            "AI Marketing Automation",
            "Lead Scoring & Lifecycle Management",
            "Go-To-Market (GTM) Strategy",
            "Performance Marketing",
            "Salesforce Administration",
            "Oracle SQL"
          ]
        },
        {
          "@type": "Organization",
          "@id": "https://renzo-francesqui.vercel.app/version-3/it/#organization",
          "name": "TOMRA",
          "areaServed": [
            {
              "@type": "City",
              "name": "Milano, Italy"
            },
            {
              "@type": "AdministrativeArea",
              "name": "Lombardy"
            }
          ],
          "location": {
            "@type": "Place",
            "name": "Milano, Italy",
            "address": {
              "@type": "PostalAddress",
              "addressLocality": "Milano",
              "addressRegion": "Lombardy",
              "addressCountry": "IT"
            }
          }
        },
        {
          "@type": "WebSite",
          "@id": "https://renzo-francesqui.vercel.app/version-3/it/#website",
          "name": "Renzo Francesqui Portfolio",
          "url": "https://renzo-francesqui.vercel.app/version-3/it/",
          "description": "Matrice solare 3D WebGL fotorealistica e Rappresentante AI interattivo di Renzo Francesqui — Marketing Operations B2B, Architetture CRM HubSpot, Paid Media & Automazioni AI.",
          "publisher": {
            "@id": "https://renzo-francesqui.vercel.app/version-3/it/#person"
          }
        },
        {
          "@type": "BreadcrumbList",
          "@id": "https://renzo-francesqui.vercel.app/version-3/it/#breadcrumb",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://renzo-francesqui.vercel.app/"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Versione 3.0 (Italiano)",
              "item": "https://renzo-francesqui.vercel.app/version-3/it/"
            }
          ]
        }
      ]
    }
    </script>'''
    it = it.replace(old_v3_schema, new_v3_schema)

    # 3. Header Brand Badge
    it = re.sub(
        r'<span class="brand-tag-badge">.*?</span>',
        '<span class="brand-tag-badge">Marketing Digitale · Architettura CRM · Business Insights</span>',
        it
    )

    # Ensure header has NO services button
    extra_header_btns_it = r'(?:<button class="hud-action-pill" onclick="focusOnPlanet\(\'services\'\)"[^>]*>[\s\S]*?</button>\s*)'
    it = re.sub(extra_header_btns_it, '', it)

    # Header Action Buttons
    it = it.replace('<span>🔊</span> SOUND: ON', '<span>🔊</span> AUDIO: ON')
    it = it.replace('<span>🪐</span> ORBIT VIEW', '<span>🪐</span> VISTA ORBITA')

    # Language Switcher
    lang_switcher_it = '''<div class="lang-switcher" aria-label="Language selector">
                    <a href="../index.html" class="lang-btn" title="English">EN</a>
                    <span class="lang-divider">/</span>
                    <a href="index.html" class="lang-btn active" title="Italiano">IT</a>
                </div>'''
    it = re.sub(r'<div class="lang-switcher" aria-label="Language selector">[\s\S]*?</div>', lang_switcher_it, it)

        # 4. Floating Orbit Hint in Italian with 5s Timer (Mission Control Welcome HUD)
    hint_it_pattern = r'[ \t]*<div class="orbit-floating-hint"[^>]*>[\s\S]*?(?=<!-- Bottom Floating Spatial Menu Dock)'
    hint_it = '''<div class="orbit-floating-hint" id="orbitFloatingHint">
            <button class="hint-close-btn" onclick="dismissFloatingHint(event)" aria-label="Chiudi guida benvenuto">✕</button>
            <div class="hint-eyebrow"><span class="hint-pulse-dot"></span> ONLINE // MILANO &amp; PARMA, ITALIA • EMEA &amp; GLOBALE</div>
            <div class="hint-headline">Renzo Francesqui — Architettura CRM, RevOps &amp; Crescita Digitale</div>
            <div class="hint-subtext">🌌 <strong>Matrice Solare Fotorealistica</strong><br>Trascina per orbitare attorno al sole in 3D • Pizzica/scorri per lo zoom • Clicca o tocca qualsiasi pianeta per esplorare.</div>
            <div class="hint-actions">
                <button class="hint-pill-btn" onclick="dismissFloatingHint(); openModalForPlanet('services');"><span>⚡</span> Esplora Servizi</button>
                <button class="hint-pill-btn" onclick="dismissFloatingHint(); openModalForPlanet('experience');"><span>🏛️</span> Visualizza Esperienza</button>
            </div>
        </div>\n\n        '''
    it = re.sub(hint_it_pattern, hint_it, it)

    # 5. Bottom Dock in Italian (Services kept in bottom dock)
    dock_it = '''<nav class="dock-pill-bar">
                <button class="dock-pill-btn" onclick="focusOnPlanet('ai_dialogue', true)">
                    <span>💬</span> Dialogo AI
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('services', true)">
                    <span>⚡</span> Servizi
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('experience', true)">
                    <span>🏛️</span> Esperienza
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('projects', true)">
                    <span>🚀</span> Progetti
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('skills', true)">
                    <span>🛠️</span> Competenze
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('tools', true)">
                    <span>🧰</span> Strumenti
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('blog', true)">
                    <span>📰</span> Blog
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('credentials', true)">
                    <span>🎓</span> Certificazioni
                </button>
                <button class="dock-pill-btn" onclick="focusOnPlanet('contact', true)">
                    <span>✉️</span> Contattami
                </button>
            </nav>'''
    it = re.sub(r'<nav class="dock-pill-bar">[\s\S]*?</nav>', dock_it, it)

    # Floating chat trigger pill text
    it = it.replace('<span class="chat-trigger-text">AI Dialogue</span>', '<span class="chat-trigger-text">Dialogo AI</span>')

    # Inspect HUD buttons
    it = it.replace('title="Close and return to orbit" aria-label="Close"', 'title="Chiudi e torna all\'orbita" aria-label="Chiudi"')
    it = it.replace('<button class="inspect-btn" onclick="openCurrentPlanetModal()">OPEN DOSSIER ▹</button>', '<button class="inspect-btn" onclick="openCurrentPlanetModal()">ESPLORA DETTAGLIO →</button>')
    it = it.replace('<button class="inspect-btn-secondary" onclick="resetToOverview()">RETURN TO ORBIT ↺</button>', '<button class="inspect-btn-secondary" onclick="resetToOverview()">↺ MATRICE</button>')

    # 6. #modalServices in Italian
    it = it.replace(
        '<h2 class="modal-title-text"><span>⚡</span> High-Impact Freelance Services & Growth Systems</h2>',
        '<h2 class="modal-title-text"><span>⚡</span> Soluzioni Freelance ad Alto Impatto & Sistemi di Crescita</h2>'
    )
    it = it.replace(
        'AVAILABLE FOR STRATEGIC FREELANCE & REVOPS CONSULTING',
        'DISPONIBILE PER CONSULENZE STRATEGICHE REVOPS & FREELANCE'
    )
    it = it.replace(
        'Specialized enterprise-grade freelance engineering across HubSpot/Salesforce CRM architecture, B2B paid demand generation, technical SEO/GEO, and executive revenue intelligence.',
        'Ingegneria freelance enterprise-grade per architetture CRM HubSpot/Salesforce, generazione della domanda B2B, SEO/GEO tecnica e intelligence direzionale.'
    )
    it = it.replace('🎯 REVOPS ARCHITECTURE & STARTUP CRM', '🎯 ARCHITETTURA REVOPS & CRM STARTUP')
    it = it.replace('HubSpot CRM Setup & RevOps Architecture', 'Setup & Architettura HubSpot CRM & RevOps')
    it = it.replace('HubSpot CRM Setup & Optimization for Startups', 'Setup & Architettura HubSpot CRM & RevOps')
    it = it.replace('Small & Startup Business CRM Setup & Optimization', 'Setup & Ottimizzazione CRM per Startup e PMI')
    it = it.replace('Inquiry%20regarding%20HubSpot%20CRM%20Setup%20and%20RevOps', 'Richiesta%20Consulenza%20Setup%20CRM%20e%20RevOps')
    it = it.replace('Inquiry%20regarding%20Startup%20CRM%20Setup%20and%20RevOps', 'Richiesta%20Consulenza%20Setup%20CRM%20e%20RevOps')
    it = it.replace('Inquiry%20regarding%20Startup%20CRM%20Setup%20and%20Optimization', 'Richiesta%20Consulenza%20Setup%20CRM%20e%20RevOps')
    it = it.replace('Inquiry%20regarding%20Paid%20Media%20Management', 'Richiesta%20Consulenza%20Paid%20Media')
    it = it.replace('Inquiry%20regarding%20SEO%20and%20GEO%20Optimization', 'Richiesta%20Consulenza%20SEO%20e%20GEO')
    it = it.replace('Inquiry%20regarding%20Marketing%20Data%20and%20KPI%20Reporting', 'Richiesta%20Consulenza%20Data%20e%20Reporting')
    it = it.replace(
        'Eliminate lead leakage and chaotic spreadsheets. Complete HubSpot/Salesforce lifecycle modeling, custom pipeline properties, and SLA automation.',
        'Elimina le perdite di contatti e il disordine dei fogli di calcolo. Modellazione completa stadi lifecycle, proprietà personalizzate e automazione SLA su HubSpot/Salesforce.'
    )
    it = it.replace('Lifecycle stage modeling (Lead → MQL → SQL → Deal)', 'Modellazione stadi del ciclo di vita del cliente (Lead → MQL → SQL → Deal)')
    it = it.replace('Automated lead routing & 0-latency SLA notifications', 'Routing automatico lead e notifiche SLA a latenza zero')
    it = it.replace('Mandatory deal-stage gating properties', 'Proprietà vincolanti per l’avanzamento delle trattative')

    it = it.replace('📈 B2B PERFORMANCE & DEMAND GENERATION', '📈 PERFORMANCE B2B & GENERAZIONE DOMANDA')
    it = it.replace('Paid Media Management for B2B & Tech', 'Gestione Paid Media per B2B & Settore Tech')
    it = it.replace(
        'Stop wasting ad budgets. Full-funnel Google Search, LinkedIn ABM, and Meta campaigns acquiring qualified demo requests at profitable CAC.',
        'Interrompi lo spreco di budget. Campagne Google Search, LinkedIn ABM e Meta ads strutturate per generare richieste demo qualificate a CAC sostenibile.'
    )
    it = it.replace('High-intent Google Search keyword architecture', 'Architettura parole chiave ad alta intenzione commerciale')
    it = it.replace('LinkedIn Account-Based Marketing matching ICP firmographics', 'Campagne ABM su LinkedIn profilate sui parametri ICP aziendali')
    it = it.replace('Server-side tracking & GA4 offline conversion import', 'Tracciamento server-side e import conversioni offline GA4')

    it = it.replace('🌐 ORGANIC SEARCH & GENERATIVE AI ENGINE VISIBILITY', '🌐 RICERCA ORGANICA & VISIBILITÀ MOTORI AI')
    it = it.replace('Technical SEO & Generative Engine Optimization (GEO)', 'SEO Tecnico & Generative Engine Optimization (GEO)')
    it = it.replace(
        'Dual-engine organic dominance: rank in top Google SERPs while ensuring generative AI answer engines (ChatGPT, Perplexity, Gemini, Claude) cite your brand.',
        'Dominio organico duale: posizionamento su Google e ottimizzazione GEO per garantire che i motori AI (ChatGPT, Perplexity, Gemini, Claude) citino il tuo brand.'
    )
    it = it.replace('Core Web Vitals, crawl budget, and hreflang routing', 'Ottimizzazione Core Web Vitals, crawl budget e routing multilingua')
    it = it.replace('Generative Engine Optimization (GEO) brand entity modeling', 'Modellazione entità di brand per motori generativi LLM')
    it = it.replace('Advanced Schema.org JSON-LD microdata implementation', 'Implementazione microdati avanzati Schema.org JSON-LD')

    it = it.replace('📊 ANALYTICS, ATTRIBUTION & EXECUTIVE INTELLIGENCE', '📊 ANALISI DATI, ATTRIBUZIONE & DASHBOARD EXECUTIVE')
    it = it.replace('Marketing Data Modeling & Automated KPI Reporting', 'Modellazione Dati Marketing & Reportistica KPI Automatizzata')
    it = it.replace(
        'Connect your CRM, ads, and web analytics into executive dashboards with automated Slack/email revenue delivery. Single Source of Truth analytics.',
        'Connetti CRM, campagne ads e web analytics in dashboard unificate con reportistica automatica su Slack ed email. Unica fonte di verità aziendale.'
    )
    it = it.replace('End-to-end GA4 measurement & multi-touch attribution', 'Misurazione avanzata GA4 e attribuzione multi-touch')
    it = it.replace('Custom SQL pipeline modeling (BigQuery, PostgreSQL)', 'Query SQL personalizzate per data warehouse (BigQuery, PostgreSQL)')
    it = it.replace('Real-time Looker Studio / Power BI executive dashboards', 'Dashboard executive in tempo reale su Looker Studio / Power BI')

    it = it.replace('Inquire / Consult ✉️', 'Richiedi Consulenza ✉️')
    it = it.replace('Explore Scope ↗', 'Esplora Scheda ↗')
    it = it.replace('/services/', '/it/services/')

    it = it.replace('Ready to scale your marketing engine?', 'Pronto a scalare il tuo motore di marketing?')
    it = it.replace('Get in touch directly or download verified CV for freelance engagement.', 'Contattami direttamente o scarica il CV verificato per collaborazioni freelance.')
    it = it.replace('<span>✉️</span> Initiate Transmission', '<span>✉️</span> Avvia Trasmissione')
    it = it.replace('<span>📄</span> Download CV (PDF)', '<span>📄</span> Scarica CV (PDF)')

    # 7. #modalExperience in Italian
    it = it.replace('Professional Track Record', 'Esperienza Professionale & Track Record')
    it = it.replace(
        'Supported end-to-end lead operations across 15–20 directly organized global trade shows per year (including IFAT and PRS Europe), ensuring 100% of captured leads were synced to HubSpot for immediate follow-up across a 30–50 person EMEA & Americas sales team.',
        'Gestione end-to-end delle operazioni di lead capture per 15-20 fiere internazionali all’anno (tra cui IFAT e PRS Europe), garantendo sincronizzazione al 100% su HubSpot per follow-up immediato del team commerciale di 30-50 agenti in EMEA e Americhe.'
    )
    it = it.replace(
        'Co-led the operational buildout of HubSpot CRM adoption from near-zero usage to an active pipeline management system, standardizing lead capture processes, contact properties, and lifecycle stages across all field events.',
        'Co-leader nell’implementazione operativa e adozione di HubSpot CRM, standardizzando processi di raccolta contatti, proprietà personalizzate e stadi di ciclo di vita.'
    )
    it = it.replace(
        'Designed and enforced lead capture standardization at field events ranging from 8 to 350+ leads per show, eliminating data gaps and field mismatches between capture tools and HubSpot.',
        'Definizione e applicazione di standard rigorosi di lead capture negli eventi fieristici (da 8 a oltre 350 lead per evento), azzerando discrepanze e dati mancanti.'
    )
    it = it.replace(
        'Managed offline-to-online data integration workflows post-event, reducing lead-to-sales-handoff time from over one week to same-week import, cleaning, and routing.',
        'Ottimizzazione dei flussi di integrazione dati offline-online post-evento, riducendo i tempi di assegnazione commerciale da oltre una settimana a pochi giorni.'
    )
    it = it.replace(
        'Collaborated with the lead generation team to define "High Intent" lead criteria and build lead scoring logic in HubSpot, accelerating MQL-to-SQL handover and reducing lead stagnation in the pipeline.',
        'Collaborazione con il team di lead generation per definire criteri di intenzione d’acquisto e logica di lead scoring in HubSpot, accelerando il passaggio da MQL a SQL.'
    )

    it = it.replace(
        'Led marketing operations for a 5-person team executing international campaigns across 10+ countries in the Americas, Europe, and the Middle East.',
        'Supervisione delle operazioni di marketing per un team di 5 persone con campagne internazionali attive in oltre 10 paesi tra Americhe, Europa e Medio Oriente.'
    )
    it = it.replace(
        'Managed HubSpot CRM data integrity across international markets, standardizing contact properties, lifecycle stages, and campaign tracking to ensure clean attribution data.',
        'Controllo integrità dati su HubSpot CRM nei mercati internazionali, standardizzazione delle proprietà contatto e monitoraggio campagne per attribuzione affidabile.'
    )
    it = it.replace(
        'Executed SEO and SEM strategies across 4 regions, achieving a 40% increase in organic traffic in 6 months and a 33% improvement in paid conversion rates through continuous A/B testing and funnel optimization.',
        'Esecuzione strategie SEO e SEM su 4 aree geografiche, ottenendo un incremento del 40% del traffico organico in 6 mesi e un miglioramento del 33% nei tassi di conversione paid.'
    )
    it = it.replace(
        'Built Executive KPI Dashboards, visualizing channel performance and ROI attribution to guide Board-level decision-making.',
        'Creazione di dashboard KPI direzionali con visualizzazione delle performance dei canali e dell’attribuzione ROI per il processo decisionale esecutivo.'
    )

    it = it.replace(
        'Architected and executed full Go-To-Market (GTM) strategies across SEO/SEM, email workflows, and CRM lead capture for high-value residential developments, driving a complete 100% inventory sell-out before construction delivery.',
        'Progettazione ed esecuzione di strategie Go-To-Market (GTM) complete attraverso SEO/SEM, flussi email e lead capture CRM per complessi immobiliari di prestigio, raggiungendo il 100% delle vendite prima del termine dei lavori.'
    )
    it = it.replace(
        'Built and optimized CRM workflows and lead nurturing automations that drove an average monthly conversion rate increase of over 50% through rigorous A/B testing and funnel stage management.',
        'Costruzione e ottimizzazione di workflow CRM e automazioni di nurturing che hanno aumentato il tasso di conversione mensile medio di oltre il 50% mediante test A/B.'
    )
    it = it.replace(
        'Managed the complete lead lifecycle from social media capture to sales handoff, defining lead qualification criteria and ensuring consistent data quality for the sales team.',
        'Gestione dell’intero ciclo di vita del lead, dalla generazione su social media al passaggio alle vendite, con rigorosi criteri di qualifica.'
    )

    # 8. #modalProjects in Italian (4 Cards Grid)
    projects_pattern = r'[ \t]*(?:<!-- Standalone Project Cards.*?-->\s*)?<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 1rem;(?:\s*margin-top: 1rem;)?"?>[\s\S]*?(?=</div>\s*</div>\s*<!-- MODAL 3: SKILLS)'
    if re.search(projects_pattern, it):
        it = re.sub(projects_pattern, PROJECTS_4_CARDS_IT + '\n        ', it)
    it = it.replace('STEP-BY-STEP PIPELINE EXPLORER', 'SIMULATORE PIPELINE REVOPS')
    it = it.replace('NEXT STAGE →', 'PROSSIMO STADIO →')

    # 9. #modalSkills in Italian
    it = it.replace('Strategic Pillars & Skill Architecture', 'Pilastri Strategici & Competenze')

    # 9.5. #modalTools in Italian (Full Interactive Suite)
    modal_tools_pattern = r'[ \t]*<!-- MODAL: TOOLS -->[\s\S]*?(?=<!-- MODAL 4: CREDENTIALS -->)'
    it = re.sub(modal_tools_pattern, UPGRADED_MODAL_TOOLS_HTML_IT + '\n\n    ', it)

    # 10. #modalCredentials in Italian
    it = it.replace('Certifications & Academic Foundation', 'Accreditamenti Accademici & Certificazioni')
    it = it.replace('Completed Professional Certifications', 'Certificazioni Professionali Completate')
    it = it.replace('Certifications in Progress (2026)', 'Certificazioni in Corso (Obiettivo 2026)')
    it = it.replace('Currently studying / in pursuit', 'Attualmente in studio / preparazione attiva')
    it = it.replace('Academic Foundation & Languages', 'Formazione Accademica & Lingue')
    it = it.replace('Master:', 'Laurea Magistrale:')
    it = it.replace('Bachelor:', 'Laurea Triennale:')
    it = it.replace('Languages: Spanish (Native), English (C1), Italian (B2)', 'Lingue: Spagnolo (Madrelingua), Inglese (C1), Italiano (B2)')

    # 11. #modalContact in Italian (IDEMPOTENT REPLACEMENT WITH CALENDLY)
    modal_contact_pattern = r'[ \t]*<!-- MODAL 6: CONTACT -->[\s\S]*?(?=<!-- THREE\.JS 3D ENGINE)'
    if re.search(modal_contact_pattern, it):
        it = re.sub(modal_contact_pattern, UPGRADED_MODAL_CONTACT_HTML_IT + '\n\n    ', it)
    else:
        it = it.replace('Initiate Direct Transmission', 'Avvia Trasmissione Diretta')
        it = it.replace('Available for high-impact opportunities in Marketing Operations, HubSpot CRM Architecture, and AI Marketing Automation workflows.', 'Disponibile per progetti freelance e collaborazioni ad alto impatto in Marketing Operations, Architetture HubSpot/Salesforce e Automazioni AI.')
        it = it.replace('Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.', 'Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA &amp; Globali.')
        it = it.replace('Based in Milan, Italy • Available for EMEA & Global Remote / Hybrid Engagements.', 'Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA & Globali.')
        it = it.replace('Based in Milan, Italy.', 'Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA & Globali.')
        it = it.replace('📅 Book a Call on Calendly', '📅 Prenota una Call su Calendly')
        it = it.replace('DOWNLOAD VERIFIED CV (PDF) ▹', 'SCARICA CV VERIFICATO (PDF) 📄')
        it = it.replace('TRANSMIT EMAIL INQUIRY ✉', 'INVIA EMAIL DIRETTA ✉️')
        it = it.replace('CONNECT ON LINKEDIN 🔗', 'CONNETTITI SU LINKEDIN 💼')

    # 12. 3D Planet Names in Italian
    it = it.replace("name: 'AI Dialogue'", "name: 'Dialogo AI'")
    it = it.replace("name: 'Services'", "name: 'Servizi'")
    it = it.replace("name: 'Experience'", "name: 'Esperienza'")
    it = it.replace("name: 'Projects'", "name: 'Progetti'")
    it = it.replace("name: 'Skills'", "name: 'Competenze'")
    it = it.replace("name: 'Tools'", "name: 'Strumenti'")
    it = it.replace("name: 'Certifications'", "name: 'Certificazioni'")
    it = it.replace("name: 'Get in Touch'", "name: 'Contattami'")

    # 13. AI Dialogue Responses in Italian
    it_welcome = "Salve! Sono il rappresentante AI ufficiale di Renzo Francesqui. Esplora la matrice solare 3D o chiedimi informazioni su architetture CRM, servizi freelance RevOps e automazioni AI."
    it = re.sub(
        r'appendMessage\(\'ai\', "Greetings! I am Renzo\'s official AI representative\.[\s\S]*?"\);',
        f'appendMessage(\'ai\', "{it_welcome}");',
        it
    )

    it_ai_services_response = """            // Services & Freelance Query
            if (query.includes('serviz') || query.includes('freelance') || query.includes('service') || query.includes('cost') || query.includes('prezz') || query.includes('offer') || query.includes('hire') || query.includes('consulenz')) {
                return "Offro **4 soluzioni freelance specializzate** per aiutare aziende B2B e startup a scalare il fatturato in modo prevedibile:\\n\\n1. **Setup & Architettura HubSpot CRM & RevOps (Architettura CRM & RevOps Startup)**: Architettura HubSpot/Salesforce, modellazione lifecycle e automazione SLA.\\n2. **Gestione Paid Media (Google, LinkedIn, Meta)**: Acquisizione lead ad alta intenzione con riduzione del CAC.\\n3. **SEO & GEO Optimization**: Posizionamento su Google e visibilità su motori generativi (ChatGPT, Perplexity, Claude).\\n4. **Dati Marketing & Reportistica KPI**: Attribuzione GA4 multi-touch, query SQL e dashboard executive Looker Studio.\\n\\nEsplora l'orb **Servizi** o inviami un messaggio in **Contattami** per discutere del tuo progetto!";
            }"""
    it = re.sub(
        r'// Services & Freelance Query[\s\S]*?return "I offer \*\*4 specialized freelance solutions\*\*[\s\S]*?;\s*\}',
        it_ai_services_response,
        it
    )

    # Audio toggle strings
    it = it.replace("'<span>🔊</span> SOUND: ON'", "'<span>🔊</span> AUDIO: ON'")
    it = it.replace("'<span>🔇</span> SOUND: OFF'", "'<span>🔇</span> AUDIO: OFF'")

    return it

def build_root_en_html(en_html):
    root_en = en_html
    # 1. Canonical tag
    root_en = root_en.replace(
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/version-3/">',
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/">'
    )
    # 2. OpenGraph & Twitter URL
    root_en = root_en.replace(
        '<meta property="og:url" content="https://renzo-francesqui.vercel.app/version-3/">',
        '<meta property="og:url" content="https://renzo-francesqui.vercel.app/">'
    )
    root_en = root_en.replace(
        '<meta name="twitter:url" content="https://renzo-francesqui.vercel.app/version-3/">',
        '<meta name="twitter:url" content="https://renzo-francesqui.vercel.app/">'
    )
    # 3. Schema.org JSON-LD
    root_en = root_en.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/#person"',
        '"@id": "https://renzo-francesqui.vercel.app/#person"'
    )
    root_en = root_en.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/#organization"',
        '"@id": "https://renzo-francesqui.vercel.app/#organization"'
    )
    root_en = root_en.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/#website"',
        '"@id": "https://renzo-francesqui.vercel.app/#website"'
    )
    root_en = root_en.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/#breadcrumb"',
        '"@id": "https://renzo-francesqui.vercel.app/#breadcrumb"'
    )
    root_en = root_en.replace(
        '"url": "https://renzo-francesqui.vercel.app/version-3/"',
        '"url": "https://renzo-francesqui.vercel.app/"'
    )
    root_en = root_en.replace(
        '"item": "https://renzo-francesqui.vercel.app/version-3/"',
        '"item": "https://renzo-francesqui.vercel.app/"'
    )
    root_en = root_en.replace(
        '"name": "Version 3.0"',
        '"name": "Home"'
    )
    # 4. Hreflang alternates: ensure they point to root / and /it/
    root_en = re.sub(
        r'<link rel="alternate" hreflang="en" href="[^"]*">',
        '<link rel="alternate" hreflang="en" href="https://renzo-francesqui.vercel.app/">',
        root_en
    )
    root_en = re.sub(
        r'<link rel="alternate" hreflang="it" href="[^"]*">',
        '<link rel="alternate" hreflang="it" href="https://renzo-francesqui.vercel.app/it/">',
        root_en
    )
    root_en = re.sub(
        r'<link rel="alternate" hreflang="x-default" href="[^"]*">',
        '<link rel="alternate" hreflang="x-default" href="https://renzo-francesqui.vercel.app/">',
        root_en
    )
    return root_en

def build_root_it_html(it_html):
    root_it = it_html
    # 1. Canonical tag
    root_it = root_it.replace(
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/version-3/it/">',
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/it/">'
    )
    # 2. OpenGraph & Twitter URL
    root_it = root_it.replace(
        '<meta property="og:url" content="https://renzo-francesqui.vercel.app/version-3/it/">',
        '<meta property="og:url" content="https://renzo-francesqui.vercel.app/it/">'
    )
    root_it = root_it.replace(
        '<meta name="twitter:url" content="https://renzo-francesqui.vercel.app/version-3/it/">',
        '<meta name="twitter:url" content="https://renzo-francesqui.vercel.app/it/">'
    )
    # 3. Schema.org JSON-LD
    root_it = root_it.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/it/#person"',
        '"@id": "https://renzo-francesqui.vercel.app/it/#person"'
    )
    root_it = root_it.replace(
        '"url": "https://renzo-francesqui.vercel.app/version-3/it/"',
        '"url": "https://renzo-francesqui.vercel.app/it/"'
    )
    root_it = root_it.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/it/#organization"',
        '"@id": "https://renzo-francesqui.vercel.app/it/#organization"'
    )
    root_it = root_it.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/it/#website"',
        '"@id": "https://renzo-francesqui.vercel.app/it/#website"'
    )
    root_it = root_it.replace(
        '"@id": "https://renzo-francesqui.vercel.app/version-3/it/#breadcrumb"',
        '"@id": "https://renzo-francesqui.vercel.app/it/#breadcrumb"'
    )
    root_it = root_it.replace(
        '"item": "https://renzo-francesqui.vercel.app/version-3/it/"',
        '"item": "https://renzo-francesqui.vercel.app/it/"'
    )
    root_it = root_it.replace(
        '"name": "Versione 3.0 (Italiano)"',
        '"name": "Versione Italiana"'
    )
    # 3.5. Project Card Translation for Root IT
    root_it = root_it.replace(
        'Motore di Attribuzione Algoritmica Markov Chain',
        'Motore di Attribuzione Algoritmica con Catene di Markov'
    )
    # 4. Hreflang alternates: ensure they point to root / and /it/
    root_it = re.sub(
        r'<link rel="alternate" hreflang="en" href="[^"]*">',
        '<link rel="alternate" hreflang="en" href="https://renzo-francesqui.vercel.app/">',
        root_it
    )
    root_it = re.sub(
        r'<link rel="alternate" hreflang="it" href="[^"]*">',
        '<link rel="alternate" hreflang="it" href="https://renzo-francesqui.vercel.app/it/">',
        root_it
    )
    root_it = re.sub(
        r'<link rel="alternate" hreflang="x-default" href="[^"]*">',
        '<link rel="alternate" hreflang="x-default" href="https://renzo-francesqui.vercel.app/">',
        root_it
    )
    return root_it

def main():
    print("Reading base index.html...")
    src = read_source_html()

    print("Building Version 3.0 English edition...")
    en_html = build_en_html(src)
    with open(V3_INDEX, "w", encoding="utf-8") as f:
        f.write(en_html)
    print(f"[OK] Saved: {V3_INDEX} ({len(en_html)} bytes)")

    print("Building Version 3.0 Italian edition...")
    it_html = build_it_html(en_html)
    os.makedirs(V3_IT_DIR, exist_ok=True)
    with open(V3_IT_INDEX, "w", encoding="utf-8") as f:
        f.write(it_html)
    print(f"[OK] Saved: {V3_IT_INDEX} ({len(it_html)} bytes)")

    print("Building Root English edition (index.html)...")
    root_en_html = build_root_en_html(en_html)
    with open(ROOT_INDEX, "w", encoding="utf-8") as f:
        f.write(root_en_html)
    print(f"[OK] Saved: {ROOT_INDEX} ({len(root_en_html)} bytes)")

    print("Building Root Italian edition (it/index.html)...")
    root_it_html = build_root_it_html(it_html)
    os.makedirs(ROOT_IT_DIR, exist_ok=True)
    with open(ROOT_IT_INDEX, "w", encoding="utf-8") as f:
        f.write(root_it_html)
    print(f"[OK] Saved: {ROOT_IT_INDEX} ({len(root_it_html)} bytes)")

    # Ensure CV PDF is present in it/ and version-3/it/
    import shutil
    cv_src = BASE_DIR / "RenzoFrancesquiCV2026.pdf"
    if cv_src.exists():
        shutil.copy2(cv_src, ROOT_IT_DIR / "RenzoFrancesquiCV2026.pdf")
        shutil.copy2(cv_src, V3_IT_DIR / "RenzoFrancesquiCV2026.pdf")
        print(f"[OK] Synced CV PDF to {ROOT_IT_DIR / 'RenzoFrancesquiCV2026.pdf'} and {V3_IT_DIR / 'RenzoFrancesquiCV2026.pdf'}")

if __name__ == "__main__":
    main()

