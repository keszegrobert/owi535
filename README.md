# Code for my OWI 535 Robotic arm

This is the robotic arm I am using in this project:
https://www.imagesco.com/robotics/owi-535.html

## For the robotic arm edge USB interface:

0. connect the robotic arm through the Edge USB controller
1. sudo apt-get install libusb-dev
2. sudo pip install pyusb

more info: https://www.instructables.com/id/Raspberry-Pi-and-Wiimote-controlled-Robot-Arm/

## For the game controller

0. connect the game controller to the USB port of the raspberry pi
1. sudo pip install evdev

more info: https://python-evdev.readthedocs.io/en/latest/usage.html

## For the IMU

0. connect the IMU to your raspberry pi
1. sudo apt-get install i2c-tools
2. sudo raspi-config 

and enable the i2c kernel at startup option

3. ls /dev/i2c*
4. sudo i2cdetect -y 1
5. sudo pip install mpu6050-raspberrypi

more info: 
https://www.instructables.com/id/MPU6050-Arduino-6-Axis-Accelerometer-Gyro-GY-521-B/

For the opengl simulation:
https://github.com/mattzzw/Arduino-mpu6050

