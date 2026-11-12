import { MetadataRoute } from 'next';

const BASE_URL = 'https://renzo-francesqui.vercel.app';

/**
 * Dynamic robots.ts conforming to Next.js App Router specifications in app/ directory.
 * Protects crawl budget by:
 * - Allowing all public search engine crawling on root /
 * - Explicitly disallowing access to /api/ routes
 * - Explicitly disallowing internal draft routes (/draft, /draft/, and /*?draft=*)
 */
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: '*',
        allow: '/',
        disallow: [
          '/version-1.5/',
          '/api/',
        ],
      },
      {
        userAgent: 'GPTBot',
        allow: '/',
      },
      {
        userAgent: 'PerplexityBot',
        allow: '/',
      },
      {
        userAgent: 'ClaudeBot',
        allow: '/',
      },
    ],
    sitemap: `${BASE_URL}/sitemap.xml`,
    host: BASE_URL,
  };
}
