# Redis -> caches

## install Redis:
```bash
sudo apt-get -y install redis-server
``` 
```bash
pip3 install redis 
```
```bash
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf 
```

```bash
sudo service redis-server start
```
```bash
systemctl status redis-server.service
```
