import threading
import time


class MotorFanThreading(threading.Thread):
    def __init__(self, motor, cycleOn = None, cycleOff = None, cycle = False):
        super(MotorFanThreading, self).__init__()
        self.isDead = False
        self.motor = motor
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.cycle = cycle
        print motor
        print cycleOn
        print cycleOff

        self.start()

    def run(self):

        if(self.cycle):
            while(not self.isDead):
                #self.motor.run(Adafruit_MotorHAT.FORWARD)
                #self.motor.setSpeed(255)


                time.sleep(self.cycleOn)


                #self.motor.run(Adafruit_MotorHAT.RELEASE)
                time.sleep(self.cycleOff)

        else:

            # self.motor.run(Adafruit_MotorHAT.FORWARD)
            # self.motor.setSpeed(255)
            while(not self.isDead):
                continue
    def die(self):
        self.isDead = True
        print "died"

        #self.motor.run(Adafruit_MotorHAT.RELEASE)
    def changeCycleOn(self, cycleOn):
        self.cycleOn = cycleOn
    def changeCycleOff(self, cycleOff):
        self.cycleOff = cycleOff






