
from MotorModule import Motor
import KeyPressModule as kp

# define motor by gpio pinout number
motor = Motor(13, 19, 26, 21, 16, 20)
kp.init()


def main():
    if kp.getKey('UP'):
<<<<<<< HEAD
        motor.move(0.2,0,0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.2,0,0.1)
    elif kp.getKey('LEFT'):
        motor.move(0.2,0.2,0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0.2,-0.2,0.1)
=======
        motor.move(0.6, 0, 0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.6, 0, 0.1)
    elif kp.getKey('LEFT'):
        motor.move(0.3, 0.3, 0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0.3, -0.3, 0.1)
>>>>>>> f4946d9ebeef8394abab8493695c35657b775d5b
    else:
        motor.stop(0.1)


if __name__ == '__main__':
    while True:
        main()
