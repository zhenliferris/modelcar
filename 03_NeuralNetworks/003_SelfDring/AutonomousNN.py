import cv2
import numpy as np
import tensorflow as tf

import CamModule as cM
import MotorModule as mM

steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
motor = mM.Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)
model = tf.lite.Interpreter('model.tflite')


def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img


while True:

    img = cM.getImg(True, size=[240, 120])
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    print(steering*steeringSen)
    motor.move(maxThrottle, -steering*steeringSen,
               maxThrottle, -steering*steeringSen)
    cv2.waitKey(1)
