import threading
import time
from ThirdPartyAPIs.Adafruit_Motor_HAT_Python_Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class MotorFanThreading(threading.Thread):
    def __init__(self, motor, cycleOn = None, cycleOff = None, cycle = False):
        super(MotorFanThreading, self).__init__()
        self.CycleOn = cycleOn
        self.CycleOff = cycleOff
        self.isDead = False
        self.motor = motor

        self.cycle = cycle
        print "Started Motor"
        self.start()

    def run(self):
        if(self.cycle):
            while(not self.isDead):
                if(self.CycleOn != 0):
                    self.motor.run(Adafruit_MotorHAT.FORWARD)
                    self.motor.setSpeed(255)
                    print "motor on for " + str(self.CycleOn)
                    time.sleep(self.CycleOn)
                    print "motor off for " + str(self.CycleOff)
                    self.motor.run(Adafruit_MotorHAT.RELEASE)
                    time.sleep(self.CycleOff)
                    continue
                time.sleep(60)
                continue

        else:

            self.motor.run(Adafruit_MotorHAT.FORWARD)
            self.motor.setSpeed(255)
            while(not self.isDead):
                time.sleep(2147483647)
                continue
    def die(self):
        self.isDead = True
        print "motor is dead"
        self.motor.run(Adafruit_MotorHAT.RELEASE)
    def changeCycleOn(self, cycleOn):
        self.CycleOn = cycleOn
    def changeCycleOff(self, cycleOff):

        self.CycleOff = cycleOff






