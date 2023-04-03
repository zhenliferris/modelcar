from MotorModule_4motors import Motor
from LaneModule import getLaneCurve
import WebcamModule

###########################################################
motor = Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)
###########################################################


def main():

    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 1)

    sen = 1.3  # SENSITIVITY
    maxVAl = 0.3  # MAX SPEED
    if curveVal > maxVAl:
        curveVal = maxVAl
    if curveVal < -maxVAl:
        curveVal = -maxVAl
    # print(curveVal)
    if curveVal > 0:
        sen = 1.7
        if curveVal < 0.05:
            curveVal = 0
    else:
        if curveVal > -0.08:
            curveVal = 0
    turnVal = curveVal*sen
    if turnVal == 0:
        motor.move(0.20, 0, 0.20, 0, 0.05)
    else:
        motor.move(0.20, -turnVal, 0, 0, 0.05)
    # cv2.waitKey(1)


if __name__ == '__main__':
    while True:
        main()
