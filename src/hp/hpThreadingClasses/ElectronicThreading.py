import threading
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
class ElectronicThreading(threading.Thread):
    def __init__(self, device, mode= None, rangeLow = None, rangeHigh = None,cycleOn = None,cycleOff = None, appData = None, monitor = None , relayData = None):
        super(ElectronicThreading, self).__init__()

        self.relayData = relayData
        self.pin = device
        self.appData = appData
        self.monitor = monitor
        self.isDead = False
        self.isOn = False
        self.mode = mode
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.RangeLow = rangeLow
        self.RangeHigh = rangeHigh
        self.start()

    def run(self):

        try:
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == self.appData.TIMER):
                while(not self.isDead):
                    if(self.cycleOn != 0):
                        GPIO.output(self.pin, GPIO.LOW)
                        print  str(self.pin) +" On for " + str(self.cycleOn)
                        time.sleep(self.cycleOn)
                        if(self.cycleOff != 0):
                            print str(self.pin) +" Off for " + str(self.cycleOff)
                            GPIO.output(self.pin, GPIO.HIGH)
                            time.sleep(self.cycleOff)
                            continue
                    time.sleep(60)
                    continue
            elif(self.mode == self.appData.ENVIRONMENTAL):
                if(self.pin == self.relayData.WATERHEATERPIN):
                    while(not self.isDead):
                        if (self.monitor.waterTemperature < self.RangeLow):
                            if(not self.isOn):
                                GPIO.output(self.pin, GPIO.LOW)
                                self.isOn = True
                                continue
                            else:
                                time.sleep(60)
                                continue
                        elif (self.monitor.waterTemperature > self.RangeHigh):
                            print "Cannot really do much We dont have a water cooler"
                            GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False
                            time.sleep(60)
                            continue

                        else:
                            GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False
                            time.sleep(60)
                            continue
                elif(self.pin == self.relayData.AIRHEATERPIN):
                    while (not self.isDead):
                        if (self.monitor.temperature < self.RangeLow):
                            if (not self.isOn):
                                GPIO.output(self.pin, GPIO.LOW)
                                self.isOn = True
                            else:
                                time.sleep(60)
                                continue
                        else:
                            GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False
                            time.sleep(60)
                            continue
                elif(self.pin == self.relayData.HUMIDIFIERPIN):
                    while (not self.isDead):
                        if (self.monitor.humidity < self.RangeLow):
                            if (not self.isOn):
                                GPIO.output(self.pin, GPIO.LOW)
                                self.isOn = True
                                continue
                            else:
                                time.sleep(60)
                                continue
                        else:
                            GPIO.output(self.pin, GPIO.HIGH)
                            self.isOn = False
                            time.sleep(60)
                            continue


            else:
                  GPIO.output(self.pin, GPIO.LOW)
                  print "Looping"
                  while (not self.isDead):
                        time.sleep(2147483647)
                        continue
        except:
                print "Error in " + str(self.pin)
                self.die()

    def die(self):
        print str(self.pin) + " is Off"
        self.isDead = True
        GPIO.output(self.pin, GPIO.HIGH)

    def changeRangeLow(self, air):

        self.RangeLow = air
    def changeRangeHigh(self, air):
        self.RangeHigh = air


