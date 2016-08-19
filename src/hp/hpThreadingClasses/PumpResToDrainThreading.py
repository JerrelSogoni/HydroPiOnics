import threading
import RPi.GPIO as GPIO

import time
GPIO.setmode(GPIO.BCM)

class PumpResToDrainThreading(threading.Thread):
    def __init__(self,pin):
        super(PumpResToDrainThreading, self).__init__()
        self.pin = pin
        self.isDead = False
        self.start()


    def run(self):

        try:

            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)

            GPIO.output(self.pin, GPIO.LOW)

            print "Res to Drain Started"

            while(not self.isDead):
                time.sleep(2147483647)
                continue
        except:
            print "Error in ResToDrain"
            self.die()

    def die(self):
        self.isDead = True
        print "Res to Drain Stopped"
        GPIO.output(self.pin, GPIO.HIGH)



