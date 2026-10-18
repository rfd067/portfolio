#!/usr/bin/env python3
"""
Generate Minimalist Editorial Freelance Service Landing Pages (EN & IT).
Rebuilds the 4 standalone B2B Service Pages linked from #modalServices:
1. /services/hubspot-crm-optimization-startups/index.html (and alias /services/small-startup-business-crm-setup-optimization/)
2. /services/paid-media-management/index.html
3. /services/seo-and-geo-optimization/index.html
4. /services/marketing-data-reporting/index.html

Strict Minimalist Editorial Design System:
- Strict Anti-Clutter: No calculators, no sliders, no fake terminals, no cartoon rockets, no widgets.
- 840px/860px Centered Editorial Column.
- Hairline borders (rgba(255, 255, 255, 0.08)) and Warm Champagne Gold (#d4a863) accent.
- Scroll-Driven Orbital Light Thread & Accordion Stages.
- Diagnostic Contrast Grid (Before vs. After).
- Verified Enterprise Track Record (TOMRA, IMBAREX, The Pisonay Company).
- Minimalist Executive CTA Console.
- Full SEO metadata, canonicals, hreflang, and Schema.org JSON-LD.
"""

from pathlib import Path
import json
import urllib.parse

BASE_DIR = Path(__file__).resolve().parent.parent

SERVICES_DATA = [
    {
        "id": "crm",
        "slug": "hubspot-crm-optimization-startups",
        "aliases": ["small-startup-business-crm-setup-optimization"],
        "service_num": "01",
        "pill_label": "01 CRM & RevOps",
        
        # Meta & Titles (<60 chars title, <160 chars desc)
        "meta_title_en": "HubSpot CRM & RevOps for Startups | Renzo Francesqui",
        "meta_title_it": "Setup CRM & RevOps per Startup | Renzo Francesqui",
        "meta_desc_en": "HubSpot CRM & RevOps architecture for startups: eliminate spreadsheet chaos, automate MQL routing, prevent dropped leads, and scale pipeline velocity.",
        "meta_desc_it": "Setup e architettura CRM & RevOps per startup: elimina fogli Excel, routing MQL automatizzato, zero lead persi e massima velocità di pipeline.",

        # Sector & Hero Header
        "eyebrow_en": "SECTOR 01 // REVOPS & CRM ARCHITECTURE",
        "eyebrow_it": "SETTORE 01 // ARCHITETTURA REVOPS & CRM",
        "hero_title_en": "HubSpot & Salesforce CRM Architecture for Scaling B2B Teams.",
        "hero_title_it": "Architettura CRM HubSpot & Salesforce per Team B2B in Crescita.",
        "hero_lead_en": "Eliminate lead leakage, manual CSV imports, and fragmented pipelines. I architect clean lifecycle stages, automated lead routing, and strict deal-stage governance so your revenue team operates from a single source of truth.",
        "hero_lead_it": "Elimina la dispersione di lead, le importazioni manuali di CSV e le pipeline frammentate. Ingegnerizzo stadi di lifecycle chiari, routing automatizzato dei lead e governance rigorosa dei deal affinché il tuo team revenue operi da un'unica fonte di verità.",

        # Hairline Metrics Strip (3 metrics)
        "metrics_en": [
            {"val": "100%", "label": "Captured Lead Synchronization"},
            {"val": "< 5 Min", "label": "Automated MQL-to-SQL Routing SLA"},
            {"val": "Zero", "label": "Unassigned or Stagnant Pipeline Deals"}
        ],
        "metrics_it": [
            {"val": "100%", "label": "Sincronizzazione Lead Acquisiti"},
            {"val": "< 5 Min", "label": "SLA Routing Automatizzato MQL-to-SQL"},
            {"val": "Zero", "label": "Trattative Non Assegnate o Stagnanti"}
        ],

        # Section 01: Diagnostic Contrast Grid
        "contrast_col1_header_en": "UNSTRUCTURED CRM STATE",
        "contrast_col1_header_it": "STATO CRM NON STRUTTURATO",
        "contrast_col1_items_en": [
            "Leads sit uncontacted for days due to manual spreadsheet uploads.",
            "Sales reps bypass lifecycle stages with zero mandatory field validation.",
            "Duplicate contacts and broken custom properties corrupt attribution.",
            "No visibility into where MQLs stall before becoming SQLs."
        ],
        "contrast_col1_items_it": [
            "I lead restano non contattati per giorni a causa di caricamenti manuali da fogli di calcolo.",
            "I commerciali saltano le fasi di lifecycle senza alcuna validazione obbligatoria dei campi.",
            "Contatti duplicati e proprietà personalizzate non governate corrompono l'attribuzione.",
            "Nessuna visibilità sui punti in cui gli MQL si bloccano prima di diventare SQL."
        ],
        "contrast_col2_header_en": "ENGINEERED REVOPS SYSTEM",
        "contrast_col2_header_it": "SISTEMA REVOPS INGEGNERIZZATO",
        "contrast_col2_items_en": [
            "Instant webhook & API ingestion with automated territory assignment.",
            "Strict deal-stage gating and validation rules enforcing data hygiene.",
            "Standardized custom object schema and lifecycle taxonomy.",
            "Automated Slack/Email SLA escalations when high-intent leads stagnate."
        ],
        "contrast_col2_items_it": [
            "Ingestione istantanea via webhook e API con assegnazione automatica del territorio.",
            "Gating rigoroso delle fasi di trattativa e regole di validazione per l'igiene dei dati.",
            "Schema standardizzato di oggetti personalizzati e tassonomia di lifecycle.",
            "Escalation automatica via Slack/Email quando i lead ad alta intenzione ristagnano."
        ],

        # Section 02: 4 Execution Stages (Orbital Timeline)
        "stages_en": [
            {
                "num": "01",
                "title": "Schema Audit & Data Governance",
                "summary": "Auditing existing properties, merging duplicates, and mapping a clean Contact, Company, and Deal data model.",
                "pills": ["Property Taxonomy", "Deduplication", "Custom Objects", "Permission Sets"]
            },
            {
                "num": "02",
                "title": "Lifecycle & Pipeline Stage Engineering",
                "summary": "Building a strict Lead → MQL → SQL → Opportunity progression with mandatory stage-gate validation rules.",
                "pills": ["Lifecycle Modeling", "Validation Rules", "Deal Stage Gating", "Pipeline Hygiene"]
            },
            {
                "num": "03",
                "title": "Behavioral Lead Scoring & 0-Latency Routing",
                "summary": "Configuring ICP firmographic + intent scoring and instant round-robin or territory-based rep assignment.",
                "pills": ["ICP Fit Scoring", "Workflow Automation", "Round-Robin Routing", "SLA Alerts"]
            },
            {
                "num": "04",
                "title": "Sales Enablement & RevOps Reporting",
                "summary": "Deploying clean rep views, automated follow-up sequences, and conversion velocity dashboards.",
                "pills": ["Pipeline Velocity", "Funnel Conversion Reports", "Rep Playbooks", "Sandbox QA"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Audit dello Schema & Data Governance",
                "summary": "Revisione delle proprietà esistenti, deduplica dei contatti e mappatura di un modello dati pulito per Contatti, Aziende e Trattative.",
                "pills": ["Tassonomia Proprietà", "Deduplica Dati", "Oggetti Personalizzati", "Set di Permessi"]
            },
            {
                "num": "02",
                "title": "Ingegnerizzazione Lifecycle & Pipeline",
                "summary": "Costruzione di una progressione rigida Lead → MQL → SQL → Opportunità con regole di validazione obbligatorie per ogni fase.",
                "pills": ["Modellazione Lifecycle", "Regole di Validazione", "Deal Stage Gating", "Igiene Pipeline"]
            },
            {
                "num": "03",
                "title": "Lead Scoring Comportamentale & Routing a 0 Latenza",
                "summary": "Configurazione scoring ICP per dati anagrafici e intenzione, con assegnazione commerciale immediata per territorio o rotazione.",
                "pills": ["Scoring Fit ICP", "Automazione Workflow", "Routing a Rotazione", "Alert SLA"]
            },
            {
                "num": "04",
                "title": "Abilitazione Commerciale & Reportistica RevOps",
                "summary": "Rilascio di viste commerciali intuitive, sequenze di follow-up automatizzate e cruscotti di velocità di conversione.",
                "pills": ["Velocità di Pipeline", "Report Conversione Funnel", "Playbook Commerciali", "QA Sandbox"]
            }
        ],

        # Service Name for Mailto Subject
        "service_name_en": "HubSpot CRM & RevOps Architecture",
        "service_name_it": "Architettura CRM & RevOps HubSpot"
    },

    {
        "id": "paid_media",
        "slug": "paid-media-management",
        "aliases": [],
        "service_num": "02",
        "pill_label": "02 Paid Media",
        
        "meta_title_en": "Paid Media for Strict Budgets | Renzo Francesqui",
        "meta_title_it": "Paid Media per Piccoli Budget | Renzo Francesqui",
        "meta_desc_en": "Stop wasting lean ad budgets on unqualified clicks. Precision Google, LinkedIn, and Meta campaigns connected to your CRM for profitable, provable CAC.",
        "meta_desc_it": "Basta spendere budget in click non qualificati. Campagne Google, LinkedIn e Meta per PMI collegate al CRM per un costo di acquisizione (CAC) sostenibile.",

        "eyebrow_en": "SECTOR 02 // B2B DEMAND GENERATION & PAID MEDIA",
        "eyebrow_it": "SETTORE 02 // DEMAND GENERATION B2B & PAID MEDIA",
        "hero_title_en": "Pipeline-Driven Paid Media for B2B & Technical Markets.",
        "hero_title_it": "Paid Media Guidato dalla Pipeline per Mercati B2B e Settori Tecnici.",
        "hero_lead_en": "Stop optimizing for cheap clicks and unqualified form fills. I engineer full-funnel Google Search, LinkedIn ABM, and Meta acquisition systems wired directly to your CRM's closed-won revenue data.",
        "hero_lead_it": "Basta ottimizzare per click a basso costo e form compilation non qualificate. Ingegnerizzo sistemi di acquisizione full-funnel su Google Search, LinkedIn ABM e Meta collegati direttamente ai dati di fatturato chiuso nel CRM.",

        "metrics_en": [
            {"val": "+33%", "label": "Verified Paid Conversion Rate Lift"},
            {"val": "10+", "label": "International Markets Scaled (EMEA & Americas)"},
            {"val": "SQL-Synced", "label": "Offline Conversion Tracking Loop"}
        ],
        "metrics_it": [
            {"val": "+33%", "label": "Incremento Verificato del Tasso di Conversione Paid"},
            {"val": "10+", "label": "Mercati Internazionali Scalati (EMEA & Americhe)"},
            {"val": "Sync SQL", "label": "Ciclo di Tracciamento Conversioni Offline"}
        ],

        "contrast_col1_header_en": "CONVENTIONAL AD SPEND",
        "contrast_col1_header_it": "SPESA PUBBLICITARIA CONVENZIONALE",
        "contrast_col1_items_en": [
            "Algorithms optimize for top-of-funnel vanity clicks and junk leads.",
            "Broad keyword matching burns budget on non-B2B search intent.",
            "Ad platforms are disconnected from HubSpot/Salesforce deal stages.",
            "Generic landing pages fail to convert technical decision-makers."
        ],
        "contrast_col1_items_it": [
            "Gli algoritmi ottimizzano per click di vanità top-of-funnel e lead fuori target.",
            "La corrispondenza generica delle keyword disperde budget su ricerche non B2B.",
            "Le piattaforme ads sono disconnesse dalle fasi di trattativa di HubSpot/Salesforce.",
            "Landing page generiche non riescono a convertire i decisori tecnici."
        ],
        "contrast_col2_header_en": "REVENUE-LINKED ACQUISITION",
        "contrast_col2_header_it": "ACQUISIZIONE COLLEGATA AL FATTURATO",
        "contrast_col2_items_en": [
            "Offline Conversion Imports train ad algorithms on real SQLs and Deals.",
            "High-intent exact/phrase search architecture with strict negative lists.",
            "Precision LinkedIn ABM targeting by company size, industry, and role.",
            "Continuous landing page A/B testing and conversion rate optimization."
        ],
        "contrast_col2_items_it": [
            "L'importazione di conversioni offline addestra gli algoritmi su SQL e vendite reali.",
            "Architettura di ricerca a corrispondenza esatta/frase con liste negative rigorose.",
            "Targeting LinkedIn ABM di precisione per dimensione aziendale, settore e ruolo.",
            "A/B testing continuo delle landing page e ottimizzazione del tasso di conversione."
        ],

        "stages_en": [
            {
                "num": "01",
                "title": "Unit Economics & Account Audit",
                "summary": "Auditing historical wasted spend, search term leakage, and establishing target CAC and pipeline payback thresholds.",
                "pills": ["CAC Modeling", "Negative Keyword Purge", "Auction Insights", "Funnel Audit"]
            },
            {
                "num": "02",
                "title": "Server-Side Tracking & CRM Feedback Loop",
                "summary": "Connecting GA4, Google Tag Manager, and HubSpot/Salesforce offline conversions so ad platforms optimize for qualified pipeline.",
                "pills": ["GA4 Custom Events", "Offline Conversion Import", "Enhanced Conversions", "UTM Governance"]
            },
            {
                "num": "03",
                "title": "High-Intent Search & LinkedIn ABM Deployment",
                "summary": "Structuring segmented Google Search campaigns and firmographic LinkedIn Account-Based Marketing ads.",
                "pills": ["Google Search & PMax", "LinkedIn ABM", "Meta Retargeting", "Ad Copy Architecture"]
            },
            {
                "num": "04",
                "title": "Landing Page CRO & Budget Velocity",
                "summary": "Running disciplined A/B tests on landing pages and reallocating spend toward highest-ROAS territories.",
                "pills": ["A/B Testing", "Landing Page CRO", "Pipeline ROAS Reporting", "Multi-Region Scaling"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Economia Unitaria & Audit Account",
                "summary": "Analisi dello storico di spesa dispersiva, dispersione dei termini di ricerca e definizione delle soglie di CAC e payback di pipeline.",
                "pills": ["Modellazione CAC", "Eliminazione Parole Negative", "Auction Insights", "Audit del Funnel"]
            },
            {
                "num": "02",
                "title": "Tracciamento Server-Side & Feedback CRM",
                "summary": "Integrazione di GA4, Google Tag Manager e conversioni offline HubSpot/Salesforce per ottimizzare le campagne sulla pipeline qualificata.",
                "pills": ["Eventi Personalizzati GA4", "Import Conversioni Offline", "Enhanced Conversions", "Governance UTM"]
            },
            {
                "num": "03",
                "title": "Google Search ad Alta Intenzione & LinkedIn ABM",
                "summary": "Strutturazione di campagne Google Search segmentate e annunci Account-Based Marketing mirati su LinkedIn.",
                "pills": ["Google Search & PMax", "LinkedIn ABM", "Retargeting Meta", "Architettura Copy Annunci"]
            },
            {
                "num": "04",
                "title": "CRO Landing Page & Efficienza di Budget",
                "summary": "Esecuzione di A/B test disciplinati sulle landing page e riallocazione del budget sui territori a più alto ROAS.",
                "pills": ["A/B Testing", "CRO Landing Page", "Report ROAS di Pipeline", "Scaling Multi-Regione"]
            }
        ],

        "service_name_en": "Pipeline-Driven Paid Media",
        "service_name_it": "Paid Media Guidato dalla Pipeline"
    },

    {
        "id": "seo_geo",
        "slug": "seo-and-geo-optimization",
        "aliases": [],
        "service_num": "03",
        "pill_label": "03 SEO & GEO",
        
        "meta_title_en": "SEO & Generative Engine Optimization | Francesqui",
        "meta_title_it": "SEO Tecnico & Ottimizzazione GEO | Francesqui",
        "meta_desc_en": "Outrank corporate competitors in high-value B2B niches. Dual-engine SEO and Generative Engine Optimization (GEO) for Google, ChatGPT, and Perplexity.",
        "meta_desc_it": "Supera i grandi competitor sui segmenti B2B ad alto valore. Strategia dual-engine per scalare Google Search e ottenere citazioni su ChatGPT e Perplexity.",

        "eyebrow_en": "SECTOR 03 // TECHNICAL SEO & GENERATIVE AI VISIBILITY",
        "eyebrow_it": "SETTORE 03 // SEO TECNICO & VISIBILITÀ MOTORI GENERATIVI AI",
        "hero_title_en": "Technical SEO & Generative Engine Optimization (GEO).",
        "hero_title_it": "SEO Tecnico & Generative Engine Optimization (GEO).",
        "hero_lead_en": "B2B buyers now research vendors across both Google Search and AI answer engines. I build technical search architecture, Schema.org entity graphs, and high-authority content systems that rank in SERPs and get cited by ChatGPT, Perplexity, and Gemini.",
        "hero_lead_it": "I buyer B2B effettuano ricerche sia su Google che sui motori di risposta AI. Costruisco architetture di ricerca tecnica, grafi di entità Schema.org e contenuti autorevoli per posizionarsi nelle SERP ed essere citati da ChatGPT, Perplexity e Gemini.",

        "metrics_en": [
            {"val": "+40%", "label": "Organic Traffic Growth in 6 Months"},
            {"val": "Dual-Engine", "label": "Google SERP + AI Answer Citation"},
            {"val": "JSON-LD", "label": "Structured Entity Knowledge Graph"}
        ],
        "metrics_it": [
            {"val": "+40%", "label": "Crescita del Traffico Organico in 6 Mesi"},
            {"val": "Dual-Engine", "label": "Risultati Google SERP + Citazioni Motori AI"},
            {"val": "JSON-LD", "label": "Grafo di Conoscenza delle Entità Strutturato"}
        ],

        "contrast_col1_header_en": "LEGACY SEO APPROACH",
        "contrast_col1_header_it": "APPROCCIO SEO TRADIZIONALE",
        "contrast_col1_items_en": [
            "Surface-level blog posts that AI models and B2B buyers ignore.",
            "Unresolved crawl budget waste, slow Core Web Vitals, and broken hreflang.",
            "Zero structured Schema.org microdata defining brand and product entities.",
            "Invisible when prospects ask ChatGPT or Perplexity for vendor recommendations."
        ],
        "contrast_col1_items_it": [
            "Articoli di blog generici e superficiali ignorati sia dai modelli AI che dai buyer B2B.",
            "Spreco di crawl budget irrisolto, Core Web Vitals lenti e tag hreflang non configurati.",
            "Zero microdati strutturati Schema.org a definire le entità del brand e dei prodotti.",
            "Invisibilità totale quando i prospect chiedono raccomandazioni di fornitori a ChatGPT o Perplexity."
        ],
        "contrast_col2_header_en": "TECHNICAL SEO + GEO ARCHITECTURE",
        "contrast_col2_header_it": "ARCHITETTURA SEO TECNICO + GEO",
        "contrast_col2_items_en": [
            "High-information-gain technical pages structured for LLM citation.",
            "Clean site architecture, international hreflang routing, and fast rendering.",
            "Deep JSON-LD entity markup connecting brand authority across the web.",
            "Commercial-intent keyword clusters mapped directly to pipeline revenue."
        ],
        "contrast_col2_items_it": [
            "Pagine tecniche ad alto valore informativo strutturate specificamente per le citazioni LLM.",
            "Architettura del sito pulita, routing internazionale hreflang e rendering ultra-veloce.",
            "Markup approfondito di entità JSON-LD che consolida l'autorevolezza del brand nel web.",
            "Cluster di parole chiave a intenzione commerciale mappati direttamente sul fatturato di pipeline."
        ],

        "stages_en": [
            {
                "num": "01",
                "title": "Technical Crawl & International Architecture",
                "summary": "Resolving indexation bottlenecks, Core Web Vitals, canonicalization, and multi-language hreflang implementation.",
                "pills": ["Technical Audit", "Core Web Vitals", "Hreflang Routing", "Crawl Optimization"]
            },
            {
                "num": "02",
                "title": "Schema.org & Entity Graph Engineering",
                "summary": "Deploying nested JSON-LD microdata (Organization, Service, FAQPage, knowsAbout) to establish machine-readable authority.",
                "pills": ["JSON-LD Schema", "Entity Reconciliation", "Knowledge Graph", "Semantic HTML"]
            },
            {
                "num": "03",
                "title": "Generative Engine Optimization (GEO) Content",
                "summary": "Structuring authoritative, data-backed B2B content clusters engineered for RAG retrieval in AI answer engines.",
                "pills": ["LLM Citation Formatting", "Commercial Topic Clusters", "On-Page Architecture", "Internal Linking"]
            },
            {
                "num": "04",
                "title": "Search Console Telemetry & Attribution",
                "summary": "Tracking organic keyword velocity, AI referral traffic, and assisted CRM pipeline conversions.",
                "pills": ["GSC Telemetry", "Multi-Region Rankings", "AI Referral Tracking", "Organic ROI"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Scansione Tecnica & Architettura Internazionale",
                "summary": "Risoluzione dei colli di bottiglia di indicizzazione, Core Web Vitals, canonical e implementazione hreflang multi-lingua.",
                "pills": ["Audit Tecnico", "Core Web Vitals", "Routing Hreflang", "Ottimizzazione Crawl"]
            },
            {
                "num": "02",
                "title": "Schema.org & Ingegnerizzazione Grafo Entità",
                "summary": "Distribuzione di microdati JSON-LD annidati (Organization, Service, FAQPage, knowsAbout) per stabilire autorevolezza leggibile dalle macchine.",
                "pills": ["Schema JSON-LD", "Riconciliazione Entità", "Grafo di Conoscenza", "HTML Semantico"]
            },
            {
                "num": "03",
                "title": "Contenuti per Generative Engine Optimization (GEO)",
                "summary": "Strutturazione di cluster di contenuti B2B autorevoli e verificabili, progettati per il recupero RAG nei motori di risposta AI.",
                "pills": ["Formattazione per Citazioni LLM", "Cluster Tematici Commerciali", "Architettura On-Page", "Linking Interno"]
            },
            {
                "num": "04",
                "title": "Telemetria Search Console & Attribuzione",
                "summary": "Monitoraggio della velocità delle keyword organiche, del traffico referral da motori AI e delle conversioni assistite nella pipeline CRM.",
                "pills": ["Telemetria GSC", "Posizionamento Multi-Regione", "Tracciamento Referral AI", "ROI Organico"]
            }
        ],

        "service_name_en": "Technical SEO & GEO",
        "service_name_it": "SEO Tecnico & GEO"
    },

    {
        "id": "marketing_data",
        "slug": "marketing-data-reporting",
        "aliases": [],
        "service_num": "04",
        "pill_label": "04 Data & BI",
        
        "meta_title_en": "Data Analytics & Actionable Reporting | Francesqui",
        "meta_title_it": "Marketing Data & Reporting Decisionale | Francesqui",
        "meta_desc_en": "Stop guessing marketing ROI. Connect HubSpot CRM, paid ads, and SEO into one unified executive dashboard with automated Slack delivery for founders.",
        "meta_desc_it": "Basta congetture sul ROI. Unifica HubSpot CRM, campagne ads e SEO in un cruscotto executive con report automatici su Slack per guidare le decisioni aziendali.",

        "eyebrow_en": "SECTOR 04 // ANALYTICS, ATTRIBUTION & EXECUTIVE BI",
        "eyebrow_it": "SETTORE 04 // ANALYTICS, ATTRIBUZIONE & BI DIREZIONALE",
        "hero_title_en": "Marketing Data Modeling & Automated Executive Reporting.",
        "hero_title_it": "Modellazione Dati Marketing & Reporting Direzionale Automatizzato.",
        "hero_lead_en": "Replace conflicting platform numbers and manual Monday morning spreadsheets with an automated analytics infrastructure. I unify your CRM, paid media, and web telemetry into real-time executive dashboards and multi-touch attribution models.",
        "hero_lead_it": "Sostituisci numeri discordanti tra piattaforme e fogli di calcolo manuali con un'infrastruttura di analisi automatizzata. Unifico CRM, paid media e telemetria web in cruscotti direzionali in tempo reale e modelli di attribuzione multi-touch.",

        "metrics_en": [
            {"val": "Single Truth", "label": "Unified Ad Spend + CRM Pipeline"},
            {"val": "Multi-Touch", "label": "Markov & Full-Funnel Attribution"},
            {"val": "Automated", "label": "Real-Time BI & Slack KPI Delivery"}
        ],
        "metrics_it": [
            {"val": "Unica Verità", "label": "Spesa Pubblicitaria e Pipeline CRM Unificate"},
            {"val": "Multi-Touch", "label": "Modelli di Attribuzione Algoritmici & Markov"},
            {"val": "Automatizzato", "label": "BI in Tempo Reale & Alert KPI su Slack"}
        ],

        "contrast_col1_header_en": "FRAGMENTED REPORTING",
        "contrast_col1_header_it": "REPORTISTICA FRAMMENTATA",
        "contrast_col1_items_en": [
            "Hours wasted every week manually copying CSVs into spreadsheets.",
            "Google Ads, LinkedIn, and HubSpot all report conflicting conversion numbers.",
            "Last-click bias hides the true ROI of upper-funnel and trade show touchpoints.",
            "Leadership lacks clear visibility into CAC, pipeline velocity, and ROI by region."
        ],
        "contrast_col1_items_it": [
            "Ore perse ogni settimana a copiare manualmente file CSV su fogli di calcolo.",
            "Google Ads, LinkedIn e HubSpot riportano dati di conversione discordanti.",
            "Il modello last-click nasconde il vero ritorno dei punti di contatto alto-funnel e fiere.",
            "La direzione non ha chiara visibilità su CAC, velocità di pipeline e ROI per mercato."
        ],
        "contrast_col2_header_en": "UNIFIED BI INFRASTRUCTURE",
        "contrast_col2_header_it": "INFRASTRUTTURA BI UNIFICATA",
        "contrast_col2_items_en": [
            "Automated data pipelines syncing ad spend and CRM revenue in real time.",
            "Standardized SQL & GA4 data modeling with strict taxonomy governance.",
            "Algorithmic multi-touch attribution across online and offline channels.",
            "Executive Looker Studio / Power BI dashboards with automated Slack digests."
        ],
        "contrast_col2_items_it": [
            "Pipeline di dati automatizzate che sincronizzano spesa e fatturato CRM in tempo reale.",
            "Modellazione dati standardizzata in SQL e GA4 con rigorosa tassonomia dei parametri.",
            "Attribuzione algoritmica multi-touch sui canali digitali e sugli eventi sul campo.",
            "Dashboard executive in Looker Studio / Power BI con digest automatici programmati su Slack."
        ],

        "stages_en": [
            {
                "num": "01",
                "title": "Measurement Audit & Event Taxonomy",
                "summary": "Standardizing GA4 custom events, UTM parameters, and CRM tracking properties across all acquisition touchpoints.",
                "pills": ["GA4 Architecture", "Event Taxonomy", "Cross-Domain Tracking", "Data Hygiene"]
            },
            {
                "num": "02",
                "title": "SQL Pipeline & Data Normalization",
                "summary": "Joining multi-channel ad spend with CRM deal stages using clean SQL transformations.",
                "pills": ["Oracle / PostgreSQL / BigQuery", "Data Normalization", "CRM API Sync", "Spend-to-Deal Joins"]
            },
            {
                "num": "03",
                "title": "Multi-Touch Attribution Modeling",
                "summary": "Implementing data-driven and Markov Chain attribution to measure true channel lift across digital campaigns and field events.",
                "pills": ["Markov Chain Attribution", "First/Last/Linear Models", "Channel Removal Effect", "ROAS Validation"]
            },
            {
                "num": "04",
                "title": "Executive Dashboards & Automated Briefings",
                "summary": "Building board-ready visual dashboards and scheduled Slack/Email anomaly and performance alerts.",
                "pills": ["Looker Studio / Power BI", "Executive KPI Views", "Automated Slack Alerts", "Board Reporting"]
            }
        ],
        "stages_it": [
            {
                "num": "01",
                "title": "Audit di Misurazione & Tassonomia Eventi",
                "summary": "Standardizzazione di eventi personalizzati GA4, parametri UTM e proprietà di tracciamento CRM su tutti i punti di contatto.",
                "pills": ["Architettura GA4", "Tassonomia Eventi", "Tracciamento Cross-Domain", "Igiene Dati"]
            },
            {
                "num": "02",
                "title": "Pipeline SQL & Normalizzazione Dati",
                "summary": "Unione della spesa adv multicanale con le fasi di trattativa CRM mediante trasformazioni SQL pulite.",
                "pills": ["Oracle / PostgreSQL / BigQuery", "Normalizzazione Dati", "Sincronizzazione API CRM", "Join Spesa-Trattative"]
            },
            {
                "num": "03",
                "title": "Modellazione Attribuzione Multi-Touch",
                "summary": "Implementazione di modelli data-driven e catene di Markov per misurare il reale impatto incrementale di campagne ed eventi.",
                "pills": ["Attribuzione Catene di Markov", "Modelli First/Last/Lineare", "Effetto Rimozione Canale", "Validazione ROAS"]
            },
            {
                "num": "04",
                "title": "Cruscotti Direzionali & Briefing Automatizzati",
                "summary": "Creazione di dashboard visive pronte per il Board e avvisi automatici di anomalie e performance via Slack/Email.",
                "pills": ["Looker Studio / Power BI", "Viste KPI Direzionali", "Alert Automatici Slack", "Reporting per il CDA"]
            }
        ],

        "service_name_en": "Marketing Data Modeling & Reporting",
        "service_name_it": "Marketing Data Modeling e Reporting"
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
    
    --text-primary: #fcfbf9;
    --text-secondary: #a8a197;
    --text-muted: #6e675d;
    
    --border-hairline: rgba(255, 255, 255, 0.08);
    --border-gold: rgba(212, 168, 99, 0.45);
    
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

.service-switcher {
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

/* 2. Minimalist Contrast Table (Before vs After) */
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

/* 3. Scroll-Driven Orbital Light Thread & Accordion Stages */
.orbital-timeline {
    position: relative;
    padding-left: 2.75rem;
}

/* Static 1px background track */
.orbital-track-bg {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 7px;
    width: 1px;
    background: var(--border-hairline);
}

/* Dynamic scroll-filled 1px gold light line */
.orbital-track-fill {
    position: absolute;
    top: 0;
    left: 7px;
    width: 1px;
    height: 0%;
    background: linear-gradient(180deg, transparent, var(--accent-gold), #fff);
    transition: height 0.1s linear;
}

/* Sleek 9px diamond spacecraft/telemetry node */
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

/* 4. Minimalist Executive CTA Footer */
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
    transition: border-color 0.2s;
}

.btn-ghost:hover {
    border-color: var(--border-gold);
    color: var(--accent-gold);
}

@media (max-width: 768px) {
    .service-switcher { display: none; }
    .metrics-strip, .contrast-grid { grid-template-columns: 1fr; }
    .contrast-col + .contrast-col { border-left: none; border-top: 1px solid var(--border-hairline); }
    .cta-console { flex-direction: column; align-items: flex-start; }
}
"""

MASTER_JS = """
document.addEventListener('DOMContentLoaded', () => {
    const timeline = document.querySelector('.orbital-timeline');
    const fill = document.querySelector('.orbital-track-fill');
    const node = document.querySelector('.orbital-node');
    const cards = document.querySelectorAll('.stage-card');

    // Accordion toggle
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const wasOpen = card.classList.contains('open');
            cards.forEach(c => c.classList.remove('open'));
            if (!wasOpen) card.classList.add('open');
        });
    });

    // Subtle Scroll-Driven Orbital Thread
    function updateOrbitalThread() {
        if (!timeline) return;
        const rect = timeline.getBoundingClientRect();
        const winH = window.innerHeight;
        const start = winH * 0.65;
        const progress = Math.max(0, Math.min(1, (start - rect.top) / rect.height));
        const pct = (progress * 100).toFixed(1) + '%';
        if (fill) fill.style.height = pct;
        if (node) node.style.top = pct;

        cards.forEach((card, idx) => {
            const cRect = card.getBoundingClientRect();
            card.classList.toggle('active-stage', cRect.top < start && cRect.bottom > winH * 0.25);
        });
    }

    window.addEventListener('scroll', updateOrbitalThread, { passive: true });
    updateOrbitalThread();
});
"""

def render_service_html(service, lang="en", current_slug=None):
    if current_slug is None:
        current_slug = service['slug']

    is_it = (lang == "it")
    canonical_base = "https://renzo-francesqui.vercel.app"
    canonical_slug = service['slug']
    en_canonical_url = f"{canonical_base}/services/{canonical_slug}/"
    it_canonical_url = f"{canonical_base}/it/services/{canonical_slug}/"
    page_canonical = it_canonical_url if is_it else en_canonical_url
    
    if is_it:
        page_url = f"{canonical_base}/it/services/{current_slug}/"
        en_url = f"{canonical_base}/services/{current_slug}/"
        it_url = f"{canonical_base}/it/services/{current_slug}/"
        en_toggle_href = f"/services/{canonical_slug}/"
        it_toggle_href = f"/it/services/{canonical_slug}/"
    else:
        page_url = f"{canonical_base}/services/{current_slug}/"
        en_url = f"{canonical_base}/services/{current_slug}/"
        it_url = f"{canonical_base}/it/services/{current_slug}/"
        en_toggle_href = f"/services/{canonical_slug}/"
        it_toggle_href = f"/it/services/{canonical_slug}/"

    meta_title = service['meta_title_it'] if is_it else service['meta_title_en']
    meta_desc = service['meta_desc_it'] if is_it else service['meta_desc_en']
    eyebrow = service['eyebrow_it'] if is_it else service['eyebrow_en']
    hero_title = service['hero_title_it'] if is_it else service['hero_title_en']
    hero_lead = service['hero_lead_it'] if is_it else service['hero_lead_en']

    metrics = service['metrics_it'] if is_it else service['metrics_en']
    c1_header = service['contrast_col1_header_it'] if is_it else service['contrast_col1_header_en']
    c2_header = service['contrast_col2_header_it'] if is_it else service['contrast_col2_header_en']
    c1_items = service['contrast_col1_items_it'] if is_it else service['contrast_col1_items_en']
    c2_items = service['contrast_col2_items_it'] if is_it else service['contrast_col2_items_en']

    stages = service['stages_it'] if is_it else service['stages_en']
    service_name = service['service_name_it'] if is_it else service['service_name_en']

    # CTA localized strings
    if is_it:
        section1_index = "01 // DIAGNOSTICA OPERATIVA"
        section1_heading = "Lo Status Quo Inefficiente vs. Il Sistema Scalabile"
        section2_index = "02 // PROTOCOLLO ESECUTIVO"
        section2_heading = "Metodologia di Ingegnerizzazione in Quattro Fasi"
        cta_heading = "Pronto a ingegnerizzare questo sistema?"
        cta_sub = "Disponibile per consulenza strategica freelance e architettura RevOps nei mercati EMEA e globali."
        cta_btn_primary = "Richiedi via Email ✉️"
        cta_btn_secondary = "Ritorna alla Matrice Solare 🪐"
        back_text = "Matrice Solare"
        encoded_subject = urllib.parse.quote(f"Richiesta Consulenza — {service_name}", safe="—")
    else:
        section1_index = "01 // DIAGNOSTIC CONTRAST"
        section1_heading = "Operational Failure vs. Engineered Revenue Architecture"
        section2_index = "02 // EXECUTION PROTOCOL"
        section2_heading = "Four-Stage Engineering Methodology"
        cta_heading = "Ready to architect this system?"
        cta_sub = "Available for strategic freelance consulting and RevOps architecture across EMEA and global markets."
        cta_btn_primary = "Inquire via Email ✉️"
        cta_btn_secondary = "Back to 3D Solar Matrix 🪐"
        back_text = "Solar Matrix"
        encoded_subject = urllib.parse.quote(f"Consulting Inquiry — {service_name}", safe="—")

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

    # Service switcher pills HTML
    switcher_pills_html = ""
    for s in SERVICES_DATA:
        active_cls = " active" if s['id'] == service['id'] else ""
        target_slug = s['slug']
        pill_href = f"/it/services/{target_slug}/" if is_it else f"/services/{target_slug}/"
        switcher_pills_html += f"""
            <a href="{pill_href}" class="switch-pill{active_cls}">{s['pill_label']}</a>"""

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
                "mainEntity": { "@id": f"{page_url}#service" }
            },
            {
                "@type": "Service",
                "@id": f"{page_url}#service",
                "serviceType": service_name,
                "name": meta_title.split('|')[0].strip(),
                "description": hero_lead,
                "provider": {
                    "@type": "Person",
                    "@id": f"{canonical_base}/it/#person" if is_it else f"{canonical_base}/#person",
                    "name": "Renzo Francesqui",
                    "jobTitle": "Specialista Marketing Operations & Architetture RevOps" if is_it else "Marketing Operations & RevOps Specialist",
                    "address": {
                        "@type": "PostalAddress",
                        "addressLocality": "Milano" if is_it else "Milan",
                        "addressRegion": "Lombardy",
                        "addressCountry": "IT"
                    }
                },
                "audience": {
                    "@type": "BusinessAudience",
                    "audienceType": "Founder di Startup e Leader B2B" if is_it else "B2B Leaders and Startup Founders"
                }
            },
            {
                "@type": "Organization",
                "@id": f"{canonical_base}/it/#organization" if is_it else f"{canonical_base}/#organization",
                "name": "Renzo Francesqui RevOps & Growth Consulting" if is_it else "Renzo Francesqui Consulting",
                "url": f"{canonical_base}/it/" if is_it else f"{canonical_base}/",
                "areaServed": [
                    { "@type": "City", "name": "Milano, Italy" },
                    { "@type": "AdministrativeArea", "name": "Lombardy" }
                ] if is_it else "EMEA & Global"
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{page_url}#breadcrumb",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Home", "item": f"{canonical_base}/it/" if is_it else f"{canonical_base}/" },
                    { "@type": "ListItem", "position": 2, "name": "Servizi" if is_it else "Services", "item": f"{canonical_base}/it/#services" if is_it else f"{canonical_base}/#services" },
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

            <nav class="service-switcher">{switcher_pills_html}
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

        <!-- 2. Minimalist Contrast Table (Before vs After) -->
        <section>
            <span class="section-index">{section1_index}</span>
            <h2 class="section-heading">{section1_heading}</h2>
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

        <!-- 3. Scroll-Driven Orbital Light Thread & Accordion Stages -->
        <section>
            <span class="section-index">{section2_index}</span>
            <h2 class="section-heading">{section2_heading}</h2>
            <div class="orbital-timeline">
                <div class="orbital-track-bg"></div>
                <div class="orbital-track-fill"></div>
                <div class="orbital-node"></div>{stages_html}
            </div>
        </section>

        <!-- 4. Minimalist Executive CTA Footer -->
        <div class="cta-console">
            <div>
                <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.35rem;">{cta_heading}</h3>
                <p style="font-size: 0.88rem; color: var(--text-secondary);">{cta_sub}</p>
            </div>
            <div class="cta-actions">
                <a href="mailto:renzo.francesqui@gmail.com?subject={encoded_subject}" class="btn-gold">{cta_btn_primary}</a>
                <a href="../../index.html" class="btn-ghost">{cta_btn_secondary}</a>
            </div>
        </div>
    </main>

    <!-- Subtle Scroll & Accordion JavaScript -->
    <script>{MASTER_JS}
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
        en_html = render_service_html(service, lang="en")
        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_html)
        count += 1

        # 2. Italian page: it/services/<slug>/index.html
        it_dir = BASE_DIR / "it" / "services" / service['slug']
        it_dir.mkdir(parents=True, exist_ok=True)
        it_file = it_dir / "index.html"
        it_html = render_service_html(service, lang="it")
        with open(it_file, "w", encoding="utf-8") as f:
            f.write(it_html)
        count += 1

        # 3. Aliases (if any)
        for alias_slug in service.get("aliases", []):
            alias_en_dir = BASE_DIR / "services" / alias_slug
            alias_en_dir.mkdir(parents=True, exist_ok=True)
            alias_en_file = alias_en_dir / "index.html"
            alias_en_html = render_service_html(service, lang="en", current_slug=alias_slug)
            with open(alias_en_file, "w", encoding="utf-8") as f:
                f.write(alias_en_html)
            count += 1

            alias_it_dir = BASE_DIR / "it" / "services" / alias_slug
            alias_it_dir.mkdir(parents=True, exist_ok=True)
            alias_it_file = alias_it_dir / "index.html"
            alias_it_html = render_service_html(service, lang="it", current_slug=alias_slug)
            with open(alias_it_file, "w", encoding="utf-8") as f:
                f.write(alias_it_html)
            count += 1

    print(f"[OK] Generated {count} minimalist editorial freelance service landing pages (EN and IT).")

if __name__ == "__main__":
    build_all_services()
