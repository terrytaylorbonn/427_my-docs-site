module.exports = {
  title: 'My Docs Site',
  tagline: 'Technical documentation made simple',
  url: 'https://localhost',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'terrytaylorbonn',
  projectName: 'my-docs-site',

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
          editUrl: 'https://github.com/terrytaylorbonn/391_my-docs-site/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Docs Site',
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/terrytaylorbonn/391_my-docs-site',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} My Docs Site.`,
    },
  },
};