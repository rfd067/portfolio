import React from 'react';

export interface ItalianGeographicSchemaProps {
  baseUrl?: string;
}

/**
 * ItalianGeographicSchema
 * 
 * Requirement 3: Geographic Schema (Milan / Lombardy)
 * Reusable Next.js component providing Schema.org Person & Organization structured data
 * with areaServed and location targeting Milano, Italy and Lombardy to capture local search intent.
 */
export function ItalianGeographicSchema({
  baseUrl = 'https://renzo-francesqui.vercel.app',
}: ItalianGeographicSchemaProps) {
  const domain = baseUrl.replace(/\/+$/, '');

  const schemaGraph = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Person',
        '@id': `${domain}/it/#person`,
        'name': 'Renzo Francesqui',
        'jobTitle': 'Specialista in Marketing Operations & RevOps',
        'description':
          'Specialista in Marketing Digitale, Revenue Operations (RevOps), architettura CRM HubSpot e automazione di workflow di marketing basati su AI basato a Milano.',
        'url': `${domain}/it/`,
        'image': `${domain}/images/renzo-francesqui.jpg`,
        'sameAs': ['https://www.linkedin.com/in/renzofrancesqui/'],
        'areaServed': [
          {
            '@type': 'City',
            'name': 'Milano, Italy',
          },
          {
            '@type': 'AdministrativeArea',
            'name': 'Lombardy',
          },
        ],
        'location': {
          '@type': 'Place',
          'name': 'Milano, Italy',
          'address': {
            '@type': 'PostalAddress',
            'addressLocality': 'Milano',
            'addressRegion': 'Lombardy',
            'addressCountry': 'IT',
          },
        },
        'worksFor': {
          '@type': 'Organization',
          '@id': `${domain}/it/#organization`,
        },
        'knowsAbout': [
          'CRM HubSpot',
          'Revenue Operations (RevOps)',
          'Automazione Marketing AI',
          'Lead Scoring & Lifecycle Management',
          'Go-To-Market (GTM) Strategy',
          'Performance Marketing',
          'Salesforce Administration',
          'Oracle SQL',
        ],
      },
      {
        '@type': 'Organization',
        '@id': `${domain}/it/#organization`,
        'name': 'Renzo Francesqui RevOps & Growth Consulting',
        'url': `${domain}/it/`,
        'logo': `${domain}/images/renzo-francesqui.jpg`,
        'areaServed': [
          {
            '@type': 'City',
            'name': 'Milano, Italy',
          },
          {
            '@type': 'AdministrativeArea',
            'name': 'Lombardy',
          },
        ],
        'location': {
          '@type': 'Place',
          'name': 'Milano, Italy',
          'address': {
            '@type': 'PostalAddress',
            'addressLocality': 'Milano',
            'addressRegion': 'Lombardy',
            'addressCountry': 'IT',
          },
        },
      },
    ],
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schemaGraph) }}
    />
  );
}

export default ItalianGeographicSchema;
