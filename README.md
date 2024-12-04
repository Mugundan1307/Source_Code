* *Commands:* *
1) * *Veml7700:* * sudo pip3 install adafruit-circuitpython-veml7700
2) * *Vl6180:* * sudo pip3 install adafruit-circuitpython-vl6180x
3) * *Create a new rule file:* * sudo vim /etc/udev/rules.d/99-i2c.rules * *(and)* * KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0660"
4) * *Reload udev rules and trigger them:* * sudo udevadm control --reload-rules * *(and)* * sudo udevadm trigger * *(and)* * ls -l /dev/i2c-1
5) * *I2C:* * sudo apt-get install -y i2c-tools * *(and)* * i2cdetect -y 1
6) * *GPIO:* * sudo apt-get install python3-rpi.gpio
