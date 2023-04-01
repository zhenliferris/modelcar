import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B, EnaC, In1C, In2C, EnaD, In1D, In2D):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        self.EnaC = EnaC
        self.In1C = In1C
        self.In2C = In2C
        self.EnaD = EnaD
        self.In1D = In1D
        self.In2D = In2D
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        GPIO.setup(self.EnaC, GPIO.OUT)
        GPIO.setup(self.In1C, GPIO.OUT)
        GPIO.setup(self.In2C, GPIO.OUT)
        GPIO.setup(self.EnaD, GPIO.OUT)
        GPIO.setup(self.In1D, GPIO.OUT)
        GPIO.setup(self.In2D, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmC = GPIO.PWM(self.EnaC, 100)
        self.pwmD = GPIO.PWM(self.EnaD, 100)
        self.pwmA.start(0)
        self.pwmB.start(0)
        self.pwmC.start(0)
        self.pwmD.start(0)
        self.mySpeed = 0

    def move(self, frontSpeed=0.5, frontTurn=0, frontT=0, rearSpeed=0.5, rearTurn=0, rearT=0):
        frontSpeed *= 100
        frontTurn *= 70
        rearSpeed *= 100
        rearTurn *= 70
        frontLeftSpeed = frontSpeed-frontTurn
        frontRightSpeed = frontSpeed+frontTurn

        if leftSpeed > 100:
            leftSpeed = 100
        elif leftSpeed < -100:
            leftSpeed = -100
        if rightSpeed > 100:
            rightSpeed = 100
        elif rightSpeed < -100:
            rightSpeed = -100
        # print(leftSpeed,rightSpeed)
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        if leftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)
        if rightSpeed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)
        sleep(t)

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        self.pwmC.ChangeDutyCycle(0)
        self.pwmD.ChangeDutyCycle(0)
        self.mySpeed = 0
        sleep(t)


def main():
    motor.move(0.5, 0, 2)
    motor.stop(2)
    motor.move(-0.5, 0, 2)
    motor.stop(2)
    motor.move(0, 0.5, 2)
    motor.stop(2)
    motor.move(0, -0.5, 2)
    motor.stop(2)


if __name__ == '__main__':
    motor = Motor(2, 3, 4, 22, 17, 27)
    main()
