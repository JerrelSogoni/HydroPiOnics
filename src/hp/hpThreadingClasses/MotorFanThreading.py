import threading
import time


class MotorFanThreading(threading.Thread):
    def __init__(self, motor, cycleOn = None,CycleOff = None, cycle = False):
        super(MotorFanThreading, self).__init__()
        self.isDead = False
        self.motor = motor
        self.cycleOn = cycleOn
        self.cycleOff = CycleOff
        self.cycle = cycle
        self.start()

    def run(self):

        if(self.cycle):
            while(not self.isDead):
                #self.motor.run(Adafruit_MotorHAT.FORWARD)
                #self.motor.setSpeed(255)
                print "cycle on"
                time.sleep(self.cycleOn)
                print "cycle off"
                #self.motor.run(Adafruit_MotorHAT.RELEASE)
                time.sleep(self.cycleOff)

        else:
            print "cycle On"
            # self.motor.run(Adafruit_MotorHAT.FORWARD)
            # self.motor.setSpeed(255)
            while(not self.isDead):
                continue
    def die(self):
        self.isDead = True
        #self.motor.run(Adafruit_MotorHAT.RELEASE)
    def changeCycleOn(self, cycleOn):
        self.cycleOn = cycleOn
    def changeCycleOff(self, cycleOff):
        self.cycleOff = cycleOff






