from servo import Servo as Servo
import time
import RPi.GPIO as IO


    IO.setmode(BOARD)
    IO.setwarnings(False)
    IO.setup(35, IO.OUT)
    IO.output(35, IO.HIGH)
    self.servo = Servo(37,50,500,2500,180)
    while True:
        self.servo.change_position(0)
        time.sleep(5)
        self.servo.change_position(180)
        time.sleep(5)
        
