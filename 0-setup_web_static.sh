#!/usr/bin/env bash
#setup new server
# check for nginx installation, install if not installed
sudo apt update -y
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
chown -R ubuntu:ubuntu /data

echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx test</p>
  </body>
</html>" >/data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

# create nginx configuration
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
