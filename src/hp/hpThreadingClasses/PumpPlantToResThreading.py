import threading
import RPi.GPIO as GPIO
import data.Pump as Pump
import time
GPIO.setmode(GPIO.BCM)

class PumpPlantToResThreading(threading.Thread):
    def __init__(self):
        super(PumpPlantToResThreading, self).__init__()
        self.isDead = False
        self.start()


    def run(self):
        self.pin = Pump.PLANTDRAINPIN
        try:
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)

            GPIO.output(self.pin, GPIO.LOW)
            print "Plant to Res Started"
            while not self.isDead:
                time.sleep(2147483647)
                continue
        except:
            print "Error in PLant Drain"
            self.die()

    def die(self):
        self.isDead = True
        print "Plant to Res Stopped"
        GPIO.output(self.pin, GPIO.HIGH)



