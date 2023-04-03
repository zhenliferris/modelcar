from MotorModule_4motors import Motor
import KeyPressModule as kp

# define motor by gpio pinout number
motor = Motor(22, 27, 17, 2, 4, 3, 13, 19, 26, 21, 16, 20)
kp.init()


def main():
    # normal movement
    if kp.getKey('UP'):
        motor.move(0.6, 0, 0.6, 0, 0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.6, 0, -0.6, 0, 0.1)
    elif kp.getKey('LEFT'):
        motor.move(0, 0.4, 0, 0, 0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0, -0.4, 0, 0, 0.1)
    # special movement
    # shifting
    elif kp.getKey('a'):
        motor.move(0, 0.4, 0, -0.4, 0.1)
    elif kp.getKey('d'):
        motor.move(0, -0.4, 0, 0.4, 0.1)
    # diagonal movement
    elif kp.getKey('q'):
        motor.move(0.14, 0.2, 0.14, -0.2, 0.1)
    elif kp.getKey('e'):
        motor.move(0.14, -0.2, 0.14, 0.2, 0.1)
    elif kp.getKey('z'):
        motor.move(-0.14, 0.2, -0.14, -0.2, 0.1)
    elif kp.getKey('c'):
        motor.move(-0.14, -0.2, -0.14, 0.2, 0.1)
    # spping
    elif kp.getKey('w'):
        motor.move(0, 0.4, 0, 0.4, 0.1)
    elif kp.getKey('x'):
        motor.move(0, -0.4, 0, -0.4, 0.1)
    else:
        motor.stop(0.1)


if __name__ == '__main__':
    while True:
        main()