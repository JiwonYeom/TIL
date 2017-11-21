### Set up Homestead and Laravel 

0. Prerequisites: mysql(+workbench), vagrant, virtual machine of our choice

1. install homestead with vagrant

2. set up `homestead.yaml` (shared folder, virtual host, etc) and your local `host` file (to access your files through browser like a normal website)

3. `vagrant up` and check if all settings are being done by speculating the log. Pay attention to `mounting shared folder...`

4. `vagrant ssh` to access its terminal

5. open the shared folder on your fav text editor. Check if it's synced

6. generate your files with `laravel` command. (Of course, install it first!)

7. Work on it with your text editor & terminal running on Vagrant!