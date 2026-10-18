#!/usr/bin/env python3
"""
Generate Minimalist Editorial Tool Landing Pages (EN & IT).
Builds the 3 standalone B2B Interactive Tool Pages linked from #modalTools:
1. /tools/mql-to-sql-sla-lead-leakage-calculator/index.html
2. /tools/b2b-campaign-utm-crm-builder/index.html
3. /tools/b2b-trade-show-roi-calculator/index.html
and their Italian localized counterparts in /it/tools/.../index.html.

Strict Minimalist Editorial Design System:
- 840px Centered Editorial Column.
- Hairline borders (rgba(255, 255, 255, 0.08)) and Warm Champagne Gold (#d4a863) accent.
- Sticky Minimalist HUD Header with Solar Matrix return, Tool Switcher pills, and EN/IT language toggle.
- Hero Section: Monospace eyebrow with live pulse dot, H1 title, AI-extractable definition lead paragraph, 3-metric strip.
- Live Interactive Tool Workspace: fully responsive, zero-dependency widget with real-time calculations.
- Diagnostic Contrast Table (Manual Ad-Hoc Process vs. Governed RevOps Protocol).
- Four-Stage Architectural Methodology (Orbital timeline with stage cards and pills).
- Executive CTA Console with Calendly booking, email inquiry, and 3D Matrix return.
- Full SEO metadata, canonicals, hreflang, Open Graph, Twitter Cards, and Schema.org WebApplication + WebPage + BreadcrumbList JSON-LD.
"""

from pathlib import Path
import json
import urllib.parse

BASE_DIR = Path(__file__).resolve().parent.parent

TOOLS_DATA = [
    {
        "id": "sla_calculator",
        "slug": "mql-to-sql-sla-lead-leakage-calculator",
        "tool_num": "01",
        "pill_label_en": "01 Leakage Calculator",
        "pill_label_it": "01 Calcolatore Leakage",
        "tool_name_en": "MQL-to-SQL SLA & Pipeline Lead Leakage Calculator",
        "tool_name_it": "Calcolatore SLA MQL-to-SQL & Dispersione Pipeline",

        # Meta & Titles (<60 chars title, <160 chars desc)
        "meta_title_en": "MQL-to-SQL SLA & Leakage Calculator | Francesqui",
        "meta_title_it": "Calcolatore SLA MQL-to-SQL & Leakage | Francesqui",
        "meta_desc_en": "Calculate B2B pipeline leakage from sales follow-up latency. Measure lost revenue and conversion lift from automated sub-5-minute HubSpot SLA routing.",
        "meta_desc_it": "Calcola la dispersione di pipeline B2B causata dalla latenza commerciale. Misura il fatturato perso e il lift di conversione con SLA sub-5-min su HubSpot.",

        # Hero
        "eyebrow_en": "TOOL 01 // REVOPS PIPELINE TELEMETRY",
        "eyebrow_it": "TOOL 01 // TELEMETRIA PIPELINE REVOPS",
        "hero_title_en": "MQL-to-SQL SLA & Lead Leakage Calculator for B2B Teams.",
        "hero_title_it": "Calcolatore SLA MQL-to-SQL & Dispersione Lead per Team B2B.",
        "hero_lead_en": "Quantify exactly how sales follow-up response latency bleeds qualified pipeline. Fast routing under 5 minutes delivers up to an 8x increase in lead-to-opportunity conversion velocity compared to manual spreadsheet distribution.",
        "hero_lead_it": "Quantifica esattamente come i tempi lenti di risposta commerciale disperdono il valore della pipeline. Il routing automatizzato sotto i 5 minuti moltiplica fino a 8 volte le conversioni da lead a opportunità rispetto alla gestione manuale.",

        # Hairline Metrics Strip (3 metrics)
        "metrics_en": [
            {"val": "< 5 Min", "label": "Target Inbound Routing SLA"},
            {"val": "75%", "label": "Lead Drop-Off Latency >48h"},
            {"val": "+775%", "label": "Potential Conversion Lift"}
        ],
        "metrics_it": [
            {"val": "< 5 Min", "label": "SLA Routing Inbound Ottimale"},
            {"val": "75%", "label": "Dispersione per Risposta >48h"},
            {"val": "+775%", "label": "Incremento Massimo di Conversione"}
        ],

        # Contrast Grid: Diagnostic Section
        "contrast_col1_header_en": "MANUAL SPREADSHEET ROUTING (>48H)",
        "contrast_col1_header_it": "GESTIONE MANUALE SU FOGLI (>48H)",
        "contrast_col1_items_en": [
            "Leads sit untouched in CSV files over weekends before rep assignment.",
            "Prospect intent decays by 80% after the first 24 hours of silence.",
            "No accountability: sales reps cherry-pick easy leads while high-intent MQLs decay.",
            "Manual round-robin creates unequal lead distribution and broken attribution."
        ],
        "contrast_col1_items_it": [
            "I lead restano intoccati nei file CSV durante i weekend prima di essere assegnati.",
            "L'intenzione d'acquisto del prospect decade dell'80% dopo le prime 24 ore di silenzio.",
            "Nessuna responsabilità: i commerciali scelgono a vista i lead facili lasciando scadere gli MQL.",
            "La rotazione manuale genera distribuzione disomogenea e tracciamenti interrotti."
        ],
        "contrast_col2_header_en": "ENGINEERED 0-LATENCY REVOPS SLA (<5 MIN)",
        "contrast_col2_header_it": "SLA REVOPS A 0 LATENZA (<5 MIN)",
        "contrast_col2_items_en": [
            "Instant webhook & API ingestion into HubSpot with territory-based routing under 5 minutes.",
            "Automated multi-channel alerts (Slack, SMS, CRM task) triggered instantly upon form submit.",
            "Enforced SLA timeouts: uncontacted leads auto-escalate to sales managers after 30 minutes.",
            "Predictable conversion lift: up to 8x higher lead-to-SQL qualification rate."
        ],
        "contrast_col2_items_it": [
            "Ingestione istantanea via webhook e API su HubSpot con routing per territorio sotto i 5 minuti.",
            "Notifiche multicanale automatiche (Slack, SMS, task CRM) all'invio del modulo.",
            "Timeout SLA vincolanti: i lead non contattati scalano automaticamente al responsabile dopo 30 minuti.",
            "Incremento prevedibile: fino a 8 volte più conversioni da MQL a SQL qualificato."
        ],

        # Methodology Stages
        "stages_en": [
            {
                "num": "01",
                "title": "Ingestion Architecture & Deduplication",
                "summary": "Building resilient webhook gateways that clean, normalize, and deduplicate inbound leads before CRM write operations.",
                "pills": ["API Webhooks", "Contact Deduplication", "Property Mapping", "Data Normalization"]
            },
            {
                "num": "02",
                "title": "Intelligent Territory & Round-Robin Routing",
                "summary": "Automating rep distribution logic based on ICP fit, company headcount, geographic territory, and rep availability.",
                "pills": ["HubSpot Routing", "Round-Robin Queues", "Territory Governance", "Capacity Balancing"]
            },
            {
                "num": "03",
                "title": "Automated SLA Escalations & Alerts",
                "summary": "Deploying zero-latency Slack bot alerts with one-click dialer actions and automated manager re-routing upon SLA breach.",
                "pills": ["Slack Webhooks", "SLA Timers", "Escalation Triggers", "Task Automation"]
            },
            {
                "num": "04",
                "title": "Pipeline Velocity & Conversion Telemetry",
                "summary": "Tracking speed-to-lead latency against win rate and deal velocity to identify friction points across sales stages.",
                "pills": ["Time-to-First-Touch", "MQL-to-SQL Velocity", "Rep Compliance", "Executive Dashboards"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Architettura di Ingestione & Deduplica",
                "summary": "Costruzione di gateway webhook affidabili che puliscono, normalizzano e deduplicano i lead inbound prima della scrittura a CRM.",
                "pills": ["Webhook API", "Deduplica Contatti", "Mappatura Proprietà", "Normalizzazione Dati"]
            },
            {
                "num": "02",
                "title": "Routing Intelligente per Territorio & Rotazione",
                "summary": "Automazione dell'assegnazione commerciale in base al fit ICP, dimensione azienda, area geografica e disponibilità.",
                "pills": ["Routing HubSpot", "Code a Rotazione", "Governance Territori", "Bilanciamento Carichi"]
            },
            {
                "num": "03",
                "title": "Alert & Escalation Automatiche per SLA",
                "summary": "Attivazione di avvisi Slack istantanei con chiamate one-click e riassegnazione automatica al manager in caso di violazione SLA.",
                "pills": ["Webhook Slack", "Timer SLA", "Trigger Escalation", "Task Automatici"]
            },
            {
                "num": "04",
                "title": "Velocità di Pipeline & Telemetria di Conversione",
                "summary": "Monitoraggio del tempo di primo contatto correlato al tasso di chiusura e alla velocità di trattativa per eliminare i colli di bottiglia.",
                "pills": ["Tempo Primo Contatto", "Velocità MQL-to-SQL", "Compliance Commerciale", "Dashboard Direzionali"]
            }
        ],

        "cta_heading_en": "Ready to eliminate pipeline leakage in your CRM?",
        "cta_heading_it": "Pronto a eliminare la dispersione della pipeline nel tuo CRM?",
        "cta_sub_en": "Book a strategic RevOps architecture audit to design automated sub-5-minute routing and SLA governance in HubSpot.",
        "cta_sub_it": "Prenota un audit architetturale RevOps per progettare routing automatizzato sotto i 5 minuti e governance SLA su HubSpot.",
        "tool_subject_en": "Consulting Inquiry — MQL-to-SQL SLA & Lead Leakage Calculator",
        "tool_subject_it": "Richiesta Consulenza — Calcolatore SLA MQL-to-SQL & Dispersione Pipeline"
    },

    {
        "id": "utm_builder",
        "slug": "b2b-campaign-utm-crm-builder",
        "tool_num": "02",
        "pill_label_en": "02 UTM Builder",
        "pill_label_it": "02 Builder UTM",
        "tool_name_en": "B2B Campaign UTM & CRM Governance Builder",
        "tool_name_it": "Builder Tassonomia UTM B2B & Governance CRM",

        # Meta & Titles (<60 chars title, <160 chars desc)
        "meta_title_en": "B2B Campaign UTM & CRM Builder | Francesqui",
        "meta_title_it": "Builder UTM Campagne B2B & CRM | Francesqui",
        "meta_desc_en": "Generate governed B2B campaign UTM parameters and clean JSON payloads for hidden HubSpot and Salesforce CRM form fields to eliminate attribution drift.",
        "meta_desc_it": "Genera parametri UTM con governance per campagne B2B e JSON puliti per campi modulo nascosti HubSpot e Salesforce, eliminando errori di attribuzione.",

        # Hero
        "eyebrow_en": "TOOL 02 // CAMPAIGN ATTRIBUTION GOVERNANCE",
        "eyebrow_it": "TOOL 02 // GOVERNANCE ATTRIBUZIONE CAMPAGNE",
        "hero_title_en": "B2B Campaign UTM & CRM Hidden Form Parameter Builder.",
        "hero_title_it": "Builder UTM per Campagne B2B & Parametri Modulo CRM Nascosti.",
        "hero_lead_en": "Enforce strict parameter casing, taxonomy standards, and hidden CRM ingestion properties across paid acquisition channels. Eliminate uppercase casing mismatches, attribution drift, and orphan conversion records in HubSpot and Salesforce.",
        "hero_lead_it": "Applica standard rigorosi di nomenclatura e tassonomia per i parametri UTM e la cattura dati CRM. Elimina discrepanze di formattazione, dispersioni di attribuzione e contatti orfani in HubSpot e Salesforce.",

        # Hairline Metrics Strip (3 metrics)
        "metrics_en": [
            {"val": "100%", "label": "Taxonomy Standardization"},
            {"val": "Zero", "label": "Unmapped Ad Spend Attribution"},
            {"val": "4 Keys", "label": "Governed CRM Ingestion Payload"}
        ],
        "metrics_it": [
            {"val": "100%", "label": "Standardizzazione Tassonomia"},
            {"val": "Zero", "label": "Spesa Adv Non Attribuita"},
            {"val": "4 Chiavi", "label": "Payload Ingestione CRM Strutturato"}
        ],

        # Contrast Grid: Diagnostic Section
        "contrast_col1_header_en": "CHAOTIC AD-HOC URL TRACKING",
        "contrast_col1_header_it": "TRACCIAMENTO AD-HOC DISORDINATO",
        "contrast_col1_items_en": [
            "Inconsistent casing (e.g., 'LinkedIn', 'linkedin', 'IN') splits ad analytics across dozens of rows.",
            "Spaces, special characters, and typos corrupt query parameters and break tracking.",
            "UTM parameters lost upon form submission; CRM records display zero source attribution.",
            "Paid ad spend cannot be matched to closed-won deals in HubSpot or Salesforce."
        ],
        "contrast_col1_items_it": [
            "Maiuscole/minuscole incoerenti (es. 'LinkedIn', 'linkedin', 'IN') frammentano i report in decine di righe.",
            "Spazi, caratteri speciali ed errori di digitazione corrompono i parametri e bloccano il tracciamento.",
            "Parametri UTM persi all'invio dei moduli; i record CRM registrano sorgente sconosciuta.",
            "La spesa pubblicitaria non può essere collegata alle trattative vinte su HubSpot o Salesforce."
        ],
        "contrast_col2_header_en": "GOVERNED CRM TAXONOMY ARCHITECTURE",
        "contrast_col2_header_it": "ARCHITETTURA TASSONOMIA CRM GOVERNATA",
        "contrast_col2_items_en": [
            "Strict lowercase underscore-delimited taxonomy enforced automatically across all links.",
            "Standardized source and medium pairings validated against enterprise taxonomy tables.",
            "Hidden form fields capture First-Touch and Last-Touch parameters on every conversion.",
            "Direct sync into CRM custom properties for accurate multi-touch and pipeline attribution."
        ],
        "contrast_col2_items_it": [
            "Tassonomia rigorosa in minuscolo con separatore underscore applicata automaticamente a ogni link.",
            "Coppie sorgente/mezzo standardizzate e convalidate rispetto a dizionari aziendali controllati.",
            "Campi modulo nascosti catturano First-Touch e Last-Touch ad ogni compilazione.",
            "Sincronizzazione diretta su proprietà personalizzate CRM per reportistica multi-touch e attribuzione di ricavi."
        ],

        # Methodology Stages
        "stages_en": [
            {
                "num": "01",
                "title": "Enterprise Taxonomy Standard Definition",
                "summary": "Establishing standardized source, medium, campaign, and content dictionaries across paid media and organic campaigns.",
                "pills": ["Naming Conventions", "Channel Governance", "UTM Dictionary", "Case Sanitization"]
            },
            {
                "num": "02",
                "title": "Hidden Form Field Capture Architecture",
                "summary": "Configuring web forms to extract URL parameters and store them into browser cookies and hidden form inputs.",
                "pills": ["Hidden Fields", "Cookie Persistence", "HubSpot Forms", "First vs Last Touch"]
            },
            {
                "num": "03",
                "title": "CRM Custom Property & Object Mapping",
                "summary": "Creating dedicated custom properties in HubSpot and Salesforce to store channel attribution on Contact, Company, and Deal levels.",
                "pills": ["Contact Properties", "Deal Attribution", "Salesforce Schema", "Original Source"]
            },
            {
                "num": "04",
                "title": "Closed-Loop Revenue Reporting",
                "summary": "Connecting ad platform spend with CRM deal pipeline to produce true ROAS, Customer Acquisition Cost (CAC), and pipeline velocity.",
                "pills": ["Closed-Loop BI", "ROAS Modeling", "Looker Studio", "Multi-Touch Models"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Definizione Standard di Tassonomia Aziendale",
                "summary": "Creazione di dizionari controllati per sorgente, mezzo, campagna e contenuto su tutti i canali paid e organici.",
                "pills": ["Convenzioni Naming", "Governance Canali", "Dizionario UTM", "Sanitizzazione Testo"]
            },
            {
                "num": "02",
                "title": "Cattura Parametri tramite Campi Nascosti",
                "summary": "Configurazione dei moduli web per estrarre i parametri URL e salvarli nei cookie e nei campi nascosti del form.",
                "pills": ["Campi Nascosti", "Persistenza Cookie", "Moduli HubSpot", "First vs Last Touch"]
            },
            {
                "num": "03",
                "title": "Mappatura Proprietà & Oggetti Personalizzati CRM",
                "summary": "Creazione di proprietà dedicate in HubSpot e Salesforce per registrare l'attribuzione a livello di Contatto, Azienda e Trattativa.",
                "pills": ["Proprietà Contatto", "Attribuzione Deal", "Schema Salesforce", "Sorgente Originale"]
            },
            {
                "num": "04",
                "title": "Reportistica di Attribuzione a Ciclo Chiuso",
                "summary": "Unione della spesa pubblicitaria con il valore delle trattative CRM per calcolare ROAS reale, CAC e velocità di pipeline.",
                "pills": ["BI a Ciclo Chiuso", "Modelli ROAS", "Looker Studio", "Modelli Multi-Touch"]
            }
        ],

        "cta_heading_en": "Need enterprise campaign governance for your CRM?",
        "cta_heading_it": "Serve una governance di tracciamento enterprise per il tuo CRM?",
        "cta_sub_en": "Book a campaign taxonomy and CRM tracking architecture consultation to eliminate attribution blind spots.",
        "cta_sub_it": "Prenota una consulenza sull'architettura di tracciamento e tassonomia CRM per eliminare le zone d'ombra nell'attribuzione.",
        "tool_subject_en": "Consulting Inquiry — B2B Campaign UTM & CRM Governance Builder",
        "tool_subject_it": "Richiesta Consulenza — Builder Tassonomia UTM B2B & Governance CRM"
    },

    {
        "id": "tradeshow_roi",
        "slug": "b2b-trade-show-roi-calculator",
        "tool_num": "03",
        "pill_label_en": "03 Trade Show ROI",
        "pill_label_it": "03 ROI Fiere B2B",
        "tool_name_en": "B2B Trade Show & Exhibition ROI Modeler",
        "tool_name_it": "Modello & Calcolatore ROI Fiere B2B",

        # Meta & Titles (<60 chars title, <160 chars desc)
        "meta_title_en": "B2B Trade Show & Event ROI Calculator | Francesqui",
        "meta_title_it": "Calcolatore ROI Fiere & Stand B2B | Francesqui",
        "meta_desc_en": "Calculate B2B trade show ROI, qualified cost per opportunity, and hours saved with automated badge-to-HubSpot CRM synchronization. Modeled on IFAT & PRS.",
        "meta_desc_it": "Calcola il ROI delle fiere B2B, il costo per SQL qualificato e le ore risparmiate con la sincronizzazione automatica badge-CRM HubSpot. Basato su IFAT e PRS.",

        # Hero
        "eyebrow_en": "TOOL 03 // FIELD MARKETING & EVENT PIPELINE",
        "eyebrow_it": "TOOL 03 // FIELD MARKETING & PIPELINE FIERE",
        "hero_title_en": "B2B Trade Show & Exhibition Financial ROI Modeler.",
        "hero_title_it": "Modello Finanziario & Calcolatore ROI per Fiere B2B.",
        "hero_lead_en": "Transform trade show sponsorship from an unaccountable marketing expense into a predictable pipeline generator. Calculate your cost per qualified opportunity, projected event ROAS, and admin hours saved through instant badge-to-CRM automation.",
        "hero_lead_it": "Trasforma la partecipazione fieristica da spesa non quantificabile a motore prevedibile di pipeline. Calcola il costo per opportunità qualificata, il ROAS previsto dell'evento e le ore risparmiate tramite l'automazione diretta badge-CRM.",

        # Hairline Metrics Strip (3 metrics)
        "metrics_en": [
            {"val": "Full Funnel", "label": "Attributed Event Pipeline"},
            {"val": "< 60s", "label": "Badge-to-HubSpot Sync SLA"},
            {"val": "30-50h", "label": "Admin Spreadsheet Time Saved"}
        ],
        "metrics_it": [
            {"val": "Full Funnel", "label": "Pipeline Fieristica Attribuita"},
            {"val": "< 60s", "label": "SLA Sincronizzazione Badge-CRM"},
            {"val": "30-50h", "label": "Ore Manuali su Fogli Salvate"}
        ],

        # Contrast Grid: Diagnostic Section
        "contrast_col1_header_en": "DISCONNECTED EVENT EXPENSE",
        "contrast_col1_header_it": "SPESA FIERISTICA DISCONNESSA",
        "contrast_col1_items_en": [
            "Paper business cards and badge scanner CSVs sit uncontacted for 2+ weeks post-show.",
            "Sales reps manually transcribe badge scans, losing context and critical conversation notes.",
            "No tracking of event-sourced pipeline; trade shows written off as untrackable 'brand spend'.",
            "High cost-per-lead with zero visibility into actual closed-won customer revenue."
        ],
        "contrast_col1_items_it": [
            "Biglietti da visita cartacei ed export CSV dello scanner restano fermi per oltre 2 settimane dopo l'evento.",
            "I commerciali trascrivono manualmente i contatti, perdendo contesto e note fondamentali.",
            "Nessun tracciamento della pipeline generata; le fiere vengono etichettate come spesa di 'brand awareness'.",
            "Costo per lead elevato con totale assenza di visibilità sulle trattative effettivamente vinte."
        ],
        "contrast_col2_header_en": "ATTRIBUTED EXHIBITION PIPELINE ENGINE",
        "contrast_col2_header_it": "MOTORE DI PIPELINE FIERISTICA ATTRIBUITO",
        "contrast_col2_items_en": [
            "Automated badge-to-HubSpot sync via OCR/API ingestion within 60 seconds of booth scan.",
            "Contextual follow-up email triggered while the prospect is still on the trade show floor.",
            "Automatic ICP qualification, tier tagging, and instant rep account assignment.",
            "Full-funnel attribution: event campaign tagged to all pipeline deals created within 90 days."
        ],
        "contrast_col2_items_it": [
            "Sincronizzazione badge-HubSpot automatizzata via OCR/API entro 60 secondi dalla scansione allo stand.",
            "Email di follow-up contestualizzata inviata mentre il prospect sta ancora visitando i padiglioni.",
            "Qualificazione ICP automatica, assegnazione priorità e distribuzione istantanea al commerciale.",
            "Attribuzione full-funnel: campagna fieristica associata a tutte le trattative generate entro 90 giorni."
        ],

        # Methodology Stages
        "stages_en": [
            {
                "num": "01",
                "title": "Pre-Show Tech Stack Integration",
                "summary": "Connecting trade show badge scanner APIs or mobile OCR tools directly with HubSpot CRM custom objects.",
                "pills": ["Scanner API", "Mobile OCR Webhook", "HubSpot Properties", "Booth Playbook"]
            },
            {
                "num": "02",
                "title": "Real-Time Ingestion & ICP Enrichment",
                "summary": "Enriching company domain, revenue band, and buyer persona in real-time as badges are scanned at the booth.",
                "pills": ["Instant Enrichment", "ICP Tier Tagging", "Booth Note Sync", "Deduplication"]
            },
            {
                "num": "03",
                "title": "Automated Same-Day Nurture Sequences",
                "summary": "Triggering dynamic email follow-ups with relevant case studies while the prospect's memory is fresh.",
                "pills": ["Dynamic Templates", "Same-Day Follow-Up", "Rep Signature Routing", "Meeting Scheduling"]
            },
            {
                "num": "04",
                "title": "Exhibition ROAS & Pipeline Velocity Tracking",
                "summary": "Tracking deal progression over 6-12 month sales cycles to measure true return on event marketing investment.",
                "pills": ["Event Campaign Attribution", "Qualified Cost per SQL", "ROAS Multipliers", "Board Dashboards"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Integrazione Stack Tecnologico Pre-Fiera",
                "summary": "Collegamento delle API dello scanner o app OCR per badge direttamente con le proprietà personalizzate di HubSpot.",
                "pills": ["API Scanner", "Webhook OCR Mobile", "Proprietà HubSpot", "Playbook Stand"]
            },
            {
                "num": "02",
                "title": "Ingestione in Tempo Reale & Arricchimento ICP",
                "summary": "Arricchimento del dominio aziendale, fatturato e profilo buyer persona in tempo reale durante la scansione allo stand.",
                "pills": ["Arricchimento Dati", "Classificazione ICP", "Sincronizzazione Note", "Deduplica"]
            },
            {
                "num": "03",
                "title": "Sequenze di Nurturing Automatizzate Same-Day",
                "summary": "Invio di email di follow-up dinamiche con case study mirati mentre il ricordo dell'incontro allo stand è ancora vivido.",
                "pills": ["Template Dinamici", "Follow-Up in Giornata", "Firma Commerciale", "Link Calendly"]
            },
            {
                "num": "04",
                "title": "Monitoraggio ROAS Fieristico & Velocità Trattative",
                "summary": "Monitoraggio della progressione dei deal su cicli commerciali complessi di 6-12 mesi per misurare il ritorno reale dell'evento.",
                "pills": ["Attribuzione Campagna Fiera", "Costo per SQL Qualificato", "Moltiplicatori ROAS", "Report Direzione"]
            }
        ],

        "cta_heading_en": "Planning your next major B2B trade show or exhibition?",
        "cta_heading_it": "Stai pianificando la prossima fiera o stand B2B?",
        "cta_sub_en": "Book an event RevOps architecture audit to design automated badge-to-CRM ingestion and full-funnel attribution.",
        "cta_sub_it": "Prenota un audit architetturale RevOps per progettare l'ingestione automatizzata badge-CRM e l'attribuzione full-funnel dei ricavi.",
        "tool_subject_en": "Consulting Inquiry — B2B Trade Show & Exhibition ROI Modeler",
        "tool_subject_it": "Richiesta Consulenza — Modello & Calcolatore ROI Fiere B2B"
    }
]

MASTER_CSS = """
:root {
    --bg-deep: #030204;
    --bg-surface: rgba(15, 12, 18, 0.72);
    --bg-surface-elevated: rgba(22, 18, 28, 0.85);
    --bg-subtle: rgba(255, 255, 255, 0.025);
    --bg-active: rgba(212, 168, 99, 0.12);
    
    --accent-gold: #d4a863;
    --accent-gold-soft: rgba(212, 168, 99, 0.35);
    --accent-emerald: #34d399;
    --accent-cyan: #38bdf8;
    --accent-purple: #a78bfa;
    --accent-rose: #fb7185;
    
    --text-primary: #fcfbf9;
    --text-secondary: #a8a197;
    --text-muted: #6e675d;
    
    --border-hairline: rgba(255, 255, 255, 0.08);
    --border-gold: rgba(212, 168, 99, 0.45);
    --border-glass: rgba(255, 255, 255, 0.12);
    
    --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
}

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    background-color: var(--bg-deep);
    color: var(--text-primary);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
    scroll-behavior: smooth;
}

body {
    min-height: 100vh;
    overflow-x: hidden;
    background: 
        radial-gradient(circle at 50% 0%, rgba(212, 168, 99, 0.07) 0%, transparent 55%),
        var(--bg-deep);
    line-height: 1.65;
}

/* Sticky Minimalist HUD Header */
.nav-Wrapper {
    position: sticky;
    top: 1.25rem;
    z-index: 100;
    padding: 0 1.5rem;
    margin-bottom: 5rem;
}

.hud-header {
    max-width: 960px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-surface);
    backdrop-filter: blur(32px) saturate(180%);
    -webkit-backdrop-filter: blur(32px) saturate(180%);
    border: 1px solid var(--border-hairline);
    border-radius: 9999px;
    padding: 0.6rem 1.25rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}

.back-link {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-secondary);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: color 0.2s var(--ease-out);
}

.back-link:hover {
    color: var(--accent-gold);
}

.tool-switcher {
    display: flex;
    align-items: center;
    gap: 0.25rem;
}

.switch-pill {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--text-muted);
    text-decoration: none;
    padding: 0.35rem 0.75rem;
    border-radius: 9999px;
    border: 1px solid transparent;
    transition: all 0.2s var(--ease-out);
}

.switch-pill:hover {
    color: var(--text-primary);
}

.switch-pill.active {
    color: var(--accent-gold);
    background: var(--bg-active);
    border-color: var(--border-gold);
}

/* Centered Editorial Container */
.editorial-container {
    max-width: 840px;
    margin: 0 auto;
    padding: 0 1.5rem 7rem;
}

section {
    margin-bottom: 6rem;
}

/* 1. Hero Section */
.eyebrow-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-bottom: 1.25rem;
}

.eyebrow-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent-emerald);
    box-shadow: 0 0 8px var(--accent-emerald);
}

.hero-title {
    font-size: clamp(2rem, 4vw, 3.1rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.15;
    color: var(--text-primary);
    margin-bottom: 1.25rem;
}

.hero-lead {
    font-size: 1.08rem;
    color: var(--text-secondary);
    max-width: 680px;
    font-weight: 400;
    margin-bottom: 2.5rem;
}

/* Hairline Metrics Strip */
.metrics-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top: 1px solid var(--border-hairline);
    border-bottom: 1px solid var(--border-hairline);
    padding: 1.5rem 0;
    gap: 1.5rem;
}

.metric-item {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
}

.metric-value {
    font-family: var(--font-mono);
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-primary);
}

.metric-label {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-muted);
}

/* Section Headers */
.section-index {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-bottom: 0.5rem;
    display: block;
}

.section-heading {
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin-bottom: 2rem;
    color: var(--text-primary);
}

/* 2. Interactive Tool Workspace Card */
.tool-workspace-card {
    background: rgba(15, 12, 18, 0.72);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(212, 168, 99, 0.32);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 24px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(212, 168, 99, 0.05);
}

.tool-grid-layout {
    display: grid;
    grid-template-columns: 1.12fr 1fr;
    gap: 1.5rem;
    align-items: start;
}

.tool-inputs-card, .tool-results-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-hairline);
    border-radius: 16px;
    padding: 1.35rem;
}

.tool-input-group {
    margin-bottom: 1.15rem;
}

.tool-input-group:last-child {
    margin-bottom: 0;
}

.tool-label-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.45rem;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-primary);
}

.tool-input-label {
    display: block;
    margin-bottom: 0.45rem;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-primary);
}

.tool-val-display {
    font-family: var(--font-mono);
    font-size: 0.82rem;
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
    gap: 0.45rem;
    flex-wrap: wrap;
}

.tool-pill-option {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-hairline);
    border-radius: 8px;
    color: var(--text-secondary);
    font-size: 0.72rem;
    font-weight: 600;
    padding: 0.38rem 0.7rem;
    cursor: pointer;
    transition: all 0.2s var(--ease-out);
}

.tool-pill-option:hover {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.08);
}

.tool-pill-option.active {
    color: var(--accent-gold);
    background: var(--bg-active);
    border-color: var(--border-gold);
    box-shadow: 0 0 10px rgba(212, 168, 99, 0.2);
}

.tool-text-input {
    width: 100%;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid var(--border-hairline);
    border-radius: 8px;
    padding: 0.55rem 0.8rem;
    color: #ffffff;
    font-family: var(--font-sans);
    font-size: 0.8rem;
    outline: none;
    transition: border-color 0.2s;
    box-sizing: border-box;
}

.tool-text-input:focus {
    border-color: var(--accent-gold);
    box-shadow: 0 0 10px rgba(212, 168, 99, 0.25);
}

.tool-kpis-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.85rem;
    margin-bottom: 1.15rem;
}

.tool-kpi-card {
    border-radius: 14px;
    padding: 1.1rem 1.25rem;
    border: 1px solid;
    transition: transform 0.2s var(--ease-out);
}

.tool-kpi-card:hover {
    transform: translateY(-2px);
}

.tool-kpi-label {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.3rem;
}

.tool-kpi-num {
    font-family: var(--font-mono);
    font-size: 1.4rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 0.25rem;
}

.tool-kpi-sub {
    font-size: 0.74rem;
    color: var(--text-secondary);
    line-height: 1.35;
}

.tool-cta-wrapper {
    margin-top: 1rem;
}

.tool-cta-btn {
    width: 100%;
    background: linear-gradient(135deg, rgba(212, 168, 99, 0.2), rgba(6, 182, 212, 0.15));
    border: 1px solid var(--border-gold);
    border-radius: 9999px;
    color: #ffffff;
    font-family: var(--font-sans);
    font-size: 0.82rem;
    font-weight: 700;
    padding: 0.75rem 1.2rem;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.25s var(--ease-out);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.tool-cta-btn:hover {
    background: linear-gradient(135deg, rgba(212, 168, 99, 0.35), rgba(6, 182, 212, 0.3));
    box-shadow: 0 6px 20px rgba(212, 168, 99, 0.3);
    transform: translateY(-1px);
}

.terminal-block {
    background: rgba(0, 0, 0, 0.45);
    border: 1px solid var(--border-hairline);
    border-radius: 12px;
    overflow: hidden;
}

.terminal-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.45rem 0.85rem;
    background: rgba(255, 255, 255, 0.03);
    border-bottom: 1px solid var(--border-hairline);
}

.terminal-tag {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.08em;
    color: var(--accent-gold);
    text-transform: uppercase;
}

.terminal-copy-btn {
    background: rgba(212, 168, 99, 0.12);
    border: 1px solid rgba(212, 168, 99, 0.35);
    color: var(--accent-gold);
    font-family: var(--font-mono);
    font-size: 0.66rem;
    padding: 0.25rem 0.65rem;
    border-radius: 9999px;
    cursor: pointer;
    transition: all 0.2s;
}

.terminal-copy-btn:hover {
    background: var(--accent-gold);
    color: #050406;
}

.terminal-content {
    padding: 0.85rem;
    font-family: var(--font-mono);
    font-size: 0.72rem;
    line-height: 1.5;
    word-break: break-all;
}

/* 3. Minimalist Contrast Table (Before vs After) */
.contrast-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border: 1px solid var(--border-hairline);
    border-radius: 16px;
    overflow: hidden;
    background: var(--bg-subtle);
}

.contrast-col {
    padding: 2rem;
}

.contrast-col + .contrast-col {
    border-left: 1px solid var(--border-hairline);
    background: rgba(212, 168, 99, 0.02);
}

.contrast-header {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1.25rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--border-hairline);
}

.contrast-header.muted { color: var(--text-muted); }
.contrast-header.gold { color: var(--accent-gold); }

.contrast-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
    font-size: 0.88rem;
    color: var(--text-secondary);
}

.contrast-list li {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
}

.contrast-list li span.marker {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--text-muted);
    flex-shrink: 0;
}

.contrast-col + .contrast-col .contrast-list li {
    color: var(--text-primary);
}

.contrast-col + .contrast-col .contrast-list li span.marker {
    color: var(--accent-gold);
}

/* 4. Scroll-Driven Orbital Light Thread & Accordion Stages */
.orbital-timeline {
    position: relative;
    padding-left: 2.75rem;
}

.orbital-track-bg {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 7px;
    width: 1px;
    background: var(--border-hairline);
}

.orbital-track-fill {
    position: absolute;
    top: 0;
    left: 7px;
    width: 1px;
    height: 0%;
    background: linear-gradient(180deg, transparent, var(--accent-gold), #fff);
    transition: height 0.1s linear;
}

.orbital-node {
    position: absolute;
    left: 3px;
    top: 0%;
    width: 9px;
    height: 9px;
    background: var(--text-primary);
    border: 1.5px solid var(--accent-gold);
    transform: rotate(45deg);
    box-shadow: 0 0 14px var(--accent-gold);
    transition: top 0.1s linear;
    z-index: 2;
}

.stage-card {
    border: 1px solid var(--border-hairline);
    border-radius: 14px;
    background: var(--bg-subtle);
    padding: 1.5rem 1.75rem;
    margin-bottom: 1rem;
    cursor: pointer;
    transition: border-color 0.3s var(--ease-out), background 0.3s var(--ease-out);
}

.stage-card:hover,
.stage-card.active-stage {
    border-color: var(--border-gold);
    background: rgba(212, 168, 99, 0.035);
}

.stage-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}

.stage-meta {
    display: flex;
    align-items: baseline;
    gap: 0.85rem;
}

.stage-number {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--accent-gold);
}

.stage-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-primary);
}

.stage-toggle-icon {
    font-family: var(--font-mono);
    font-size: 0.85rem;
    color: var(--text-muted);
    transition: transform 0.3s var(--ease-out), color 0.3s;
}

.stage-card.open .stage-toggle-icon {
    transform: rotate(45deg);
    color: var(--accent-gold);
}

.stage-summary {
    font-size: 0.88rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
}

.stage-details {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.35s var(--ease-out), margin-top 0.35s var(--ease-out);
}

.stage-card.open .stage-details {
    max-height: 260px;
    margin-top: 1.25rem;
    padding-top: 1.15rem;
    border-top: 1px solid var(--border-hairline);
}

.deliverables-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.75rem;
}

.deliverable-pill {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--text-secondary);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-hairline);
    padding: 4px 10px;
    border-radius: 9999px;
}

/* 5. Minimalist Executive CTA Console */
.cta-console {
    border: 1px solid var(--border-gold);
    border-radius: 18px;
    padding: 2.5rem 2rem;
    background: linear-gradient(145deg, rgba(24, 19, 32, 0.7), rgba(10, 8, 14, 0.9));
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1.5rem;
}

.cta-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
}

.btn-gold {
    background: var(--accent-gold);
    color: #050406;
    font-family: var(--font-sans);
    font-size: 0.82rem;
    font-weight: 700;
    padding: 0.7rem 1.4rem;
    border-radius: 9999px;
    text-decoration: none;
    transition: opacity 0.2s, transform 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}

.btn-gold:hover {
    opacity: 0.92;
    transform: translateY(-1px);
}

.btn-ghost {
    background: rgba(255, 255, 255, 0.04);
    color: var(--text-primary);
    border: 1px solid var(--border-hairline);
    font-family: var(--font-sans);
    font-size: 0.82rem;
    font-weight: 600;
    padding: 0.7rem 1.3rem;
    border-radius: 9999px;
    text-decoration: none;
    transition: border-color 0.2s, color 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}

.btn-ghost:hover {
    border-color: var(--border-gold);
    color: var(--accent-gold);
}

@media (max-width: 768px) {
    .tool-switcher { display: none; }
    .metrics-strip, .contrast-grid, .tool-grid-layout { grid-template-columns: 1fr; }
    .contrast-col + .contrast-col { border-left: none; border-top: 1px solid var(--border-hairline); }
    .cta-console { flex-direction: column; align-items: flex-start; }
}
"""

MASTER_JS_TIMELINE = """
document.addEventListener('DOMContentLoaded', () => {
    const timeline = document.querySelector('.orbital-timeline');
    const fill = document.querySelector('.orbital-track-fill');
    const node = document.querySelector('.orbital-node');
    const cards = document.querySelectorAll('.stage-card');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            const wasOpen = card.classList.contains('open');
            cards.forEach(c => c.classList.remove('open'));
            if (!wasOpen) card.classList.add('open');
        });
    });

    function updateOrbitalThread() {
        if (!timeline) return;
        const rect = timeline.getBoundingClientRect();
        const winH = window.innerHeight;
        const start = winH * 0.65;
        const progress = Math.max(0, Math.min(1, (start - rect.top) / rect.height));
        const pct = (progress * 100).toFixed(1) + '%';
        if (fill) fill.style.height = pct;
        if (node) node.style.top = pct;

        cards.forEach(card => {
            const cRect = card.getBoundingClientRect();
            card.classList.toggle('active-stage', cRect.top < start && cRect.bottom > winH * 0.25);
        });
    }

    window.addEventListener('scroll', updateOrbitalThread, { passive: true });
    updateOrbitalThread();
});
"""

def render_tool_workspace_html(tool_id, is_it=False):
    if tool_id == "sla_calculator":
        leads_label = "Lead Inbound / Fiere Mensili" if is_it else "Monthly Inbound / Event Leads"
        leads_unit = "lead" if is_it else "leads"
        acv_label = "Valore Medio Trattativa B2B (€)" if is_it else "Average B2B Deal Value (€)"
        speed_label = "Tempo Medio Attuale di Risposta Commerciale" if is_it else "Current Average Sales Follow-Up Time"
        opt_slow = "> 48 Ore (CSV Manuali)" if is_it else "> 48 Hours (Manual CSV)"
        opt_med = "24 Ore" if is_it else "24 Hours"
        opt_fast = "< 5 Minuti (Webhook + SLA HubSpot)" if is_it else "< 5 Minutes (Automated Webhook + HubSpot SLA)"

        kpi1_title = "Pipeline Annuale Dispersa (€)" if is_it else "Estimated Annual Pipeline Leaked (€)"
        kpi1_sub = "75% dispersione per latenza (> 48h)" if is_it else "75% lead drop-off due to latency (> 48h)"
        kpi2_title = "Pipeline Recuperabile con Routing a 0 Latenza (€)" if is_it else "Recoverable Pipeline with 0-Latency Routing (€)"
        kpi2_sub = "Con routing automatizzato SLA < 5 min" if is_it else "With sub-5min automated SLA"
        kpi3_title = "Incremento Previsto Conversione MQL-to-SQL (%)" if is_it else "Projected MQL-to-SQL Conversion Lift (%)"
        kpi3_sub = "4% attuale → 35% target SLA" if is_it else "4% current → 35% SLA target"

        cta_card_btn = "Risolvi Questa Dispersione con un Audit Architetturale 📅" if is_it else "Fix This Pipeline Leakage via Architecture Audit 📅"

        return f"""
        <div class="tool-workspace-card">
            <div class="tool-grid-layout">
                <div class="tool-inputs-card">
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="slaLeadsInput">{leads_label}</label>
                            <span class="tool-val-display" id="slaLeadsVal">350 {leads_unit}</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="slaLeadsInput" min="50" max="2500" step="25" value="350" oninput="updateSlaCalculator()">
                    </div>
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="slaAcvInput">{acv_label}</label>
                            <span class="tool-val-display" id="slaAcvVal">€15,000</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="slaAcvInput" min="2000" max="100000" step="1000" value="15000" oninput="updateSlaCalculator()">
                    </div>
                    <div class="tool-input-group">
                        <label class="tool-input-label">{speed_label}</label>
                        <div class="tool-pills-row" id="slaSpeedPills">
                            <button type="button" class="tool-pill-option active" data-speed="slow" onclick="setSlaFollowup('slow')">{opt_slow}</button>
                            <button type="button" class="tool-pill-option" data-speed="medium" onclick="setSlaFollowup('medium')">{opt_med}</button>
                            <button type="button" class="tool-pill-option" data-speed="fast" onclick="setSlaFollowup('fast')">{opt_fast}</button>
                        </div>
                    </div>
                </div>

                <div class="tool-results-card">
                    <div class="tool-kpis-grid">
                        <div class="tool-kpi-card" style="border-color: rgba(251, 113, 133, 0.4); background: rgba(251, 113, 133, 0.05);">
                            <div class="tool-kpi-label">{kpi1_title}</div>
                            <div class="tool-kpi-num" id="slaLeakedVal" style="color: var(--accent-rose);">€19,530,000</div>
                            <div class="tool-kpi-sub" id="slaLeakedSub">{kpi1_sub}</div>
                        </div>
                        <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                            <div class="tool-kpi-label">{kpi2_title}</div>
                            <div class="tool-kpi-num" id="slaRecoverableVal" style="color: var(--accent-emerald);">€13,671,000</div>
                            <div class="tool-kpi-sub" id="slaRecoverableSub">{kpi2_sub}</div>
                        </div>
                        <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                            <div class="tool-kpi-label">{kpi3_title}</div>
                            <div class="tool-kpi-num" id="slaLiftVal" style="color: var(--accent-gold);">+775%</div>
                            <div class="tool-kpi-sub" id="slaLiftSub">{kpi3_sub}</div>
                        </div>
                    </div>
                    <div class="tool-cta-wrapper">
                        <a href="https://calendly.com/renzo-francesqui" target="_blank" rel="noopener noreferrer" class="tool-cta-btn">
                            <span>⚡</span> {cta_card_btn}
                        </a>
                    </div>
                </div>
            </div>
        </div>"""

    elif tool_id == "utm_builder":
        default_url = "https://renzo-francesqui.vercel.app/it/services/hubspot-crm-optimization-startups/" if is_it else "https://renzo-francesqui.vercel.app/services/hubspot-crm-optimization-startups/"
        url_label = "URL Pagina di Destinazione (Landing Page)" if is_it else "Landing Page Destination URL"
        source_label = "Sorgente di Acquisizione (utm_source)" if is_it else "Acquisition Channel / Source (utm_source)"
        medium_label = "Mezzo di Campagna (utm_medium)" if is_it else "Campaign Medium (utm_medium)"
        camp_label = "Nome Campagna (utm_campaign — auto-slug in minuscolo)" if is_it else "Campaign Name (utm_campaign — auto-slugified with underscores)"
        region_label = "Segmento ICP / Mercato (custom_icp_region)" if is_it else "ICP Segment / Target Region (custom_icp_region)"

        tag_url = "URL CON GOVERNANCE STANDARD" if is_it else "GOVERNED CAMPAIGN URL"
        btn_copy = "📋 Copia URL con Governance" if is_it else "📋 Copy Governed URL"
        tag_json = "PARAMETRI MODULO NASCOSTI HUBSPOT / SALESFORCE" if is_it else "HUBSPOT / SALESFORCE HIDDEN FORM FIELDS"
        tag_payload = "PAYLOAD INGESTIONE" if is_it else "INGESTION JSON"

        cta_card_btn = "Pianifica Audit Architettura Tracciamento CRM 📅" if is_it else "Audit Your Campaign Tracking & CRM Taxonomy 📅"

        return f"""
        <div class="tool-workspace-card">
            <div class="tool-grid-layout">
                <div class="tool-inputs-card">
                    <div class="tool-input-group">
                        <label for="utmUrlInput" class="tool-input-label">{url_label}</label>
                        <input type="url" class="tool-text-input" id="utmUrlInput" value="{default_url}" oninput="updateUtmBuilder()">
                    </div>
                    <div class="tool-input-group">
                        <label class="tool-input-label">{source_label}</label>
                        <div class="tool-pills-row" id="utmSourcePills">
                            <button type="button" class="tool-pill-option active" data-src="linkedin" onclick="setUtmSource('linkedin')">linkedin</button>
                            <button type="button" class="tool-pill-option" data-src="google" onclick="setUtmSource('google')">google</button>
                            <button type="button" class="tool-pill-option" data-src="meta" onclick="setUtmSource('meta')">meta</button>
                            <button type="button" class="tool-pill-option" data-src="tradeshow_qr" onclick="setUtmSource('tradeshow_qr')">tradeshow_qr</button>
                            <button type="button" class="tool-pill-option" data-src="email_nurture" onclick="setUtmSource('email_nurture')">email_nurture</button>
                        </div>
                    </div>
                    <div class="tool-input-group">
                        <label class="tool-input-label">{medium_label}</label>
                        <div class="tool-pills-row" id="utmMediumPills">
                            <button type="button" class="tool-pill-option active" data-med="cpc" onclick="setUtmMedium('cpc')">cpc</button>
                            <button type="button" class="tool-pill-option" data-med="abm_sponsored" onclick="setUtmMedium('abm_sponsored')">abm_sponsored</button>
                            <button type="button" class="tool-pill-option" data-med="offline_badge" onclick="setUtmMedium('offline_badge')">offline_badge</button>
                            <button type="button" class="tool-pill-option" data-med="automation" onclick="setUtmMedium('automation')">automation</button>
                        </div>
                    </div>
                    <div class="tool-input-group">
                        <label for="utmCampaignInput" class="tool-input-label">{camp_label}</label>
                        <input type="text" class="tool-text-input" id="utmCampaignInput" value="2026_q2_enterprise_revops_scale" oninput="updateUtmBuilder()">
                    </div>
                    <div class="tool-input-group">
                        <label class="tool-input-label">{region_label}</label>
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
                            <span class="terminal-tag">{tag_url}</span>
                            <button class="terminal-copy-btn" id="btnCopyUtm" onclick="copyGovernedUrl()">{btn_copy}</button>
                        </div>
                        <div class="terminal-content" id="utmOutputUrl" style="color: var(--accent-cyan);">
                            {default_url}?utm_source=linkedin&amp;utm_medium=cpc&amp;utm_campaign=2026_q2_enterprise_revops_scale&amp;custom_icp_region=emea
                        </div>
                    </div>

                    <div class="terminal-block" style="margin-top: 1rem;">
                        <div class="terminal-bar">
                            <span class="terminal-tag">{tag_json}</span>
                            <span style="font-family: var(--font-mono); font-size: 0.62rem; color: var(--accent-gold);">{tag_payload}</span>
                        </div>
                        <pre class="terminal-content" id="utmJsonPreview" style="color: var(--accent-purple); margin: 0; overflow-x: auto;">{{
  "utm_source": "linkedin",
  "utm_medium": "cpc",
  "utm_campaign": "2026_q2_enterprise_revops_scale",
  "custom_icp_region": "emea"
}}</pre>
                    </div>

                    <div class="tool-cta-wrapper" style="margin-top: 1.15rem;">
                        <a href="https://calendly.com/renzo-francesqui" target="_blank" rel="noopener noreferrer" class="tool-cta-btn">
                            <span>🔗</span> {cta_card_btn}
                        </a>
                    </div>
                </div>
            </div>
        </div>"""

    elif tool_id == "tradeshow_roi":
        cost_label = "Costo Totale Stand & Sponsorizzazione Fiera (€)" if is_it else "Total Booth & Event Sponsorship Cost (€)"
        badges_label = "Badge Scansionati allo Stand" if is_it else "Badges Scanned at Show"
        badges_unit = "badge" if is_it else "badges"
        qual_label = "Tasso di Qualificazione (% ICP High-Intent)" if is_it else "Qualification Rate (% High-Intent ICP)"
        acv_label = "Valore Medio Contratto B2B (€)" if is_it else "Average Contract Value (€)"
        win_label = "Tasso di Chiusura Opportunità (%)" if is_it else "Close Rate (%)"

        kpi1_title = "Costo per Lead Scansionato (€)" if is_it else "Cost Per Scanned Lead (€)"
        kpi1_sub = "Costo per SQL qualificato: €313" if is_it else "Cost per qualified SQL: €313"
        kpi2_title = "Pipeline SQL Generata (€)" if is_it else "Generated SQL Pipeline (€)"
        kpi2_sub = "Fatturato previsto vinto: €887,040" if is_it else "Projected won: €887,040"
        kpi3_title = "ROAS Stimato Evento (x)" if is_it else "Projected Event ROAS (x)"
        kpi3_sub = "Ritorno sul capitale investito" if is_it else "Return on event capital invested"
        kpi4_title = "Ore Risparmiate con Sincronizzazione Badge-CRM" if is_it else "Time Saved via Automated Badge-to-HubSpot Sync (Hours)"
        kpi4_sub = "Tramite ingestione CRM a 0 latenza" if is_it else "Via zero-latency CRM ingestion"

        cta_card_btn = "Ingegnerizza la Tua Pipeline Fieristica con Renzo 📅" if is_it else "Model Your Trade Show Lead Engine with Renzo 📅"

        return f"""
        <div class="tool-workspace-card">
            <div class="tool-grid-layout">
                <div class="tool-inputs-card">
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="tsCostInput">{cost_label}</label>
                            <span class="tool-val-display" id="tsCostVal">€45,000</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="tsCostInput" min="5000" max="250000" step="2500" value="45000" oninput="updateTradeShowRoi()">
                    </div>
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="tsBadgesInput">{badges_label}</label>
                            <span class="tool-val-display" id="tsBadgesVal">320 {badges_unit}</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="tsBadgesInput" min="20" max="2500" step="10" value="320" oninput="updateTradeShowRoi()">
                    </div>
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="tsQualInput">{qual_label}</label>
                            <span class="tool-val-display" id="tsQualVal">45%</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="tsQualInput" min="5" max="90" step="5" value="45" oninput="updateTradeShowRoi()">
                    </div>
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="tsAcvInput">{acv_label}</label>
                            <span class="tool-val-display" id="tsAcvVal">€28,000</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="tsAcvInput" min="2000" max="150000" step="1000" value="28000" oninput="updateTradeShowRoi()">
                    </div>
                    <div class="tool-input-group">
                        <div class="tool-label-row">
                            <label for="tsWinRateInput">{win_label}</label>
                            <span class="tool-val-display" id="tsWinRateVal">22%</span>
                        </div>
                        <input type="range" class="tool-range-slider" id="tsWinRateInput" min="2" max="60" step="1" value="22" oninput="updateTradeShowRoi()">
                    </div>
                </div>

                <div class="tool-results-card">
                    <div class="tool-kpis-grid" style="grid-template-columns: repeat(2, 1fr);">
                        <div class="tool-kpi-card" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.05);">
                            <div class="tool-kpi-label">{kpi1_title}</div>
                            <div class="tool-kpi-num" id="tsCplVal" style="color: var(--accent-cyan);">€141</div>
                            <div class="tool-kpi-sub" id="tsCplSub">{kpi1_sub}</div>
                        </div>
                        <div class="tool-kpi-card" style="border-color: rgba(212, 168, 99, 0.4); background: rgba(212, 168, 99, 0.05);">
                            <div class="tool-kpi-label">{kpi2_title}</div>
                            <div class="tool-kpi-num" id="tsPipelineVal" style="color: var(--accent-gold);">€4,032,000</div>
                            <div class="tool-kpi-sub" id="tsPipelineSub">{kpi2_sub}</div>
                        </div>
                        <div class="tool-kpi-card" style="border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.05);">
                            <div class="tool-kpi-label">{kpi3_title}</div>
                            <div class="tool-kpi-num" id="tsRoasVal" style="color: var(--accent-emerald);">19.7x</div>
                            <div class="tool-kpi-sub" id="tsRoasSub">{kpi3_sub}</div>
                        </div>
                        <div class="tool-kpi-card" style="border-color: rgba(167, 139, 250, 0.4); background: rgba(167, 139, 250, 0.05);">
                            <div class="tool-kpi-label">{kpi4_title}</div>
                            <div class="tool-kpi-num" id="tsHoursVal" style="color: var(--accent-purple);">43 hrs</div>
                            <div class="tool-kpi-sub" id="tsHoursSub">{kpi4_sub}</div>
                        </div>
                    </div>
                    <div class="tool-cta-wrapper">
                        <a href="https://calendly.com/renzo-francesqui" target="_blank" rel="noopener noreferrer" class="tool-cta-btn">
                            <span>🎪</span> {cta_card_btn}
                        </a>
                    </div>
                </div>
            </div>
        </div>"""
    return ""

def render_tool_interactive_js(tool_id):
    if tool_id == "sla_calculator":
        return """
        let currentSlaSpeed = 'slow';
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
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', updateSlaCalculator);
        } else {
            updateSlaCalculator();
        }
        """

    elif tool_id == "utm_builder":
        return """
        let currentUtmSource = 'linkedin';
        let currentUtmMedium = 'cpc';
        let currentUtmRegion = 'emea';
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
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', updateUtmBuilder);
        } else {
            updateUtmBuilder();
        }
        """

    elif tool_id == "tradeshow_roi":
        return """
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
            document.addEventListener('DOMContentLoaded', updateTradeShowRoi);
        } else {
            updateTradeShowRoi();
        }
        """
    return ""

def render_tool_html(tool, lang="en"):
    is_it = (lang == "it")
    canonical_base = "https://renzo-francesqui.vercel.app"
    slug = tool['slug']
    en_canonical_url = f"{canonical_base}/tools/{slug}/"
    it_canonical_url = f"{canonical_base}/it/tools/{slug}/"
    page_canonical = it_canonical_url if is_it else en_canonical_url
    page_url = page_canonical
    en_toggle_href = f"/tools/{slug}/"
    it_toggle_href = f"/it/tools/{slug}/"

    meta_title = tool['meta_title_it'] if is_it else tool['meta_title_en']
    meta_desc = tool['meta_desc_it'] if is_it else tool['meta_desc_en']
    eyebrow = tool['eyebrow_it'] if is_it else tool['eyebrow_en']
    hero_title = tool['hero_title_it'] if is_it else tool['hero_title_en']
    hero_lead = tool['hero_lead_it'] if is_it else tool['hero_lead_en']

    metrics = tool['metrics_it'] if is_it else tool['metrics_en']
    c1_header = tool['contrast_col1_header_it'] if is_it else tool['contrast_col1_header_en']
    c2_header = tool['contrast_col2_header_it'] if is_it else tool['contrast_col2_header_en']
    c1_items = tool['contrast_col1_items_it'] if is_it else tool['contrast_col1_items_en']
    c2_items = tool['contrast_col2_items_it'] if is_it else tool['contrast_col2_items_en']

    stages = tool['stages_it'] if is_it else tool['stages_en']
    tool_name = tool['tool_name_it'] if is_it else tool['tool_name_en']
    cta_heading = tool['cta_heading_it'] if is_it else tool['cta_heading_en']
    cta_sub = tool['cta_sub_it'] if is_it else tool['cta_sub_en']
    tool_subject = tool['tool_subject_it'] if is_it else tool['tool_subject_en']
    encoded_subject = urllib.parse.quote(tool_subject, safe="—")

    if is_it:
        section_workspace_index = "01 // WORKSPACE OPERATIVO"
        section_workspace_heading = "Configurazione Parametri & Telemetria in Tempo Reale"
        section_contrast_index = "02 // DIAGNOSTICA OPERATIVA"
        section_contrast_heading = "Processo Manuale Disordinato vs. Protocollo Ingegnerizzato"
        section_stages_index = "03 // PROTOCOLLO DI IMPLEMENTAZIONE"
        section_stages_heading = "Ingegnerizzazione dei Sistemi RevOps in Quattro Fasi"
        cta_btn_primary = "Prenota Audit via Calendly 📅"
        cta_btn_inquire = "Richiedi via Email ✉️"
        cta_btn_secondary = "Ritorna alla Matrice Solare 🪐"
        back_text = "Matrice Solare"
    else:
        section_workspace_index = "01 // INTERACTIVE WORKSPACE"
        section_workspace_heading = "Live Parameter Configuration & Real-Time Telemetry"
        section_contrast_index = "02 // DIAGNOSTIC CONTRAST"
        section_contrast_heading = "Ad-Hoc Manual Process vs. Engineered RevOps Protocol"
        section_stages_index = "03 // EXECUTION PROTOCOL"
        section_stages_heading = "Four-Stage Revenue Architecture Methodology"
        cta_btn_primary = "Book Architecture Audit via Calendly 📅"
        cta_btn_inquire = "Inquire via Email ✉️"
        cta_btn_secondary = "Back to 3D Solar Matrix 🪐"
        back_text = "Solar Matrix"

    # Metrics HTML
    metrics_html = "".join([f"""
            <div class="metric-item">
                <span class="metric-value">{m['val']}</span>
                <span class="metric-label">{m['label']}</span>
            </div>""" for m in metrics])

    # Contrast items HTML
    c1_html = "".join([f"""
                    <li>
                        <span class="marker">–</span>
                        <span>{item}</span>
                    </li>""" for item in c1_items])

    c2_html = "".join([f"""
                    <li>
                        <span class="marker">→</span>
                        <span>{item}</span>
                    </li>""" for item in c2_items])

    # Stages HTML (Stage 01 starts open)
    stages_html = ""
    for idx, stage in enumerate(stages):
        is_first = (idx == 0)
        open_cls = " open" if is_first else ""
        pills_html = "".join([f'<span class="deliverable-pill">{pill}</span>' for pill in stage['pills']])
        stages_html += f"""
            <div class="stage-card{open_cls}">
                <div class="stage-top">
                    <div class="stage-meta">
                        <span class="stage-number">{stage['num']}</span>
                        <h3 class="stage-title">{stage['title']}</h3>
                    </div>
                    <span class="stage-toggle-icon">+</span>
                </div>
                <p class="stage-summary">{stage['summary']}</p>
                <div class="stage-details">
                    <div class="deliverables-pills">
                        {pills_html}
                    </div>
                </div>
            </div>"""

    # Tool switcher pills HTML
    switcher_pills_html = ""
    for t in TOOLS_DATA:
        active_cls = " active" if t['id'] == tool['id'] else ""
        target_slug = t['slug']
        pill_label = t['pill_label_it'] if is_it else t['pill_label_en']
        pill_href = f"/it/tools/{target_slug}/" if is_it else f"/tools/{target_slug}/"
        switcher_pills_html += f"""
            <a href="{pill_href}" class="switch-pill{active_cls}">{pill_label}</a>"""

    # Interactive workspace content and js
    tool_workspace_html = render_tool_workspace_html(tool['id'], is_it=is_it)
    tool_interactive_js = render_tool_interactive_js(tool['id'])

    # Schema.org JSON-LD
    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_url,
                "url": page_url,
                "name": meta_title,
                "description": meta_desc,
                "inLanguage": "it" if is_it else "en",
                "isPartOf": {
                    "@type": "WebSite",
                    "name": "Renzo Francesqui Portfolio",
                    "url": f"{canonical_base}/it/" if is_it else f"{canonical_base}/"
                },
                "mainEntity": { "@id": f"{page_url}#app" }
            },
            {
                "@type": "WebApplication",
                "@id": f"{page_url}#app",
                "name": tool_name,
                "description": hero_lead,
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "All",
                "browserRequirements": "Requires JavaScript. Requires HTML5.",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                },
                "creator": {
                    "@type": "Person",
                    "@id": f"{canonical_base}/it/#person" if is_it else f"{canonical_base}/#person",
                    "name": "Renzo Francesqui",
                    "jobTitle": "Specialista Marketing Operations, Architetture CRM & RevOps" if is_it else "Marketing Operations & RevOps Specialist",
                    "address": {
                        "@type": "PostalAddress",
                        "addressLocality": "Milano" if is_it else "Milan",
                        "addressRegion": "Lombardy",
                        "addressCountry": "IT"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{page_url}#breadcrumb",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Home", "item": f"{canonical_base}/it/" if is_it else f"{canonical_base}/" },
                    { "@type": "ListItem", "position": 2, "name": "Strumenti" if is_it else "Tools", "item": f"{canonical_base}/it/#tools" if is_it else f"{canonical_base}/#tools" },
                    { "@type": "ListItem", "position": 3, "name": meta_title.split('|')[0].strip(), "item": page_url }
                ]
            }
        ]
    }
    schema_json_str = json.dumps(schema_data, indent=2, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="{'it' if is_it else 'en'}" data-theme="dark">
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
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="alternate icon" href="/favicon.ico">

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

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

    <style>{MASTER_CSS}
    </style>
</head>
<body>
    <!-- Sticky Minimalist HUD Header -->
    <div class="nav-Wrapper">
        <header class="hud-header">
            <a href="../../index.html" class="back-link">
                <span>←</span> {back_text}
            </a>

            <nav class="tool-switcher">{switcher_pills_html}
            </nav>

            <div class="lang-switcher" style="display: flex; align-items: center; gap: 0.25rem;">
                <a href="{en_toggle_href}" class="switch-pill{' active' if not is_it else ''}">EN</a>
                <a href="{it_toggle_href}" class="switch-pill{' active' if is_it else ''}">IT</a>
            </div>
        </header>
    </div>

    <!-- Centered Editorial Container -->
    <main class="editorial-container">
        <!-- 1. Hero Section -->
        <section class="hero-section">
            <div class="eyebrow-badge">
                <span class="eyebrow-dot"></span>
                <span>{eyebrow}</span>
            </div>
            <h1 class="hero-title">{hero_title}</h1>
            <p class="hero-lead">{hero_lead}</p>
            <div class="metrics-strip">{metrics_html}
            </div>
        </section>

        <!-- 2. Interactive Tool Workspace -->
        <section>
            <span class="section-index">{section_workspace_index}</span>
            <h2 class="section-heading">{section_workspace_heading}</h2>{tool_workspace_html}
        </section>

        <!-- 3. Minimalist Contrast Table (Diagnostic Section) -->
        <section>
            <span class="section-index">{section_contrast_index}</span>
            <h2 class="section-heading">{section_contrast_heading}</h2>
            <div class="contrast-grid">
                <div class="contrast-col">
                    <div class="contrast-header muted">{c1_header}</div>
                    <ul class="contrast-list">{c1_html}
                    </ul>
                </div>
                <div class="contrast-col">
                    <div class="contrast-header gold">{c2_header}</div>
                    <ul class="contrast-list">{c2_html}
                    </ul>
                </div>
            </div>
        </section>

        <!-- 4. Implementation Protocol & Architecture Stages -->
        <section>
            <span class="section-index">{section_stages_index}</span>
            <h2 class="section-heading">{section_stages_heading}</h2>
            <div class="orbital-timeline">
                <div class="orbital-track-bg"></div>
                <div class="orbital-track-fill"></div>
                <div class="orbital-node"></div>{stages_html}
            </div>
        </section>

        <!-- 5. Minimalist Executive CTA Console -->
        <div class="cta-console">
            <div>
                <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.35rem;">{cta_heading}</h3>
                <p style="font-size: 0.88rem; color: var(--text-secondary);">{cta_sub}</p>
            </div>
            <div class="cta-actions">
                <a href="https://calendly.com/renzo-francesqui" target="_blank" rel="noopener noreferrer" class="btn-gold">{cta_btn_primary}</a>
                <a href="mailto:renzo.francesqui@gmail.com?subject={encoded_subject}" class="btn-ghost">{cta_btn_inquire}</a>
                <a href="../../index.html" class="btn-ghost">{cta_btn_secondary}</a>
            </div>
        </div>
    </main>

    <!-- Scroll & Interactive Tool JavaScript -->
    <script>{MASTER_JS_TIMELINE}
{tool_interactive_js}
    </script>
</body>
</html>"""

def build_all_tools():
    count = 0
    for tool in TOOLS_DATA:
        # 1. English page: tools/<slug>/index.html
        en_dir = BASE_DIR / "tools" / tool['slug']
        en_dir.mkdir(parents=True, exist_ok=True)
        en_file = en_dir / "index.html"
        en_html = render_tool_html(tool, lang="en")
        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_html)
        count += 1

        # 2. Italian page: it/tools/<slug>/index.html
        it_dir = BASE_DIR / "it" / "tools" / tool['slug']
        it_dir.mkdir(parents=True, exist_ok=True)
        it_file = it_dir / "index.html"
        it_html = render_tool_html(tool, lang="it")
        with open(it_file, "w", encoding="utf-8") as f:
            f.write(it_html)
        count += 1

    print(f"[OK] Generated {count} minimalist editorial tool landing pages (EN and IT).")

if __name__ == "__main__":
    build_all_tools()
