import threading
import RPi.GPIO as GPIO
import time
import data.ElectronicRelayEnviroment as ElectronicRelayEnvironment
import data.HydroPiOnicsM as appData
import data.Monitor as monitor
GPIO.setmode(GPIO.BCM)
class airHeaterThreading(threading.Thread):
    def __init__(self,airLow = None, airHigh = None,cycleOn = None,cycleOff = None,mode= None):
        super(airHeaterThreading, self).__init__()
        self.isDead = False
        self.mode = mode
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.airLow = airLow
        self.airHigh = airHigh
        self.start()

    def run(self):

        try:
            self.pin = ElectronicRelayEnvironment.AIRHEATERPIN
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == appData.TIMER):
                while(not self.isDead):
                    GPIO.output(self.pin, GPIO.LOW)
                    print "Air Heater On for " + str(self.cycleOn)
                    time.sleep(self.cycleOn)
                    print "Air Heater Off for " + str(self.cycleOff)
                    GPIO.output(self.pin, GPIO.HIGH)
                    time.sleep(self.cycleOff)
            elif(self.mode == appData.ENVIRONMENTAL):
                while(not self.isDead):
                    if(monitor.temperature < self.airLow):
                        if(not self.isOn):
                            GPIO.output(self.pin, GPIO.LOW)
                            self.isOn = True
                        else:
                            continue
                    else:
                        GPIO.output(self.pin, GPIO.HIGH)
                        self.isOn = False

            else:
                  GPIO.output(self.pin, GPIO.LOW)
                  while (not self.isDead):
                        continue
        except:
                print "Error in Air Heater"
                self.die()

    def die(self):
        self.isDead = True
        GPIO.output(self.pin, GPIO.HIGH)

    def changeAirLow(self, air):
        self.airLow = air
    def changeAirHigh(self, air):
        self.airHigh=





