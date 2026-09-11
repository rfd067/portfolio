#!/usr/bin/env python3
"""
Generate the Italian localized version (it/index.html) from index.html.
Ensures identical design, animations, and canvas engine with professional B2B Italian translations.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_HTML = BASE_DIR / "index.html"
IT_HTML = BASE_DIR / "it" / "index.html"

def build_italian_page():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. HTML lang attribute
    html = re.sub(r'<html lang="en"', '<html lang="it"', html)

    # 2. Metadata: Title, Description, Keywords
    html = html.replace(
        '<title>Renzo Francesqui — Digital Marketing | AI Marketing Automation, CRM & RevOps</title>',
        '<title>Renzo Francesqui — Marketing Digitale | Automazione Marketing AI, CRM & RevOps</title>'
    )
    html = html.replace(
        '<meta name="description" content="Spatial 3D constellation & interactive AI representative for Renzo Francesqui — Digital Marketing, Marketing Operations, HubSpot CRM Architecture & AI Marketing Automation.">',
        '<meta name="description" content="Costellazione spaziale 3D e rappresentante AI interattivo di Renzo Francesqui — Marketing Digitale, Marketing Operations, Architettura CRM HubSpot e Automazione AI.">'
    )
    html = html.replace(
        '<meta name="keywords" content="Renzo Francesqui, Digital Marketing, AI Marketing Automation, Spatial Portfolio, Interactive RevOps, HubSpot CRM, AI Automation Agent">',
        '<meta name="keywords" content="Renzo Francesqui, Marketing Digitale, Automazione Marketing AI, Portfolio Spaziale, RevOps, CRM HubSpot, Agente AI Marketing, Parma, Milano">'
    )

    # 3. Canonical URL & Hreflang
    html = html.replace(
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/">',
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/it/">'
    )

    # 4. OpenGraph & Twitter
    html = html.replace(
        '<meta property="og:title" content="Renzo Francesqui — Digital Marketing | AI Marketing Automation, CRM & RevOps">',
        '<meta property="og:title" content="Renzo Francesqui — Marketing Digitale | Automazione Marketing AI, CRM & RevOps">\n    <meta property="og:locale" content="it_IT">\n    <meta property="og:locale:alternate" content="en_US">'
    )
    html = html.replace(
        '<meta property="og:url" content="https://renzo-francesqui.vercel.app/">',
        '<meta property="og:url" content="https://renzo-francesqui.vercel.app/it/">'
    )
    html = html.replace(
        '<meta property="og:description" content="Official portfolio and AI representative of Renzo Francesqui. Specializing in Digital Marketing, HubSpot CRM architecture, B2B marketing operations, and AI automation workflows.">',
        '<meta property="og:description" content="Portfolio ufficiale e rappresentante AI di Renzo Francesqui. Specializzato in Marketing Digitale, architettura CRM HubSpot, operazioni di marketing B2B e workflow di automazione AI.">'
    )
    html = html.replace(
        '<meta name="twitter:url" content="https://renzo-francesqui.vercel.app/">',
        '<meta name="twitter:url" content="https://renzo-francesqui.vercel.app/it/">'
    )
    html = html.replace(
        '<meta name="twitter:title" content="Renzo Francesqui — Digital Marketing | AI Marketing Automation, CRM & RevOps">',
        '<meta name="twitter:title" content="Renzo Francesqui — Marketing Digitale | Automazione Marketing AI, CRM & RevOps">'
    )
    html = html.replace(
        '<meta name="twitter:description" content="Official portfolio and AI representative of Renzo Francesqui. Specializing in Digital Marketing, HubSpot CRM architecture, B2B marketing operations, and AI automation workflows.">',
        '<meta name="twitter:description" content="Portfolio ufficiale e rappresentante AI di Renzo Francesqui. Specializzato in Marketing Digitale, architettura CRM HubSpot, operazioni di marketing B2B e workflow di automazione AI.">'
    )

    # 5. JSON-LD Schema translation
    old_schema = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Renzo Francesqui",
      "jobTitle": "Marketing Operations & RevOps Specialist",
      "url": "https://renzo-francesqui.vercel.app/",
      "image": "https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg",
      "sameAs": [
        "https://www.linkedin.com/in/renzofrancesqui/"
      ],
      "knowsAbout": [
        "HubSpot CRM",
        "Revenue Operations (RevOps)",
        "AI Marketing Automation",
        "Google Antigravity",
        "B2B Lead Lifecycle Management",
        "Trade Show Lead Operations",
        "Digital Marketing",
        "Technical SEO & SEM"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "Università degli Studi di Parma"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Universidad San Ignacio de Loyola"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Cologne Business School"
        }
      ]
    }
    </script>"""

    new_schema = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Renzo Francesqui",
      "jobTitle": "Specialista in Marketing Operations & RevOps",
      "description": "Specialista in Marketing Digitale, Revenue Operations (RevOps), architettura CRM HubSpot e automazione di workflow di marketing basati su AI.",
      "url": "https://renzo-francesqui.vercel.app/it/",
      "image": "https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg",
      "sameAs": [
        "https://www.linkedin.com/in/renzofrancesqui/"
      ],
      "knowsAbout": [
        "CRM HubSpot",
        "Revenue Operations (RevOps)",
        "Automazione Marketing AI",
        "Google Antigravity",
        "Gestione del Ciclo di Vita del Lead B2B",
        "Operazioni Lead per Fiere ed Eventi",
        "Marketing Digitale",
        "SEO Tecnico & SEM",
        "Sincronizzazione API REST CRM"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "Università degli Studi di Parma"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Universidad San Ignacio de Loyola"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Cologne Business School"
        }
      ]
    }
    </script>"""

    html = html.replace(old_schema, new_schema)

    # 6. Relative asset adjustments (ensure images and PDFs work from /it/ subdirectory)
    html = html.replace('src="images/renzo-francesqui.jpg"', 'src="/images/renzo-francesqui.jpg"')
    html = html.replace('href="RenzoFrancesquiCV2026.pdf"', 'href="/RenzoFrancesquiCV2026.pdf"')

    # 7. Language Switcher in Header
    old_lang_switcher = """            <div class="lang-switcher" aria-label="Language selector">
                <a href="/" class="lang-btn active" aria-current="page" title="English">EN</a>
                <span class="lang-divider">/</span>
                <a href="/it/" class="lang-btn" title="Italiano">IT</a>
            </div>"""

    new_lang_switcher = """            <div class="lang-switcher" aria-label="Selezione lingua">
                <a href="/" class="lang-btn" title="English">EN</a>
                <span class="lang-divider">/</span>
                <a href="/it/" class="lang-btn active" aria-current="page" title="Italiano">IT</a>
            </div>"""

    html = html.replace(old_lang_switcher, new_lang_switcher)

    # 8. Header brand badge
    html = html.replace(
        '<span class="brand-tag-badge">Digital Marketing | AI Marketing Automation, CRM and Operations</span>',
        '<span class="brand-tag-badge">Marketing Digitale | Automazione Marketing AI, CRM e Operazioni</span>'
    )

    # 9. Center Stage Orbit Hint
    html = html.replace(
        """                🌌 <strong>Gravitational Matrix</strong><br>
                Click any glowing orb (<strong>AI Dialogue</strong>, <strong>Blog</strong>, <strong>Experience</strong>, <strong>Projects</strong>, <strong>Skills</strong>, <strong>Certifications</strong>, <strong>Contact</strong>) or drag to rotate.""",
        """                🌌 <strong>Matrice Gravitazionale</strong><br>
                Clicca su qualsiasi orbe splendente (<strong>Dialogo AI</strong>, <strong>Blog</strong>, <strong>Esperienza</strong>, <strong>Progetti</strong>, <strong>Competenze</strong>, <strong>Certificazioni</strong>, <strong>Contatti</strong>) o trascina per ruotare lo spazio."""
    )

    # 10. AI Chat Console Header, Banner & Runes
    html = html.replace(
        '<div class="agent-text-title">Renzo Francesqui • AI Representative</div>',
        '<div class="agent-text-title">Renzo Francesqui • Rappresentante AI</div>'
    )
    html = html.replace(
        'title="Close & Return to Orbit">✕</button>',
        'title="Chiudi e torna all\'orbita">✕</button>'
    )
    html = html.replace(
        """        <!-- Welcome/Explainer Banner -->
        <div class="chat-welcome-banner">
            👋 <strong>Ask me anything!</strong> I am Renzo's official AI representative, personally trained by him on his verified career achievements, HubSpot workflows, and technical expertise.
        </div>""",
        """        <!-- Welcome/Explainer Banner -->
        <div class="chat-welcome-banner">
            👋 <strong>Chiedimi qualsiasi cosa!</strong> Sono il rappresentante AI ufficiale di Renzo, addestrato personalmente da lui sui suoi risultati professionali verificati, flussi di lavoro HubSpot e competenze tecniche.
        </div>"""
    )

    old_runes = """        <!-- Suggestion Runes -->
        <div class="chat-runes">
            <button class="rune-btn" onclick="askAiQuestion('HubSpot CRM Architecture')">HubSpot Experience</button>
            <button class="rune-btn" onclick="askAiQuestion('RevOps MQL to SQL Routing')">MQL-to-SQL Routing</button>
            <button class="rune-btn" onclick="askAiQuestion('AI Marketing Automation')">AI Automations</button>
            <button class="rune-btn" onclick="askAiQuestion('Current Role at TOMRA')">Current Role at TOMRA</button>
            <button class="rune-btn" onclick="askAiQuestion('Location and Availability')">EMEA Availability</button>
            <button class="rune-btn" onclick="askAiQuestion('Certifications and Degrees')">Certifications Held</button>
        </div>"""

    new_runes = """        <!-- Suggestion Runes -->
        <div class="chat-runes">
            <button class="rune-btn" onclick="askAiQuestion('Architettura CRM HubSpot')">Esperienza HubSpot</button>
            <button class="rune-btn" onclick="askAiQuestion('Routing MQL a SQL e SLA')">Routing MQL-a-SQL</button>
            <button class="rune-btn" onclick="askAiQuestion('Automazioni Marketing AI')">Automazioni AI</button>
            <button class="rune-btn" onclick="askAiQuestion('Ruolo attuale in TOMRA')">Ruolo attuale in TOMRA</button>
            <button class="rune-btn" onclick="askAiQuestion('Disponibilità e Sede in Italia / EMEA')">Disponibilità EMEA</button>
            <button class="rune-btn" onclick="askAiQuestion('Certificazioni e Titoli di Studio')">Certificazioni possedute</button>
        </div>"""

    html = html.replace(old_runes, new_runes)

    html = html.replace(
        'placeholder="Ask anything about Renzo Francesqui"',
        'placeholder="Fai una domanda su Renzo Francesqui..."'
    )
    html = html.replace(
        'aria-label="Send Inquiry"',
        'aria-label="Invia richiesta"'
    )

    # 11. Bottom Dock Menu Navigation Buttons
    html = html.replace('<span>💬</span> AI Dialogue', '<span>💬</span> Dialogo AI')
    html = html.replace('<span>🏛️</span> Experience', '<span>🏛️</span> Esperienza')
    html = html.replace('<span>⚡</span> Projects', '<span>⚡</span> Progetti')
    html = html.replace('<span>🛠️</span> Skills', '<span>🛠️</span> Competenze')
    html = html.replace('<span>🎓</span> Certifications', '<span>🎓</span> Certificazioni')
    html = html.replace('<span>✉️</span> Get in Touch', '<span>✉️</span> Contatti')

    # 12. Modal 1: Experience
    html = html.replace('<span>🏛️</span> Professional Track Record', '<span>🏛️</span> Percorso Professionale')
    html = html.replace('Parma, Italy • Marketing Events Support | CRM & Marketing Operations', 'Parma, Italia • Supporto Eventi Marketing | CRM & Marketing Operations')
    html = html.replace('OCT 2024 — PRESENT', 'OTT 2024 — PRESENTE')
    html = html.replace(
        '<li>Supported end-to-end lead operations across 15–20 directly organized global trade shows per year (including IFAT and PRS Europe), ensuring 100% of captured leads were synced to HubSpot for immediate follow-up across a 30–50 person EMEA & Americas sales team.</li>',
        '<li>Supporto operativo end-to-end per 15–20 fiere B2B internazionali organizzate direttamente ogni anno (tra cui IFAT e PRS Europe), garantendo la sincronizzazione al 100% dei lead catturati su HubSpot per il follow-up immediato di un team vendite di 30–50 persone in EMEA e Americhe.</li>'
    )
    html = html.replace(
        '<li>Co-led the operational buildout of HubSpot CRM adoption from near-zero usage to an active pipeline management system, standardizing lead capture processes, contact properties, and lifecycle stages across all field events.</li>',
        '<li>Co-guida dello sviluppo e adozione del CRM HubSpot da utilizzo iniziale a sistema attivo di gestione pipeline, standardizzando acquisizione lead, proprietà contatti e lifecycle stages per tutti gli eventi field.</li>'
    )
    html = html.replace(
        '<li>Designed and enforced lead capture standardization at field events ranging from 8 to 350+ leads per show, eliminating data gaps and field mismatches between capture tools and HubSpot.</li>',
        '<li>Progettazione e standardizzazione della lead capture fieristica per volumi da 8 a oltre 350 lead per evento, eliminando lacune nei dati e discrepanze di mappatura tra strumenti di scansione e HubSpot.</li>'
    )
    html = html.replace(
        '<li>Managed offline-to-online data integration workflows post-event, reducing lead-to-sales-handoff time from over one week to same-week import, cleaning, and routing.</li>',
        '<li>Gestione dei workflow di integrazione dati offline-to-online post-evento, riducendo i tempi di passaggio dal lead alle vendite da oltre una settimana a elaborazione, pulizia e instradamento nella stessa settimana.</li>'
    )
    html = html.replace(
        '<li>Collaborated with the lead generation team to define "High Intent" lead criteria and build lead scoring logic in HubSpot, accelerating MQL-to-SQL handover and reducing lead stagnation in the pipeline.</li>',
        '<li>Collaborazione con il team di lead generation per definire i criteri di "Alto Intento" e configurare la logica di lead scoring su HubSpot, accelerando il passaggio MQL-a-SQL e riducendo la stagnazione nella pipeline.</li>'
    )

    html = html.replace('Lima, Peru • Digital Marketing Specialist | Marketing Operations', 'Lima, Perù • Specialista Marketing Digitale | Marketing Operations')
    html = html.replace('OCT 2022 — APR 2024', 'OTT 2022 — APR 2024')
    html = html.replace(
        '<li>Led marketing operations for a 5-person team executing international campaigns across 10+ countries in the Americas, Europe, and the Middle East.</li>',
        '<li>Guida delle marketing operations per un team di 5 persone nell\'esecuzione di campagne internazionali in oltre 10 paesi in Americhe, Europa e Medio Oriente.</li>'
    )
    html = html.replace(
        '<li>Managed HubSpot CRM data integrity across international markets, standardizing contact properties, lifecycle stages, and campaign tracking to ensure clean attribution data.</li>',
        '<li>Gestione dell\'integrità dei dati nel CRM HubSpot per mercati esteri, standardizzando proprietà contatti, lifecycle stages e tracciamento campagne per garantire un\'attribuzione pulita.</li>'
    )
    html = html.replace(
        '<li>Executed SEO and SEM strategies across 4 regions, achieving a 40% increase in organic traffic in 6 months and a 33% improvement in paid conversion rates through continuous A/B testing and funnel optimization.</li>',
        '<li>Esecuzione di strategie SEO e SEM in 4 regioni, ottenendo un incremento del 40% del traffico organico in 6 mesi e un miglioramento del 33% nei tassi di conversione a pagamento tramite A/B testing continuo e ottimizzazione del funnel.</li>'
    )
    html = html.replace(
        '<li>Built Executive KPI Dashboards, visualizing channel performance and ROI attribution to guide Board-level decision-making.</li>',
        '<li>Creazione di Dashboard KPI direzionali, visualizzando le performance di canale e l\'attribuzione del ROI a supporto delle decisioni a livello di CdA.</li>'
    )
    html = html.replace(
        '<li>Designed automated email nurture sequences and lead segmentation workflows, improving lead-to-opportunity conversion rates.</li>',
        '<li>Progettazione di sequenze automatizzate di email nurturing e workflow di segmentazione lead, migliorando i tassi di conversione da lead a opportunità commerciale.</li>'
    )

    html = html.replace(
        '<div style="font-size: 0.82rem; color: var(--accent-gold);">Lima, Peru • Digital Marketing Executive | Go-To-Market (GTM) Strategy</div>',
        '<div style="font-size: 0.82rem; color: var(--accent-gold);">Lima, Perù • Digital Marketing Executive | Strategia Go-To-Market (GTM)</div>'
    )
    html = html.replace('MAY 2019 — APR 2022', 'MAG 2019 — APR 2022')
    html = html.replace(
        '<li>Architected and executed full Go-To-Market (GTM) strategies across SEO/SEM, email workflows, and CRM lead capture for high-value residential developments, driving a complete 100% inventory sell-out before construction delivery.</li>',
        '<li>Progettazione ed esecuzione della strategia Go-To-Market (GTM) completa (SEO/SEM, Email, workflow CRM) per sviluppi immobiliari residenziali di alto valore, raggiungendo il 100% di sell-out dell\'inventario prima della consegna costruttiva.</li>'
    )
    html = html.replace(
        '<li>Built and optimized CRM workflows and lead nurturing automations that drove an average monthly conversion rate increase of over 50% through rigorous A/B testing and funnel stage management.</li>',
        '<li>Creazione e ottimizzazione di flussi di lavoro CRM e automazioni di lead nurturing che hanno generato un aumento medio mensile del tasso di conversione superiore al 50% tramite rigorosi test A/B e gestione delle fasi del funnel.</li>'
    )
    html = html.replace(
        '<li>Managed the complete lead lifecycle from social media capture to sales handoff, defining lead qualification criteria and ensuring consistent data quality for the sales team.</li>',
        '<li>Gestione dell\'intero ciclo di vita del lead dalla cattura sui canali social al passaggio alle vendite, definendo i criteri di qualificazione e assicurando standard elevati di qualità del dato per il team commerciale.</li>'
    )

    # 13. Modal 2: Projects & AI Simulator
    html = html.replace('<span>⚡</span> Technical Projects & AI Simulator', '<span>⚡</span> Progetti Tecnici & Simulatore AI')
    html = html.replace('STEP-BY-STEP PIPELINE EXPLORER', 'ESPLORATORE DI PIPELINE STEP-BY-STEP')
    html = html.replace('Click each stage to inspect live scraping, ICP scoring, and CRM synchronization flow.', 'Clicca su ogni fase per ispezionare il flusso live di scraping, scoring ICP e sincronizzazione CRM.')
    html = html.replace('↻ RESET', '↻ REIMPOSTA')
    html = html.replace('NEXT STAGE →', 'PROSSIMA FASE →')
    html = html.replace('Webhook Ingestion', 'Ingestione Webhook')
    html = html.replace('AI Domain Crawler', 'Crawler AI del Dominio')
    html = html.replace('LLM Fit Scoring', 'Fit Scoring LLM')
    html = html.replace('HubSpot Sync & SLA', 'Sincronizzazione HubSpot & SLA')
    html = html.replace('SELECTED', 'SELEZIONATO')
    html = html.replace('CLICK TO RUN', 'CLICCA PER ESEGUIRE')

    html = html.replace(
        '<div class="narrative-stage-tag">📥 STAGE 01: WEBHOOK INGESTION</div>',
        '<div class="narrative-stage-tag">📥 FASE 01: INGESTIONE WEBHOOK</div>'
    )
    html = html.replace(
        '<div class="narrative-stage-body">An instantaneous Webhook payload is captured from the TOMRA Exhibition badge scanner (e.g. IFAT Munich trade show floor) with contact name, raw email, and domain details.</div>',
        '<div class="narrative-stage-body">Un payload Webhook istantaneo viene catturato dal lettore badge fieristico di TOMRA (es. stand IFAT Monaco) contenente nome del contatto, email e dettagli del dominio.</div>'
    )
    html = html.replace(
        '[STAGE 01 // WEBHOOK INGESTION]<br>\n                    > Received scanner payload from trade show badge reader (IFAT Munich)...<br>\n                    > Payload: { "contact": "lead_9481", "event": "IFAT_Munich", "email": "j.mueller@circ-recycling.de", "domain": "circ-recycling.de" }<br>\n                    > Status: 200 OK — Ready for AI Web Enrichment Agent.',
        '[FASE 01 // INGESTIONE WEBHOOK]<br>\n                    > Ricevuto payload dallo scanner badge fieristico (IFAT Monaco)...<br>\n                    > Payload: { "contact": "lead_9481", "event": "IFAT_Munich", "email": "j.mueller@circ-recycling.de", "domain": "circ-recycling.de" }<br>\n                    > Stato: 200 OK — Pronto per l\'Agente AI di Arricchimento Web.'
    )

    html = html.replace('Automated CRM Enrichment Agent', 'Agente Automatico di Arricchimento CRM')
    html = html.replace(
        'Google Antigravity + HubSpot API. Automatically scrapes corporate domains and classifies company firmographics against ICP in 30 seconds, saving 15+ hours weekly.',
        'Google Antigravity + API HubSpot. Esegue lo scraping autonomo dei domini aziendali e classifica la firmografica rispetto all\'ICP in 30 secondi, risparmiando oltre 15 ore settimanali.'
    )
    html = html.replace('View LinkedIn Post →', 'Visualizza Post LinkedIn →')
    html = html.replace('Market Intelligence Pipeline', 'Pipeline di Market Intelligence')
    html = html.replace(
        'Automated Workflow + Slack + HubSpot. Monitors competitor pricing shifts every 6 hours and logs intelligence summaries.',
        'Workflow Automatizzato + Slack + HubSpot. Monitora le variazioni di prezzo dei competitor ogni 6 ore e registra report di sintesi dell\'intelligence.'
    )

    # 14. Modal 3: Skills
    html = html.replace('<span>🛠️</span> Technical & Strategic Skills Matrix', '<span>🛠️</span> Matrice Competenze Tecniche e Strategiche')
    html = html.replace(
        'Comprehensive domain expertise structured across enterprise CRM systems, revenue operations, AI automation workflows, and full-funnel digital marketing.',
        'Esperienza di dominio completa strutturata su sistemi CRM aziendali, revenue operations, flussi di automazione AI e marketing digitale full-funnel.'
    )
    html = html.replace('CRM Architecture & Administration', 'Architettura & Amministrazione CRM')
    html = html.replace(
        'End-to-end administration, property governance, custom objects, permission sets, and cross-team adoption standardizing data for 50+ sales reps.',
        'Amministrazione end-to-end, governance delle proprietà, oggetti personalizzati, set di autorizzazioni e adozione cross-team standardizzando i dati per oltre 50 sales rep.'
    )

    html = html.replace('Marketing Operations (MktOps) & SLAs', 'Marketing Operations (MktOps) & SLA')
    html = html.replace(
        'Standardizing lead flows from offline global trade shows to CRM routing, establishing stringent response SLAs, and eliminating pipeline stagnation.',
        'Standardizzazione dei flussi di lead dalle fiere internazionali offline all\'instradamento nel CRM, definizione di rigidi SLA di risposta ed eliminazione della stagnazione della pipeline.'
    )

    html = html.replace('AI Marketing Automation & Workflows', 'Automazione Marketing AI & Flussi di Lavoro')
    html = html.replace(
        'Architecting autonomous AI enrichment workflows and webhook automations using tools like Google Antigravity to evaluate ICP criteria and enrich inbound leads without manual research.',
        'Progettazione di workflow autonomi di arricchimento AI e automazioni webhook con strumenti come Google Antigravity per valutare criteri ICP e arricchire lead in entrata senza ricerca manuale.'
    )

    html = html.replace('Performance Marketing & SEM', 'Performance Marketing & SEM')
    html = html.replace(
        'Designing high-intent international paid search and social campaigns across EMEA and Americas, boosting conversion rates by +33%.',
        'Progettazione di campagne internazionali a pagamento di ricerca e social ad alto intento in EMEA e Americhe, aumentando i tassi di conversione del +33%.'
    )

    html = html.replace('Organic Growth & Technical SEO', 'Crescita Organica & SEO Tecnico')
    html = html.replace(
        'Driving +40% organic growth in 6 months through technical site audits, structured markup architecture, and multi-language search optimization.',
        'Incremento del +40% del traffico organico in 6 mesi attraverso audit tecnici del sito, architettura di markup strutturato e ottimizzazione della ricerca multi-lingua.'
    )

    html = html.replace('Analytics, BI & Data Intelligence', 'Analytics, BI & Data Intelligence')
    html = html.replace(
        'Translating multi-channel marketing data into executive dashboards, tracking full-funnel customer journeys and revenue attribution.',
        'Traduzione dei dati di marketing multicanale in dashboard direzionali, tracciamento del customer journey full-funnel e attribuzione del fatturato.'
    )

    # 15. Modal 4: Credentials
    html = html.replace('<span>🎓</span> Certifications & Academic Foundation', '<span>🎓</span> Certificazioni & Fondamenti Accademici')
    html = html.replace('Completed Professional Certifications', 'Certificazioni Professionali Completate')
    html = html.replace('Certifications in Progress (2026)', 'Certificazioni in Corso (2026)')
    html = html.replace(
        '<li>⏳ <strong>Salesforce Administrator</strong> (Currently studying / in pursuit)</li>',
        '<li>⏳ <strong>Salesforce Administrator</strong> (In corso di studio / preparazione)</li>'
    )
    html = html.replace(
        '<li>⏳ <strong>SQL Oracle Database</strong> (Currently studying)</li>',
        '<li>⏳ <strong>Database SQL Oracle</strong> (In corso di studio)</li>'
    )
    html = html.replace('Academic Foundation & Languages', 'Percorso Accademico & Lingue')
    html = html.replace('Master:', 'Laurea Magistrale:')
    html = html.replace('Bachelor:', 'Laurea Triennale:')
    html = html.replace('Study Abroad:', 'Studio all\'estero:')
    html = html.replace('Languages:', 'Lingue:')
    html = html.replace('Spanish (Native), English (C1), Italian (B2)', 'Spagnolo (Madrelingua), Inglese (C1), Italiano (B2)')

    # 16. Modal 5: Blog
    html = html.replace('<span>📰</span> Editorial Hub & Publications', '<span>📰</span> Hub Editoriale & Pubblicazioni')
    html = html.replace(
        'Field-tested frameworks, operational blueprints, and technical architecture guides for modern B2B revenue and marketing teams.',
        'Framework testati sul campo, modelli operativi e guide di architettura tecnica per i moderni team B2B di marketing e revenue.'
    )
    html = html.replace('ENTER FULL BLOG ARCHIVE →', 'ACCEDI ALL\'ARCHIVIO COMPLETO DEL BLOG →')
    html = html.replace('READ ARTICLE →', 'LEGGI ARTICOLO →')

    # 17. Modal 6: Contact
    html = html.replace('<span>✉️</span> Initiate Direct Transmission', '<span>✉️</span> Entra in Contatto')
    html = html.replace(
        'Available for senior opportunities in Marketing Operations, CRM Architecture, and AI Automation Systems.',
        'Disponibile per opportunità B2B in Marketing Operations, Architettura CRM ed Ecosistemi di Automazione AI.'
    )
    html = html.replace('Direct Inquiries:', 'Contatto Diretto:')
    html = html.replace(
        '📍 Based in Milano / Parma, Italy. Valid Italian work permit.',
        '📍 Sede: Milano / Parma, Italia. Permesso di soggiorno/lavoro UE valido.'
    )
    html = html.replace('Open to hybrid & remote roles across EMEA.', 'Disponibile per ruoli ibridi o full-remote in tutta EMEA.')
    html = html.replace('DOWNLOAD VERIFIED CV (PDF)', 'SCARICA CV COMPLETO (PDF)')
    html = html.replace('TRANSMIT EMAIL INQUIRY', 'INVIA EMAIL DIRETTA')
    html = html.replace('CONNECT ON LINKEDIN', 'PROFILO LINKEDIN')
    html = html.replace('EXPLORE GITHUB WORKSPACE', 'CANALE GITHUB')

    # 18. JavaScript: Nodes Labels in 3D Canvas
    old_nodes = """            // 7 Celestial Nodes with Harmonic Colors & Orbital Offsets (Comfortably spaced)
            const nodes = [
                { id: 'ai_dialogue', label: 'AI Dialogue', icon: '💬', x: -300, y: -110, z: 80, color: '#c084fc' },
                { id: 'blog', label: 'Blog', icon: '📰', x: 300, y: -90, z: -60, color: '#fb7185' },
                { id: 'experience', label: 'Experience', icon: '🏛️', x: -240, y: 190, z: -90, color: '#38bdf8' },
                { id: 'projects', label: 'Projects', icon: '⚡', x: 240, y: 190, z: 90, color: '#34d399' },
                { id: 'skills', label: 'Skills', icon: '🛠️', x: 0, y: -260, z: 40, color: '#d4a863' },
                { id: 'credentials', label: 'Certifications', icon: '🎓', x: -160, y: -200, z: -100, color: '#e69138' },
                { id: 'contact', label: 'Get in Touch', icon: '✉️', x: 0, y: 250, z: -30, color: '#60a5fa' },
            ];"""

    new_nodes = """            // 7 Celestial Nodes with Harmonic Colors & Orbital Offsets (Comfortably spaced)
            const nodes = [
                { id: 'ai_dialogue', label: 'Dialogo AI', icon: '💬', x: -300, y: -110, z: 80, color: '#c084fc' },
                { id: 'blog', label: 'Blog', icon: '📰', x: 300, y: -90, z: -60, color: '#fb7185' },
                { id: 'experience', label: 'Esperienza', icon: '🏛️', x: -240, y: 190, z: -90, color: '#38bdf8' },
                { id: 'projects', label: 'Progetti', icon: '⚡', x: 240, y: 190, z: 90, color: '#34d399' },
                { id: 'skills', label: 'Competenze', icon: '🛠️', x: 0, y: -260, z: 40, color: '#d4a863' },
                { id: 'credentials', label: 'Certificazioni', icon: '🎓', x: -160, y: -200, z: -100, color: '#e69138' },
                { id: 'contact', label: 'Contatti', icon: '✉️', x: 0, y: 250, z: -30, color: '#60a5fa' },
            ];"""

    html = html.replace(old_nodes, new_nodes)

    # 19. JavaScript: Pipeline simulation data & AI Responses
    old_sim_code = """        // Step-by-Step Manual Pipeline Controller
        let currentSimStage = 1;
        const pipelineData = {
            1: {
                pill: "200 OK",
                narrative: '<div class="narrative-stage-tag">📥 STAGE 01: WEBHOOK INGESTION</div><div class="narrative-stage-body">An instantaneous Webhook payload is captured from the TOMRA Exhibition badge scanner (IFAT Munich trade show floor) with contact name, email, and domain details.</div>',
                log: `[STAGE 01 // WEBHOOK INGESTION]<br>> Inbound webhook received from field badge scanner (IFAT Munich)...<br>> Payload: { "contact": "lead_9481", "event": "IFAT_Munich_2024", "domain": "circ-recycling.de" }<br>> Status: 200 OK — Transferred to AI Enrichment Agent.`
            },
            2: {
                pill: "EXTRACTED",
                narrative: '<div class="narrative-stage-tag">🤖 STAGE 02: AI DOMAIN CRAWLER</div><div class="narrative-stage-body">Autonomous AI crawler parses the prospect\\'s live corporate domain, extracting metadata, product lines, technology stack, and company size in under 2 seconds.</div>',
                log: `[STAGE 02 // AI DOMAIN CRAWLER]<br>> AI Agent initialized -> Target: https://circ-recycling.de<br>> Extracted firmographics: Vertical: "Circular Waste Management", Sub-sector: "Optical Sorting", Team: "200-500"<br>> Status: Extraction complete (1.2s).`
            },
            3: {
                pill: "SCORE: 98",
                narrative: '<div class="narrative-stage-tag">🧠 STAGE 03: LLM ICP FIT SCORER</div><div class="narrative-stage-body">The reasoning layer analyzes extracted firmographics against predefined revenue and industry ICP thresholds, generating an objective qualification score.</div>',
                log: `[STAGE 03 // LLM ICP SCORER]<br>> Comparing extracted attributes against EMEA Enterprise ICP Matrix...<br>> Match verified on: Annual Revenue (>€50M), Industry Match (Sorting), Geography (DACH)<br>> Fit Score: <span style="color:#34d399; font-weight:700;">98/100 (HIGH INTENT TIER 1 ENTERPRISE)</span>.`
            },
            4: {
                pill: "SYNCED 200",
                narrative: '<div class="narrative-stage-tag">🔄 STAGE 04: HUBSPOT REST API PATCH & SALES SLA</div><div class="narrative-stage-body">Automated REST API call patches the HubSpot Company Record properties directly and fires an instant Slack notification to the DACH Territory Sales Rep.</div>',
                log: `[STAGE 04 // HUBSPOT REST API PATCH & SALES SLA]<br>> REST API: PATCH https://api.hubspot.com/crm/v3/objects/companies/1849204 (200 OK)<br>> Slack SLA Alert sent to #sales-leads-emea (Target Rep: DACH Territory Lead)<br>> <span style="color:#d4a863; font-weight:700;">[SUCCESS] Lead enriched & routed with 0 manual research!</span>`
            }
        };

        function selectPipelineStage(stageNum) {
            currentSimStage = stageNum;
            playTone(450 + stageNum * 90, 'sine', 0.08);

            for (let i = 1; i <= 4; i++) {
                const node = document.getElementById(`simNode${i}`);
                const pill = document.getElementById(`simPill${i}`);
                if (!node || !pill) continue;

                if (i < stageNum) {
                    node.className = 'pipeline-stage-node complete';
                    pill.innerText = pipelineData[i].pill;
                } else if (i === stageNum) {
                    node.className = 'pipeline-stage-node active';
                    pill.innerText = 'ACTIVE';
                } else {
                    node.className = 'pipeline-stage-node';
                    pill.innerText = 'CLICK TO RUN';
                }
            }

            const data = pipelineData[stageNum];
            document.getElementById('simNarrative').innerHTML = data.narrative;
            document.getElementById('modalSimTerminal').innerHTML = data.log;

            const nextBtn = document.getElementById('simNextBtn');
            if (nextBtn) {
                nextBtn.innerText = stageNum === 4 ? 'RESTART PIPELINE ↻' : `NEXT: STAGE 0${stageNum + 1} →`;
            }
        }"""

    new_sim_code = """        // Step-by-Step Manual Pipeline Controller
        let currentSimStage = 1;
        const pipelineData = {
            1: {
                pill: "200 OK",
                narrative: '<div class="narrative-stage-tag">📥 FASE 01: INGESTIONE WEBHOOK</div><div class="narrative-stage-body">Un payload Webhook istantaneo viene catturato dal lettore badge fieristico di TOMRA (IFAT Monaco) con nome del contatto, email e dettagli del dominio.</div>',
                log: `[FASE 01 // INGESTIONE WEBHOOK]<br>> Webhook in entrata ricevuto dallo scanner fiera (IFAT Monaco)...<br>> Payload: { "contact": "lead_9481", "event": "IFAT_Munich_2024", "domain": "circ-recycling.de" }<br>> Stato: 200 OK — Inoltrato all'Agente AI di Arricchimento.`
            },
            2: {
                pill: "ESTRATTO",
                narrative: '<div class="narrative-stage-tag">🤖 FASE 02: CRAWLER AI DEL DOMINIO</div><div class="narrative-stage-body">Il crawler AI autonomo analizza il dominio aziendale del prospect, estraendo metadati, linee di prodotto, stack tecnologico e dimensione aziendale in meno di 2 secondi.</div>',
                log: `[FASE 02 // CRAWLER AI DOMINIO]<br>> Agente AI inizializzato -> Target: https://circ-recycling.de<br>> Firmografica estratta: Verticale: "Circular Waste Management", Sottosettore: "Optical Sorting", Team: "200-500"<br>> Stato: Estrazione completata con successo (1.2s).`
            },
            3: {
                pill: "PUNTEGGIO: 98",
                narrative: '<div class="narrative-stage-tag">🧠 FASE 03: FIT SCORING LLM</div><div class="narrative-stage-body">Il layer di ragionamento LLM confronta gli attributi firmografici estratti con le soglie ICP predefinite di fatturato e settore, generando un punteggio oggettivo di qualificazione.</div>',
                log: `[FASE 03 // SCORER ICP LLM]<br>> Valutazione attributi rispetto alla Matrice ICP Enterprise EMEA...<br>> Corrispondenza confermata: Fatturato (>€50M), Settore (Sorting), Area Geografica (DACH)<br>> Punteggio ICP: <span style="color:#34d399; font-weight:700;">98/100 (ALTO INTENTO - TIER 1 ENTERPRISE)</span>.`
            },
            4: {
                pill: "SYNC 200 OK",
                narrative: '<div class="narrative-stage-tag">🔄 FASE 04: PATCH API REST HUBSPOT & SLA VENDITE</div><div class="narrative-stage-body">Una chiamata API REST automatizzata aggiorna direttamente le proprietà aziendali in HubSpot e genera una notifica Slack istantanea al referente vendite territoriale.</div>',
                log: `[FASE 04 // PATCH API REST HUBSPOT & SLA]<br>> Chiamata REST API: PATCH https://api.hubspot.com/crm/v3/objects/companies/1849204 (200 OK)<br>> Notifica SLA inviata su Slack: #sales-leads-emea (Destinatario: DACH Territory Lead)<br>> <span style="color:#d4a863; font-weight:700;">[SUCCESSO] Lead arricchito e instradato con 0 ricerca manuale!</span>`
            }
        };

        function selectPipelineStage(stageNum) {
            currentSimStage = stageNum;
            playTone(450 + stageNum * 90, 'sine', 0.08);

            for (let i = 1; i <= 4; i++) {
                const node = document.getElementById(`simNode${i}`);
                const pill = document.getElementById(`simPill${i}`);
                if (!node || !pill) continue;

                if (i < stageNum) {
                    node.className = 'pipeline-stage-node complete';
                    pill.innerText = pipelineData[i].pill;
                } else if (i === stageNum) {
                    node.className = 'pipeline-stage-node active';
                    pill.innerText = 'ATTIVO';
                } else {
                    node.className = 'pipeline-stage-node';
                    pill.innerText = 'CLICCA PER ESEGUIRE';
                }
            }

            const data = pipelineData[stageNum];
            document.getElementById('simNarrative').innerHTML = data.narrative;
            document.getElementById('modalSimTerminal').innerHTML = data.log;

            const nextBtn = document.getElementById('simNextBtn');
            if (nextBtn) {
                nextBtn.innerText = stageNum === 4 ? 'REIMPOSTA PIPELINE ↻' : `PROSSIMA: FASE 0${stageNum + 1} →`;
            }
        }"""

    html = html.replace(old_sim_code, new_sim_code)

    # 20. JavaScript: AI Chat Response Generator (Italian Knowledge Base)
    old_ai_code = """        function appendMessage(sender, text) {
            const formattedHTML = text.replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');

            if (!chatStream) return;
            const b = document.createElement('div');
            b.className = 'chat-bubble';
            const auth = document.createElement('div');
            auth.className = `bubble-author ${sender === 'ai' ? 'renzo' : 'user'}`;
            auth.innerText = sender === 'ai' ? 'Renzo Francesqui • AI Representative' : 'Inquiry';
            const body = document.createElement('div');
            body.className = 'bubble-body';
            body.innerHTML = formattedHTML;
            b.appendChild(auth);
            b.appendChild(body);
            chatStream.appendChild(b);
            chatStream.scrollTop = chatStream.scrollHeight;
        }

        function getChatResponse(q) {
            const query = q.toLowerCase();
            if (query.includes('hubspot') || query.includes('crm')) {
                return "My **HubSpot CRM Experience** spans over 5 years across platform administration, schema design, and pipeline operations. At TOMRA, I co-led the HubSpot buildout for 30–50 sales reps in EMEA and Americas. At IMBAREX, I standardized property schemas across 10+ countries. I hold certifications in **HubSpot CRM Administration**, **RevOps**, and **Marketing Automation**.";
            }
            if (query.includes('salesforce')) {
                return "I am currently **preparing for and actively pursuing the Salesforce Administrator certification** to expand multi-CRM interoperability alongside my 5+ years of advanced HubSpot administration.";
            }
            if (query.includes('automation') || query.includes('agent') || query.includes('ai') || query.includes('python')) {
                return "I design and orchestrate **AI marketing automation workflows** using tools like Google Antigravity, LLM prompt architectures, and HubSpot webhooks. My **Automated CRM Enrichment Agent** extracts domain insights and classifies firmographics against ICP criteria in under 30 seconds, saving 15+ hours weekly.";
            }
            if (query.includes('tomra') || query.includes('current') || query.includes('job') || query.includes('work')) {
                return "I currently work at **TOMRA** in Parma, Italy, as **Marketing Events Support | CRM & Marketing Operations** (since October 2024), managing lead capture operations for 15–20 global exhibitions and building lead scoring logic.";
            }
            if (query.includes('locate') || query.includes('location') || query.includes('milan') || query.includes('parma') || query.includes('italy') || query.includes('emea')) {
                return "I am based in **Milano (Milan) / Parma, Italy**, holding a valid Italian work permit. I am open to hybrid or remote roles across EMEA. For roles outside Italy, I require visa sponsorship.";
            }
            if (query.includes('cert') || query.includes('degree') || query.includes('master') || query.includes('sql') || query.includes('education')) {
                return "I hold a **Master's in International Business & Development** from *Università degli Studi di Parma*. Certifications completed: **HubSpot CRM Administration, RevOps, Marketing Automation, Google Digital Marketing, Meta Associate**. Currently in progress (2026): **Salesforce Administrator** and **SQL Oracle Database**.";
            }
            if (query.includes('gtm') || query.includes('pisonay')) {
                return "At **The Pisonay Company**, I led the **Go-To-Market (GTM)** execution across SEO/SEM, email automations, and CRM workflows for high-value developments, achieving a 100% inventory sell-out before project completion.";
            }
            if (query.includes('skill') || query.includes('seo') || query.includes('sem') || query.includes('ads') || query.includes('analytics')) {
                return "My skills span 6 core areas: **CRM Architecture** (HubSpot CRM), **Marketing Operations** (Lifecycle SLAs, Lead Scoring), **AI Marketing Automation** (Google Antigravity, Webhooks), **Performance Marketing** (Google Ads, Meta Ads, LinkedIn), **Technical SEO** (+40% organic growth), and **Analytics / BI** (GA4, SQL, KPI dashboards). Check the **Skills** orb!";
            }
            return "I am Renzo's AI representative, trained exclusively by him on his 5+ years of experience across HubSpot architectures, B2B marketing operations, and AI marketing automation workflows. Ask me anything or explore the 3D celestial matrix!";
        }"""

    new_ai_code = """        function appendMessage(sender, text) {
            const formattedHTML = text.replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');

            if (!chatStream) return;
            const b = document.createElement('div');
            b.className = 'chat-bubble';
            const auth = document.createElement('div');
            auth.className = `bubble-author ${sender === 'ai' ? 'renzo' : 'user'}`;
            auth.innerText = sender === 'ai' ? 'Renzo Francesqui • Rappresentante AI' : 'Richiesta';
            const body = document.createElement('div');
            body.className = 'bubble-body';
            body.innerHTML = formattedHTML;
            b.appendChild(auth);
            b.appendChild(body);
            chatStream.appendChild(b);
            chatStream.scrollTop = chatStream.scrollHeight;
        }

        function getChatResponse(q) {
            const query = q.toLowerCase();
            if (query.includes('hubspot') || query.includes('crm')) {
                return "La mia **Esperienza con HubSpot CRM** supera i 5 anni di amministrazione avanzata, progettazione schemi dati e gestione delle pipeline. In TOMRA ho co-guidato l'adozione e standardizzazione di HubSpot per 30–50 commerciali in EMEA e Americhe. In IMBAREX ho standardizzato le proprietà per oltre 10 paesi. Possiedo certificazioni in **HubSpot CRM Administration**, **Revenue Operations (RevOps)** e **Marketing Automation**.";
            }
            if (query.includes('salesforce')) {
                return "Attualmente sto **studiando e preparando attivamente la certificazione Salesforce Administrator**, per consolidare l'interoperabilità multi-CRM e l'integrazione di sistemi enterprise accanto ai miei oltre 5 anni di specializzazione su HubSpot.";
            }
            if (query.includes('automazione') || query.includes('automation') || query.includes('agent') || query.includes('ai') || query.includes('workflow')) {
                return "Progetto e implemento **workflow di automazione di marketing basati su AI** utilizzando strumenti come Google Antigravity, architetture di prompt LLM e webhook HubSpot. Il mio **Agente Automatico di Arricchimento CRM** estrae informazioni sui domini e classifica la firmografica rispetto all'ICP in meno di 30 secondi, risparmiando oltre 15 ore settimanali.";
            }
            if (query.includes('tomra') || query.includes('ruolo') || query.includes('lavoro') || query.includes('attuale')) {
                return "Attualmente lavoro presso **TOMRA** a Parma, Italia, come **Marketing Events Support | CRM & Marketing Operations** (da ottobre 2024), gestendo le operazioni di lead generation fieristica per 15–20 esposizioni internazionali all'anno e strutturando logiche di lead scoring.";
            }
            if (query.includes('sede') || query.includes('milano') || query.includes('parma') || query.includes('italia') || query.includes('disponibil') || query.includes('dove')) {
                return "Ho sede tra **Milano e Parma, Italia**, con regolare permesso di lavoro UE. Sono disponibile per opportunità in modalità **ibrida o full-remote** in tutta l'area EMEA.";
            }
            if (query.includes('certificazion') || query.includes('laurea') || query.includes('master') || query.includes('studio') || query.includes('formazione') || query.includes('sql')) {
                return "Ho conseguito una **Laurea Magistrale in International Business & Development** presso l'Università degli Studi di Parma. Certificazioni completate: **HubSpot CRM Administration, RevOps, Marketing Automation, Google Digital Marketing, Meta Associate**. In corso (2026): **Salesforce Administrator** e **Database SQL Oracle**.";
            }
            if (query.includes('gtm') || query.includes('pisonay') || query.includes('go-to-market')) {
                return "Presso **The Pisonay Company**, ho guidato l'esecuzione della strategia **Go-To-Market (GTM)** attraverso canali SEO/SEM, email automation e workflow CRM per progetti immobiliari di alto valore, ottenendo il 100% di sell-out prima del completamento dei lavori.";
            }
            if (query.includes('competenze') || query.includes('skill') || query.includes('seo') || query.includes('sem') || query.includes('ads') || query.includes('analytics')) {
                return "Le mie competenze principali coprono 6 pilastri strategici: **Architettura CRM** (HubSpot), **Marketing Operations & SLA** (MQL-to-SQL), **Automazione Marketing AI** (Google Antigravity, Webhook), **Performance Marketing** (Google Ads, Meta, LinkedIn), **SEO Tecnico** (+40% traffico organico) e **Analytics / BI** (GA4, SQL, Dashboard Direzionali). Esplora l'orbe **Competenze** per maggiori dettagli!";
            }
            return "Sono il rappresentante AI ufficiale di Renzo Francesqui, addestrato sui suoi oltre 5 anni di esperienza tra architettura CRM HubSpot, operazioni di marketing B2B e flussi di automazione AI. Fai pure una domanda o esplora la matrice 3D!";
        }"""

    html = html.replace(old_ai_code, new_ai_code)

    with open(IT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Successfully generated {IT_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    build_italian_page()
