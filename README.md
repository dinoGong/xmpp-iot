```
pip install sleekxmpp
pip install baidu-aip
```

```
sudo nano /etc/rc.local
```


respberry pi:
```
su pi -c "python /home/pi/bot.py &"
```

armbian && dietpi:
```
su root -c "python /home/pi/bot.py &"
```



respberry pi:
```
sudo apt-get install autoconf automake libtool libffi-dev openssl libssl-dev
```




```
git clone https://github.com/strophe/libstrophe
./bootstrap.sh
./configure
make
make install
gcc -o bot bot.c `pkg-config --cflags --libs libstrophe`
```
