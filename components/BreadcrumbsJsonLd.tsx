'use client';

import React from 'react';
import { usePathname } from 'next/navigation';

/**
 * Interface representing an individual item within the breadcrumb hierarchy.
 */
export interface BreadcrumbSegment {
  name: string;
  item: string;
}

export interface BreadcrumbsJsonLdProps {
  /**
   * Explicit breadcrumb items (e.g., [{ name: 'Home', item: '/' }, { name: 'Services', item: '/services' }]).
   * If provided, overrides dynamic parsing from pathname.
   */
  items?: BreadcrumbSegment[];
  /**
   * The current URL path or route string (e.g., '/services/crm-optimization').
   * If omitted, dynamically extracted from the Next.js App Router usePathname() hook.
   */
  pathname?: string;
  /**
   * Production domain / base URL. Defaults to 'https://renzo-francesqui.vercel.app'
   */
  baseUrl?: string;
}

/**
 * Set of technical and marketing acronyms that must retain uppercase formatting.
 */
const ACRONYMS: Record<string, string> = {
  crm: 'CRM',
  seo: 'SEO',
  geo: 'GEO',
  ai: 'AI',
  b2b: 'B2B',
  api: 'API',
  revops: 'RevOps',
  hubspot: 'HubSpot',
  salesforce: 'Salesforce',
  sql: 'SQL',
  ga4: 'GA4',
  sla: 'SLA',
  kpi: 'KPI',
  cac: 'CAC',
  mql: 'MQL',
  gtm: 'GTM',
  emea: 'EMEA',
  utm: 'UTM',
  roi: 'ROI',
};

/**
 * Known route slug dictionaries for humanized breadcrumb labels.
 */
const KNOWN_SLUGS_EN: Record<string, string> = {
  '': 'Home',
  'services': 'Services',
  'servizi': 'Services',
  'tools': 'Tools',
  'blog': 'Blog',
  'crm-optimization': 'CRM Optimization',
  'hubspot-crm-optimization-startups': 'HubSpot CRM Setup & RevOps Architecture',
  'small-startup-business-crm-setup-optimization': 'HubSpot CRM Setup & RevOps Architecture',
  'paid-media-management': 'Paid Media Management',
  'seo-and-geo-optimization': 'SEO & GEO Optimization',
  'marketing-data-reporting': 'Marketing Data & Reporting',
  'mql-to-sql-sla-lead-leakage-calculator': 'MQL-to-SQL SLA & Lead Leakage Calculator',
  'b2b-campaign-utm-crm-builder': 'B2B Campaign UTM & CRM Governance Builder',
  'b2b-trade-show-roi-calculator': 'B2B Trade Show & Exhibition ROI Modeler',
  'hubspot-ai-enrichment-agent.html': 'HubSpot AI Enrichment Agent',
  'hubspot-ai-enrichment-agent': 'HubSpot AI Enrichment Agent',
  'b2b-event-lead-operations.html': 'B2B Event Lead Operations',
  'b2b-event-lead-operations': 'B2B Event Lead Operations',
  'modern-revops-lifecycle-architecture.html': 'Modern RevOps Lifecycle Architecture',
  'modern-revops-lifecycle-architecture': 'Modern RevOps Lifecycle Architecture',
  'classic': 'Classic Edition',
  'version-1.5': 'Version 1.5',
  'version-3': 'Version 3.0',
};

const KNOWN_SLUGS_IT: Record<string, string> = {
  '': 'Home',
  'services': 'Servizi',
  'servizi': 'Servizi',
  'tools': 'Strumenti',
  'strumenti': 'Strumenti',
  'blog': 'Blog',
  'crm-optimization': 'Ottimizzazione CRM',
  'hubspot-crm-optimization-startups': 'Setup & Architettura HubSpot CRM & RevOps',
  'small-startup-business-crm-setup-optimization': 'Setup & Architettura HubSpot CRM & RevOps',
  'paid-media-management': 'Gestione Paid Media',
  'seo-and-geo-optimization': 'SEO Tecnico & Ottimizzazione GEO',
  'marketing-data-reporting': 'Dati Marketing & Reportistica',
  'mql-to-sql-sla-lead-leakage-calculator': 'Calcolatore Leakage & SLA MQL-to-SQL',
  'b2b-campaign-utm-crm-builder': 'Generatore UTM & Governance CRM B2B',
  'b2b-trade-show-roi-calculator': 'Calcolatore ROI Fiere ed Esposizioni B2B',
  'hubspot-ai-enrichment-agent.html': 'Agente AI Arricchimento HubSpot',
  'hubspot-ai-enrichment-agent': 'Agente AI Arricchimento HubSpot',
  'b2b-event-lead-operations.html': 'Operazioni Lead Fiere B2B',
  'b2b-event-lead-operations': 'Operazioni Lead Fiere B2B',
  'modern-revops-lifecycle-architecture.html': 'Architettura Lifecycle RevOps',
  'modern-revops-lifecycle-architecture': 'Architettura Lifecycle RevOps',
  'classic': 'Edizione Classica',
  'version-1.5': 'Versione 1.5',
  'version-3': 'Versione 3.0',
};

/**
 * Converts a URL slug into Title Case, respecting known dictionary terms and acronyms.
 */
export function humanizeSlug(slug: string, isItalian: boolean = false): string {
  const normalized = slug.toLowerCase();
  const dict = isItalian ? KNOWN_SLUGS_IT : KNOWN_SLUGS_EN;

  if (dict[normalized]) {
    return dict[normalized];
  }

  // Fallback slug humanization
  const cleaned = slug.replace(/\.html$/i, '');
  return cleaned
    .split(/[-_]+/)
    .filter(Boolean)
    .map((word) => {
      const lower = word.toLowerCase();
      if (ACRONYMS[lower]) {
        return ACRONYMS[lower];
      }
      return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    })
    .join(' ');
}

/**
 * Dynamically converts a route pathname into a structured array of breadcrumb items.
 * Example: '/services/crm-optimization' ->
 * [
 *   { name: 'Home', item: 'https://renzo-francesqui.vercel.app/' },
 *   { name: 'Services', item: 'https://renzo-francesqui.vercel.app/services/' },
 *   { name: 'CRM Optimization', item: 'https://renzo-francesqui.vercel.app/services/crm-optimization/' }
 * ]
 */
export function generateBreadcrumbsFromPath(
  pathname: string,
  baseUrl: string = 'https://renzo-francesqui.vercel.app'
): BreadcrumbSegment[] {
  const domain = baseUrl.replace(/\/+$/, '');
  const cleanPath = (pathname || '/').split(/[?#]/)[0];
  const segments = cleanPath.split('/').filter(Boolean);

  const isItalian = segments[0] === 'it';
  const rootLabel = 'Home';
  const rootUrl = isItalian ? `${domain}/it/` : `${domain}/`;

  const crumbs: BreadcrumbSegment[] = [
    {
      name: rootLabel,
      item: rootUrl,
    },
  ];

  let currentPath = isItalian ? '/it' : '';
  const remainingSegments = isItalian ? segments.slice(1) : segments;

  for (const seg of remainingSegments) {
    currentPath += `/${seg}`;
    const name = humanizeSlug(seg, isItalian);
    const item = `${domain}${currentPath}${seg.endsWith('.html') ? '' : '/'}`;
    crumbs.push({ name, item });
  }

  return crumbs;
}

/**
 * Pure helper function to generate the Schema.org BreadcrumbList JSON-LD object.
 * Can be used in Server Components, API routes, or generateMetadata.
 */
export function generateBreadcrumbJsonLd(
  pathnameOrItems: string | BreadcrumbSegment[],
  baseUrl: string = 'https://renzo-francesqui.vercel.app'
) {
  const domain = baseUrl.replace(/\/+$/, '');
  let breadcrumbs: BreadcrumbSegment[];

  if (Array.isArray(pathnameOrItems)) {
    breadcrumbs = pathnameOrItems.map((crumb) => ({
      name: crumb.name,
      item: crumb.item.startsWith('http')
        ? crumb.item
        : `${domain}${crumb.item.startsWith('/') ? crumb.item : '/' + crumb.item}`,
    }));
  } else {
    breadcrumbs = generateBreadcrumbsFromPath(pathnameOrItems, domain);
  }

  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: breadcrumbs.map((crumb, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: crumb.name,
      item: crumb.item,
    })),
  };
}

/**
 * BreadcrumbsJsonLd
 * Reusable React component that generates Schema.org BreadcrumbList JSON-LD structured data.
 * Dynamically computes from the current route via usePathname() or accepts explicit props.
 */
export function BreadcrumbsJsonLd({
  items,
  pathname: explicitPathname,
  baseUrl = 'https://renzo-francesqui.vercel.app',
}: BreadcrumbsJsonLdProps) {
  let hookPathname: string | null = null;
  try {
    // Dynamic client-side route discovery in Next.js App Router
    hookPathname = usePathname();
  } catch {
    hookPathname = null;
  }

  const effectivePathname = explicitPathname || hookPathname || '/';
  const jsonLd = generateBreadcrumbJsonLd(items || effectivePathname, baseUrl);

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
    />
  );
}

export default BreadcrumbsJsonLd;
