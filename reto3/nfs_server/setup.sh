sudo apt update
sudo apt install nfs-kernel-server
sudo mkdir /var/www/html -p
ls -dl /var/www/html
sudo chown nobody:nogroup /var/www/html
#sudo nano /etc/exports
#Add this lines: /var/www/html    client_ip1(rw,sync,no_subtree_check)
#                /var/www/html    client_ip2(rw,sync,no_subtree_check)
sudo systemctl restart nfs-kernel-server
sudo ufw enable
sudo ufw allow from client_ip1 to any port nfs
sudo ufw allow from client_ip2 to any port nfs
sudo ufw status