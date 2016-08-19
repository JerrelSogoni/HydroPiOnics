import threading
import RPi.GPIO as GPIO
import data.Pump as Pump
import time
GPIO.setmode(GPIO.BCM)

class PumpResToPlantThreading(threading.Thread):
    def __init__(self):
        super(PumpResToPlantThreading, self).__init__()
        self.isDead = False
        self.start()


    def run(self):
        self.pin = Pump.RESTOPLANTPIN
        try:
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)

            GPIO.output(self.pin, GPIO.LOW)
            print "Res to Plant Started"
            while not self.isDead:
                time.sleep(2147483647)
                continue
        except:
            print "Error in Res to plant"
            self.die()

    def die(self):
        self.isDead = True
        print "Res to Plant stopped"
        GPIO.output(self.pin, GPIO.HIGH)
