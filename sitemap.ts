import { MetadataRoute } from 'next';

const BASE_URL = 'https://renzo-francesqui.vercel.app';

export default function sitemap(): MetadataRoute.Sitemap {
  const currentDate = new Date().toISOString().split('T')[0];

  return [
    // Primary English Default Route
    {
      url: `${BASE_URL}/`,
      lastModified: currentDate,
      changeFrequency: 'weekly',
      priority: 1.0,
      alternates: {
        languages: {
          en: `${BASE_URL}/`,
          it: `${BASE_URL}/it/`,
          'x-default': `${BASE_URL}/`,
        },
      },
    },
    // Italian Localized Route
    {
      url: `${BASE_URL}/it/`,
      lastModified: currentDate,
      changeFrequency: 'weekly',
      priority: 0.98,
      alternates: {
        languages: {
          en: `${BASE_URL}/`,
          it: `${BASE_URL}/it/`,
          'x-default': `${BASE_URL}/`,
        },
      },
    },
    // Dedicated Blog Hub
    {
      url: `${BASE_URL}/blog/`,
      lastModified: currentDate,
      changeFrequency: 'weekly',
      priority: 0.9,
    },
    // Version 1.5 Architecture
    {
      url: `${BASE_URL}/version-1.5/`,
      lastModified: currentDate,
      changeFrequency: 'weekly',
      priority: 0.85,
    },
    // Standalone Blog Post: HubSpot AI Enrichment Agent
    {
      url: `${BASE_URL}/blog/hubspot-ai-enrichment-agent.html`,
      lastModified: '2026-03-15',
      changeFrequency: 'monthly',
      priority: 0.85,
    },
    // Standalone Blog Post: B2B Event Lead Operations
    {
      url: `${BASE_URL}/blog/b2b-event-lead-operations.html`,
      lastModified: '2026-03-20',
      changeFrequency: 'monthly',
      priority: 0.85,
    },
    // Standalone Blog Post: Modern RevOps Lifecycle Architecture
    {
      url: `${BASE_URL}/blog/modern-revops-lifecycle-architecture.html`,
      lastModified: '2026-03-25',
      changeFrequency: 'monthly',
      priority: 0.85,
    },
  ];
}
