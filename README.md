# Use Raspberry Pi to control model car following path.

# Reference
# https://www.computervision.zone/courses/self-driving-car-using-raspberry-pi/
# https://www.raspberrypi.com/documentation/computers/camera_software.html
# https://www.pygame.org/docs/ref/joystick.html
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
# https://github.com/raspberrypi/libcamera-apps/issues/487
# https://www.shellhacks.com/raspberry-pi-force-hdmi-hotplug/
# https://www.raspberrypi.com/documentation/computers/config_txt.html#video-options
# https://github.com/murtazahassan/Neural-Networks-Self-Driving-Car-Raspberry-Pi


# Hardware List
# 1. Mecanum Wheels Chassis Kit
# 2. LiPo battery 
# 3. Powerbank 
# 4. Raspberry Pi 4B 4GB 
# 5. Camera module 
# 6. 128GB SDHC 
# 7. L298N 
# 8. Bluetooth Keyboard and Mouse 
# 9. PS4 Whireless Controller
# 10. Cables and Screws
# 11. 3D printed parts


# 00 Perameters finders and Code Testing:
# 1. CodeTester
# 2. ColorPickerScript
# 3. vid1.mp4


# 01 Manually control:
# 1. JoyStickModule 
# 2. KeyPressModule  
# 3. MotorModule
# 4. ManuallyKeyboardControl
# 5. ManuallyStickControl


# 02 Autonomous Model Car by Image Processing:
# 1. LaneModule
# 2. MainRobot
# 3. MotorModule
# 4. Utlis
# 5. vid1.mp4
# 6. WebcamModule



# 03 Autonomous Model Car by Neural Networks:
# 1. CamModule
# 2. DataCollectionMain
# 3. DataCollectionModule
# 4. JoyStickModule
# 5. MotorModule
# 6. utlis
# 7. Training
# 8. AutonomousNN

# system backup
# remake a bootdisk with bullseye 64bit image and add the required libraries
# using disk tools to regain 100GB lost sd capcity, if using sd card copier from Raspberry Pi at 128GB SDHC card
#      sudo raspi-config 
#      git clone https://github.com/zhenliferris/modelcar.git
#      sudo apt update
#      sudo apt upgrade
#      sudo apt install libatlas-base-dev
#      pip3 install tensorflow
#      sudo apt install python3-opencv
#      sudo pip install keras
   