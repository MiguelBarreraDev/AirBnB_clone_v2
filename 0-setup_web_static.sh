#!/usr/bin/env bash
## Script that sets up your web servers for the deployment of web_static
### Update of the repositories and run upgrade
sudo apt-get -y update
sudo apt-get -y upgrade
### Install Nginx web server
sudo apt-get -y install nginx
### Create directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
### Adding fake content in the index.html file
sudo echo "
html>
  <head>
  </head>
  <body>
    <h1>Holberton School</h1>
  </body>
</html>
" > /data/web_static/releases/test/index.html
### Create symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current/
### Modify owner and group of the data directory
sudo chown -hR ubuntu:ubuntu /data/
### Adding an alias in the configuration of Nginx
conf="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sed -i '56i $conf' /etc/nginx/sites-available/default
### Restart service of the web sever
sudo service nginx restart
