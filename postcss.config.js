const assets = require('postcss-assets');

module.exports = {
  plugins: [
    assets({
      loadPaths: ['static/'],
    })
  ]
}
