/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/index.html', './src/**/*.svelte'],
  theme: {
    extend: {
      screens: {
        "2xl-w": { 'raw': '(max-width: 1536px)' },
        "2xl-a": { 'raw': '(max-height: 1536px),(max-width: 1536px)' },
        'xl-w': { 'raw': '(max-width: 1280px)' },
        'xl-a': { 'raw': '(max-height: 1280px),(max-width: 1280px)' },
        'lg-w': { 'raw': '(max-width: 1024px)' },
        'lg-a': { 'raw': '(max-height: 1024px),(max-width: 1024px)' },
        'md-w': { 'raw': '(max-width: 768px)' },
        'md-a': { 'raw': '(max-height: 768px),(max-width: 768px)' },
        'sm-w': { 'raw': '(max-width: 640px)' },
        'sm-a': { 'raw': '(max-height: 640px),(max-width: 640px)' },
        'xs-w': { 'raw': '(max-width: 320px)' },
        'xs-a': { 'raw': '(max-height: 320px),(max-width: 320px)' },

      },
    },
  },
  plugins: [],
}
