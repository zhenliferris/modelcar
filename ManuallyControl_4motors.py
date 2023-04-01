from MotorModule_4mortors import Motor
import KeyPressModule as kp

# define motor by gpio pinout number
motor = Motor(2, 3, 4, 22, 17, 27, 13, 19, 26, 40, 16, 20)
kp.init()


def main():
    if kp.getKey('UP'):
        motor.move(0.6, 0, 0.6, 0, 0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.6, 0, -0.6, 0, 0.1)
    elif kp.getKey('LEFT'):
        motor.move(0.3, 0.3, 0.3, 0.3, 0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0.3, -0.3, 0.3, -0.3, 0.1)
    else:
        motor.stop(0.1)


if __name__ == '__main__':
    while True:
        main()
