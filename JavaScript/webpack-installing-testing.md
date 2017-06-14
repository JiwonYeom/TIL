# Notes while installing and testing Webpack 2.0
This is my first time actually trying to use a bundler, and here are several notes while installing webpack.

#### You need to initialize your package.json by
```
npm init -y
```

#### `--save` or `--save-dev` option

You'd probably face this option to be used by many tutorials. This means it will look for `package.json` and include itself into dependencies.

#### `webpack.config.js`

This file allows some configurations, such as importing files or using utilities through `require(...)`, use constants, use functions for some parts... etc.

#### Installing a library locally will add it to package.json, which will allow automatic bundling.

(continued)
