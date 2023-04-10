# import utlis
# import WebcamModule
# import pandas as pd
# import os
# import cv2
# from datetime import datetime
# import WebcamModule as wM
# import DataCollectionModule as dcM
# import JoyStickModule as jsM
# import MotorModule_4motors as mM
# import cv2
# from time import sleep

# from MotorModule import Motor
# import KeyPressModule as kp

# # define motor by gpio pinout number
# motor = Motor(13, 19, 26, 21, 16, 20)
# kp.init()


# def main():
#     if kp.getKey('UP'):
#         motor.move(0.6, 0, 0.1)
#     elif kp.getKey('DOWN'):
#         motor.move(-0.6, 0, 0.1)
#     elif kp.getKey('LEFT'):
#         motor.move(0.3, 0.3, 0.1)
#     elif kp.getKey('RIGHT'):
#         motor.move(0.3, -0.3, 0.1)
#     else:
#         motor.stop(0.1)


# if __name__ == '__main__':
#     while True:
#         main()

# from MotorModule import Motor
# from LaneModule import getLaneCurve
# import WebcamModule

# ##################################################
# motor = Motor(2,3,4,22,17,27)
# ##################################################

# def main():

#     img = WebcamModule.getImg()
#     curveVal= getLaneCurve(img,1)

#     sen = 1.3  # SENSITIVITY
#     maxVAl= 0.3 # MAX SPEED
#     if curveVal>maxVAl:curveVal = maxVAl
#     if curveVal<-maxVAl: curveVal =-maxVAl
#     #print(curveVal)
#     if curveVal>0:
#         sen =1.7
#         if curveVal<0.05: curveVal=0
#     else:
#         if curveVal>-0.08: curveVal=0
#     motor.move(0.20,-curveVal*sen,0.05)
#     #cv2.waitKey(1)


# if __name__ == '__main__':
#     while True:
#         main()

# import RPi.GPIO as GPIO
# from time import sleep
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


# class Motor():
#     def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
#         self.EnaA= EnaA
#         self.In1A = In1A
#         self.In2A = In2A
#         self.EnaB= EnaB
#         self.In1B = In1B
#         self.In2B = In2B
#         GPIO.setup(self.EnaA,GPIO.OUT);GPIO.setup(self.In1A,GPIO.OUT);GPIO.setup(self.In2A,GPIO.OUT)
#         GPIO.setup(self.EnaB,GPIO.OUT);GPIO.setup(self.In1B,GPIO.OUT);GPIO.setup(self.In2B,GPIO.OUT)
#         self.pwmA = GPIO.PWM(self.EnaA, 100);
#         self.pwmB = GPIO.PWM(self.EnaB, 100);
#         self.pwmA.start(0);
#         self.pwmB.start(0);
#         self.mySpeed=0

#     def move(self,speed=0.5,turn=0,t=0):
#         speed *=100
#         turn *=70
#         leftSpeed = speed-turn
#         rightSpeed = speed+turn

#         if leftSpeed>100: leftSpeed =100
#         elif leftSpeed<-100: leftSpeed = -100
#         if rightSpeed>100: rightSpeed =100
#         elif rightSpeed<-100: rightSpeed = -100
#         #print(leftSpeed,rightSpeed)
#         self.pwmA.ChangeDutyCycle(abs(leftSpeed))
#         self.pwmB.ChangeDutyCycle(abs(rightSpeed))
#         if leftSpeed>0:GPIO.output(self.In1A,GPIO.HIGH);GPIO.output(self.In2A,GPIO.LOW)
#         else:GPIO.output(self.In1A,GPIO.LOW);GPIO.output(self.In2A,GPIO.HIGH)
#         if rightSpeed>0:GPIO.output(self.In1B,GPIO.HIGH);GPIO.output(self.In2B,GPIO.LOW)
#         else:GPIO.output(self.In1B,GPIO.LOW);GPIO.output(self.In2B,GPIO.HIGH)
#         sleep(t)

#     def stop(self,t=0):
#         self.pwmA.ChangeDutyCycle(0);
#         self.pwmB.ChangeDutyCycle(0);
#         self.mySpeed=0
#         sleep(t)

# def main():
#     motor.move(0.5,0,2)
#     motor.stop(2)
#     motor.move(-0.5,0,2)
#     motor.stop(2)
#     motor.move(0,0.5,2)
#     motor.stop(2)
#     motor.move(0,-0.5,2)
#     motor.stop(2)

# if __name__ == '__main__':
#     motor= Motor(2,3,4,22,17,27)
#     main()

import cv2
# import numpy as np
# import utlis

# curveList = []
# avgVal = 10


# def getLaneCurve(img, display=2):

#     imgCopy = img.copy()
#     imgResult = img.copy()
#     # STEP 1
#     imgThres = utlis.thresholding(img)

#     # STEP 2
#     hT, wT, c = img.shape
#     points = utlis.valTrackbars()
#     imgWarp = utlis.warpImg(imgThres, points, wT, hT)
#     imgWarpPoints = utlis.drawPoints(imgCopy, points)

#     # STEP 3
#     middlePoint, imgHist = utlis.getHistogram(
#         imgWarp, display=True, minPer=0.5, region=4)
#     curveAveragePoint, imgHist = utlis.getHistogram(
#         imgWarp, display=True, minPer=0.9)
#     curveRaw = curveAveragePoint - middlePoint

#     # SETP 4
#     curveList.append(curveRaw)
#     if len(curveList) > avgVal:
#         curveList.pop(0)
#     curve = int(sum(curveList)/len(curveList))

#     # STEP 5
#     if display != 0:
#         imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
#         imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
#         imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
#         imgLaneColor = np.zeros_like(img)
#         imgLaneColor[:] = 0, 255, 0
#         imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
#         imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
#         midY = 450
#         cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85),
#                     cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
#         cv2.line(imgResult, (wT // 2, midY),
#                  (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
#         cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25),
#                  (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
#         for x in range(-30, 30):
#             w = wT // 20
#             cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
#                      (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
#         #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
#         #cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
#     if display == 2:
#         imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
#                                              [imgHist, imgLaneColor, imgResult]))
#         cv2.imshow('ImageStack', imgStacked)
#     elif display == 1:
#         cv2.imshow('Resutlt', imgResult)

#     # NORMALIZATION
#     curve = curve/100
#     if curve > 1:
#         curve == 1
#     if curve < -1:
#         curve == -1

#     return curve


# if __name__ == '__main__':
#     cap = cv2.VideoCapture(0)
#     intialTrackBarVals = [102, 80, 20, 214]
#     utlis.initializeTrackbars(intialTrackBarVals)
#     frameCounter = 0
#     while True:
#         frameCounter += 1
#         if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
#             cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#             frameCounter = 0

#         success, img = cap.read()
#         img = cv2.resize(img, (480, 240))
#         curve = getLaneCurve(img, display=2)
#         print(curve)
#         # cv2.imshow('Vid',img)
#         cv2.waitKey(1)

# from MotorModule_4motors import Motor
# from LaneModule import getLaneCurve
# import WebcamModule

# ###########################################################
# motor = Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)
# ###########################################################


# def main():

#     img = WebcamModule.getImg()
#     curveVal = getLaneCurve(img, 1)

#     sen = 1.8  # SENSITIVITY
#     maxVAl = 0.3  # MAX SPEED
#     if curveVal > maxVAl:
#         curveVal = maxVAl
#     if curveVal < -maxVAl:
#         curveVal = -maxVAl
#     # print(curveVal)
#     #if curveVal > 0:
#         #sen = 1.8
#     #    if curveVal < 0.05:
#     #        curveVal = 0
#     #else:
#     #    if curveVal > -0.08:
#     #        curveVal = 0
#     turnVal = curveVal*sen
#     if turnVal == 0:
#         motor.move(0.20, 0, 0.20, 0, 0.05)
#     else:
#         motor.move(0.20, -turnVal, 0, 0, 0.05)
#     # cv2.waitKey(1)


# if __name__ == '__main__':
#     while True:
#         main()
