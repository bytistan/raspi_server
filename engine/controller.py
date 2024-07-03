import RPi.GPIO as GPIO
from .motor import Motor
from .pins import *

class Controller:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.motor_nw = Motor(NW_PIN_FW, NW_PIN_BW, NW_PIN_PWM)
        self.motor_ne = Motor(NE_PIN_FW, NE_PIN_BW, NE_PIN_PWM)
        self.motor_sw = Motor(SW_PIN_FW, SW_PIN_BW, SW_PIN_PWM)
        self.motor_se = Motor(SE_PIN_FW, SE_PIN_BW, SE_PIN_PWM)

    def forward(self,speed):
        self.motor_nw.go_forward(speed)
        self.motor_ne.go_forward(speed)
        self.motor_sw.go_forward(speed)
        self.motor_se.go_forward(speed)

    def backward(self,speed):
        self.motor_nw.go_backward(speed)
        self.motor_ne.go_backward(speed)
        self.motor_sw.go_backward(speed)
        self.motor_se.go_backward(speed)

    def right(self,speed):
        self.motor_nw.go_backward(speed)
        self.motor_ne.go_forward(speed)
        self.motor_sw.go_forward(speed)
        self.motor_se.go_backward(speed)

    def left(self,speed):
        self.motor_nw.go_forward(speed)
        self.motor_ne.go_backward(speed)
        self.motor_sw.go_backward(speed)
        self.motor_se.go_forward(speed)

    def turning_right(self,speed):
        self.motor_nw.go_forward(speed)
        self.motor_ne.go_backward(speed)
        self.motor_sw.go_forward(speed)
        self.motor_se.go_backward(speed)

    def turning_left(self,speed):
        self.motor_nw.go_backward(speed)
        self.motor_ne.go_forward(speed)
        self.motor_sw.go_backward(speed)
        self.motor_se.go_forward(speed)

    def stop(self):
        self.motor_nw.stop()
        self.motor_ne.stop()
        self.motor_sw.stop()
        self.motor_se.stop()

    def update(self, order ,speed=0):
        if order == 0:
            self.stop()
        elif order == 1:
            self.forward(speed)
        elif order == 2:
            self.backward(speed)
        elif order == 3:
            self.right(speed)
        elif order == 4:
            self.left(speed)
        elif order == 5:
            self.turning_right(speed)
        elif order == 6:
            self.turning_left(speed)
