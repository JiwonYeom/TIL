# Open Source Analysis Series(1) - Laravel

### File Structure
- app : core code of application.
- bootstrap : contains `app.php` file which bootstraps the framework. Houses a `cache` directory which contains cache files for optimized performances (generated)
- config : contains all of config files.
- database : contains database migration & seeds. Can also be used as SQLite database.
- public : contains `index.php` file. Also houses assets.
- resources : views + raw,un-compiled assets (LESS, SASS, js..) + all language files.
- routes : all route definitions. Default route files : `web.php`, `api.php`, `console.php`, `channels.php`
    - `web.php` : routes that `RouteServiceProivder` places in the `web` middleware group.
        - session state, CSRF protection, cookie encryption
        - If your app does not offer a stateless, RESTful API, most likely all routes will be here.
    - `api.php` : routes that `RouteServiceProvider` places in the `api` middleware group.
        - Intended to be stateless. Requests entering the app through these routes are intended to be authenticated via tokens.
        - It will also not have access to session state.
    - `console.php` : define Closure based console commands. 
    - `channels.php` " register all the event broadcasting channels
- storage : contains compiled Blade templates, file based sessions, file caches, other files generated. 
    - gets segregated into `app`, `framework`, `logs` directories.
- tests

> Structure intended to provide good starting point for both large & small apps.
> No `models` directory, and placed in `app` directory by default but can be moved out if wanted by the developer.

### Bundler

### Third-Party

### git

### Others
- `server.php`: emulate Apache's mod_rewrite functionality. Allows testing Laravel application without installing real web server.

- `phpunit.xml`: phpunit config file.

- `artisan`: 

- `gitattributes`

++++
- PHP `$_SERVER`: contains information such as headers, paths, and script locations. 
