module.exports = {
  presets: [
    ['@babel/preset-react', {
      'pragma': 'h',
      'pragmaFrag': 'Fragment'
    }]
  ],
  plugins: ['@babel/plugin-syntax-import-meta'],
  env: {
    development: {
      plugins: ['react-refresh/babel']
    }
  }
}
