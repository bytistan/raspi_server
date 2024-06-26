import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pin_fw, pin_bw, pin_pwm):
        self.pin_fw = pin_fw
        self.pin_bw = pin_bw
        self.pin_pwm = pin_pwm
        
        GPIO.setup(self.pin_fw, GPIO.OUT)
        GPIO.setup(self.pin_bw, GPIO.OUT)
        GPIO.setup(self.pin_pwm, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin_pwm, 100)  # 100 Hz
        self.pwm.start(0)

    def go_forward(self, speed):
        GPIO.output(self.pin_fw, GPIO.HIGH)
        GPIO.output(self.pin_bw, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def go_backward(self, speed):
        GPIO.output(self.pin_bw, GPIO.HIGH)
        GPIO.output(self.pin_fw, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.pin_fw, GPIO.LOW)
        GPIO.output(self.pin_bw, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
