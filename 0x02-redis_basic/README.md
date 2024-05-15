# Redis -> caches

## install Redis:

sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf


sudo service redis-server start
systemctl status redis-server.service
