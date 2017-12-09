## Webpack Environment setting for React
reference: https://www.youtube.com/watch?v=uextYhQGP6k&t=638s

1. initialize npm with `npm init`
2. Install `react`, `react-dom` as production dependency with `--save` option
3. Install `webpack`, `webpack-dev-server` (server is needed to observe the actual changes with http protocol), `babel-loader`, `babel-preset-2015`, `babel-preset-react`, `babel-preset-stage-2` with `--save-dev` option for development dependency (will not be deployed)
4. Set up directories and files (src-app, index.html, index.js)
5. Set `package.json` scripts to execute for `npm start` and build processes