import type { Metadata } from 'next';
import React from 'react';

export const PRODUCTION_DOMAIN = 'https://renzo-francesqui.vercel.app';

/**
 * Root Layout for Next.js App Router
 * 
 * Requirement 1: Absolute URLs (metadataBase)
 * metadataBase ensures that all dynamically generated canonical tags,
 * alternate language links, and Open Graph / Twitter image URLs resolve
 * against the production domain: https://renzo-francesqui.vercel.app
 */
export const metadata: Metadata = {
  metadataBase: new URL(PRODUCTION_DOMAIN),
  title: {
    default: 'Renzo Francesqui — Digital Marketing, CRM Architecture & RevOps',
    template: '%s | Renzo Francesqui',
  },
  description:
    'Digital Marketing, CRM Architecture & RevOps Specialist based in Milan, Italy. HubSpot CRM setups, paid media management, SEO/GEO optimization, and actionable business intelligence.',
  applicationName: 'Renzo Francesqui Portfolio',
  authors: [{ name: 'Renzo Francesqui', url: PRODUCTION_DOMAIN }],
  creator: 'Renzo Francesqui',
  publisher: 'Renzo Francesqui',
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
    title: 'Renzo Francesqui — Digital Marketing, CRM Architecture & RevOps',
    description:
      'Digital Marketing, CRM Architecture & RevOps Specialist based in Milan, Italy. HubSpot CRM setups, paid media management, SEO/GEO optimization, and actionable business intelligence.',
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
        alt: 'Renzo Francesqui — RevOps Architecture & Digital Marketing Specialist',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Renzo Francesqui — Digital Marketing, CRM Architecture & RevOps',
    description:
      'Digital Marketing, CRM Architecture & RevOps Specialist based in Milan, Italy. HubSpot CRM setups, paid media management, SEO/GEO optimization, and actionable business intelligence.',
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
 * Helper utility to build dynamic child page metadata guaranteed to produce
 * absolute canonical tags and absolute Open Graph / Twitter image URLs.
 * With metadataBase defined above, passing relative paths here automatically
 * resolves them into complete absolute URLs under https://renzo-francesqui.vercel.app.
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
      </head>
      <body>{children}</body>
    </html>
  );
}
