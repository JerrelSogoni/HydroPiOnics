import threading
import RPi.GPIO as GPIO
import time
import data.ElectronicRelayEnviroment as ElectronicRelayEnvironment
import data.HydroPiOnicsM as appData
GPIO.setmode(GPIO.BCM)
class airFilterThreading(threading.Thread):
    def __init__(self ,mode, cycleOn = None, cycleOff = None):
        super(airFilterThreading, self).__init__()
        self.isDead = False
        self.mode = mode
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.start()

    def run(self):
        try:
            self.pin = ElectronicRelayEnvironment.AIRFILTERPIN
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == appData.TIMER or self.mode == appData.ENVIRONMENTAL):
                while(not self.isDead):
                    GPIO.output(self.pin, GPIO.LOW)
                    print "Turning on Filter for " + str(self.cycleOn)
                    time.sleep(self.cycleOn)
                    print "Turning off Filter for " + str(self.cycleOff)
                    GPIO.output(self.pin, GPIO.HIGH)
                    time.sleep(self.cycleOff)
            else:
                GPIO.output(self.pin, GPIO.LOW)
                print "Filter always On"
                while(not self.isDead):
                    continue

        except :
            print "Filter Off"
            self.die()


    def die(self):
        print "Filter Off"
        self.isDead = True
        GPIO.output(self.pin, GPIO.HIGH)

