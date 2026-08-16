import os

def build_root():
    src_path = os.path.join(os.path.dirname(__file__), '..', 'version-b', 'index.html')
    dest_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update title and canonical
    content = content.replace(
        '<title>Renzo Francesqui — AI Marketing Automation, CRM and Operations (Version B)</title>',
        '<title>Renzo Francesqui — AI Marketing Automation, CRM and RevOps Specialist</title>'
    )
    content = content.replace(
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/version-b/">',
        '<link rel="canonical" href="https://renzo-francesqui.vercel.app/">'
    )

    # Replace ../blog/ with blog/
    content = content.replace('../blog/', 'blog/')

    # Add Open Graph, Twitter Card, and Schema.org in <head> if not present
    seo_block = '''    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://renzo-francesqui.vercel.app/">
    <meta property="og:title" content="Renzo Francesqui — AI Marketing Automation, CRM & RevOps Specialist">
    <meta property="og:description" content="Official portfolio and AI representative of Renzo Francesqui. Specializing in HubSpot CRM architecture, B2B marketing automation, and Python AI enrichment agents.">
    <meta property="og:image" content="https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg">
    <meta property="og:site_name" content="Renzo Francesqui Portfolio">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://renzo-francesqui.vercel.app/">
    <meta name="twitter:title" content="Renzo Francesqui — AI Marketing Automation, CRM & RevOps Specialist">
    <meta name="twitter:description" content="Official portfolio and AI representative of Renzo Francesqui. Specializing in HubSpot CRM architecture, B2B marketing automation, and Python AI enrichment agents.">
    <meta name="twitter:image" content="https://renzo-francesqui.vercel.app/images/renzo-francesqui.jpg">

    <!-- Schema.org Structured Data -->
    <script type="application/ld+json">
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
        "Python AI Automation Agents",
        "Google Antigravity",
        "B2B Lead Lifecycle Management",
        "Trade Show Lead Operations"
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
    </script>
'''

    if '<!-- Open Graph / Facebook -->' not in content:
        content = content.replace('<!-- Typography -->', seo_block + '\n    <!-- Typography -->')

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print('Successfully generated root index.html with complete SEO metadata and Google Analytics!')

if __name__ == '__main__':
    build_root()
