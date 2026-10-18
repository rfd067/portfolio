#!/usr/bin/env python3
"""
apply_v3_upgrade.py
Surgically applies:
1. PulseLive keyframe animation & upgraded Mission Control Welcome HUD styles & Interactive Tools Suite CSS to UPGRADED_MOBILE_CSS in compile_v3.py.
2. UPGRADED_MODAL_TOOLS_HTML and UPGRADED_MODAL_TOOLS_HTML_IT with 3 interactive tools (SLA Leakage, UTM Builder, Trade Show ROI).
3. Welcome HUD replacement in build_en_html and build_it_html.
4. Touch controls with hint dismissal on drag and background click.
5. Navigation UX: focusOnPlanet(planetId, autoOpen = false) with 350ms delay when true; handlePointerClick passes false; dock pills pass true.
6. Deduplication of base64 avatar into RENZO_AVATAR_DATA_URI in version-3/index.html.
7. Expansion of #modalProjects bottom grid from 2 to 4 cards in version-3/index.html, index.html, compile_v3.py, and build_italian_version.py.
8. #modalContact location badge update.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ========================================================
# 1. UPGRADED CSS FOR compile_v3.py
# ========================================================
NEW_UPGRADED_MOBILE_CSS = '''        /* ======================================================== */
        /* PULSE LIVE ANIMATION & STATUS INDICATORS                 */
        /* ======================================================== */
        @keyframes pulseLive {
            0% {
                transform: scale(0.95);
                box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
            }
            70% {
                transform: scale(1.05);
                box-shadow: 0 0 0 6px rgba(16, 185, 129, 0);
            }
            100% {
                transform: scale(0.95);
                box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
            }
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
# 2. UPGRADED TOUCH CONTROLS FOR compile_v3.py
# ========================================================
NEW_UPGRADED_TOUCH_AND_CAMERA_CONTROLS = '''        // Multi-touch & Pointer Tracking for Mobile & Desktop (Smooth rotate, pinch-to-zoom, tap)
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
# 3. UPGRADED MODAL TOOLS HTML (EN & IT)
# ========================================================
NEW_UPGRADED_MODAL_TOOLS_HTML = '''    <!-- MODAL: TOOLS -->
    <div class="spatial-modal-card" id="modalTools">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>🧰</span> Tools</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <div class="tools-suite-header">
                <h3 class="tools-suite-title"><span>🧰</span> Interactive Tools & Utilities</h3>
                <p class="tools-suite-subtitle">Production-grade Revenue Operations calculators, campaign governance builders, and event lead modeling tools engineered by Renzo Francesqui.</p>
            </div>

            <div class="tools-tab-switcher">
                <button class="tools-tab-btn active" id="tabBtnSla" onclick="switchToolsTab('sla')">
                    <span>⚡</span> SLA &amp; Lead Leakage
                </button>
                <button class="tools-tab-btn" id="tabBtnUtm" onclick="switchToolsTab('utm')">
                    <span>🏷️</span> UTM &amp; CRM Governance
                </button>
                <button class="tools-tab-btn" id="tabBtnTradeShow" onclick="switchToolsTab('tradeshow')">
                    <span>🎪</span> Trade Show ROI Modeler
                </button>
            </div>

            <!-- TAB 1: MQL-to-SQL SLA & Lead Leakage Calculator -->
            <div class="tool-pane" id="paneToolsSla">
                <div class="tool-intro-box">
                    <h4 class="tool-pane-title">MQL-to-SQL SLA &amp; Lead Leakage Calculator</h4>
                    <p class="tool-pane-desc">Quantify how follow-up response latency degrades inbound pipeline conversion. Sub-5-minute routing consistently delivers up to 8x higher lead-to-opportunity velocity compared to manual spreadsheets.</p>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaLeadsInput">Monthly Inbound Leads</label>
                                <span class="tool-val-display" id="slaLeadsVal">350 leads</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaLeadsInput" min="20" max="2000" step="10" value="350" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaAcvInput">Average Deal Value / ACV ($ / €)</label>
                                <span class="tool-val-display" id="slaAcvVal">$15,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaAcvInput" min="1000" max="100000" step="1000" value="15000" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Current Sales Follow-up Time</label>
                            <div class="tool-pills-row" id="slaSpeedPills">
                                <button type="button" class="tool-pill-option active" data-speed="slow" onclick="setSlaFollowup('slow')">&gt; 48 Hours</button>
                                <button type="button" class="tool-pill-option" data-speed="medium" onclick="setSlaFollowup('medium')">24 Hours</button>
                                <button type="button" class="tool-pill-option" data-speed="fast" onclick="setSlaFollowup('fast')">&lt; 5 Minutes</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid">
                            <div class="tool-kpi-card" style="border-color: rgba(251, 113, 133, 0.4); background: rgba(251, 113, 133, 0.05);">
                                <div class="tool-kpi-label">Leaked Pipeline / Mo</div>
                                <div class="tool-kpi-num" id="slaLeakedVal" style="color: #fb7185;">$1,627,500</div>
                                <div class="tool-kpi-sub" id="slaLeakedSub">75% lead drop-off due to latency (> 48h)</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">Recoverable Pipeline / Mo</div>
                                <div class="tool-kpi-num" id="slaRecoverableVal" style="color: #34d399;">$1,139,250</div>
                                <div class="tool-kpi-sub" id="slaRecoverableSub">With sub-5min automated SLA</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Conversion Rate Lift</div>
                                <div class="tool-kpi-num" id="slaLiftVal" style="color: #d4a863;">+775%</div>
                                <div class="tool-kpi-sub" id="slaLiftSub">4% current → 35% SLA target</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('contact');">
                                <span>⚡</span> Audit SLA Routing &amp; Recover Pipeline ▹
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: B2B Campaign UTM & CRM Governance Builder -->
            <div class="tool-pane" id="paneToolsUtm" style="display: none;">
                <div class="tool-intro-box">
                    <h4 class="tool-pane-title">B2B Campaign UTM &amp; CRM Governance Builder</h4>
                    <p class="tool-pane-desc">Enforce naming conventions across paid acquisition and map attribution keys into hidden HubSpot/Salesforce form properties.</p>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <label for="utmUrlInput" class="tool-input-label">Destination Landing URL</label>
                            <input type="url" class="tool-text-input" id="utmUrlInput" value="https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Primary Source (Channel)</label>
                            <div class="tool-pills-row" id="utmSourcePills">
                                <button type="button" class="tool-pill-option active" onclick="setUtmSource('linkedin')">LinkedIn Ads</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmSource('google')">Google Ads</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmSource('meta')">Meta Ads</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmSource('newsletter')">Newsletter</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Marketing Medium</label>
                            <div class="tool-pills-row" id="utmMediumPills">
                                <button type="button" class="tool-pill-option active" onclick="setUtmMedium('paid-social')">paid-social</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmMedium('cpc')">cpc</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmMedium('email')">email</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmMedium('organic-social')">organic-social</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label for="utmCampaignInput" class="tool-input-label">Campaign Name (Auto-Slugified)</label>
                            <input type="text" class="tool-text-input" id="utmCampaignInput" value="2026 Q2 Enterprise RevOps Scale" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">ICP Target Region</label>
                            <div class="tool-pills-row" id="utmRegionPills">
                                <button type="button" class="tool-pill-option active" onclick="setUtmRegion('emea')">EMEA</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmRegion('namer')">NAMER</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmRegion('latam')">LATAM</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmRegion('global')">GLOBAL</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="terminal-block">
                            <div class="terminal-bar">
                                <span class="terminal-tag">GOVERNED CAMPAIGN URL</span>
                                <button class="terminal-copy-btn" id="btnCopyUtm" onclick="copyGovernedUrl()">📋 Copy URL</button>
                            </div>
                            <div class="terminal-content" id="utmOutputUrl" style="word-break: break-all; font-family: var(--font-mono); font-size: 0.72rem; color: #38bdf8; line-height: 1.5; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px;">
                                https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/?utm_source=linkedin&amp;utm_medium=paid-social&amp;utm_campaign=2026-q2-enterprise-revops-scale&amp;utm_region=emea
                            </div>
                        </div>

                        <div class="terminal-block" style="margin-top: 1rem;">
                            <div class="terminal-bar">
                                <span class="terminal-tag">CRM HIDDEN FORM FIELDS INGESTION PREVIEW</span>
                                <span style="font-family: var(--font-mono); font-size: 0.62rem; color: var(--accent-gold);">HUBSPOT / SALESFORCE SCHEMA</span>
                            </div>
                            <pre class="terminal-content" id="utmJsonPreview" style="font-family: var(--font-mono); font-size: 0.68rem; color: #a78bfa; line-height: 1.45; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px; margin: 0; overflow-x: auto;"></pre>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: B2B Trade Show & Exhibition ROI Calculator -->
            <div class="tool-pane" id="paneToolsTradeShow" style="display: none;">
                <div class="tool-intro-box">
                    <h4 class="tool-pane-title">B2B Trade Show &amp; Exhibition ROI Modeler</h4>
                    <p class="tool-pane-desc">Modeled on real-world industrial exhibition operations (IFAT Munich, PRS Europe). Measure pipeline creation, qualified cost per opportunity, and automated sync hours saved.</p>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsCostInput">Total Exhibition Investment ($ / €)</label>
                                <span class="tool-val-display" id="tsCostVal">$45,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsCostInput" min="5000" max="250000" step="2500" value="45000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsBadgesInput">Total Badges Scanned / Captured</label>
                                <span class="tool-val-display" id="tsBadgesVal">320 badges</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsBadgesInput" min="20" max="1500" step="10" value="320" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsQualInput">ICP Qualification Rate (%)</label>
                                <span class="tool-val-display" id="tsQualVal">45%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsQualInput" min="10" max="90" step="5" value="45" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsAcvInput">Average Contract Value / ACV ($ / €)</label>
                                <span class="tool-val-display" id="tsAcvVal">$28,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsAcvInput" min="3000" max="150000" step="1000" value="28000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsWinRateInput">Opportunity Win Rate (%)</label>
                                <span class="tool-val-display" id="tsWinRateVal">22%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsWinRateInput" min="5" max="60" step="1" value="22" oninput="updateTradeShowRoi()">
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid" style="grid-template-columns: repeat(2, 1fr);">
                            <div class="tool-kpi-card" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.05);">
                                <div class="tool-kpi-label">CPL / Cost Per SQL</div>
                                <div class="tool-kpi-num" id="tsCplVal" style="color: #38bdf8;">$141 / $313</div>
                                <div class="tool-kpi-sub" id="tsCplSub">144 qualified sales opportunities</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">SQL Pipeline Generated</div>
                                <div class="tool-kpi-num" id="tsPipelineVal" style="color: #d4a863;">$4,032,000</div>
                                <div class="tool-kpi-sub" id="tsPipelineSub">Projected won: $887,040</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">Projected Event ROAS</div>
                                <div class="tool-kpi-num" id="tsRoasVal" style="color: #34d399;">19.7x</div>
                                <div class="tool-kpi-sub" id="tsRoasSub">Return on event capital invested</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(167, 139, 250, 0.4); background: rgba(167, 139, 250, 0.05);">
                                <div class="tool-kpi-label">Admin Hours Saved</div>
                                <div class="tool-kpi-num" id="tsHoursVal" style="color: #a78bfa;">43 hrs</div>
                                <div class="tool-kpi-sub" id="tsHoursSub">Via zero-latency CRM ingestion</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('contact');">
                                <span>🎪</span> Standardize Trade Show Ingestion ▹
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>'''

NEW_UPGRADED_MODAL_TOOLS_HTML_IT = '''    <!-- MODAL: TOOLS -->
    <div class="spatial-modal-card" id="modalTools">
        <div class="modal-top-bar">
            <h2 class="modal-title-text"><span>🧰</span> Strumenti</h2>
            <button class="modal-close-trigger" onclick="closeActiveModal()">✕</button>
        </div>
        <div class="modal-body-scroll">
            <div class="tools-suite-header">
                <h3 class="tools-suite-title"><span>🧰</span> Strumenti & Utility Interattive</h3>
                <p class="tools-suite-subtitle">Calcolatori Revenue Operations enterprise, costruttori di governance tracciamento campagne e modelli di acquisizione fieristica sviluppati da Renzo Francesqui.</p>
            </div>

            <div class="tools-tab-switcher">
                <button class="tools-tab-btn active" id="tabBtnSla" onclick="switchToolsTab('sla')">
                    <span>⚡</span> SLA &amp; Lead Leakage
                </button>
                <button class="tools-tab-btn" id="tabBtnUtm" onclick="switchToolsTab('utm')">
                    <span>🏷️</span> Governance UTM &amp; CRM
                </button>
                <button class="tools-tab-btn" id="tabBtnTradeShow" onclick="switchToolsTab('tradeshow')">
                    <span>🎪</span> Modello ROI Fiere B2B
                </button>
            </div>

            <!-- TAB 1: MQL-to-SQL SLA & Lead Leakage Calculator (IT) -->
            <div class="tool-pane" id="paneToolsSla">
                <div class="tool-intro-box">
                    <h4 class="tool-pane-title">Calcolatore SLA MQL-to-SQL &amp; Dispersione Lead</h4>
                    <p class="tool-pane-desc">Quantifica come la latenza di risposta commerciale degrada la conversione della pipeline inbound. Il routing sotto i 5 minuti genera fino a 8 volte più conversioni rispetto ai tradizionali fogli di calcolo.</p>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaLeadsInput">Lead Inbound Mensili</label>
                                <span class="tool-val-display" id="slaLeadsVal">350 lead</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaLeadsInput" min="20" max="2000" step="10" value="350" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="slaAcvInput">Valore Medio Trattativa / ACV ($ / €)</label>
                                <span class="tool-val-display" id="slaAcvVal">$15,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="slaAcvInput" min="1000" max="100000" step="1000" value="15000" oninput="updateSlaCalculator()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Tempo Attuale di Follow-up Commerciale</label>
                            <div class="tool-pills-row" id="slaSpeedPills">
                                <button type="button" class="tool-pill-option active" data-speed="slow" onclick="setSlaFollowup('slow')">&gt; 48 Ore</button>
                                <button type="button" class="tool-pill-option" data-speed="medium" onclick="setSlaFollowup('medium')">24 Ore</button>
                                <button type="button" class="tool-pill-option" data-speed="fast" onclick="setSlaFollowup('fast')">&lt; 5 Minuti</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid">
                            <div class="tool-kpi-card" style="border-color: rgba(251, 113, 133, 0.4); background: rgba(251, 113, 133, 0.05);">
                                <div class="tool-kpi-label">Pipeline Dispersa / Mese</div>
                                <div class="tool-kpi-num" id="slaLeakedVal" style="color: #fb7185;">$1,627,500</div>
                                <div class="tool-kpi-sub" id="slaLeakedSub">75% dispersione per latenza (> 48h)</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">Pipeline Recuperabile / Mese</div>
                                <div class="tool-kpi-num" id="slaRecoverableVal" style="color: #34d399;">$1,139,250</div>
                                <div class="tool-kpi-sub" id="slaRecoverableSub">Con routing automatizzato SLA &lt; 5 min</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Incremento Tasso di Conversione</div>
                                <div class="tool-kpi-num" id="slaLiftVal" style="color: #d4a863;">+775%</div>
                                <div class="tool-kpi-sub" id="slaLiftSub">4% attuale → 35% target SLA</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('contact');">
                                <span>⚡</span> Audit Routing SLA &amp; Recupera Pipeline ▹
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: Governance UTM & CRM (IT) -->
            <div class="tool-pane" id="paneToolsUtm" style="display: none;">
                <div class="tool-intro-box">
                    <h4 class="tool-pane-title">Builder Governance UTM &amp; Campagne CRM</h4>
                    <p class="tool-pane-desc">Definisci convenzioni di tracciamento rigorose per l'acquisizione a pagamento e mappa i parametri nei campi modulo nascosti di HubSpot/Salesforce.</p>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <label for="utmUrlInput" class="tool-input-label">URL Landing Page di Destinazione</label>
                            <input type="url" class="tool-text-input" id="utmUrlInput" value="https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Sorgente Principale (Canale)</label>
                            <div class="tool-pills-row" id="utmSourcePills">
                                <button type="button" class="tool-pill-option active" onclick="setUtmSource('linkedin')">LinkedIn Ads</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmSource('google')">Google Ads</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmSource('meta')">Meta Ads</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmSource('newsletter')">Newsletter</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Medium di Marketing</label>
                            <div class="tool-pills-row" id="utmMediumPills">
                                <button type="button" class="tool-pill-option active" onclick="setUtmMedium('paid-social')">paid-social</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmMedium('cpc')">cpc</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmMedium('email')">email</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmMedium('organic-social')">organic-social</button>
                            </div>
                        </div>
                        <div class="tool-input-group">
                            <label for="utmCampaignInput" class="tool-input-label">Nome Campagna (Formattazione Automatica)</label>
                            <input type="text" class="tool-text-input" id="utmCampaignInput" value="2026 Q2 Enterprise RevOps Scale" oninput="updateUtmBuilder()">
                        </div>
                        <div class="tool-input-group">
                            <label class="tool-input-label">Regione Target ICP</label>
                            <div class="tool-pills-row" id="utmRegionPills">
                                <button type="button" class="tool-pill-option active" onclick="setUtmRegion('emea')">EMEA</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmRegion('namer')">NAMER</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmRegion('latam')">LATAM</button>
                                <button type="button" class="tool-pill-option" onclick="setUtmRegion('global')">GLOBAL</button>
                            </div>
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="terminal-block">
                            <div class="terminal-bar">
                                <span class="terminal-tag">URL CAMPAGNA TRACCIATO</span>
                                <button class="terminal-copy-btn" id="btnCopyUtm" onclick="copyGovernedUrl()">📋 Copia URL</button>
                            </div>
                            <div class="terminal-content" id="utmOutputUrl" style="word-break: break-all; font-family: var(--font-mono); font-size: 0.72rem; color: #38bdf8; line-height: 1.5; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px;">
                                https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/?utm_source=linkedin&amp;utm_medium=paid-social&amp;utm_campaign=2026-q2-enterprise-revops-scale&amp;utm_region=emea
                            </div>
                        </div>

                        <div class="terminal-block" style="margin-top: 1rem;">
                            <div class="terminal-bar">
                                <span class="terminal-tag">ANTEPRIMA CAMPI MODULO NASCOSTI CRM</span>
                                <span style="font-family: var(--font-mono); font-size: 0.62rem; color: var(--accent-gold);">SCHEMA HUBSPOT / SALESFORCE</span>
                            </div>
                            <pre class="terminal-content" id="utmJsonPreview" style="font-family: var(--font-mono); font-size: 0.68rem; color: #a78bfa; line-height: 1.45; padding: 0.75rem; background: rgba(0,0,0,0.4); border-radius: 8px; margin: 0; overflow-x: auto;"></pre>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: Modello ROI Fiere B2B (IT) -->
            <div class="tool-pane" id="paneToolsTradeShow" style="display: none;">
                <div class="tool-intro-box">
                    <h4 class="tool-pane-title">Modello ROI Fiere B2B &amp; Eventi Field</h4>
                    <p class="tool-pane-desc">Basato su operazioni reali in fiere industriali internazionali (IFAT Monaco, PRS Europe). Calcola la generazione di pipeline, il costo per opportunità qualificata e le ore di lavoro manuale risparmiate.</p>
                </div>
                <div class="tool-grid-layout">
                    <div class="tool-inputs-card">
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsCostInput">Investimento Totale Fiera ($ / €)</label>
                                <span class="tool-val-display" id="tsCostVal">$45,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsCostInput" min="5000" max="250000" step="2500" value="45000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsBadgesInput">Totale Badge Scannerizzati / Raccolti</label>
                                <span class="tool-val-display" id="tsBadgesVal">320 badge</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsBadgesInput" min="20" max="1500" step="10" value="320" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsQualInput">Tasso di Qualificazione ICP (%)</label>
                                <span class="tool-val-display" id="tsQualVal">45%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsQualInput" min="10" max="90" step="5" value="45" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsAcvInput">Valore Medio Contratto / ACV ($ / €)</label>
                                <span class="tool-val-display" id="tsAcvVal">$28,000</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsAcvInput" min="3000" max="150000" step="1000" value="28000" oninput="updateTradeShowRoi()">
                        </div>
                        <div class="tool-input-group">
                            <div class="tool-label-row">
                                <label for="tsWinRateInput">Tasso di Chiusura Opportunità (%)</label>
                                <span class="tool-val-display" id="tsWinRateVal">22%</span>
                            </div>
                            <input type="range" class="tool-range-slider" id="tsWinRateInput" min="5" max="60" step="1" value="22" oninput="updateTradeShowRoi()">
                        </div>
                    </div>

                    <div class="tool-results-card">
                        <div class="tool-kpis-grid" style="grid-template-columns: repeat(2, 1fr);">
                            <div class="tool-kpi-card" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.05);">
                                <div class="tool-kpi-label">CPL / Costo Per SQL Qualificato</div>
                                <div class="tool-kpi-num" id="tsCplVal" style="color: #38bdf8;">$141 / $313</div>
                                <div class="tool-kpi-sub" id="tsCplSub">144 opportunità commerciali qualificate</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                                <div class="tool-kpi-label">Pipeline SQL Generata</div>
                                <div class="tool-kpi-num" id="tsPipelineVal" style="color: #d4a863;">$4,032,000</div>
                                <div class="tool-kpi-sub" id="tsPipelineSub">Fatturato previsto vinto: $887,040</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                                <div class="tool-kpi-label">ROAS Evento Previsto</div>
                                <div class="tool-kpi-num" id="tsRoasVal" style="color: #34d399;">19.7x</div>
                                <div class="tool-kpi-sub" id="tsRoasSub">Rendimento sul capitale investito</div>
                            </div>
                            <div class="tool-kpi-card" style="border-color: rgba(167, 139, 250, 0.4); background: rgba(167, 139, 250, 0.05);">
                                <div class="tool-kpi-label">Ore Amministrative Risparmiate</div>
                                <div class="tool-kpi-num" id="tsHoursVal" style="color: #a78bfa;">43 ore</div>
                                <div class="tool-kpi-sub" id="tsHoursSub">Grazie all'acquisizione CRM automatica</div>
                            </div>
                        </div>
                        <div class="tool-cta-wrapper">
                            <button class="tool-cta-btn" onclick="closeActiveModal(); openModalForPlanet('contact');">
                                <span>🎪</span> Standardizza Ingestione Lead Fiere ▹
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>'''

# ========================================================
# 4. STANDALONE 4 PROJECT CARDS HTML
# ========================================================
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
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Python + BigQuery SQL + Looker Studio. Multi-touch algorithmic attribution using first-order Markov chains to calculate removal effects and true channel revenue contribution beyond last-touch bias.</p>
                    <button onclick="closeActiveModal(); focusOnPlanet('services', true);" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Explore Data Architecture →</button>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Enterprise HubSpot &amp; Salesforce RevOps Architecture</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">B2B Lead Lifecycle + SLA Routing Engine. Complete enterprise alignment between marketing qualified leads (MQL) and sales accepted leads (SAL) with sub-5-minute routing, custom deal-stage gating, and zero lead leakage.</p>
                    <button onclick="closeActiveModal(); focusOnPlanet('services', true);" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Explore RevOps Architecture →</button>
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
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Python + BigQuery SQL + Looker Studio. Attribuzione multi-touch algoritmica basata su catene di Markov di primo ordine per calcolare gli effetti di rimozione e la reale incidenza sul fatturato oltre il bias dell'ultimo tocco.</p>
                    <button onclick="closeActiveModal(); focusOnPlanet('services', true);" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Esplora Architettura Dati →</button>
                </div>
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: 16px; padding: 1.25rem;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: var(--text-primary);">Architettura RevOps Enterprise HubSpot &amp; Salesforce</h4>
                    <p style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5;">Ciclo di Vita Lead B2B + Motore di Routing SLA. Allineamento enterprise completo tra MQL e SQL con routing sotto i 5 minuti, gate obbligatori di avanzamento deal e azzeramento delle perdite contatti.</p>
                    <button onclick="closeActiveModal(); focusOnPlanet('services', true);" style="background: none; border: none; padding: 0; font-size: 0.72rem; color: var(--accent-gold); text-decoration: none; font-weight: 700; display: inline-block; margin-top: 0.75rem; cursor: pointer;">Esplora Architettura RevOps →</button>
                </div>
            </div>'''

# ========================================================
# 5. JAVASCRIPT TOOLS SUITE & DISMISSAL CODE
# ========================================================
TOOLS_SUITE_JS_CODE = '''        // ========================================================
        // INTERACTIVE TOOLS SUITE LOGIC (#modalTools)
        // ========================================================
        let currentSlaSpeed = 'slow';
        let currentUtmSource = 'linkedin';
        let currentUtmMedium = 'paid-social';
        let currentUtmRegion = 'emea';

        function switchToolsTab(tabId) {
            const tabs = ['sla', 'utm', 'tradeshow'];
            tabs.forEach(t => {
                const pane = document.getElementById(t === 'sla' ? 'paneToolsSla' : (t === 'utm' ? 'paneToolsUtm' : 'paneToolsTradeShow'));
                const btn = document.getElementById(t === 'sla' ? 'tabBtnSla' : (t === 'utm' ? 'tabBtnUtm' : 'tabBtnTradeShow'));
                if (pane) pane.style.display = (t === tabId) ? 'block' : 'none';
                if (btn) btn.classList.toggle('active', t === tabId);
            });
            playSynthTone(520, 'sine', 0.06);
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
            if (acvVal) acvVal.innerText = `$${acv.toLocaleString()}`;

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

            const leakedVal = lostSqls * acv;
            const recoverableVal = lostSqls * 0.70 * acv;
            const liftPct = currentRate > 0 ? Math.round(((optimalRate - currentRate) / currentRate) * 100) : 0;

            const elLeaked = document.getElementById('slaLeakedVal');
            const elLeakedSub = document.getElementById('slaLeakedSub');
            const elRec = document.getElementById('slaRecoverableVal');
            const elRecSub = document.getElementById('slaRecoverableSub');
            const elLift = document.getElementById('slaLiftVal');
            const elLiftSub = document.getElementById('slaLiftSub');

            if (elLeaked) elLeaked.innerText = `$${Math.round(leakedVal).toLocaleString()}`;
            if (elLeakedSub) {
                elLeakedSub.innerText = isIt
                    ? `${Math.round(leakageRate * 100)}% dispersione per latenza (${speedLabel})`
                    : `${Math.round(leakageRate * 100)}% lead drop-off due to latency (${speedLabel})`;
            }
            if (elRec) elRec.innerText = `$${Math.round(recoverableVal).toLocaleString()}`;
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
            pills.forEach(p => p.classList.toggle('active', p.innerText.toLowerCase().includes(src)));
            updateUtmBuilder();
        }

        function setUtmMedium(med) {
            currentUtmMedium = med;
            const pills = document.querySelectorAll('#utmMediumPills .tool-pill-option');
            pills.forEach(p => p.classList.toggle('active', p.innerText.toLowerCase() === med));
            updateUtmBuilder();
        }

        function setUtmRegion(reg) {
            currentUtmRegion = reg;
            const pills = document.querySelectorAll('#utmRegionPills .tool-pill-option');
            pills.forEach(p => p.classList.toggle('active', p.innerText.toLowerCase() === reg));
            updateUtmBuilder();
        }

        function updateUtmBuilder() {
            const urlInput = document.getElementById('utmUrlInput');
            const campInput = document.getElementById('utmCampaignInput');
            if (!urlInput || !campInput) return;

            const isIt = document.documentElement.lang === 'it';
            let defaultBase = isIt ? 'https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/' : 'https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/';
            let baseUrl = urlInput.value.trim() || defaultBase;
            baseUrl = baseUrl.split('?')[0];

            const rawCamp = campInput.value.trim() || 'enterprise-revops-scale';
            const slugCamp = rawCamp.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

            const finalUrl = `${baseUrl}?utm_source=${encodeURIComponent(currentUtmSource)}&utm_medium=${encodeURIComponent(currentUtmMedium)}&utm_campaign=${encodeURIComponent(slugCamp)}&utm_region=${encodeURIComponent(currentUtmRegion)}`;

            const outEl = document.getElementById('utmOutputUrl');
            if (outEl) outEl.innerText = finalUrl;

            const jsonPreview = {
                "hs_analytics_source": currentUtmSource.toUpperCase(),
                "utm_campaign": slugCamp,
                "utm_source": currentUtmSource,
                "utm_medium": currentUtmMedium,
                "utm_region": currentUtmRegion,
                "lead_lifecycle_stage": "marketingqualifiedlead",
                "sla_routing_priority": "Tier-1 High Intent"
            };

            const jsonEl = document.getElementById('utmJsonPreview');
            if (jsonEl) jsonEl.innerText = JSON.stringify(jsonPreview, null, 2);
        }

        function copyGovernedUrl() {
            const outEl = document.getElementById('utmOutputUrl');
            const btn = document.getElementById('btnCopyUtm');
            if (!outEl) return;
            const isIt = document.documentElement.lang === 'it';
            navigator.clipboard.writeText(outEl.innerText.trim()).then(() => {
                if (btn) {
                    btn.innerText = isIt ? 'Copiato! ✓' : 'Copied! ✓';
                    setTimeout(() => { btn.innerText = isIt ? '📋 Copia URL' : '📋 Copy URL'; }, 2000);
                }
            }).catch(() => {
                if (btn) btn.innerText = 'Error copying';
            });
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

            document.getElementById('tsCostVal').innerText = `$${cost.toLocaleString()}`;
            document.getElementById('tsBadgesVal').innerText = `${badges.toLocaleString()} ${isIt ? 'badge' : 'badges'}`;
            document.getElementById('tsQualVal').innerText = `${qualPct}%`;
            document.getElementById('tsAcvVal').innerText = `$${acv.toLocaleString()}`;
            document.getElementById('tsWinRateVal').innerText = `${winRate}%`;

            const qualSqls = Math.round(badges * (qualPct / 100));
            const cpl = Math.round(cost / badges);
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

            if (elCpl) elCpl.innerText = `$${cpl} / $${costPerSql}`;
            if (elCplSub) elCplSub.innerText = isIt ? `${qualSqls} opportunità qualificate` : `${qualSqls} qualified sales opportunities`;
            if (elPipe) elPipe.innerText = `$${pipeline.toLocaleString()}`;
            if (elPipeSub) elPipeSub.innerText = isIt ? `Fatturato previsto vinto: $${wonRev.toLocaleString()}` : `Projected won: $${wonRev.toLocaleString()}`;
            if (elRoas) elRoas.innerText = `${roas}x`;
            if (elHours) elHours.innerText = `${hoursSaved} ${isIt ? 'ore' : 'hrs'}`;
        }

        function dismissFloatingHint(e) {
            if (e && e.stopPropagation) e.stopPropagation();
            const hint = document.getElementById('orbitFloatingHint');
            if (hint && !hint.classList.contains('fade-out')) {
                hint.classList.add('fade-out');
                setTimeout(() => { hint.style.display = 'none'; }, 600);
            }
        }
'''

def main():
    print("Applying V3 upgrades cleanly...")

    # 1. Update version-3/index.html
    v3_index_path = BASE_DIR / "version-3" / "index.html"
    v3_html = v3_index_path.read_text(encoding="utf-8")

    # Extract avatar base64 data URI
    avatar_match = re.search(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', v3_html)
    if not avatar_match:
        raise ValueError("Could not locate avatar base64 data URI in version-3/index.html")
    avatar_data_uri = avatar_match.group(0)

    # A. Deduplicate Avatar in version-3/index.html
    v3_html = re.sub(
        r'<div class="agent-ring">\s*<img src="data:image/jpeg;base64,[^"]*" onerror="[^"]*" alt="[^"]*">\s*</div>',
        '<div class="agent-ring">\n                    <img src="" id="agentAvatarImg" onerror="this.onerror=null; this.src=\'images/renzo-francesqui.jpg\';" alt="Renzo Francesqui">\n                </div>',
        v3_html
    )
    v3_html = re.sub(
        r'<div class="chat-trigger-avatar">\s*<img src="data:image/jpeg;base64,[^"]*" onerror="[^"]*" alt="[^"]*">\s*<span class="trigger-live-indicator"></span>\s*</div>',
        '<div class="chat-trigger-avatar">\n            <img src="" id="chatTriggerAvatarImg" onerror="this.onerror=null; this.src=\'images/renzo-francesqui.jpg\';" alt="Renzo AI">\n            <span class="trigger-live-indicator"></span>\n        </div>',
        v3_html
    )

    # Insert RENZO_AVATAR_DATA_URI right after GARGANTUA_DATA_URI
    if 'const RENZO_AVATAR_DATA_URI' not in v3_html:
        v3_html = v3_html.replace(
            'const GARGANTUA_DATA_URI = "',
            'const RENZO_AVATAR_DATA_URI = "' + avatar_data_uri + '";\n        const GARGANTUA_DATA_URI = "'
        )

    # Avatar assignment
    avatar_assign_code = (
        "\n        // Initialize deduplicated Renzo avatar data URI\n"
        "        document.querySelectorAll('.agent-ring img, .chat-trigger-avatar img').forEach(img => {\n"
        "            img.src = RENZO_AVATAR_DATA_URI;\n"
        "        });\n"
    )
    if "document.querySelectorAll('.agent-ring img" not in v3_html:
        v3_html = v3_html.replace(
            "const gargantuaTexLoader = new THREE.TextureLoader();",
            avatar_assign_code + "\n        const gargantuaTexLoader = new THREE.TextureLoader();"
        )

    # B. Projects 4 Cards Grid in version-3/index.html
    # Landmark replacement
    landmark_projects_start = '<!-- Standalone Project Cards -->'
    landmark_projects_end = '<!-- MODAL 3: SKILLS -->'
    idx_proj_start = v3_html.find(landmark_projects_start)
    idx_proj_end = v3_html.find(landmark_projects_end)
    if idx_proj_start != -1 and idx_proj_end != -1:
        # Find the closing div of modal-body-scroll / modalProjects right before landmark_projects_end
        # The projects grid is inside modal-body-scroll
        v3_html = (
            v3_html[:idx_proj_start]
            + PROJECTS_4_CARDS_EN.strip()
            + "\n        </div>\n    </div>\n\n    "
            + v3_html[idx_proj_end:]
        )
        print("[OK] Replaced Projects Cards in version-3/index.html")

    # C. Contact Location Badge in version-3/index.html
    v3_html = v3_html.replace(
        '📍 <strong>Based in Milan, Italy.</strong>',
        '📍 <strong>Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.</strong>'
    )
    v3_html = v3_html.replace(
        'Based in Milan, Italy.',
        'Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.'
    )

    # D. Navigation UX: focusOnPlanet with autoOpen parameter & handlePointerClick
    focus_planet_old = (
        "        function focusOnPlanet(planetId) {\n"
        "            closeActiveModal(false);\n"
        "            const p = planets.find(item => item.id === planetId);\n"
        "            if (!p) return;\n\n"
        "            playSynthTone(740, 'sine', 0.18, 0.12);\n"
        "            viewMode = 'INSPECT';\n"
        "            focusedPlanet = p;\n\n"
        "            // Highlight dock button\n"
        "            document.querySelectorAll('.dock-pill-btn').forEach(b => b.classList.remove('active'));\n"
        "            const btn = Array.from(document.querySelectorAll('.dock-pill-btn')).find(b => b.innerText.includes(p.config.name));\n"
        "            if (btn) btn.classList.add('active');\n\n"
        "            // Update Cam Button\n"
        "            const camBtn = document.getElementById('camModeBtn');\n"
        "            if (camBtn) {\n"
        "                const isIt = document.documentElement.lang === 'it';\n"
        "                camBtn.innerHTML = isIt ? '<span>↺</span> RESET ORBITA' : '<span>↺</span> RESET ORBIT';\n"
        "            }\n\n"
        "            // Show Inspect HUD\n"
        "            const hud = document.getElementById('planetInspectHUD');\n"
        "            document.getElementById('inspectSector').innerText = p.config.sector;\n"
        "            document.getElementById('inspectTitle').innerHTML = `<span>${p.config.icon}</span> ${p.config.name}`;\n"
        "            document.getElementById('inspectDesc').innerText = p.config.desc;\n"
        "            hud.style.display = 'block';\n\n"
        "            // Auto-open modal after smooth glide\n"
        "            if (focusTimerId) clearTimeout(focusTimerId);\n"
        "            focusTimerId = setTimeout(() => {\n"
        "                if (viewMode === 'INSPECT' && focusedPlanet === p) {\n"
        "                    openModalForPlanet(p.id);\n"
        "                }\n"
        "            }, 600);\n"
        "        }"
    )

    focus_planet_new = (
        "        function focusOnPlanet(planetId, autoOpen = false) {\n"
        "            closeActiveModal(false);\n"
        "            const p = planets.find(item => item.id === planetId);\n"
        "            if (!p) return;\n\n"
        "            playSynthTone(740, 'sine', 0.18, 0.12);\n"
        "            viewMode = 'INSPECT';\n"
        "            focusedPlanet = p;\n\n"
        "            // Highlight dock button\n"
        "            document.querySelectorAll('.dock-pill-btn').forEach(b => b.classList.remove('active'));\n"
        "            const btn = Array.from(document.querySelectorAll('.dock-pill-btn')).find(b => b.innerText.includes(p.config.name));\n"
        "            if (btn) btn.classList.add('active');\n\n"
        "            // Update Cam Button\n"
        "            const camBtn = document.getElementById('camModeBtn');\n"
        "            if (camBtn) {\n"
        "                const isIt = document.documentElement.lang === 'it';\n"
        "                camBtn.innerHTML = isIt ? '<span>↺</span> RESET ORBITA' : '<span>↺</span> RESET ORBIT';\n"
        "            }\n\n"
        "            // Show Inspect HUD\n"
        "            const hud = document.getElementById('planetInspectHUD');\n"
        "            document.getElementById('inspectSector').innerText = p.config.sector;\n"
        "            document.getElementById('inspectTitle').innerHTML = `<span>${p.config.icon}</span> ${p.config.name}`;\n"
        "            document.getElementById('inspectDesc').innerText = p.config.desc;\n"
        "            hud.style.display = 'block';\n\n"
        "            // Auto-open modal after smooth glide only if autoOpen is true (e.g. bottom dock clicks)\n"
        "            if (focusTimerId) {\n"
        "                clearTimeout(focusTimerId);\n"
        "                focusTimerId = null;\n"
        "            }\n"
        "            if (autoOpen) {\n"
        "                focusTimerId = setTimeout(() => {\n"
        "                    if (viewMode === 'INSPECT' && focusedPlanet === p) {\n"
        "                        openModalForPlanet(p.id);\n"
        "                    }\n"
        "                }, 350);\n"
        "            }\n"
        "        }"
    )

    if focus_planet_old in v3_html:
        v3_html = v3_html.replace(focus_planet_old, focus_planet_new)
        print("[OK] Replaced focusOnPlanet in version-3/index.html")

    # In handlePointerClick, call focusOnPlanet(hitId, false)
    v3_html = v3_html.replace("focusOnPlanet(hitId);", "focusOnPlanet(hitId, false);")

    # In openModalForPlanet, call dismissFloatingHint and update tools if id === 'tools'
    open_modal_target = "function openModalForPlanet(id) {\n            closeActiveModal(false);"
    open_modal_replacement = (
        "function openModalForPlanet(id) {\n"
        "            if (typeof dismissFloatingHint === 'function') dismissFloatingHint();\n"
        "            if (id === 'tools' && typeof updateSlaCalculator === 'function') {\n"
        "                setTimeout(() => { updateSlaCalculator(); updateUtmBuilder(); updateTradeShowRoi(); }, 50);\n"
        "            }\n"
        "            closeActiveModal(false);"
    )
    if open_modal_target in v3_html:
        v3_html = v3_html.replace(open_modal_target, open_modal_replacement)

    # Insert TOOLS_SUITE_JS_CODE right before function resetCameraToOverview()
    if 'function switchToolsTab' not in v3_html:
        v3_html = v3_html.replace(
            "function resetCameraToOverview() {",
            TOOLS_SUITE_JS_CODE + "\n        function resetCameraToOverview() {"
        )

    # Call update calculators on initial load
    init_calc_call = "\n        // Initialize Tools Suite Calculations\n        if (typeof updateSlaCalculator === 'function') { updateSlaCalculator(); updateUtmBuilder(); updateTradeShowRoi(); }\n"
    if 'Initialize Tools Suite Calculations' not in v3_html:
        v3_html = v3_html.replace(
            "animate();",
            "animate();" + init_calc_call
        )

    # Save version-3/index.html
    v3_index_path.write_text(v3_html, encoding="utf-8")
    print(f"[OK] Upgraded {v3_index_path}")

    # 2. Update scripts/compile_v3.py
    compile_v3_path = BASE_DIR / "scripts" / "compile_v3.py"
    compile_py = compile_v3_path.read_text(encoding="utf-8")

    # A. Replace UPGRADED_MOBILE_CSS between landmarks
    landmark_css_start = "UPGRADED_MOBILE_CSS = '''"
    landmark_css_end = "# ========================================================\n# 2. UPGRADED PROCEDURAL TEXTURES & SHADERS (Sun & Planets)"
    idx_css_s = compile_py.find(landmark_css_start)
    idx_css_e = compile_py.find(landmark_css_end)
    if idx_css_s != -1 and idx_css_e != -1:
        compile_py = (
            compile_py[:idx_css_s]
            + f"UPGRADED_MOBILE_CSS = '''{NEW_UPGRADED_MOBILE_CSS}'''\n\n"
            + compile_py[idx_css_e:]
        )
        print("[OK] Replaced UPGRADED_MOBILE_CSS in compile_v3.py")

    # B. Replace UPGRADED_TOUCH_AND_CAMERA_CONTROLS between landmarks
    landmark_touch_start = "UPGRADED_TOUCH_AND_CAMERA_CONTROLS = '''"
    landmark_touch_end = "# ========================================================\n# 7. UPGRADED ANIMATE LOOP (Sun time uniform, thermal pulses)"
    idx_tch_s = compile_py.find(landmark_touch_start)
    idx_tch_e = compile_py.find(landmark_touch_end)
    if idx_tch_s != -1 and idx_tch_e != -1:
        compile_py = (
            compile_py[:idx_tch_s]
            + f"UPGRADED_TOUCH_AND_CAMERA_CONTROLS = '''{NEW_UPGRADED_TOUCH_AND_CAMERA_CONTROLS}'''\n\n"
            + compile_py[idx_tch_e:]
        )
        print("[OK] Replaced UPGRADED_TOUCH_AND_CAMERA_CONTROLS in compile_v3.py")

    # C. Replace UPGRADED_MODAL_TOOLS_HTML and define UPGRADED_MODAL_TOOLS_HTML_IT between landmarks
    landmark_tools_start = "UPGRADED_MODAL_TOOLS_HTML = '''"
    landmark_tools_end = "def build_en_html(src):"
    idx_tls_s = compile_py.find(landmark_tools_start)
    idx_tls_e = compile_py.find(landmark_tools_end)
    if idx_tls_s != -1 and idx_tls_e != -1:
        new_tools_block = (
            f"UPGRADED_MODAL_TOOLS_HTML = '''{NEW_UPGRADED_MODAL_TOOLS_HTML}'''\n\n"
            f"UPGRADED_MODAL_TOOLS_HTML_IT = '''{NEW_UPGRADED_MODAL_TOOLS_HTML_IT}'''\n\n"
            f"PROJECTS_4_CARDS_EN = '''{PROJECTS_4_CARDS_EN}'''\n\n"
            f"PROJECTS_4_CARDS_IT = '''{PROJECTS_4_CARDS_IT}'''\n\n"
        )
        compile_py = (
            compile_py[:idx_tls_s]
            + new_tools_block
            + compile_py[idx_tls_e:]
        )
        print("[OK] Replaced UPGRADED_MODAL_TOOLS_HTML and added constants in compile_v3.py")

    # D. In build_en_html:
    # Landmark replacement for hint_pattern and hint_replacement
    old_hint_en_block = (
        "    hint_pattern = r'<div class=\"orbit-floating-hint\"[^>]*>[\\s\\S]*?</div>'\n"
        "    hint_replacement = '''<div class=\"orbit-floating-hint\" id=\"orbitFloatingHint\">\n"
        "            🌌 <strong>Photorealistic Solar Matrix</strong><br>\n"
        "            Drag to orbit the sun in full 3D • Pinch/scroll to zoom • Click or tap any planet to inspect close-up.\n"
        "        </div>'''"
    )
    new_hint_en_block = (
        "    hint_pattern = r'[ \\t]*<div class=\"orbit-floating-hint\"[^>]*>[\\s\\S]*?(?=<!-- Bottom Floating Spatial Menu Dock)'\n"
        "    hint_replacement = '''<div class=\"orbit-floating-hint\" id=\"orbitFloatingHint\">\n"
        "            <button class=\"hint-close-btn\" onclick=\"dismissFloatingHint(event)\" aria-label=\"Close welcome HUD\">✕</button>\n"
        "            <div class=\"hint-eyebrow\"><span class=\"hint-pulse-dot\"></span> ONLINE // MILAN &amp; PARMA, ITALY • EMEA &amp; GLOBAL</div>\n"
        "            <div class=\"hint-headline\">Renzo Francesqui — CRM Architecture, RevOps &amp; Digital Growth</div>\n"
        "            <div class=\"hint-subtext\">🌌 <strong>Photorealistic Solar Matrix</strong><br>Drag to orbit the sun in 3D • Pinch/scroll to zoom • Click or tap any planet to inspect close-up.</div>\n"
        "            <div class=\"hint-actions\">\n"
        "                <button class=\"hint-pill-btn\" onclick=\"dismissFloatingHint(); openModalForPlanet('services');\"><span>⚡</span> Explore Services</button>\n"
        "                <button class=\"hint-pill-btn\" onclick=\"dismissFloatingHint(); openModalForPlanet('experience');\"><span>🏛️</span> View Experience</button>\n"
        "            </div>\n"
        "        </div>\\n\\n        '''"
    )
    if old_hint_en_block in compile_py:
        compile_py = compile_py.replace(old_hint_en_block, new_hint_en_block)
        print("[OK] Updated hint_replacement in compile_v3.py")

    # Upgrade dock_replacement to pass true to focusOnPlanet
    dock_old_item = '<button class="dock-pill-btn" onclick="focusOnPlanet(\'ai_dialogue\')">'
    dock_new_item = '<button class="dock-pill-btn" onclick="focusOnPlanet(\'ai_dialogue\', true)">'
    # Replace in dock_replacement
    old_dock_en_block = (
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('ai_dialogue')\">\n"
        "                    <span>💬</span> AI Dialogue\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('services')\">\n"
        "                    <span>⚡</span> Services\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('experience')\">\n"
        "                    <span>🏛️</span> Experience\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('projects')\">\n"
        "                    <span>🚀</span> Projects\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('skills')\">\n"
        "                    <span>🛠️</span> Skills\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('tools')\">\n"
        "                    <span>🧰</span> Tools\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('blog')\">\n"
        "                    <span>📰</span> Blog\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('credentials')\">\n"
        "                    <span>🎓</span> Certifications\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('contact')\">\n"
        "                    <span>✉️</span> Get in Touch\n"
        "                </button>"
    )
    new_dock_en_block = (
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('ai_dialogue', true)\">\n"
        "                    <span>💬</span> AI Dialogue\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('services', true)\">\n"
        "                    <span>⚡</span> Services\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('experience', true)\">\n"
        "                    <span>🏛️</span> Experience\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('projects', true)\">\n"
        "                    <span>🚀</span> Projects\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('skills', true)\">\n"
        "                    <span>🛠️</span> Skills\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('tools', true)\">\n"
        "                    <span>🧰</span> Tools\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('blog', true)\">\n"
        "                    <span>📰</span> Blog\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('credentials', true)\">\n"
        "                    <span>🎓</span> Certifications\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('contact', true)\">\n"
        "                    <span>✉️</span> Get in Touch\n"
        "                </button>"
    )
    if old_dock_en_block in compile_py:
        compile_py = compile_py.replace(old_dock_en_block, new_dock_en_block)
        print("[OK] Updated dock_replacement in compile_v3.py")

    # In build_en_html, ensure projects 4 cards replacement and contact badge
    en_projects_sub = (
        "    # 6.4. Projects 4 Cards Grid (IDEMPOTENT REPLACEMENT)\n"
        "    projects_pattern = r'[ \\t]*<!-- Standalone Project Cards.*?-->\\s*<div style=\"display: grid; grid-template-columns: repeat\\(auto-fit, minmax\\(280px, 1fr\\)\\); gap: 1rem;(?:\\s*margin-top: 1rem;)?\"?>[\\s\\S]*?(?=</div>\\s*</div>\\s*<!-- MODAL 3: SKILLS)'\n"
        "    if re.search(projects_pattern, html):\n"
        "        html = re.sub(projects_pattern, PROJECTS_4_CARDS_EN + '\\n        ', html)\n\n"
        "    # 6.6. Contact Location Badge in EN\n"
        "    html = html.replace('Based in Milan, Italy.', 'Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.')\n"
        "    html = html.replace('📍 <strong>Based in Milan, Italy.</strong>', '📍 <strong>Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.</strong>')\n\n"
    )
    if '6.4. Projects 4 Cards Grid' not in compile_py:
        compile_py = compile_py.replace(
            "    # 6.5. #modalTools Modal Card (IDEMPOTENT REPLACEMENT)",
            en_projects_sub + "    # 6.5. #modalTools Modal Card (IDEMPOTENT REPLACEMENT)"
        )

    # Floating hint 5-second dismiss timer call
    compile_py = compile_py.replace(
        "            if (hint) {\n                hint.classList.add('fade-out');\n                setTimeout(() => { hint.style.display = 'none'; }, 1000);\n            }",
        "            if (typeof dismissFloatingHint === 'function') dismissFloatingHint();"
    )

    # E. In build_it_html:
    # Italian hint replacement (Mission Control Welcome HUD)
    old_hint_it_block = (
        "    # 4. Floating Orbit Hint in Italian with 5s Timer\n"
        "    hint_it = '''<div class=\"orbit-floating-hint\" id=\"orbitFloatingHint\">\n"
        "            🌌 <strong>Matrice Solare Fotorealistica</strong><br>\n"
        "            Trascina per orbitare attorno al sole in 3D • Pizzica/scorri per lo zoom • Clicca o tocca qualsiasi pianeta per esplorare.\n"
        "        </div>'''\n"
        "    it = re.sub(r'<div class=\"orbit-floating-hint\"[^>]*>[\\s\\S]*?</div>', hint_it, it)"
    )
    new_hint_it_block = (
        "    # 4. Floating Orbit Hint in Italian with 5s Timer (Mission Control Welcome HUD)\n"
        "    hint_it_pattern = r'[ \\t]*<div class=\"orbit-floating-hint\"[^>]*>[\\s\\S]*?(?=<!-- Bottom Floating Spatial Menu Dock)'\n"
        "    hint_it = '''<div class=\"orbit-floating-hint\" id=\"orbitFloatingHint\">\n"
        "            <button class=\"hint-close-btn\" onclick=\"dismissFloatingHint(event)\" aria-label=\"Chiudi guida benvenuto\">✕</button>\n"
        "            <div class=\"hint-eyebrow\"><span class=\"hint-pulse-dot\"></span> ONLINE // MILANO &amp; PARMA, ITALIA • EMEA &amp; GLOBALE</div>\n"
        "            <div class=\"hint-headline\">Renzo Francesqui — Architettura CRM, RevOps &amp; Crescita Digitale</div>\n"
        "            <div class=\"hint-subtext\">🌌 <strong>Matrice Solare Fotorealistica</strong><br>Trascina per orbitare attorno al sole in 3D • Pizzica/scorri per lo zoom • Clicca o tocca qualsiasi pianeta per esplorare.</div>\n"
        "            <div class=\"hint-actions\">\n"
        "                <button class=\"hint-pill-btn\" onclick=\"dismissFloatingHint(); openModalForPlanet('services');\"><span>⚡</span> Esplora Servizi</button>\n"
        "                <button class=\"hint-pill-btn\" onclick=\"dismissFloatingHint(); openModalForPlanet('experience');\"><span>🏛️</span> Visualizza Esperienza</button>\n"
        "            </div>\n"
        "        </div>\\n\\n        '''\n"
        "    it = re.sub(hint_it_pattern, hint_it, it)"
    )
    if old_hint_it_block in compile_py:
        compile_py = compile_py.replace(old_hint_it_block, new_hint_it_block)
        print("[OK] Updated hint_it in compile_v3.py")

    # Italian dock replacement
    old_dock_it_block = (
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('ai_dialogue')\">\n"
        "                    <span>💬</span> Dialogo AI\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('services')\">\n"
        "                    <span>⚡</span> Servizi\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('experience')\">\n"
        "                    <span>🏛️</span> Esperienza\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('projects')\">\n"
        "                    <span>🚀</span> Progetti\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('skills')\">\n"
        "                    <span>🛠️</span> Competenze\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('tools')\">\n"
        "                    <span>🧰</span> Strumenti\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('blog')\">\n"
        "                    <span>📰</span> Blog\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('credentials')\">\n"
        "                    <span>🎓</span> Certificazioni\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('contact')\">\n"
        "                    <span>✉️</span> Contattami\n"
        "                </button>"
    )
    new_dock_it_block = (
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('ai_dialogue', true)\">\n"
        "                    <span>💬</span> Dialogo AI\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('services', true)\">\n"
        "                    <span>⚡</span> Servizi\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('experience', true)\">\n"
        "                    <span>🏛️</span> Esperienza\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('projects', true)\">\n"
        "                    <span>🚀</span> Progetti\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('skills', true)\">\n"
        "                    <span>🛠️</span> Competenze\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('tools', true)\">\n"
        "                    <span>🧰</span> Strumenti\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('blog', true)\">\n"
        "                    <span>📰</span> Blog\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('credentials', true)\">\n"
        "                    <span>🎓</span> Certificazioni\n"
        "                </button>\n"
        "                <button class=\"dock-pill-btn\" onclick=\"focusOnPlanet('contact', true)\">\n"
        "                    <span>✉️</span> Contattami\n"
        "                </button>"
    )
    if old_dock_it_block in compile_py:
        compile_py = compile_py.replace(old_dock_it_block, new_dock_it_block)
        print("[OK] Updated dock_it in compile_v3.py")

    # Italian #modalTools replacement with UPGRADED_MODAL_TOOLS_HTML_IT
    old_tools_it_block = (
        "    # 9.5. #modalTools in Italian\n"
        "    it = it.replace(\n"
        "        '<h2 class=\"modal-title-text\"><span>🧰</span> Tools</h2>',\n"
        "        '<h2 class=\"modal-title-text\"><span>🧰</span> Strumenti</h2>'\n"
        "    )\n"
        "    it = it.replace(\n"
        "        '<h3 style=\"font-size: 1.15rem; color: #06b6d4; margin-bottom: 0.5rem; font-weight: 700;\">Interactive Tools & Utilities</h3>',\n"
        "        '<h3 style=\"font-size: 1.15rem; color: #06b6d4; margin-bottom: 0.5rem; font-weight: 700;\">Strumenti & Utility Interattive</h3>'\n"
        "    )\n"
        "    it = it.replace(\n"
        "        'Workspace module under construction. Interactive MarTech utilities, CRM calculators, and automation tooling will be deployed here soon.',\n"
        "        'Modulo in fase di configurazione. Utility MarTech interattive, calcolatori CRM e strumenti di automazione saranno disponibili a breve in quest\\'area.'\n"
        "    )"
    )
    new_tools_it_block = (
        "    # 9.5. #modalTools in Italian (Full Interactive Suite)\n"
        "    modal_tools_pattern = r'[ \\t]*<!-- MODAL: TOOLS -->[\\s\\S]*?(?=<!-- MODAL 4: CREDENTIALS -->)'\n"
        "    it = re.sub(modal_tools_pattern, UPGRADED_MODAL_TOOLS_HTML_IT + '\\n\\n    ', it)"
    )
    if old_tools_it_block in compile_py:
        compile_py = compile_py.replace(old_tools_it_block, new_tools_it_block)
        print("[OK] Updated tools_it in compile_v3.py")

    # Italian contact location badge & 4 project cards translation
    old_it_projects_block = (
        "    # 8. #modalProjects in Italian\n"
        "    it = it.replace('STEP-BY-STEP PIPELINE EXPLORER', 'SIMULATORE PIPELINE REVOPS')\n"
        "    it = it.replace('NEXT STAGE →', 'PROSSIMO STADIO →')"
    )
    new_it_projects_block = (
        "    # 8. #modalProjects in Italian (4 Cards Grid)\n"
        "    projects_pattern = r'[ \\t]*<!-- Standalone Project Cards.*?-->\\s*<div style=\"display: grid; grid-template-columns: repeat\\(auto-fit, minmax\\(280px, 1fr\\)\\); gap: 1rem;(?:\\s*margin-top: 1rem;)?\"?>[\\s\\S]*?(?=</div>\\s*</div>\\s*<!-- MODAL 3: SKILLS)'\n"
        "    it = re.sub(projects_pattern, PROJECTS_4_CARDS_IT + '\\n        ', it)\n"
        "    it = it.replace('STEP-BY-STEP PIPELINE EXPLORER', 'SIMULATORE PIPELINE REVOPS')\n"
        "    it = it.replace('NEXT STAGE →', 'PROSSIMO STADIO →')"
    )
    if old_it_projects_block in compile_py:
        compile_py = compile_py.replace(old_it_projects_block, new_it_projects_block)
        print("[OK] Updated IT projects block in compile_v3.py")

    old_contact_it_badge = "it = it.replace('Based in Milan, Italy.', 'Basato a Milano, Italia.')"
    new_contact_it_badge = (
        "it = it.replace('Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements.', 'Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA &amp; Globali.')\n"
        "    it = it.replace('Based in Milan, Italy • Available for EMEA & Global Remote / Hybrid Engagements.', 'Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA & Globali.')\n"
        "    it = it.replace('Based in Milan, Italy.', 'Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA & Globali.')"
    )
    if old_contact_it_badge in compile_py:
        compile_py = compile_py.replace(old_contact_it_badge, new_contact_it_badge)
        print("[OK] Updated IT contact badge in compile_v3.py")

    compile_v3_path.write_text(compile_py, encoding="utf-8")
    print(f"[OK] Upgraded {compile_v3_path}")

    # 3. Update root index.html with 4 project cards
    root_index_path = BASE_DIR / "index.html"
    root_html = root_index_path.read_text(encoding="utf-8")

    landmark_root_proj_start = '<!-- Standalone Project Cards -->'
    landmark_root_proj_end = '<!-- MODAL 3: SKILLS (CATEGORIZED BY AREAS) -->'
    idx_r_s = root_html.find(landmark_root_proj_start)
    idx_r_e = root_html.find(landmark_root_proj_end)
    if idx_r_s != -1 and idx_r_e != -1:
        root_html = (
            root_html[:idx_r_s]
            + PROJECTS_4_CARDS_EN.strip()
            + "\n        </div>\n    </div>\n\n    "
            + root_html[idx_r_e:]
        )
        root_index_path.write_text(root_html, encoding="utf-8")
        print(f"[OK] Upgraded {root_index_path}")
    else:
        print("[WARN] Could not find standalone project cards landmarks in root index.html")

    # 4. Update scripts/build_italian_version.py for Card 3 and Card 4
    b_it_path = BASE_DIR / "scripts" / "build_italian_version.py"
    b_it_code = b_it_path.read_text(encoding="utf-8")

    old_b_it_target = "html = html.replace('Market Intelligence Pipeline', 'Pipeline di Market Intelligence')"
    new_b_it_block = (
        "html = html.replace('Market Intelligence Pipeline', 'Pipeline di Market Intelligence')\n"
        "    html = html.replace(\n"
        "        'Automated Workflow + Slack + HubSpot. Monitors competitor pricing shifts every 6 hours and logs intelligence summaries.',\n"
        "        'Workflow Automatizzato + Slack + HubSpot. Monitora le variazioni di prezzo dei competitor ogni 6 ore e registra report di sintesi dell\\'intelligence.'\n"
        "    )\n"
        "    html = html.replace('Algorithmic Markov Chain Attribution Engine', 'Motore di Attribuzione Algoritmica Markov Chain')\n"
        "    html = html.replace(\n"
        "        'Python + BigQuery SQL + Looker Studio. Multi-touch algorithmic attribution using first-order Markov chains to calculate removal effects and true channel revenue contribution beyond last-touch bias.',\n"
        "        'Python + BigQuery SQL + Looker Studio. Attribuzione multi-touch algoritmica basata su catene di Markov di primo ordine per calcolare gli effetti di rimozione e la reale incidenza sul fatturato oltre il bias dell\\'ultimo tocco.'\n"
        "    )\n"
        "    html = html.replace('Explore Data Architecture →', 'Esplora Architettura Dati →')\n"
        "    html = html.replace('Enterprise HubSpot & Salesforce RevOps Architecture', 'Architettura RevOps Enterprise HubSpot & Salesforce')\n"
        "    html = html.replace('Enterprise HubSpot &amp; Salesforce RevOps Architecture', 'Architettura RevOps Enterprise HubSpot &amp; Salesforce')\n"
        "    html = html.replace(\n"
        "        'B2B Lead Lifecycle + SLA Routing Engine. Complete enterprise alignment between marketing qualified leads (MQL) and sales accepted leads (SAL) with sub-5-minute routing, custom deal-stage gating, and zero lead leakage.',\n"
        "        'Ciclo di Vita Lead B2B + Motore di Routing SLA. Allineamento enterprise completo tra MQL e SQL con routing sotto i 5 minuti, gate obbligatori di avanzamento deal e azzeramento delle perdite contatti.'\n"
        "    )\n"
        "    html = html.replace('Explore RevOps Architecture →', 'Esplora Architettura RevOps →')"
    )

    if old_b_it_target in b_it_code and 'Algorithmic Markov Chain' not in b_it_code:
        # replace the existing Market Intelligence replacement
        b_it_code = re.sub(
            r"html = html\.replace\('Market Intelligence Pipeline', 'Pipeline di Market Intelligence'\)[\s\S]*?sintesi dell'intelligence\.'\s*\)",
            new_b_it_block,
            b_it_code
        )
        b_it_path.write_text(b_it_code, encoding="utf-8")
        print(f"[OK] Upgraded {b_it_path}")

    print("All upgrades applied successfully!")

if __name__ == "__main__":
    main()
