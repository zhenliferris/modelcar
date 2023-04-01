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

    def move(self, frontSpeed=0.5, frontTurn=0, rearSpeed=0.5, rearTurn=0, t=0):
        frontSpeed *= 100
        frontTurn *= 70
        rearSpeed *= 100
        rearTurn *= 70
        frontLeftSpeed = frontSpeed-frontTurn
        frontRightSpeed = frontSpeed+frontTurn
        rearLeftSpeed = rearSpeed-rearTurn
        rearRightSpeed = rearSpeed+rearTurn

        if frontLeftSpeed > 100:
            frontLeftSpeed = 100
        elif frontLeftSpeed < -100:
            frontLeftSpeed = -100
        if frontRightSpeed > 100:
            frontRightSpeed = 100
        elif frontRightSpeed < -100:
            frontRightSpeed = -100
        if rearLeftSpeed > 100:
            rearLeftSpeed = 100
        elif rearLeftSpeed < -100:
            rearLeftSpeed = -100
        if rearRightSpeed > 100:
            rearRightSpeed = 100
        elif rearRightSpeed < -100:
            rearRightSpeed = -100

        self.pwmA.ChangeDutyCycle(abs(frontLeftSpeed))
        self.pwmB.ChangeDutyCycle(abs(frontRightSpeed))
        self.pwmC.ChangeDutyCycle(abs(rearLeftSpeed))
        self.pwmD.ChangeDutyCycle(abs(rearRightSpeed))
        if frontLeftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)
        if frontRightSpeed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)
        if rearLeftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)
        if rearRightSpeed > 0:
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
    motor.move(0.5, 0, 0.5, 0, 2)
    motor.stop(2)
    motor.move(-0.5, 0, -0.5, 0, 2)
    motor.stop(2)
    motor.move(0, 0.5, -0.5, 0, 2)
    motor.stop(2)
    motor.move(0, -0.5, -0.5, 0, 2)
    motor.stop(2)


if __name__ == '__main__':
    motor = Motor(2, 3, 4, 22, 17, 27, 13, 19, 26, 21, 16, 20)
    main()
