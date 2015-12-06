Peru Call
==========

Call Center System


Repositorio
===========

ssh://root@188.166.72.64:5022/opt/perucall.git 

ip: 188.166.72.64
port: 5022
pass: 4pp$X13nc14$2015*

Base Datos
==========

user: root
pass :d4t4B4$3*



Dependencias
============

sudo apt-get update
sudo apt-get install python-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

pip install Django==1.7.4
pip install django-redis-sessions
pip install django-websocket-redis
pip install simplejson


sudo apt-get install libssl-dev
sudo apt-get install python-MySQLdb
sudo apt-get install libffi-dev
sudo apt-get install build-essential python-dev libmysqlclient-dev
sudo apt-get build-dep python-mysqldb

sudo pip install requests
sudo pip install xlrd
sudo pip install simplejson
sudo pip install pudb
sudo pip install MySQL-python
sudo pip install xlwt

wget http://download.redis.io/releases/redis-3.0.2.tar.gz
tar xzf redis-3.0.2.tar.gz
cd redis-3.0.2
make
src/redis-server

Git
===
 
git config --global user.name "Name" 
git config --global user.email [correo]
git clone [paquete]
git branch
git branch "name" 
git checkout "name"   
git remote -v  
git push [conexion] [rama]
git pull [conexion] [rama]
git clean  -d  -fx ""
cd repository.git
git --bare init
git config core.sharedRepository true
pc1: nc IP 8000
pc2: nc -l -p 8000



Comandos Linux
==============

Ataques: tail -f /var/log/asterisk/messages/
Procesos: ps aux | grep python
du -sh /var/log*
pkill -9 -t pts/*
sudo crontab -l
sudo crontab -e
* * * * * /bin/execute/this/script.sh
/etc/init.d/cron start
ls -tp | grep -v /$ | grep '.xls' | head -1
http://kvz.io/blog/2007/07/29/schedule-tasks-on-linux-using-crontab/
find / -type f -size +100M
iftop -i eth0
sudo fuser -vki  /var/lib/dpkg/lock
cd /var/spool/cron/
tail -f /var/log/syslog
mcedit /etc/init.d/rc.local
locate service | grep -v git
chmod +rwx archivo
scp /origen usuario@ordenador:/directorio-destino/
ssh-keygen
cat ~/.ssh/id_rsa.pub
cd ~/.ssh 
authorized_keys
core restart gracefull
mysqldump -u root -p diloo > backup.sql
Si no ingresa
mysql -u root -p
Enter password actual
use mysql;
update user set password=PASSWORD('your_new_password') where User='root';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'DBPassw' WITH GRANT OPTION;
flush privileges;
quit
Servidor
cd /etc/mysql
nano my.cnf
comentar bind-address = 127.0.0.0
bind-address=0.0.0.0
/etc/init.d/mysql restart
nano /etc/fail2ban/jail.conf 
mysqldump -p --routines orionc7 > bup_oric7.sql





Logs
====

/var/log/apache2/access.log
/var/www-mapfre/logs


