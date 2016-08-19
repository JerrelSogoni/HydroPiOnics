import threading
import time
from ThirdPartyAPIs.Adafruit_Motor_HAT_Python_Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class MotorFanThreading(threading.Thread):
    def __init__(self, motor, cycleOn = None, cycleOff = None, cycle = False):
        super(MotorFanThreading, self).__init__()
        self.isDead = False
        self.motor = motor
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.cycle = cycle
        self.start()

    def run(self):

        if(self.cycle):
            while(not self.isDead):
                if(self.cycleOn != 0):
                    self.motor.run(Adafruit_MotorHAT.FORWARD)
                    self.motor.setSpeed(255)
                    time.sleep(self.cycleOn)
                    self.motor.run(Adafruit_MotorHAT.RELEASE)
                    time.sleep(self.cycleOff)

        else:

            self.motor.run(Adafruit_MotorHAT.FORWARD)
            self.motor.setSpeed(255)
            while(not self.isDead):
                time.sleep(2147483647)
                continue
    def die(self):
        self.isDead = True
        self.motor.run(Adafruit_MotorHAT.RELEASE)
    def changeCycleOn(self, cycleOn):
        self.cycleOn = cycleOn
    def changeCycleOff(self, cycleOff):
        self.cycleOff = cycleOff






