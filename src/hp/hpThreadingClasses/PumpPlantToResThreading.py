import threading
import RPi.GPIO as GPIO
from data.Pump import Pump

class PumpPlantToResThreading(threading.Thread):
    def __init__(self):
        super(PumpPlantToResThreading, self).__init__()
        self.isDead = False
        self.start()


    def run(self):
        # self.pin = Pump.PLANTDRAINPIN
        try:
            # GPIO.setup(self.pin, GPIO.OUT)
            # GPIO.output(self.pin, GPIO.HIGH)
            #
            # GPIO.output(self.pin, GPIO.LOW)
            print "Plant to Res Started"
            while not self.isDead:

                continue
        except:
            print "Error in PLant Drain"
            self.die()

    def die(self, bool):
        self.isDead = True
        print "Plant to Res Stopped"
        # GPIO.output(self.pin, GPIO.HIGH)



