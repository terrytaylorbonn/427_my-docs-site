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
  ],
  // ##############

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