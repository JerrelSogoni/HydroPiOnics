import threading
import RPi.GPIO as GPIO
from data.Pump import Pump
import time
import wx

class PumpDrainOutThreading(threading.Thread):
    def __init__(self, list):
        super(PumpDrainOutThreading, self).__init__()
        self.DRAINOUTTIME = 300
        self.list = list
        self.start()

    def run(self):
        # self.pinList = [Pump.PLANTDRAINPIN, Pump.RESDRAINPIN]
        # for  i in self.pinList:
        #     GPIO.setup(i, GPIO.OUT)
        #     GPIO.output(i, GPIO.HIGH)

        try:
            # GPIO.output(self.pinList[0], GPIO.LOW)
            # GPIO.output(self.pinList[1], GPIO.LOW)
            # time.sleep(self.DRAINOUTTIME);
            print "Drain Out started"
            self.die()

        except:
            print "Error occured Drain Out System"
            self.die()

    def die(self):
        print "Drain Out Completed"
        # GPIO.output(self.pinList[0], GPIO.HIGH)
        # GPIO.output(self.pinList[1], GPIO.HIGH)
        for i in self.list:
            i.Show(True)


















