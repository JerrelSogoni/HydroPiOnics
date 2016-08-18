import threading
import RPi.GPIO as GPIO
from data.Pump as pump
GPIO.setmode(GPIO.BCM)

class PumpResToDrainThreading(threading.Thread):
    def __init__(self):
        super(PumpResToDrainThreading, self).__init__()
        self.isDead = False
        self.start()


    def run(self):

        try:
            self.pin = pump.RESDRAINPIN
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)

            GPIO.output(self.pin, GPIO.LOW)

            print "Res to Drain Started"

            while(not self.isDead):
                continue
        except:
            print "Error in ResToDrain"
            self.die()

    def die(self):
        self.isDead = True
        print "Res to Drain Stopped"
        GPIO.output(self.pin, GPIO.HIGH)



