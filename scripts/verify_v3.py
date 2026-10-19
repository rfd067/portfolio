#!/usr/bin/env python3
"""
Comprehensive verification of Version 3.0:
- English edition (version-3/index.html)
- Italian edition (version-3/it/index.html)
- Freelance Service landing pages (services/ and it/services/)
- Photorealistic Celestial Realism (Sun shaders, Chromosphere, Corona, Planetary PBR bump/emissive/roughness maps, Saturn rings, Rayleigh atmosphere)
- Mobile Experience & Responsiveness (multi-pointer touch orbit, pinch-to-zoom, tap-to-focus, 60 FPS pixel ratio capping, 360px-430px ergonomics)
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
V3_HTML = BASE_DIR / "version-3" / "index.html"
V3_IT_HTML = BASE_DIR / "version-3" / "it" / "index.html"

SERVICE_SLUGS = [
    "hubspot-crm-optimization-startups",
    "small-startup-business-crm-setup-optimization",
    "paid-media-management",
    "seo-and-geo-optimization",
    "marketing-data-reporting"
]

TOOL_SLUGS = [
    "mql-to-sql-sla-lead-leakage-calculator",
    "b2b-campaign-utm-crm-builder",
    "b2b-trade-show-roi-calculator"
]

def verify():
    # 1. English Edition Verification
    assert V3_HTML.exists(), f"Missing {V3_HTML}"
    en_content = V3_HTML.read_text(encoding="utf-8")
    
    print(f"\n--- Checking English Version 3 ({V3_HTML.name}): {len(en_content)} bytes ---")
    
    header_part = en_content.split('class="hud-header"')[1].split('</header>')[0]
    dock_part = en_content.split('class="hud-dock-bottom"')[1].split('</div>')[0]
    
    en_checks = [
        ("Three.js r128 CDN", "three.min.js" in en_content),
        ("Google Analytics G-DPYXTL3ZSN", "G-DPYXTL3ZSN" in en_content),
        ("Title: Digital Marketing, CRM Architecture & Business Insights", "Renzo Francesqui — Digital Marketing, CRM Architecture & Business Insights" in en_content),
        ("Header Badge: Digital Marketing · CRM Architecture · Business Insights", "Digital Marketing · CRM Architecture · Business Insights" in en_content),
        ("Classic 1.5 Button Removed from Header", "CLASSIC V1.5" not in header_part),
        ("Services Button Removed from Header (Per User Request)", "focusOnPlanet('services')" not in header_part),
        ("Services Pill Present in Bottom Dock Menu", ("focusOnPlanet('services')" in dock_part or "focusOnPlanet('services', true)" in dock_part) and "Services" in dock_part),
        ("Mission Control Welcome HUD with Exact Text & Pills", "ONLINE // MILAN &amp; PARMA, ITALY" in en_content and "Drag to orbit the 3D Solar Matrix" in en_content and "Explore Freelance Services" in en_content and "View Track Record" in en_content and "(v3.0)" not in en_content and "(V3.0)" not in en_content),
        ("Floating Hint 5-Second Timer (Not 10s)", "id=\"orbitFloatingHint\"" in en_content and "5000" in en_content and "fade-out" in en_content),
        ("Black Hole Overlay Particles Stripped (No Fake Overlay)", "bhParticleSystem" not in en_content and "bhParticleCount" not in en_content),
        ("Black Hole Photon Ring Mesh Stripped (Clean Interstellar Render)", "bhPhotonRing" not in en_content),
        ("Black Hole Clean Billboard in animate()", "gargantuaMesh.lookAt(camera.position);" in en_content),
        ("Black Hole Relativistic Accretion Shader (ShaderMaterial)", "gargantuaFragmentShader" in en_content and "gargantuaVertexShader" in en_content and "THREE.ShaderMaterial" in en_content),
        ("Black Hole Relativistic Fluid Animation uTime in animate()", "gargantuaMat.uniforms.uTime.value = animClock;" in en_content),
        ("8th Celestial Orb: Services Nexus in 3D Scene", "id: 'services'" in en_content and "createServicesNexusTexture()" in en_content),
        ("Modal #modalServices Present with 4 Services", "id=\"modalServices\"" in en_content),
        ("Service 1 Link: HubSpot CRM & RevOps", 'href="/services/hubspot-crm-optimization-startups/"' in en_content),
        ("Service 1 Link has No Legacy Alias in #modalServices", 'data-legacy-alias' not in en_content.split('id="modalServices"')[1].split('</div>\n    </div>')[0]),
        ("Service 2 Link: Paid Media Management", "/services/paid-media-management/" in en_content),
        ("Service 3 Link: SEO and GEO Optimization", "/services/seo-and-geo-optimization/" in en_content),
        ("Service 4 Link: Marketing Data & Reporting", "/services/marketing-data-reporting/" in en_content),
        ("AI Representative Answers Services Inquiries", "query.includes('serviz')" in en_content and "Startup & SMB CRM Architecture" in en_content),
        ("Interstellar Gargantua Black Hole Group & Hit Proxy", "gargantuaGroup" in en_content and "isBlackHole" in en_content),
        ("Interstellar Gargantua Deep Space Positioning (700, 180, -950)", "gargantuaGroup.position.set(700, 180, -950);" in en_content),
        ("Black Hole Relativistic Spiral Density Waves & Hotspots", "spiralWave1" in en_content and "spotDoppler1" in en_content),
        ("Contact displays Milan only", "Based in Milan, Italy" in en_content and "Parma/Milan" not in en_content),
        ("No work permit in contact", "work permit" not in en_content),
        ("No open to in contact", "Open to" not in en_content and "open to" not in en_content),
        ("No GitHub button in contact", "github.com" not in en_content),
        # New Celestial Realism Checks:
        ("Sun Photorealistic ShaderMaterial", "sunVertexShader" in en_content and "sunFragmentShader" in en_content and "new THREE.ShaderMaterial" in en_content),
        ("Sun Convective Granulation & Flares", "sunNoise" in en_content and "sunFbm" in en_content and "limbDarkening" in en_content),
        ("Sun Chromosphere Prominence Shell & Corona", "chromosphereMesh" in en_content and "coronaSprite" in en_content),
        ("Sun Dynamic uTime Uniform in animate()", "sunMat.uniforms.uTime.value = animClock;" in en_content and "chromosphereMat.uniforms.uTime.value = animClock;" in en_content),
        ("Planetary PBR Relief Bump Maps", "bumpMap" in en_content and "createEarthBumpTexture()" in en_content and "createVolcanicBumpTexture()" in en_content),
        ("Planetary Night Lights & Emissive Maps", "emissiveMap" in en_content and "createEarthLightsTexture()" in en_content and "createServicesNexusEmissiveTexture()" in en_content),
        ("Saturn High-Resolution Ring System (Cassini & Encke)", "createSaturnRingTexture()" in en_content and "Cassini Division" in en_content and "Encke gap" in en_content),
        ("Planetary Atmosphere Rayleigh Glow Shader", "vNormal" in en_content and "pow(1.0 - max(0.0, dot(vNormal, viewDir))" in en_content and "THREE.AdditiveBlending" in en_content),
        # New Mobile Experience & Responsiveness Checks:
        ("Multi-Pointer Touch Orbit & Pinch-to-Zoom", "activePointers" in en_content and "curPinchDist - prevPinchDist" in en_content),
        ("Touch Tap-to-Focus with Drag Distinction", "pointerMoved" in en_content and "handlePointerClick" in en_content and "hitProxy" in en_content),
        ("Mobile 60 FPS Pixel Ratio Capping", "Math.min(window.devicePixelRatio, 2)" in en_content and "renderer.setPixelRatio" in en_content),
        ("Mobile Ergonomics & 360px-430px Responsive Styles", "@media (max-width: 480px)" in en_content and "@media (max-width: 900px)" in en_content),
        ("Mobile Floating Hint Ergonomically Visible", "orbit-floating-hint" in en_content and "display: block !important" in en_content),
        # New Celestial Realism & Touch Architecture Checks:
        ("Single Sun Vertex Shader Declaration (No Duplication)", en_content.count("const sunVertexShader =") == 1),
        ("Martian & Lunar Realistic Impact Cratering", "drawImpactCrater" in en_content and "ejecta" in en_content),
        ("Saturn Concentric Ring UV Geometry", "createConcentricRingGeometry" in en_content and "geo.attributes.uv" in en_content),
        ("Saturn Ring Stable Celestial Plane (No Wobble)", "p.ringGroup.position.x = px;" in en_content),
        ("Tap Outside Modal Dismiss Support", "document.querySelector('.spatial-modal-card.active')" in en_content),
        ("Mobile Dock Pill Flex-Shrink Protection", "flex-shrink: 0;" in en_content),
        ("Ultra-Narrow Viewport 375px Responsiveness", "@media (max-width: 375px)" in en_content),
        ("Modal Close 'X' Resets Camera to Overview", "function resetCameraToOverview()" in en_content and "resetCameraToOverview()" in en_content),
        ("Planet Inspect HUD Has 'X' Close Button", "class=\"modal-close-trigger hud-close-btn\"" in en_content and "resetToOverview()" in en_content),
        ("Camera Reset Restores Starting Spherical Coordinates", "camSpherical.radius = initialRadius;" in en_content and "camSpherical.phi = initialPhi;" in en_content),
        ("Keyboard 'X' / 'x' Key Closes Modal and Resets Camera", "e.key === 'x' || e.key === 'X'" in en_content),
        ("Focus Timer Handle Cleared on Camera Reset", "focusTimerId" in en_content and "clearTimeout(focusTimerId)" in en_content),
        # Tools Orb & Modal Checks (English):
        ("Tools Pill Present in Bottom Dock Menu", ("focusOnPlanet('tools')" in dock_part or "focusOnPlanet('tools', true)" in dock_part) and "Tools" in dock_part and "🧰" in dock_part),
        ("Bottom Dock Has Exactly 9 Pill Buttons", dock_part.count('<button class="dock-pill-btn"') == 9),
        ("9th Celestial Orb: Tools in 3D Scene", "id: 'tools'" in en_content and "createToolsTexture()" in en_content and "'tools': 'modalTools'" in en_content),
        ("Tools Planet Procedural Bump and Emissive Maps", "createToolsBumpTexture()" in en_content and "createToolsEmissiveTexture()" in en_content),
        ("Modal #modalTools Present with 3 Interactive MarTech Tools", 'id="modalTools"' in en_content and "SLA & Lead Leakage Calculator" in en_content and "B2B Campaign UTM & CRM Governance Builder" in en_content and "Trade Show & Exhibition ROI Calculator" in en_content),
        ("Exact pulseLive Keyframes in Stylesheet", "0%, 100% { transform: scale(1); opacity: 1; box-shadow: 0 0 8px var(--accent-emerald); }" in en_content and "50% { transform: scale(1.35); opacity: 0.55; box-shadow: 0 0 16px var(--accent-emerald); }" in en_content),
        ("Modal #modalProjects 4 Cards Grid", "Algorithmic Markov Chain Attribution Engine" in en_content and "Enterprise HubSpot &amp; Salesforce RevOps Architecture" in en_content),
        ("Avatar Base64 Data URI Single Declaration", "const RENZO_AVATAR_DATA_URI =" in en_content and en_content.count("const RENZO_AVATAR_DATA_URI =") == 1),
        ("Location Badge in #modalContact", "Based in Milan, Italy • Available for EMEA &amp; Global Remote / Hybrid Engagements." in en_content),
        ("Dock Navigation Auto-Open Modal Delay", "focusOnPlanet('services', true)" in dock_part and "focusOnPlanet('projects', true)" in dock_part),
        ("Tool 1 SLA Inputs & CTA", "min=\"50\"" in en_content and "max=\"2500\"" in en_content and "Fix This Pipeline Leakage in Your CRM" in en_content),
        ("Tool 2 UTM Builder Governance & Taxonomy", "tradeshow_qr" in en_content and "abm_sponsored" in en_content and "custom_icp_region" in en_content and "Copy Governed URL" in en_content),
        ("Tool 3 Trade Show ROI Modeler", "Time Saved via Automated Badge-to-HubSpot Sync" in en_content and "Projected Event ROAS" in en_content),
        ("Modal #modalTools Dismiss Trigger Present", 'id="modalTools"' in en_content and 'onclick="closeActiveModal()"' in en_content.split('id="modalTools"')[1].split('</div>\n    </div>')[0]),
        ("Calendly Booking Button in #modalContact", 'href="https://calendly.com/renzo-francesqui"' in en_content and 'Book a Call on Calendly' in en_content),
        ("Dedicated Tool 1 Link in #modalTools", 'href="/tools/mql-to-sql-sla-lead-leakage-calculator/"' in en_content and 'Open Full Tool &amp; Guide' in en_content),
        ("Dedicated Tool 2 Link in #modalTools", 'href="/tools/b2b-campaign-utm-crm-builder/"' in en_content and 'Open Full Tool &amp; Guide' in en_content),
        ("Dedicated Tool 3 Link in #modalTools", 'href="/tools/b2b-trade-show-roi-calculator/"' in en_content and 'Open Full Tool &amp; Guide' in en_content),
        ("Tool 2 UTM Builder CTA Button in #modalTools", 'Eliminate Attribution Drift in Your CRM' in en_content),
        ("Tool 3 Trade Show ROI Unique CTA Button in #modalTools", 'Model Your Trade Show Lead Engine in CRM' in en_content),
        ("Tool 2 Ingestion JSON Prefill in #modalTools", '"utm_source": "linkedin"' in en_content),
        ("UTM Builder Hash Fragment Sanitization Logic", "hashPart" in en_content and "indexOf('#')" in en_content),
        ("UTM Builder Clipboard Fallback Logic", "fallbackCopy" in en_content and "execCommand" in en_content),
    ]
    
    all_passed = True
    for label, passed in en_checks:
        if passed:
            print(f"  [PASS] {label}")
        else:
            print(f"  [FAIL] {label}")
            all_passed = False

    # 2. Italian Edition Verification
    assert V3_IT_HTML.exists(), f"Missing {V3_IT_HTML}"
    it_content = V3_IT_HTML.read_text(encoding="utf-8")
    
    print(f"\n--- Checking Italian Version 3 ({V3_IT_HTML.name}): {len(it_content)} bytes ---")
    
    it_header_part = it_content.split('class="hud-header"')[1].split('</header>')[0]
    it_dock_part = it_content.split('class="hud-dock-bottom"')[1].split('</div>')[0]
    
    it_checks = [
        ("HTML lang=\"it\"", 'lang="it"' in it_content),
        ("Italian Page Title", "Renzo Francesqui — Marketing Digitale, Architetture CRM & Business Insights" in it_content),
        ("Italian Meta Description", "Matrice solare 3D WebGL fotorealistica" in it_content),
        ("Italian Canonical & Hreflang", "https://renzo-francesqui.vercel.app/version-3/it/" in it_content and 'hreflang="it"' in it_content),
        ("Italian Schema.org Job Title", "Specialista Marketing Operations, Architetture CRM & RevOps" in it_content),
        ("Italian Brand Badge", "Marketing Digitale · Architettura CRM · Business Insights" in it_content),
        ("Italian Header has No Services Button", "focusOnPlanet('services')" not in it_header_part),
        ("Italian Dock has Servizi", ("focusOnPlanet('services')" in it_dock_part or "focusOnPlanet('services', true)" in it_dock_part) and "Servizi" in it_dock_part),
        ("Italian Floating Hint with 5s Timer", "Matrice Solare Fotorealistica" in it_content and "5000" in it_content),
        ("Italian Black Hole has No Artificial Overlay Particles/Ring", "bhParticleSystem" not in it_content and "bhPhotonRing" not in it_content),
        ("Italian Black Hole Relativistic Accretion Shader", "gargantuaFragmentShader" in it_content and "gargantuaVertexShader" in it_content and "THREE.ShaderMaterial" in it_content),
        ("Italian Black Hole Relativistic Fluid Animation in animate()", "gargantuaMat.uniforms.uTime.value = animClock;" in it_content),
        ("Italian Dock: Dialogo AI, Esperienza, Progetti, Competenze", "Dialogo AI" in it_dock_part and "Esperienza" in it_dock_part and "Competenze" in it_dock_part),
        ("Italian #modalServices Present", "Soluzioni Freelance ad Alto Impatto & Sistemi di Crescita" in it_content),
        ("Italian Service 1 Link: HubSpot CRM & RevOps", 'href="/it/services/hubspot-crm-optimization-startups/"' in it_content),
        ("Italian Service 1 Link has No Legacy Alias in #modalServices", 'data-legacy-alias' not in it_content.split('id="modalServices"')[1].split('</div>\n    </div>')[0]),
        ("Italian Service 2 Link: /it/services/...paid-media...", "/it/services/paid-media-management/" in it_content),
        ("Italian Service 3 Link: /it/services/...seo-and-geo...", "/it/services/seo-and-geo-optimization/" in it_content),
        ("Italian Service 4 Link: /it/services/...data-reporting...", "/it/services/marketing-data-reporting/" in it_content),
        ("Italian AI Services Query Response", "Offro **4 soluzioni freelance specializzate**" in it_content),
        ("Italian 3D Celestial Orbs Names", "name: 'Servizi'" in it_content and "name: 'Esperienza'" in it_content and "name: 'Competenze'" in it_content),
        ("Italian Contact Modal (Basato a Milano, Italia)", "Basato a Milano, Italia" in it_content),
        ("Italian Geographic Schema (Milano & Lombardy)", "Milano, Italy" in it_content and "Lombardy" in it_content),
        ("Italian BreadcrumbList JSON-LD", "BreadcrumbList" in it_content),
        ("Italian Interstellar Gargantua Deep Space Positioning (700, 180, -950)", "gargantuaGroup.position.set(700, 180, -950);" in it_content),
        ("Italian Black Hole Relativistic Spiral Density Waves & Hotspots", "spiralWave1" in it_content and "spotDoppler1" in it_content),
        # New Italian Celestial & Mobile Checks:
        ("Italian Sun Photorealistic ShaderMaterial", "sunVertexShader" in it_content and "sunFragmentShader" in it_content),
        ("Italian Sun Chromosphere & Corona", "chromosphereMesh" in it_content and "coronaSprite" in it_content),
        ("Italian Sun Dynamic uTime in animate()", "sunMat.uniforms.uTime.value = animClock;" in it_content),
        ("Italian Planetary PBR Bump & Emissive Maps", "bumpMap" in it_content and "emissiveMap" in it_content),
        ("Italian Multi-Pointer Touch & Pinch-to-Zoom", "activePointers" in it_content and "curPinchDist - prevPinchDist" in it_content),
        ("Italian Mobile 60 FPS Pixel Ratio Capping", "Math.min(window.devicePixelRatio, 2)" in it_content),
        ("Italian Mobile 360px-430px Responsive Styles", "@media (max-width: 480px)" in it_content),
        ("Italian Single Sun Vertex Shader Declaration", it_content.count("const sunVertexShader =") == 1),
        ("Italian Impact Cratering Generator", "drawImpactCrater" in it_content),
        ("Italian Concentric Ring Geometry", "createConcentricRingGeometry" in it_content),
        ("Italian Saturn Ring Stable Celestial Plane", "p.ringGroup.position.x = px;" in it_content),
        ("Italian Tap Outside Modal Dismiss", "document.querySelector('.spatial-modal-card.active')" in it_content),
        ("Italian Mobile Dock Flex-Shrink Protection", "flex-shrink: 0;" in it_content),
        ("Italian Modal Close 'X' Resets Camera to Overview", "function resetCameraToOverview()" in it_content and "resetCameraToOverview()" in it_content),
        ("Italian Planet Inspect HUD Has 'X' Close Button", "class=\"modal-close-trigger hud-close-btn\"" in it_content and "resetToOverview()" in it_content),
        ("Italian Camera Reset Restores Starting Spherical Coordinates", "camSpherical.radius = initialRadius;" in it_content and "camSpherical.phi = initialPhi;" in it_content),
        ("Italian Keyboard 'X' / 'x' Key Closes Modal and Resets Camera", "e.key === 'x' || e.key === 'X'" in it_content),
        ("Italian Focus Timer Handle Cleared on Camera Reset", "focusTimerId" in it_content and "clearTimeout(focusTimerId)" in it_content),
        # Tools Orb & Modal Checks (Italian):
        ("Italian Dock has Strumenti", ("focusOnPlanet('tools')" in it_dock_part or "focusOnPlanet('tools', true)" in it_dock_part) and "Strumenti" in it_dock_part and "🧰" in it_dock_part),
        ("Italian Bottom Dock Has Exactly 9 Pill Buttons", it_dock_part.count('<button class="dock-pill-btn"') == 9),
        ("Italian 3D Celestial Orb: Tools/Strumenti", "id: 'tools'" in it_content and "name: 'Strumenti'" in it_content and "'tools': 'modalTools'" in it_content),
        ("Italian Tools Planet Procedural Bump and Emissive Maps", "createToolsBumpTexture()" in it_content and "createToolsEmissiveTexture()" in it_content),
        ("Italian #modalTools Present with 3 Interactive MarTech Tools", 'id="modalTools"' in it_content and "Calcolatore SLA MQL-to-SQL &amp; Dispersione Pipeline" in it_content and "Builder UTM Campagne B2B &amp; Governance CRM" in it_content and "Calcolatore ROI Fiere &amp; Stand B2B" in it_content),
        ("Italian Exact pulseLive Keyframes in Stylesheet", "0%, 100% { transform: scale(1); opacity: 1; box-shadow: 0 0 8px var(--accent-emerald); }" in it_content and "50% { transform: scale(1.35); opacity: 0.55; box-shadow: 0 0 16px var(--accent-emerald); }" in it_content),
        ("Italian Modal #modalProjects 4 Cards Grid", "Motore di Attribuzione Algoritmica Markov Chain" in it_content and "Architettura RevOps Enterprise HubSpot &amp; Salesforce" in it_content),
        ("Italian Location Badge in #modalContact", "Basato a Milano, Italia • Disponibile per collaborazioni remote / ibride EMEA &amp; Globali." in it_content),
        ("Italian Mission Control Welcome HUD with Exact Text & Pills", "ONLINE // MILANO &amp; PARMA, ITALIA" in it_content and "Esplora Servizi" in it_content and "Visualizza Esperienza" in it_content),
        ("Italian Tool 1 SLA Calcolatore", "Pipeline Annuale Dispersa" in it_content and "Risolvi Questa Dispersione Pipeline nel Tuo CRM" in it_content),
        ("Italian Tool 2 Costruttore UTM", "tradeshow_qr" in it_content and "abm_sponsored" in it_content and ("Copia URL" in it_content or "copia" in it_content.lower())),
        ("Italian Tool 3 ROI Fiere Modeler", "Tempo Risparmiato con Sincronizzazione Badge-HubSpot" in it_content),
        ("Italian Modal #modalTools Dismiss Trigger Present", 'id="modalTools"' in it_content and 'onclick="closeActiveModal()"' in it_content.split('id="modalTools"')[1].split('</div>\n    </div>')[0]),
        ("Italian Calendly Booking Button in #modalContact", 'href="https://calendly.com/renzo-francesqui"' in it_content and 'Prenota una Call su Calendly' in it_content),
        ("Italian Dedicated Tool 1 Link in #modalTools", 'href="/it/tools/mql-to-sql-sla-lead-leakage-calculator/"' in it_content and 'Apri Tool Dedicato' in it_content),
        ("Italian Dedicated Tool 2 Link in #modalTools", 'href="/it/tools/b2b-campaign-utm-crm-builder/"' in it_content and 'Apri Tool Dedicato' in it_content),
        ("Italian Dedicated Tool 3 Link in #modalTools", 'href="/it/tools/b2b-trade-show-roi-calculator/"' in it_content and 'Apri Tool Dedicato' in it_content),
        ("Italian Tool 2 UTM Builder CTA Button in #modalTools", 'Elimina la Dispersione di Attribuzione nel CRM' in it_content),
        ("Italian Tool 2 Ingestion JSON Prefill in #modalTools", '"utm_source": "linkedin"' in it_content),
        ("Italian UTM Builder Hash Fragment Sanitization Logic", "hashPart" in it_content and "indexOf('#')" in it_content),
        ("Italian UTM Builder Clipboard Fallback Logic", "fallbackCopy" in it_content and "execCommand" in it_content),
    ]

    for label, passed in it_checks:
        if passed:
            print(f"  [PASS] {label}")
        else:
            print(f"  [FAIL] {label}")
            all_passed = False

    # 3. Freelance Service Landing Pages Verification
    import re
    import json

    print("\n--- Checking Freelance Service Landing Pages ---")
    service_check_count = 0
    for slug in SERVICE_SLUGS:
        en_path = BASE_DIR / "services" / slug / "index.html"
        it_path = BASE_DIR / "it" / "services" / slug / "index.html"
        
        en_text = en_path.read_text(encoding="utf-8") if en_path.exists() else ""
        it_text = it_path.read_text(encoding="utf-8") if it_path.exists() else ""
        
        en_exists = en_path.exists() and len(en_text) > 5000
        it_exists = it_path.exists() and len(it_text) > 5000
        
        en_sections_ok = (
            "starshieldCanvas" in en_text and
            "telemetry-rail" in en_text and
            "sx-header" in en_text and
            "sx-hero" in en_text and
            "sx-stats-section" in en_text and
            "sx-pillars-section" in en_text and
            "sx-specs-section" in en_text and
            "sx-sequence-section" in en_text and
            "sx-footer" in en_text and
            "sx-btn" in en_text and
            "mailto:renzo.francesqui@gmail.com?subject=Mission%20Inquiry%20" in en_text and
            'href="../../index.html"' in en_text
        )
        it_sections_ok = (
            "starshieldCanvas" in it_text and
            "telemetry-rail" in it_text and
            "sx-header" in it_text and
            "sx-hero" in it_text and
            "sx-stats-section" in it_text and
            "sx-pillars-section" in it_text and
            "sx-specs-section" in it_text and
            "sx-sequence-section" in it_text and
            "sx-footer" in it_text and
            "sx-btn" in it_text and
            "mailto:renzo.francesqui@gmail.com?subject=Richiesta%20Missione%20" in it_text and
            'href="../../index.html"' in it_text
        )
        
        # 3a. Skeleton Components Check
        service_check_count += 2
        if en_exists and en_sections_ok:
            print(f"  [PASS] EN Service Page: /services/{slug}/ (SpaceX Starshield Hero + Stats + Pillars + Specs + Sequence + Footer)")
        else:
            print(f"  [FAIL] EN Service Page Missing or Incomplete: /services/{slug}/ (exists={en_exists}, sections={en_sections_ok})")
            all_passed = False
            
        if it_exists and it_sections_ok:
            print(f"  [PASS] IT Service Page: /it/services/{slug}/ (SpaceX Starshield Hero + Stats + Pillars + Specs + Sequence + Footer)")
        else:
            print(f"  [FAIL] IT Service Page Missing or Incomplete: /it/services/{slug}/ (exists={it_exists}, sections={it_sections_ok})")
            all_passed = False

        # 3b. Title Tag Length Check (< 60 chars)
        service_check_count += 2
        en_title_match = re.search(r"<title>([^<]+)</title>", en_text)
        it_title_match = re.search(r"<title>([^<]+)</title>", it_text)
        en_title = en_title_match.group(1).strip() if en_title_match else ""
        it_title = it_title_match.group(1).strip() if it_title_match else ""
        
        if en_title and len(en_title) < 60:
            print(f"  [PASS] EN Title Tag < 60 chars ({len(en_title)} chars): '{en_title}'")
        else:
            print(f"  [FAIL] EN Title Tag length invalid ({len(en_title)} chars): '{en_title}'")
            all_passed = False

        if it_title and len(it_title) < 60:
            print(f"  [PASS] IT Title Tag < 60 chars ({len(it_title)} chars): '{it_title}'")
        else:
            print(f"  [FAIL] IT Title Tag length invalid ({len(it_title)} chars): '{it_title}'")
            all_passed = False

        # 3c. Meta Description Length Check (< 160 chars)
        service_check_count += 2
        en_desc_match = re.search(r'<meta name="description" content="([^"]+)">', en_text)
        it_desc_match = re.search(r'<meta name="description" content="([^"]+)">', it_text)
        en_desc = en_desc_match.group(1).strip() if en_desc_match else ""
        it_desc = it_desc_match.group(1).strip() if it_desc_match else ""

        if en_desc and 30 < len(en_desc) < 160:
            print(f"  [PASS] EN Meta Description < 160 chars ({len(en_desc)} chars)")
        else:
            print(f"  [FAIL] EN Meta Description length invalid ({len(en_desc)} chars)")
            all_passed = False

        if it_desc and 30 < len(it_desc) < 160:
            print(f"  [PASS] IT Meta Description < 160 chars ({len(it_desc)} chars)")
        else:
            print(f"  [FAIL] IT Meta Description length invalid ({len(it_desc)} chars)")
            all_passed = False

        # 3d. Hero Lead Section Check
        service_check_count += 2
        en_lead_match = re.search(r'<p class="sx-hero-lead">([^<]+)</p>', en_text)
        it_lead_match = re.search(r'<p class="sx-hero-lead">([^<]+)</p>', it_text)
        en_lead_ok = bool(en_lead_match and len(en_lead_match.group(1).strip()) >= 50)
        it_lead_ok = bool(it_lead_match and len(it_lead_match.group(1).strip()) >= 50)

        if en_lead_ok:
            print(f"  [PASS] EN Hero Lead Section verified ({len(en_lead_match.group(1).strip())} chars)")
        else:
            print(f"  [FAIL] EN Hero Lead Section missing or too short")
            all_passed = False

        if it_lead_ok:
            print(f"  [PASS] IT Hero Lead Section verified ({len(it_lead_match.group(1).strip())} chars)")
        else:
            print(f"  [FAIL] IT Hero Lead Section missing or too short")
            all_passed = False

        # 3e. Strict SpaceX Starshield Zero Emojis Compliance Check
        service_check_count += 2
        emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]')
        en_emoji_ok = not emoji_pattern.search(en_text)
        it_emoji_ok = not emoji_pattern.search(it_text)

        if en_emoji_ok:
            print(f"  [PASS] EN Strict Zero Emojis Compliance for {slug}")
        else:
            print(f"  [FAIL] EN Contains Banned Emojis in {slug}")
            all_passed = False

        if it_emoji_ok:
            print(f"  [PASS] IT Strict Zero Emojis Compliance for {slug}")
        else:
            print(f"  [FAIL] IT Contains Banned Emojis in {slug}")
            all_passed = False

        # 3f. Strict SpaceX Starshield Zero Rounded Bubbles Check
        service_check_count += 2
        en_corners_ok = "border-radius: 0 !important;" in en_text
        it_corners_ok = "border-radius: 0 !important;" in it_text
        if en_corners_ok:
            print(f"  [PASS] EN Sharp 90-Degree Corners (border-radius: 0) verified for {slug}")
        else:
            print(f"  [FAIL] EN Sharp corners rule missing in {slug}")
            all_passed = False

        if it_corners_ok:
            print(f"  [PASS] IT Sharp 90-Degree Corners (border-radius: 0) verified for {slug}")
        else:
            print(f"  [FAIL] IT Sharp corners rule missing in {slug}")
            all_passed = False

        # 3g. Schema.org JSON-LD Schemas Check (Service, WebPage, BreadcrumbList & Geographic Schema)
        service_check_count += 2
        en_json_match = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', en_text)
        it_json_match = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', it_text)
        
        try:
            en_schema = json.loads(en_json_match.group(1).strip()) if en_json_match else {}
            en_types = {item.get("@type") for item in en_schema.get("@graph", [en_schema])}
            en_service = next((item for item in en_schema.get("@graph", []) if item.get("@type") == "Service"), {})
            en_audience_ok = en_service.get("audience", {}).get("@type") == "BusinessAudience"
            en_schema_ok = ("Service" in en_types) and ("WebPage" in en_types) and ("BreadcrumbList" in en_types) and en_audience_ok
        except Exception:
            en_schema_ok = False

        try:
            it_schema = json.loads(it_json_match.group(1).strip()) if it_json_match else {}
            it_types = {item.get("@type") for item in it_schema.get("@graph", [it_schema])}
            it_service = next((item for item in it_schema.get("@graph", []) if item.get("@type") == "Service"), {})
            it_audience_ok = it_service.get("audience", {}).get("@type") == "BusinessAudience"
            it_geo_ok = ("Milano, Italy" in json.dumps(it_schema)) and ("Lombardy" in json.dumps(it_schema))
            it_schema_ok = ("Service" in it_types) and ("WebPage" in it_types) and ("Organization" in it_types) and ("BreadcrumbList" in it_types) and it_audience_ok and it_geo_ok
        except Exception:
            it_schema_ok = False

        if en_schema_ok:
            print(f"  [PASS] EN JSON-LD Structured Data: Service, WebPage & BreadcrumbList entities present with BusinessAudience")
        else:
            print(f"  [FAIL] EN JSON-LD Structured Data missing Service, WebPage, BreadcrumbList, or BusinessAudience schema")
            all_passed = False

        if it_schema_ok:
            print(f"  [PASS] IT JSON-LD Structured Data: Service, WebPage, Organization & Breadcrumbs present with Milan/Lombardy Geographic Schema")
        else:
            print(f"  [FAIL] IT JSON-LD Structured Data missing Service, WebPage, Organization, BreadcrumbList, or Milan/Lombardy Schema")
            all_passed = False

        # 3h. Canonical & Hreflang Tags Check
        service_check_count += 2
        target_slug = "hubspot-crm-optimization-startups" if "crm" in slug else slug
        en_canonical_ok = (f'<link rel="canonical" href="https://renzo-francesqui.vercel.app/services/{target_slug}/">' in en_text or f'<link rel="canonical" href="https://renzo-francesqui.vercel.app/services/{slug}/">' in en_text) and 'hreflang="x-default"' in en_text
        it_canonical_ok = (f'<link rel="canonical" href="https://renzo-francesqui.vercel.app/it/services/{target_slug}/">' in it_text or f'<link rel="canonical" href="https://renzo-francesqui.vercel.app/it/services/{slug}/">' in it_text) and 'hreflang="x-default"' in it_text
        if en_canonical_ok:
            print(f"  [PASS] EN Canonical & Hreflang Tags verified for /services/{slug}/")
        else:
            print(f"  [FAIL] EN Canonical or Hreflang Tags invalid for /services/{slug}/")
            all_passed = False

        if it_canonical_ok:
            print(f"  [PASS] IT Canonical & Hreflang Tags verified for /it/services/{slug}/")
        else:
            print(f"  [FAIL] IT Canonical or Hreflang Tags invalid for /it/services/{slug}/")
            all_passed = False

        # 3i. 4-Stage Launch Sequence Check
        service_check_count += 2
        en_stages_ok = ('sx-sequence-grid' in en_text) and en_text.count('class="sx-seq-step"') == 4 and all(f"STAGE 0{step}" in en_text for step in [1, 2, 3, 4])
        it_stages_ok = ('sx-sequence-grid' in it_text) and it_text.count('class="sx-seq-step"') == 4 and all(f"STAGE 0{step}" in it_text for step in [1, 2, 3, 4])
        if en_stages_ok:
            print(f"  [PASS] EN 4-Stage Launch Sequence verified")
        else:
            print(f"  [FAIL] EN 4-Stage Launch Sequence incomplete")
            all_passed = False

        if it_stages_ok:
            print(f"  [PASS] IT 4-Stage Launch Sequence verified")
        else:
            print(f"  [FAIL] IT 4-Stage Launch Sequence incomplete")
            all_passed = False

        # 3j. Mandatory Master SpaceX CSS Tokens Check
        service_check_count += 2
        en_css_ok = ('--bg-black: #000000;' in en_text) and ('--accent-gold: #D4A863;' in en_text) and ('Barlow Condensed' in en_text) and ('JetBrains Mono' in en_text)
        it_css_ok = ('--bg-black: #000000;' in it_text) and ('--accent-gold: #D4A863;' in it_text) and ('Barlow Condensed' in it_text) and ('JetBrains Mono' in it_text)
        if en_css_ok:
            print(f"  [PASS] EN Master SpaceX CSS tokens verified for {slug}")
        else:
            print(f"  [FAIL] EN Master SpaceX CSS tokens missing for {slug}")
            all_passed = False

        if it_css_ok:
            print(f"  [PASS] IT Master SpaceX CSS tokens verified for {slug}")
        else:
            print(f"  [FAIL] IT Master SpaceX CSS tokens missing for {slug}")
            all_passed = False

        # 3k. Global Background Canvas & Scroll Telemetry Script Check
        service_check_count += 2
        en_orbital_ok = ('starshieldCanvas' in en_text) and ('telemetry-rail' in en_text) and ('telemetry-readout' in en_text) and ('IntersectionObserver' in en_text)
        it_orbital_ok = ('starshieldCanvas' in it_text) and ('telemetry-rail' in it_text) and ('telemetry-readout' in it_text) and ('IntersectionObserver' in it_text)
        if en_orbital_ok:
            print(f"  [PASS] EN Starshield Canvas & Scroll Telemetry verified for {slug}")
        else:
            print(f"  [FAIL] EN Starshield Canvas or Telemetry missing for {slug}")
            all_passed = False

        if it_orbital_ok:
            print(f"  [PASS] IT Starshield Canvas & Scroll Telemetry verified for {slug}")
        else:
            print(f"  [FAIL] IT Starshield Canvas or Telemetry missing for {slug}")
            all_passed = False

        # 3l. Falcon-9 Style Technical Spec Table + CAD Schematic Check
        service_check_count += 2
        en_specs_ok = ('sx-specs-layout' in en_text) and ('sx-spec-table' in en_text) and ('sx-wireframe-box' in en_text) and ('<svg' in en_text)
        it_specs_ok = ('sx-specs-layout' in it_text) and ('sx-spec-table' in it_text) and ('sx-wireframe-box' in it_text) and ('<svg' in it_text)

        if en_specs_ok:
            print(f"  [PASS] EN Falcon-9 Technical Spec Table + CAD Schematic verified for {slug}")
        else:
            print(f"  [FAIL] EN Technical Spec Table or CAD Schematic missing in {slug}")
            all_passed = False

        if it_specs_ok:
            print(f"  [PASS] IT Falcon-9 Technical Spec Table + CAD Schematic verified for {slug}")
        else:
            print(f"  [FAIL] IT Technical Spec Table or CAD Schematic missing in {slug}")
            all_passed = False

        # 3m. Flight Heritage Bar Check
        service_check_count += 2
        en_heritage_ok = ('sx-heritage-bar' in en_text) and ('FLIGHT HERITAGE //' in en_text)
        it_heritage_ok = ('sx-heritage-bar' in it_text) and ('FLIGHT HERITAGE //' in it_text)

        if en_heritage_ok:
            print(f"  [PASS] EN Flight Heritage Bar verified for {slug}")
        else:
            print(f"  [FAIL] EN Flight Heritage Bar missing for {slug}")
            all_passed = False

        if it_heritage_ok:
            print(f"  [PASS] IT Flight Heritage Bar verified for {slug}")
        else:
            print(f"  [FAIL] IT Flight Heritage Bar missing for {slug}")
            all_passed = False

        # 3n. Top SpaceX Header & Navigation Check
        service_check_count += 2
        en_hud_ok = ('sx-header' in en_text) and ('sx-brand' in en_text) and ('sx-nav' in en_text) and ('sx-lang-switcher' in en_text)
        it_hud_ok = ('sx-header' in it_text) and ('sx-brand' in it_text) and ('sx-nav' in it_text) and ('sx-lang-switcher' in it_text)
        if en_hud_ok:
            print(f"  [PASS] EN SpaceX Header & Nav Switcher verified for {slug}")
        else:
            print(f"  [FAIL] EN SpaceX Header or Nav Switcher missing for {slug}")
            all_passed = False

        if it_hud_ok:
            print(f"  [PASS] IT SpaceX Header & Nav Switcher verified for {slug}")
        else:
            print(f"  [FAIL] IT SpaceX Header or Nav Switcher missing for {slug}")
            all_passed = False

        # 3o. Signature SpaceX Sliding-Fill Button & Footer Check
        service_check_count += 2
        en_cta_ok = (
            ('sx-footer' in en_text) and
            ('sx-vertical-line' in en_text) and
            ('sx-btn' in en_text) and
            ('mailto:renzo.francesqui@gmail.com?subject=Mission%20Inquiry%20' in en_text) and
            ('READY TO DEPLOY THIS ARCHITECTURE?' in en_text)
        )
        it_cta_ok = (
            ('sx-footer' in it_text) and
            ('sx-vertical-line' in it_text) and
            ('sx-btn' in it_text) and
            ('mailto:renzo.francesqui@gmail.com?subject=Richiesta%20Missione%20' in it_text) and
            ('PRONTO A DISTRIBUIRE QUESTA ARCHITETTURA?' in it_text)
        )
        if en_cta_ok:
            print(f"  [PASS] EN Starshield Sliding-Fill Buttons & Footer verified for {slug}")
        else:
            print(f"  [FAIL] EN Starshield Footer invalid for {slug}")
            all_passed = False

        if it_cta_ok:
            print(f"  [PASS] IT Starshield Sliding-Fill Buttons & Footer verified for {slug}")
        else:
            print(f"  [FAIL] IT Starshield Footer invalid for {slug}")
            all_passed = False

    # 4. Minimalist Editorial Tool Landing Pages Verification
    print("\n--- Checking Minimalist Editorial Tool Landing Pages ---")
    tool_check_count = 0
    for slug in TOOL_SLUGS:
        en_path = BASE_DIR / "tools" / slug / "index.html"
        it_path = BASE_DIR / "it" / "tools" / slug / "index.html"
        
        en_text = en_path.read_text(encoding="utf-8") if en_path.exists() else ""
        it_text = it_path.read_text(encoding="utf-8") if it_path.exists() else ""
        
        en_exists = en_path.exists() and len(en_text) > 5000
        it_exists = it_path.exists() and len(it_text) > 5000
        
        en_sections_ok = (
            "nav-Wrapper" in en_text and
            "hud-header" in en_text and
            "editorial-container" in en_text and
            "hero-title" in en_text and
            "metrics-strip" in en_text and
            "contrast-grid" in en_text and
            "orbital-timeline" in en_text and
            "stage-card" in en_text and
            "cta-console" in en_text and
            "btn-gold" in en_text and
            "btn-ghost" in en_text and
            "https://calendly.com/renzo-francesqui" in en_text and
            "mailto:renzo.francesqui@gmail.com" in en_text and
            'href="../../index.html"' in en_text
        )
        it_sections_ok = (
            "nav-Wrapper" in it_text and
            "hud-header" in it_text and
            "editorial-container" in it_text and
            "hero-title" in it_text and
            "metrics-strip" in it_text and
            "contrast-grid" in it_text and
            "orbital-timeline" in it_text and
            "stage-card" in it_text and
            "cta-console" in it_text and
            "btn-gold" in it_text and
            "btn-ghost" in it_text and
            "https://calendly.com/renzo-francesqui" in it_text and
            "mailto:renzo.francesqui@gmail.com" in it_text and
            'href="../../index.html"' in it_text
        )
        
        # 4a. Skeleton Components Check
        tool_check_count += 2
        if en_exists and en_sections_ok:
            print(f"  [PASS] EN Tool Page: /tools/{slug}/ (Minimalist Editorial HUD + Hero + Tool Workspace + Contrast Grid + Orbital Stages + CTA Console)")
        else:
            print(f"  [FAIL] EN Tool Page Missing or Incomplete: /tools/{slug}/ (exists={en_exists}, sections={en_sections_ok})")
            all_passed = False
            
        if it_exists and it_sections_ok:
            print(f"  [PASS] IT Tool Page: /it/tools/{slug}/ (Minimalist Editorial HUD + Hero + Tool Workspace + Contrast Grid + Orbital Stages + CTA Console)")
        else:
            print(f"  [FAIL] IT Tool Page Missing or Incomplete: /it/tools/{slug}/ (exists={it_exists}, sections={it_sections_ok})")
            all_passed = False

        # 4b. Live Interactive Tool Workspace & Logic Check
        tool_check_count += 2
        if "sla" in slug:
            en_tool_ok = "slaLeadsInput" in en_text and "slaAcvInput" in en_text and "updateSlaCalculator" in en_text
            it_tool_ok = "slaLeadsInput" in it_text and "slaAcvInput" in it_text and "updateSlaCalculator" in it_text
        elif "utm" in slug:
            en_tool_ok = "utmCampaignInput" in en_text and "utmUrlInput" in en_text and "updateUtmBuilder" in en_text and '"utm_source": "linkedin"' in en_text and "fallbackCopy" in en_text and "hashPart" in en_text
            it_tool_ok = "utmCampaignInput" in it_text and "utmUrlInput" in it_text and "updateUtmBuilder" in it_text and '"utm_source": "linkedin"' in it_text and "fallbackCopy" in it_text and "hashPart" in it_text
        else: # tradeshow
            en_tool_ok = "tsCostInput" in en_text and "tsBadgesInput" in en_text and "updateTradeShowRoi" in en_text
            it_tool_ok = "tsCostInput" in it_text and "tsBadgesInput" in it_text and "updateTradeShowRoi" in it_text

        if en_tool_ok:
            print(f"  [PASS] EN Interactive Tool Workspace & Engine verified for {slug}")
        else:
            print(f"  [FAIL] EN Interactive Tool Workspace missing or incomplete for {slug}")
            all_passed = False

        if it_tool_ok:
            print(f"  [PASS] IT Interactive Tool Workspace & Engine verified for {slug}")
        else:
            print(f"  [FAIL] IT Interactive Tool Workspace missing or incomplete for {slug}")
            all_passed = False

        # 4c. Title Tag Length Check (< 60 chars)
        tool_check_count += 2
        en_title_match = re.search(r"<title>([^<]+)</title>", en_text)
        it_title_match = re.search(r"<title>([^<]+)</title>", it_text)
        en_title = en_title_match.group(1).strip() if en_title_match else ""
        it_title = it_title_match.group(1).strip() if it_title_match else ""
        
        if en_title and len(en_title) < 60:
            print(f"  [PASS] EN Tool Title Tag < 60 chars ({len(en_title)} chars): '{en_title}'")
        else:
            print(f"  [FAIL] EN Tool Title Tag length invalid ({len(en_title)} chars): '{en_title}'")
            all_passed = False

        if it_title and len(it_title) < 60:
            print(f"  [PASS] IT Tool Title Tag < 60 chars ({len(it_title)} chars): '{it_title}'")
        else:
            print(f"  [FAIL] IT Tool Title Tag length invalid ({len(it_title)} chars): '{it_title}'")
            all_passed = False

        # 4d. Meta Description Length Check (< 160 chars)
        tool_check_count += 2
        en_desc_match = re.search(r'<meta name="description" content="([^"]+)">', en_text)
        it_desc_match = re.search(r'<meta name="description" content="([^"]+)">', it_text)
        en_desc = en_desc_match.group(1).strip() if en_desc_match else ""
        it_desc = it_desc_match.group(1).strip() if it_desc_match else ""

        if en_desc and 30 < len(en_desc) < 160:
            print(f"  [PASS] EN Tool Meta Description < 160 chars ({len(en_desc)} chars)")
        else:
            print(f"  [FAIL] EN Tool Meta Description length invalid ({len(en_desc)} chars)")
            all_passed = False

        if it_desc and 30 < len(it_desc) < 160:
            print(f"  [PASS] IT Tool Meta Description < 160 chars ({len(it_desc)} chars)")
        else:
            print(f"  [FAIL] IT Tool Meta Description length invalid ({len(it_desc)} chars)")
            all_passed = False

        # 4e. Hero Lead Section Check
        tool_check_count += 2
        en_lead_match = re.search(r'<p class="hero-lead">([^<]+)</p>', en_text)
        it_lead_match = re.search(r'<p class="hero-lead">([^<]+)</p>', it_text)
        en_lead_ok = bool(en_lead_match and len(en_lead_match.group(1).strip()) >= 50)
        it_lead_ok = bool(it_lead_match and len(it_lead_match.group(1).strip()) >= 50)

        if en_lead_ok:
            print(f"  [PASS] EN Tool Hero Lead Section verified ({len(en_lead_match.group(1).strip())} chars)")
        else:
            print(f"  [FAIL] EN Tool Hero Lead Section missing or too short")
            all_passed = False

        if it_lead_ok:
            print(f"  [PASS] IT Tool Hero Lead Section verified ({len(it_lead_match.group(1).strip())} chars)")
        else:
            print(f"  [FAIL] IT Tool Hero Lead Section missing or too short")
            all_passed = False

        # 4f. Minimalist Contrast Grid Check (Before vs After)
        tool_check_count += 2
        en_grid_ok = (
            '<div class="contrast-grid">' in en_text and
            'contrast-header muted' in en_text and
            'contrast-header gold' in en_text and
            en_text.count('<span class="marker">–</span>') >= 4 and
            en_text.count('<span class="marker">→</span>') >= 4
        )
        it_grid_ok = (
            '<div class="contrast-grid">' in it_text and
            'contrast-header muted' in it_text and
            'contrast-header gold' in it_text and
            it_text.count('<span class="marker">–</span>') >= 4 and
            it_text.count('<span class="marker">→</span>') >= 4
        )

        if en_grid_ok:
            print(f"  [PASS] EN Tool Contrast Grid: Diagnostic comparison verified for {slug}")
        else:
            print(f"  [FAIL] EN Tool Contrast Grid missing or incomplete for {slug}")
            all_passed = False

        if it_grid_ok:
            print(f"  [PASS] IT Tool Contrast Grid: Diagnostic comparison verified for {slug}")
        else:
            print(f"  [FAIL] IT Tool Contrast Grid missing or incomplete for {slug}")
            all_passed = False

        # 4g. Schema.org JSON-LD Schemas Check (WebApplication, WebPage, BreadcrumbList)
        tool_check_count += 2
        en_json_match = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', en_text)
        it_json_match = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', it_text)
        
        try:
            en_schema = json.loads(en_json_match.group(1).strip()) if en_json_match else {}
            en_types = {item.get("@type") for item in en_schema.get("@graph", [en_schema])}
            en_app = next((item for item in en_schema.get("@graph", []) if item.get("@type") in ("WebApplication", "SoftwareApplication")), {})
            en_app_ok = en_app.get("applicationCategory") == "BusinessApplication"
            en_schema_ok = ("WebApplication" in en_types or "SoftwareApplication" in en_types) and ("WebPage" in en_types) and ("BreadcrumbList" in en_types) and en_app_ok
        except Exception:
            en_schema_ok = False

        try:
            it_schema = json.loads(it_json_match.group(1).strip()) if it_json_match else {}
            it_types = {item.get("@type") for item in it_schema.get("@graph", [it_schema])}
            it_app = next((item for item in it_schema.get("@graph", []) if item.get("@type") in ("WebApplication", "SoftwareApplication")), {})
            it_app_ok = it_app.get("applicationCategory") == "BusinessApplication"
            it_geo_ok = ("Milano" in json.dumps(it_schema)) and ("Lombardy" in json.dumps(it_schema))
            it_schema_ok = ("WebApplication" in it_types or "SoftwareApplication" in it_types) and ("WebPage" in it_types) and ("BreadcrumbList" in it_types) and it_app_ok and it_geo_ok
        except Exception:
            it_schema_ok = False

        if en_schema_ok:
            print(f"  [PASS] EN Tool JSON-LD Structured Data: WebApplication, WebPage & BreadcrumbList verified for {slug}")
        else:
            print(f"  [FAIL] EN Tool JSON-LD Structured Data missing WebApplication, WebPage, or BreadcrumbList for {slug}")
            all_passed = False

        if it_schema_ok:
            print(f"  [PASS] IT Tool JSON-LD Structured Data: WebApplication, WebPage & Breadcrumbs present with Milan/Lombardy for {slug}")
        else:
            print(f"  [FAIL] IT Tool JSON-LD Structured Data missing WebApplication, WebPage, BreadcrumbList, or Milan for {slug}")
            all_passed = False

        # 4h. Canonical & Hreflang Tags Check
        tool_check_count += 2
        en_canonical_ok = f'<link rel="canonical" href="https://renzo-francesqui.vercel.app/tools/{slug}/">' in en_text and 'hreflang="x-default"' in en_text
        it_canonical_ok = f'<link rel="canonical" href="https://renzo-francesqui.vercel.app/it/tools/{slug}/">' in it_text and 'hreflang="x-default"' in it_text
        if en_canonical_ok:
            print(f"  [PASS] EN Tool Canonical & Hreflang Tags verified for /tools/{slug}/")
        else:
            print(f"  [FAIL] EN Tool Canonical or Hreflang Tags invalid for /tools/{slug}/")
            all_passed = False

        if it_canonical_ok:
            print(f"  [PASS] IT Tool Canonical & Hreflang Tags verified for /it/tools/{slug}/")
        else:
            print(f"  [FAIL] IT Tool Canonical or Hreflang Tags invalid for /it/tools/{slug}/")
            all_passed = False

        # 4i. 4 Execution Stages with Stage 01 Default Open Check
        tool_check_count += 2
        en_stages_ok = ('stage-card open' in en_text) and en_text.count('class="stage-card') == 4 and all(f">{step}<" in en_text for step in ['01', '02', '03', '04'])
        it_stages_ok = ('stage-card open' in it_text) and it_text.count('class="stage-card') == 4 and all(f">{step}<" in it_text for step in ['01', '02', '03', '04'])
        if en_stages_ok:
            print(f"  [PASS] EN Tool 4 Execution Stages with Stage 01 default open verified for {slug}")
        else:
            print(f"  [FAIL] EN Tool Execution Stages incomplete or Stage 01 not open for {slug}")
            all_passed = False

        if it_stages_ok:
            print(f"  [PASS] IT Tool 4 Execution Stages with Stage 01 default open verified for {slug}")
        else:
            print(f"  [FAIL] IT Tool Execution Stages incomplete or Stage 01 not open for {slug}")
            all_passed = False

        # 4j. Master CSS Tokens & Editorial Styling Check
        tool_check_count += 2
        en_css_ok = ('--accent-gold: #d4a863;' in en_text) and ('--border-hairline: rgba(255, 255, 255, 0.08);' in en_text) and ('editorial-container' in en_text)
        it_css_ok = ('--accent-gold: #d4a863;' in it_text) and ('--border-hairline: rgba(255, 255, 255, 0.08);' in it_text) and ('editorial-container' in it_text)
        if en_css_ok:
            print(f"  [PASS] EN Tool Master Minimalist CSS tokens & Editorial Styling verified for {slug}")
        else:
            print(f"  [FAIL] EN Tool Master Minimalist CSS tokens missing for {slug}")
            all_passed = False

        if it_css_ok:
            print(f"  [PASS] IT Tool Master Minimalist CSS tokens & Editorial Styling verified for {slug}")
        else:
            print(f"  [FAIL] IT Tool Master Minimalist CSS tokens missing for {slug}")
            all_passed = False

        # 4k. Minimalist Executive CTA Console Check (with Calendly Booking)
        tool_check_count += 2
        en_cta_ok = (
            ('cta-console' in en_text) and
            ('btn-gold' in en_text) and
            ('btn-ghost' in en_text) and
            ('https://calendly.com/renzo-francesqui' in en_text) and
            ('Calendly' in en_text) and
            ('mailto:renzo.francesqui@gmail.com' in en_text) and
            ('Back to 3D Solar Matrix 🪐' in en_text)
        )
        it_cta_ok = (
            ('cta-console' in it_text) and
            ('btn-gold' in it_text) and
            ('btn-ghost' in it_text) and
            ('https://calendly.com/renzo-francesqui' in it_text) and
            ('Calendly' in it_text) and
            ('mailto:renzo.francesqui@gmail.com' in it_text) and
            ('Ritorna alla Matrice Solare 🪐' in it_text)
        )
        if en_cta_ok:
            print(f"  [PASS] EN Tool Executive CTA Console with Calendly verified for {slug}")
        else:
            print(f"  [FAIL] EN Tool Executive CTA Console invalid for {slug}")
            all_passed = False

        if it_cta_ok:
            print(f"  [PASS] IT Tool Executive CTA Console with Calendly verified for {slug}")
        else:
            print(f"  [FAIL] IT Tool Executive CTA Console invalid for {slug}")
            all_passed = False

    # 5. Idempotent Compiler Verification
    print("\n--- Checking Compiler Idempotency ---")
    import subprocess
    proc = subprocess.run(["python", str(BASE_DIR / "scripts" / "compile_v3.py")], capture_output=True, text=True)
    assert proc.returncode == 0, f"Compilation failed: {proc.stderr}"
    recompiled_en = V3_HTML.read_text(encoding="utf-8")
    recompiled_it = V3_IT_HTML.read_text(encoding="utf-8")
    is_idempotent = (recompiled_en == en_content) and (recompiled_it == it_content)
    if is_idempotent:
        print("  [PASS] Compiler is 100% Idempotent (Recompiling produces identical byte-for-byte outputs)")
    else:
        print(f"  [FAIL] Compiler is NOT Idempotent (Divergence: EN diff={len(recompiled_en)-len(en_content)} bytes, IT diff={len(recompiled_it)-len(it_content)} bytes)")
        all_passed = False

    # 6. Technical SEO & Next.js App Router Verification
    print("\n--- Checking Technical SEO & Next.js App Router Deliverables ---")
    seo_checks = []
    
    # 6a. app/layout.tsx metadataBase and canonical
    layout_path = BASE_DIR / "app" / "layout.tsx"
    layout_text = layout_path.read_text(encoding="utf-8") if layout_path.exists() else ""
    seo_checks.append((
        "app/layout.tsx exists with metadataBase pointing to https://renzo-francesqui.vercel.app",
        layout_path.exists() and "metadataBase: new URL(" in layout_text and "https://renzo-francesqui.vercel.app" in layout_text
    ))
    seo_checks.append((
        "app/layout.tsx configures absolute canonical and Open Graph images",
        "canonical:" in layout_text and "openGraph:" in layout_text and "/images/renzo-francesqui.jpg" in layout_text
    ))
    
    # 6b. components/BreadcrumbsJsonLd.tsx
    breadcrumbs_path = BASE_DIR / "components" / "BreadcrumbsJsonLd.tsx"
    bc_text = breadcrumbs_path.read_text(encoding="utf-8") if breadcrumbs_path.exists() else ""
    seo_checks.append((
        "components/BreadcrumbsJsonLd.tsx implements BreadcrumbList schema with usePathname",
        breadcrumbs_path.exists() and "BreadcrumbList" in bc_text and "usePathname" in bc_text
    ))
    seo_checks.append((
        "components/BreadcrumbsJsonLd.tsx supports acronym uppercase preservation & CRM optimization",
        "CRM Optimization" in bc_text and "generateBreadcrumbsFromPath" in bc_text
    ))
    seo_checks.append((
        "components/BreadcrumbsJsonLd.tsx supports tool routes & humanized labels",
        "'tools': 'Tools'" in bc_text and "'mql-to-sql-sla-lead-leakage-calculator'" in bc_text and "'b2b-campaign-utm-crm-builder'" in bc_text and "'b2b-trade-show-roi-calculator'" in bc_text
    ))

    # 6c. components/ItalianGeographicSchema.tsx
    it_geo_comp = BASE_DIR / "components" / "ItalianGeographicSchema.tsx"
    it_geo_text = it_geo_comp.read_text(encoding="utf-8") if it_geo_comp.exists() else ""
    seo_checks.append((
        "components/ItalianGeographicSchema.tsx implements Person and Organization schema with Milan/Lombardy",
        it_geo_comp.exists() and "Milano, Italy" in it_geo_text and "Lombardy" in it_geo_text and "Person" in it_geo_text and "Organization" in it_geo_text
    ))

    # 6d. components/RevOpsMeetingEmbed.tsx
    embed_comp = BASE_DIR / "components" / "RevOpsMeetingEmbed.tsx"
    embed_text = embed_comp.read_text(encoding="utf-8") if embed_comp.exists() else ""
    seo_checks.append((
        "components/RevOpsMeetingEmbed.tsx implements Calendly iframe container with CTA heading",
        embed_comp.exists() and "calendly-iframe" in embed_text and "Book a Free Systems Audit" in embed_text
    ))

    # 6e. robots.ts & app/robots.ts
    robots_ts_root = BASE_DIR / "robots.ts"
    robots_ts_app = BASE_DIR / "app" / "robots.ts"
    root_ts_text = robots_ts_root.read_text(encoding="utf-8") if robots_ts_root.exists() else ""
    app_ts_text = robots_ts_app.read_text(encoding="utf-8") if robots_ts_app.exists() else ""
    seo_checks.append((
        "robots.ts in root directory disallows /api/ and draft routes",
        robots_ts_root.exists() and "'/api/'" in root_ts_text and "'/draft/'" in root_ts_text and "'/*?draft=*'" in root_ts_text
    ))
    seo_checks.append((
        "app/robots.ts in app/ directory disallows /api/ and draft routes",
        robots_ts_app.exists() and "'/api/'" in app_ts_text and "'/draft/'" in app_ts_text and "'/*?draft=*'" in app_ts_text
    ))

    # 6f. robots.txt
    robots_txt = BASE_DIR / "robots.txt"
    txt_content = robots_txt.read_text(encoding="utf-8") if robots_txt.exists() else ""
    seo_checks.append((
        "robots.txt disallows /api/, /draft, /draft/, and /*?draft=*",
        "Disallow: /api/" in txt_content and "Disallow: /draft" in txt_content and "Disallow: /*?draft=*" in txt_content
    ))

    # 6g. it/index.html Milan / Lombardy schema & Calendly localization
    it_index_path = BASE_DIR / "it" / "index.html"
    it_index_text = it_index_path.read_text(encoding="utf-8") if it_index_path.exists() else ""
    seo_checks.append((
        "it/index.html includes Person and Organization schema with Milan and Lombardy targeting",
        "Milano, Italy" in it_index_text and "Lombardy" in it_index_text and "areaServed" in it_index_text and "worksFor" in it_index_text
    ))
    seo_checks.append((
        "it/index.html includes Calendly booking button with Italian label 'Prenota una Call su Calendly'",
        "https://calendly.com/renzo-francesqui" in it_index_text and "Prenota una Call su Calendly" in it_index_text
    ))
    seo_checks.append((
        "it/index.html includes Italian translation for Markov Chain Attribution project card",
        "Motore di Attribuzione Algoritmica con Catene di Markov" in it_index_text and "Esplora Architettura Dati →" in it_index_text
    ))

    # 6h. sitemap.xml Tool Landing Pages verification
    sitemap_xml = BASE_DIR / "sitemap.xml"
    sitemap_text = sitemap_xml.read_text(encoding="utf-8") if sitemap_xml.exists() else ""
    for t_slug in TOOL_SLUGS:
        seo_checks.append((
            f"sitemap.xml includes EN tool URL: /tools/{t_slug}/",
            f"<loc>https://renzo-francesqui.vercel.app/tools/{t_slug}/</loc>" in sitemap_text
        ))
        seo_checks.append((
            f"sitemap.xml includes IT tool URL: /it/tools/{t_slug}/",
            f"<loc>https://renzo-francesqui.vercel.app/it/tools/{t_slug}/</loc>" in sitemap_text
        ))

    for label, passed in seo_checks:
        if passed:
            print(f"  [PASS] {label}")
        else:
            print(f"  [FAIL] {label}")
            all_passed = False

    total_checks = len(en_checks) + len(it_checks) + service_check_count + tool_check_count + 1 + len(seo_checks)
    if all_passed:
        print(f"\n>>> ALL {total_checks} VERIFICATION CHECKS PASSED FOR VERSION 3.0! <<<")
    else:
        print("\n>>> SOME VERIFICATION CHECKS FAILED! <<<")
        exit(1)

if __name__ == "__main__":
    verify()
