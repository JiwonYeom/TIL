## Preparing your AWS Linux server for Symfony

This is a step by step write up for how to prepare your AWS Linux server environment for `Symfony`.

1. Get your `EC2 instance` with `AWS Linux`. I set everything default so that I can enjoy Free Tier. I strongly suggest you to get `EIP`(Elastic IP) too, so your instance won't change its IP every time you reboot it.

2. Install NGINX, php, php-fpm, and mysql. Here's shell script that I used.

```BASH
# Basic Settings
sudo yum update
sudo yum install nginx
sudo mkdir -p /tmp/php7
cd /tmp/php7/
sudo wget https://mirror.webtatic.com/yum/el6/latest.rpm
sudo yum install latest.rpm
sudo vi /etc/yum.repos.d/webtatic.repo
sudo yum clean all

#webtatic repo & php installation
sudo yum install --enablerepo=webtatic php70w
php -v  #php7.0
sudo yum install php70w-opcache php70w-xml php70w-pdo
sudo yum install php70w-mysqlnd php70w-gd php70w-apcu php70w-pecl-apcu php70w-mbstring php70w-imap
sudo vi /etc/php.ini #cgi.fix_pathinfo=0
sudo yum install php70w-fpm
sudo vi /etc/php-fpm.d/www.conf
# check listen, listen.owner, listen.group, user, group
# listen = /var/run/php-fpm/php-fpm.sock
# listen.owner = ec2-user
# listen.group = ec2-user
# user = ec2-user
# group = ec2-user
sudo service php-fpm start
sudo service php-fpm stataus #should success here

#nginx - see nginx conf script that follows
sudo vi /etc/nginx/nginx.conf
sudo service nginx restart
cd /usr/share/nginx/html/

#phpinfo check
sudo vi phpinfo.php  #host/phpinfo.php
sudo service nginx reload

sudo vi /etc/php.ini  # date.timezone = [your timezone]
sudo service nginx reload
sudo service nginx restart

# mysql
sudo yum install -y mysql56-server
sudo service mysqld start
sudo mysql_secure_installation

# set restart when server goes off & on
sudo chkconfig nginx on
sudo chkconfig php-fpm on
sudo chkconfig mysqld on
sudo chkconfig mysqld on

```

your nginx.conf settings:
```
# your directory
root /var/www/symfony/web;

location / {
	try_files $uri /app.php$is_args$args;
}

# DEV
    # This rule should only be placed on your development environment
    # In production, don't include this and don't deploy app_dev.php or config.php
    location ~ ^/(app_dev|config)\.php(/|$) {
        fastcgi_pass unix:/var/run/php5-fpm.sock;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        # When you are using symlinks to link the document root to the
        # current version of your application, you should pass the real
        # application path instead of the path to the symlink to PHP
        # FPM.
        # Otherwise, PHP's OPcache may not properly detect changes to
        # your PHP files (see https://github.com/zendtech/ZendOptimizerPlus/issues/126
        # for more information).
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
    }
    # PROD
    location ~ ^/app\.php(/|$) {
        fastcgi_pass unix:/var/run/php5-fpm.sock;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        # When you are using symlinks to link the document root to the
        # current version of your application, you should pass the real
        # application path instead of the path to the symlink to PHP
        # FPM.
        # Otherwise, PHP's OPcache may not properly detect changes to
        # your PHP files (see https://github.com/zendtech/ZendOptimizerPlus/issues/126
        # for more information).
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        # Prevents URIs that include the front controller. This will 404:
        # http://domain.tld/app.php/some-path
        # Remove the internal directive to allow URIs like this
        internal;
    }
```
