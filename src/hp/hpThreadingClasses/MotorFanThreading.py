import threading
import time
from ThirdPartyAPIs.Adafruit_Motor_HAT_Python_Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

global CycleOn
global CycleOff
class MotorFanThreading(threading.Thread):
    def __init__(self, motor, cycleOn = None, cycleOff = None, cycle = False):
        super(MotorFanThreading, self).__init__()
        global CycleOn
        global CycleOff
        self.isDead = False
        self.motor = motor
        CycleOn = cycleOn
        CycleOff = cycleOff
        self.cycle = cycle
        self.start()

    def run(self):

        if(self.cycle):
            while(not self.isDead):
                if(self.cycleOn != 0):
                    self.motor.run(Adafruit_MotorHAT.FORWARD)
                    self.motor.setSpeed(255)
                    time.sleep(CycleOn)
                    self.motor.run(Adafruit_MotorHAT.RELEASE)
                    time.sleep(CycleOff)
                    continue
                time.sleep(2147483647)
                continue

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
        global CycleOn
        CycleOn = cycleOn
    def changeCycleOff(self, cycleOff):
        global CycleOff
        CycleOff = cycleOff






