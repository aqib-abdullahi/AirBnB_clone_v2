#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

apt update
# Install Nginx
apt install -y nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_path="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/server_name _;/a $nginx_alias" $config_path

# Restart Nginx
sudo service nginx restart
