import threading
import RPi.GPIO as GPIO
import time
import data.ElectronicRelayEnviroment as ElectronicRelayEnvironment
import data.HydroPiOnicsM as appData
GPIO.setmode(GPIO.BCM)



class ledThreading(threading.Thread):
    def __init__(self, mode, cycleOn = None, cycleOff = None):
        super(ledThreading, self).__init__()
        self.isDead = False
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.mode = mode
        self.start()

    def run(self):
        try:
            self.pin = ElectronicRelayEnvironment.LEDPIN
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == appData.TIMER or self.mode == appData.ENVIRONMENTAL):
                while(not self.isDead):
                    GPIO.output(self.pin, GPIO.LOW)
                    print "Turning on Led for " + str(self.cycleOn)
                    time.sleep(self.cycleOn)
                    print "Turning off Led for " + str(self.cycleOff)
                    GPIO.output(self.pin, GPIO.HIGH)
                    time.sleep(self.cycleOff)
            else:
                GPIO.output(self.pin, GPIO.LOW)
                print "Led always On"
                while(not self.isDead):
                    continue

        except :
            print "Lights Off"
            self.die()


    def die(self):
        print "Lights Off"
        self.isDead = True
        GPIO.output(self.pin, GPIO.HIGH)








