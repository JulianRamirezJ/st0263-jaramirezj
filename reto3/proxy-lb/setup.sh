sudo vim /etc/nginx/nginx.conf
#Edit the conf file
sudo mkdir -p /var/www/letsencrypt
sudo nginx -t

sudo service nginx reload