sudo apt update
sudo apt install nfs-common
sudo mkdir -p /var/www/html
sudo mount {$nfs_server_ip}:/var/www/html /mnt/wordpress
df -h
sudo nano /etc/fstab
 #Add this line
    host_ip:/var/www/html    /mnt/wordpress  nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0