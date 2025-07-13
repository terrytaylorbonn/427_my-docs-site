module.exports = {
  title: 'My Docs Site',
  tagline: 'Technical documentation made simple',
  url: process.env.NODE_ENV === 'production' ? 'https://four27-my-docs-site.onrender.com' : 'https://localhost',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'terrytaylorbonn',
  projectName: 'my-docs-site',

  // Algolia domain verification ##############
  headTags: [
    {
      tagName: 'meta',
      attributes: {
        name: 'algolia-site-verification',
        content: 'FF14F5E36F82A306',
      },
    },
    // (1) Open Graph meta tags #############
    {
      tagName: 'meta',
      attributes: {
        property: 'og:title',
        content: 'My Docs Site - Technical documentation made simple',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        property: 'og:description',
        content: 'Comprehensive technical documentation and tutorials. Learn through clear guides and examples.',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        property: 'og:image',
        content: 'https://four27-my-docs-site.onrender.com/img/docusaurus-social-card.jpg',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        property: 'og:url',
        content: 'https://four27-my-docs-site.onrender.com',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        property: 'og:type',
        content: 'website',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        property: 'og:site_name',
        content: 'My Docs Site',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        property: 'og:locale',
        content: 'en_US',
      },
    },
    // #############
    // (2) Twitter Card meta tags #############
    {
      tagName: 'meta',
      attributes: {
        name: 'twitter:card',
        content: 'summary_large_image',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'twitter:title',
        content: 'My Docs Site - Technical documentation made simple',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'twitter:description',
        content: 'Comprehensive technical documentation and tutorials. Learn through clear guides and examples.',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'twitter:image',
        content: 'https://four27-my-docs-site.onrender.com/img/docusaurus-social-card.jpg',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'twitter:site',
        content: '@mydocssite',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'twitter:creator',
        content: '@terrytaylorbonn',
      },
    },
    // #############
    // (3) Structured Data (JSON-LD) for search engines #############
    {
      tagName: 'script',
      attributes: {
        type: 'application/ld+json',
      },
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Organization',
            '@id': 'https://four27-my-docs-site.onrender.com/#organization',
            name: 'My Docs Site',
            url: 'https://four27-my-docs-site.onrender.com',
            logo: {
              '@type': 'ImageObject',
              url: 'https://four27-my-docs-site.onrender.com/img/logo.svg'
            },
            sameAs: [
              'https://github.com/terrytaylorbonn/427_my-docs-site'
            ]
          },
          {
            '@type': 'WebSite',
            '@id': 'https://four27-my-docs-site.onrender.com/#website',
            url: 'https://four27-my-docs-site.onrender.com',
            name: 'My Docs Site',
            description: 'Technical documentation made simple',
            publisher: {
              '@id': 'https://four27-my-docs-site.onrender.com/#organization'
            },
            potentialAction: {
              '@type': 'SearchAction',
              target: 'https://four27-my-docs-site.onrender.com/search?q={search_term_string}',
              'query-input': 'required name=search_term_string'
            }
          },
          {
            '@type': 'WebPage',
            '@id': 'https://four27-my-docs-site.onrender.com/#webpage',
            url: 'https://four27-my-docs-site.onrender.com',
            name: 'My Docs Site - Technical documentation made simple',
            description: 'Comprehensive technical documentation and tutorials. Learn through clear guides and examples.',
            isPartOf: {
              '@id': 'https://four27-my-docs-site.onrender.com/#website'
            },
            about: {
              '@id': 'https://four27-my-docs-site.onrender.com/#organization'
            },
            datePublished: '2025-07-12',
            dateModified: '2025-07-12'
          }
        ]
      })
    },
    // #############
    // (4) Canonical URLs and language tags #############
    {
      tagName: 'link',
      attributes: {
        rel: 'canonical',
        href: 'https://four27-my-docs-site.onrender.com',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'alternate',
        hreflang: 'en',
        href: 'https://four27-my-docs-site.onrender.com',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'alternate',
        hreflang: 'x-default',
        href: 'https://four27-my-docs-site.onrender.com',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'language',
        content: 'en',
      },
    },
    {
      tagName: 'meta',
      attributes: {
        httpEquiv: 'content-language',
        content: 'en-US',
      },
    },
    // #############
  ],

  // (GA) Google Analytics configuration #############
  plugins: [
    [
      '@docusaurus/plugin-google-gtag',
      {
        trackingID: 'G-MX9MT9MK97',
        anonymizeIP: true,
      },
    ],
  ],
  // #############

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          sidebarItemsGenerator: async function({ defaultSidebarItemsGenerator }) {
            return defaultSidebarItemsGenerator(...arguments);
          },
          editUrl: 'https://github.com/terrytaylorbonn/427_my-docs-site/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        // Sitemap configuration ##############
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
        // ##############
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Docs Site CPLT30',
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/terrytaylorbonn/427_my-docs-site',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} My Docs Site.`,
    },
    // Algolia search configuration ##############
    algolia: {
      appId: '6B0P0R08FS',
      apiKey: '853723f13c4712cb093ef196a181f04d',
      indexName: 'my-docs-site',
      contextualSearch: false,
    },
    // ############## 
  },
};