#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "Holberton School!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}/" /etc/nginx/sites-available/default
service nginx restart
exit 0
