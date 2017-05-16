# NGINX and PHP settings
NGINX by itself does not provide PHP support. In order to make it work smoothly with PHP, additional implementation, which is PHP-FPM. When first installed NGINX, begin with installing php and php-fpm. (CentOS-base)

```
sudo yum install php php-mysql php-fpm
```
One thing to note here is that, if you are to add external repository to install newer version of php like php-7, you should take note that you must use it carefully so that php version can be tracked and updated consistently.

After that, you should set up some config files, which are `nginx.conf`, `php-fpm.d/www.conf`, and `php.ini`.

As you fix these files, do not forget to check the nginx and php status by commands like `sudo service nginx restart` and `sudo service nginx status`. (The same for `php-fpm`).
