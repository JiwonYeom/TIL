## Setting multiple application environment for Codeigniter

- Load different configurations  (ex. dev / production) depending on current environment

- This influences logging and error reporting

##### How to?

1. Include Environment variable in your server config. `CI_ENV` in the following example
```ssh
    listen       8800;
    server_name  localhost [your-website-address];
    root    /var/www/[application-name];

    ...

    location ~ \.php$ {
        fastcgi_pass    unix:/var/run/php-fpm/php-fpm.sock;
        fastcgi_index   index.php;
        #fastcgi_param   SCRIPT_FILENAME  /var/www/html$fastcgi_script_name;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param CI_ENV testing;
        include         fastcgi_params;
    }
```

2. Use that variable to set certain configs in codeigniter. This code should be in `index.php`

```PHP
    // set default CI_ENV to 'development'
	define('ENVIRONMENT', isset($_SERVER['CI_ENV']) ? $_SERVER['CI_ENV'] : 'development');
    // disable cache
    header("Cache-Control: no-store, no-cache, must-revalidate");
```

```PHP
//set different error handling for different configurations

switch (ENVIRONMENT)
{
	case 'development':
		error_reporting(-1);
		ini_set('display_errors', 1);
	break;

	case 'testing':
	case 'production':
		ini_set('display_errors', 0);
		if (version_compare(PHP_VERSION, '5.3', '>='))
		{
			error_reporting(E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_STRICT & ~E_USER_NOTICE & ~E_USER_DEPRECATED);
		}
		else
		{
			error_reporting(E_ALL & ~E_NOTICE & ~E_STRICT & ~E_USER_NOTICE);
		}
	break;

	default:
		header('HTTP/1.1 503 Service Unavailable.', TRUE, 503);
		echo 'The application environment is not set correctly.';
		exit(1); // EXIT_ERROR
}
```

3. Done!

Now your Codeigniter app will take in the environment variable and use that to set appropriate configs.