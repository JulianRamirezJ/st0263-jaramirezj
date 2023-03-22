sudo apt update
sudo apt install nfs-common
sudo mkdir -p /var/www/html
sudo mount server_ip :/var/www/html /mnt/wordpress
df -h