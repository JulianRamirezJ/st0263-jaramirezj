sudo vim /etc/nginx/nginx.conf
#Edit the conf file
sudo mkdir -p /var/www/letsencrypt
sudo nginx -t
sudo service nginx reload

#Generar el SSL
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d julianrjdev.site --manual --preferred-challenges dns-01 certonly
#Creo un registro txt en el DNS Gestor con la key y name  
#Guardar las rutas de las keys y ponerlas en el nginx
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.julianrjdev.site --manual --preferred-challenges dns-01 certonly
#Creo un registro txt en el DNS Gestor con la key y name  
