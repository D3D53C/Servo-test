from servo import Servo as Servo
import time

class main:
    def __init__(self):
        self.servo = Servo(37,50,500,2500,180)
        while True:
            self.servo.change_position(0)
            time.sleep(5)
            self.servo.change_position(180)
            time.sleep(5)