import threading
import RPi.GPIO as GPIO
import time
import data.ElectronicRelayEnviroment as ElectronicRelayEnvironment
import data.HydroPiOnicsM as appData
import data.Monitor as monitor
GPIO.setmode(GPIO.BCM)

class UnderwaterHeaterThreading(threading.Thread):
    def __init__(self ,tempLow = None, tempHigh = None,cycleOn = None,cycleOff = None,mode= None):
        super(UnderwaterHeaterThreading, self).__init__()
        self.isDead = False
        self.mode = mode
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.tempLow = tempLow
        self.tempHigh = tempHigh

    def run(self):
        try:
            self.pin = ElectronicRelayEnvironment.WATERHEATERPIN
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == appData.TIMER ):
                while(not self.isDead):
                    GPIO.output(self.pin, GPIO.LOW)
                    print "Running for " + str(self.cycleOn)
                    time.sleep(self.cycleOn)
                    GPIO.output(self.pin, GPIO.HIGH)
                    print "Off for " + str(self.cycleOff)
                    time.sleep(self.cycleOff)

            elif(self.mode == appData.ENVIRONMENTAL):
                while(not self.isDead):
                    if(monitor.waterTemperature < self.tempLow):
                        GPIO.output(self.pin, GPIO.LOW)
                    elif(monitor.waterTemperature > self.tempHigh):
                        print "Cannot really do much We dont have a water cooler"
                    else:

                        GPIO.output(ElectronicRelayEnvironment.WATERHEATERPIN, GPIO.HIGH)
            else:
                GPIO.output(self.pin, GPIO.LOW)
                while(not self.isDead):
                    continue

        except:
            print "underwater Heater Died"
            self.die()

    def changeLowTemp(self, lowTemp):
        self.tempLow = lowTemp
    def changeHighTemp(self, highTemp):
        self.tempHigh = highTemp
    def die(self):
        print "Underwater Heater Died"
        self.isDead = True
        GPIO.output(self.pin, GPIO.HIGH)

