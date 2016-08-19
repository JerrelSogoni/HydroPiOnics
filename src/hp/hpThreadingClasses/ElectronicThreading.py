import threading
import RPi.GPIO as GPIO
import time
import data.ElectronicRelayEnviroment as ElectronicRelayEnvironment
import data.HydroPiOnicsM as appData
import data.Monitor as monitor
GPIO.setmode(GPIO.BCM)
class ElectronicThreading(threading.Thread):
    def __init__(self, device, mode= None,rangeLow = None, rangeHigh = None,cycleOn = None,cycleOff = None):
        super(ElectronicThreading, self).__init__()
        self.pin = device
        self.isDead = False
        self.isOn = False
        self.mode = mode
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.RangeLow = rangeLow
        self.RangeHigh = rangeHigh
        self.start()

    def run(self):
        print "run Entered"
        print self.mode
        try:
            # GPIO.setup(self.pin, GPIO.OUT)
            # GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == appData.TIMER):
                while(not self.isDead):
                    if(self.cycleOn != 0):
                        # GPIO.output(self.pin, GPIO.LOW)
                        print  str(self.pin) +" On for " + str(self.cycleOn)
                        time.sleep(self.cycleOn)
                        print str(self.pin) +" Off for " + str(self.cycleOff)
                        # GPIO.output(self.pin, GPIO.HIGH)
                        time.sleep(self.cycleOff)
            elif(self.mode == appData.ENVIRONMENTAL):
                if(self.pin == ElectronicRelayEnvironment.WATERHEATERPIN):
                    while(not self.isDead):
                        if (monitor.waterTemperature < self.RangeLow):
                            if(not self.isOn):
                                # GPIO.output(self.pin, GPIO.LOW)
                                self.isOn = True
                        elif (monitor.waterTemperature > self.RangeHigh):
                            print "Cannot really do much We dont have a water cooler"
                            # GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False

                        else:
                            # GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False
                elif(self.pin == ElectronicRelayEnvironment.AIRHEATERPIN):
                    while (not self.isDead):
                        if (monitor.temperature < self.RangeLow):
                            if (not self.isOn):
                                # GPIO.output(self.pin, GPIO.LOW)
                                self.isOn = True
                            else:
                                continue
                        else:
                            # GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False
                elif(self.pin == ElectronicRelayEnvironment.HUMIDIFIERPIN):
                    while (not self.isDead):
                        if (monitor.humidity < self.RangeLow):
                            if (not self.isOn):
                                # GPIO.output(self.pin, GPIO.LOW)
                                self.isOn = True
                            else:
                                continue
                        else:
                            # GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False


            else:
                  # GPIO.output(self.pin, GPIO.LOW)
                  print "Looping"
                  while (not self.isDead):

                        continue
        except:
                print "Error in " + str(self.pin)
                self.die()

    def die(self):
        print str(self.pin) + " is Off"
        self.isDead = True
        # GPIO.output(self.pin, GPIO.HIGH)

    def changeRangeLow(self, air):
        self.airLow = air
    def changeRangeHigh(self, air):
        self.airHigh = air

