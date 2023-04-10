from MotorModule import Motor
import JoyStickModule as jsM

# define motor by BCM pinout number
motor = Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)


def main():
    maxThrottle = 0.5
    throttle = 0
    joyVal = jsM.getJS()
    steering = joyVal['axis1']
    if joyVal['o']:
        throttle = maxThrottle
    elif joyVal['s']:
        throttle = - maxThrottle

    motor.move(throttle, -steering, throttle, -steering)


if __name__ == '__main__':
    while True:
        main()
