import type { Metadata } from 'next';
import React from 'react';

export const BASE_URL = 'https://renzo-francesqui.vercel.app';
export const PRODUCTION_DOMAIN = BASE_URL;
export const BRAND_TITLE = 'Marketing Operations Specialist | CRM & RevOps Architect | Automation & AI Workflows';
export const PERSON_NAME = 'Renzo Francesqui';

/**
 * Root Layout for Next.js App Router
 * 
 * Requirement 1: Absolute URLs (metadataBase)
 * metadataBase ensures that all dynamically generated canonical tags,
 * alternate language links, and Open Graph / Twitter image URLs resolve
 * against the production domain: https://renzo-francesqui.vercel.app
 */
export const metadata: Metadata = {
  metadataBase: new URL(BASE_URL),
  title: {
    default: 'Renzo Francesqui | Marketing Operations Specialist | CRM & RevOps Architect',
    template: '%s | Renzo Francesqui',
  },
  description:
    'Marketing Operations Specialist & CRM/RevOps Architect specializing in HubSpot & Salesforce architecture, B2B pipeline automation, and custom AI enrichment workflows.',
  applicationName: 'Renzo Francesqui Portfolio',
  authors: [{ name: PERSON_NAME, url: BASE_URL }],
  creator: PERSON_NAME,
  publisher: PERSON_NAME,
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  alternates: {
    canonical: '/',
    languages: {
      'en': '/',
      'it': '/it/',
      'x-default': '/',
    },
  },
  openGraph: {
    title: 'Renzo Francesqui | Marketing Operations Specialist | CRM & RevOps Architect | Automation & AI Workflows',
    description:
      'Marketing Operations Specialist & CRM/RevOps Architect specializing in HubSpot & Salesforce architecture, B2B pipeline automation, and custom AI enrichment workflows.',
    url: '/',
    siteName: 'Renzo Francesqui Portfolio',
    locale: 'en_US',
    alternateLocale: ['it_IT'],
    type: 'website',
    images: [
      {
        url: '/images/renzo-francesqui.jpg',
        width: 1200,
        height: 630,
        alt: 'Renzo Francesqui | Marketing Operations Specialist | CRM & RevOps Architect | Automation & AI Workflows',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Renzo Francesqui | Marketing Operations Specialist | CRM & RevOps Architect | Automation & AI Workflows',
    description:
      'Marketing Operations Specialist & CRM/RevOps Architect specializing in HubSpot & Salesforce architecture, B2B pipeline automation, and custom AI enrichment workflows.',
    images: ['/images/renzo-francesqui.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

/**
 * Step 7: Global Connected JSON-LD Schema
 */
const GLOBAL_SCHEMA = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Person',
      '@id': `${BASE_URL}/#person`,
      'name': PERSON_NAME,
      'url': `${BASE_URL}/`,
      'jobTitle': BRAND_TITLE,
      'description': 'Marketing Operations Specialist and CRM & RevOps Architect engineering enterprise pipeline governance, lead scoring, and automated AI enrichment workflows.',
      'worksFor': {
        '@type': 'Organization',
        'name': 'Freelance RevOps & Marketing Operations',
      },
      'sameAs': [
        'https://www.linkedin.com/in/renzofrancesqui',
      ],
    },
    {
      '@type': 'ProfessionalService',
      '@id': `${BASE_URL}/#business`,
      'name': 'Renzo Francesqui — RevOps Architecture & Growth Consulting',
      'url': `${BASE_URL}/`,
      'founder': { '@id': `${BASE_URL}/#person` },
      'areaServed': ['EMEA', 'US', 'IT'],
      'hasOfferCatalog': {
        '@type': 'OfferCatalog',
        'name': 'B2B RevOps & Growth Services',
        'itemListElement': [
          {
            '@type': 'Offer',
            'itemOffered': {
              '@type': 'Service',
              'name': 'HubSpot & Salesforce CRM Architecture',
              'description': 'Lifecycle modeling, MQL-to-SQL routing SLAs, and pipeline hygiene.',
            },
          },
          {
            '@type': 'Offer',
            'itemOffered': {
              '@type': 'Service',
              'name': 'B2B Paid Media & ABM Management',
              'description': 'Closed-loop offline CRM attribution and intent-driven search acquisition.',
            },
          },
          {
            '@type': 'Offer',
            'itemOffered': {
              '@type': 'Service',
              'name': 'Technical SEO & Generative Engine Optimization',
              'description': 'Core Web Vitals optimization and AI engine visibility modeling.',
            },
          },
          {
            '@type': 'Offer',
            'itemOffered': {
              '@type': 'Service',
              'name': 'Marketing Data Modeling & Executive BI',
              'description': 'SQL pipelines, Markov Chain attribution, and Looker Studio dashboards.',
            },
          },
        ],
      },
    },
  ],
};

/**
 * Helper utility to build dynamic child page metadata guaranteed to produce
 * absolute canonical tags and absolute Open Graph / Twitter image URLs.
 */
export function constructDynamicMetadata({
  title,
  description,
  path = '/',
  ogImage = '/images/renzo-francesqui.jpg',
  noIndex = false,
}: {
  title?: string;
  description?: string;
  path?: string;
  ogImage?: string;
  noIndex?: boolean;
}): Metadata {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return {
    title,
    description,
    alternates: {
      canonical: normalizedPath,
    },
    openGraph: {
      title: title ? `${title} | Renzo Francesqui` : undefined,
      description,
      url: normalizedPath,
      images: [
        {
          url: ogImage,
        },
      ],
    },
    twitter: {
      title: title ? `${title} | Renzo Francesqui` : undefined,
      description,
      images: [ogImage],
    },
    ...(noIndex && {
      robots: {
        index: false,
        follow: false,
      },
    }),
  };
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" data-theme="dark">
      <head>
        <link rel="icon" href="/favicon.ico" />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(GLOBAL_SCHEMA) }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
