#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
sudo apt update

sudo apt -y upgrade

sudo apt install -y nginx

#flag -p es para hacerlo recursivo y cofirmar si existe
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello Bruno" | sudo tee  /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sudo sed -i "/listen 80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart
