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
    // Service Pages
    {
      url: `${BASE_URL}/services/hubspot-crm-optimization-startups`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.9,
      alternates: {
        languages: {
          en: `${BASE_URL}/services/hubspot-crm-optimization-startups`,
          it: `${BASE_URL}/it/services/hubspot-crm-optimization-startups`,
          'x-default': `${BASE_URL}/services/hubspot-crm-optimization-startups`,
        },
      },
    },
    {
      url: `${BASE_URL}/services/paid-media-management`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.9,
      alternates: {
        languages: {
          en: `${BASE_URL}/services/paid-media-management`,
          it: `${BASE_URL}/it/services/paid-media-management`,
          'x-default': `${BASE_URL}/services/paid-media-management`,
        },
      },
    },
    {
      url: `${BASE_URL}/services/seo-and-geo-optimization`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.9,
      alternates: {
        languages: {
          en: `${BASE_URL}/services/seo-and-geo-optimization`,
          it: `${BASE_URL}/it/services/seo-and-geo-optimization`,
          'x-default': `${BASE_URL}/services/seo-and-geo-optimization`,
        },
      },
    },
    {
      url: `${BASE_URL}/services/marketing-data-reporting`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.9,
      alternates: {
        languages: {
          en: `${BASE_URL}/services/marketing-data-reporting`,
          it: `${BASE_URL}/it/services/marketing-data-reporting`,
          'x-default': `${BASE_URL}/services/marketing-data-reporting`,
        },
      },
    },
    // Interactive Utility Tools
    {
      url: `${BASE_URL}/tools/mql-to-sql-sla-lead-leakage-calculator`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: `${BASE_URL}/tools/b2b-campaign-utm-crm-builder`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: `${BASE_URL}/tools/b2b-trade-show-roi-calculator`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    // Blog & Insights Articles
    {
      url: `${BASE_URL}/blog/hubspot-ai-enrichment-agent`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.7,
    },
    {
      url: `${BASE_URL}/blog/b2b-event-lead-operations`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.7,
    },
    {
      url: `${BASE_URL}/blog/modern-revops-lifecycle-architecture`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.7,
    },
  ];
}
