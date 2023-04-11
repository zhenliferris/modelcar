from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule as WebcamModule
import cv2

###########################################################
motor = Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)
###########################################################


def main():

    img = WebcamModule.getImg()
    # for testing, using set 2, for performance using 1
    curveVal = getLaneCurve(img, 1)

    sen = 0.9  # SENSITIVITY
    maxVAl = 0.1  # MAX SPEED
    if curveVal > maxVAl:
        curveVal = maxVAl
    if curveVal < -maxVAl:
        curveVal = -maxVAl
    print(curveVal)
    if curveVal > 0:
        if curveVal < 0.03:
            curveVal = 0
    else:
        if curveVal > -0.03:
            curveVal = 0

    turnVal = -curveVal*sen

    motor.move(0.20, turnVal, 0.20, turnVal, 0.05)

    cv2.waitKey(1)


if __name__ == '__main__':
    while True:
        main()