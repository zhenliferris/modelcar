import CamModule as cM
import DataCollectionModule as dcM
import JoyStickModule as jsM
import MotorModule as mM
import cv2
from time import sleep


maxThrottle = 0.25
motor = mM.Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)

record = 0
while True:
    joyVal = jsM.getJS()
    # print(joyVal)
    steering = joyVal['axis1']
    throttle = joyVal['o']*maxThrottle
    if joyVal['t'] == 1:
        if record == 0:
            print('Recording Started ...')
        record += 1
        sleep(0.300)
    if record == 1:
        img = cM.getImg(True, size=[240, 120])
        dcM.saveData(img, steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle, -steering, throttle, -steering)
    cv2.waitKey(1)
