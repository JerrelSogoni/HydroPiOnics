import threading
import RPi.GPIO as GPIO
from data.Pump import Pump

class PumpResToDrainThreading(threading.Thread):
    def __init__(self):
        super(PumpResToDrainThreading, self).__init__()
        self.isDead = False
        self.start()


    def run(self):
        # self.pin = Pump.RESDRAINPIN
        try:
            # GPIO.setup(self.pin, GPIO.OUT)
            # GPIO.output(self.pin, GPIO.HIGH)
            #
            # GPIO.output(self.pin, GPIO.LOW)

            print "Res to Drain Started"

            while not self.isDead:
                continue
        except:
            print "Error in ResToDrain"
            self.die()

    def die(self):
        self.isDead = True
        print "Res to Drain Stopped"
        # GPIO.output(self.pin, GPIO.HIGH)



