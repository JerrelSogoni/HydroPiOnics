import threading
import sys
print sys.path
from ThirdPartyAPIs.Adafruit_Python_DHT.examples.AdafruitDHT2 import AdafruitDHT2
from data.Monitor import Monitor
class MonitorThreading(threading.Thread):
    def __init__(self,monitorController):
        super(MonitorThreading, self).__init__()
        self.monitorController = monitorController
        self.isDead = False
        self.initAirTemperature()

    def run(self):
        while(self.isDead != True):
            print "Hello"


    def initAirTemperature(self):
        self.airTemperatureRightSideSensor = AdafruitDHT2('22', Monitor.RIGHTSIDEAIRSENSOR)
        self.airTemperatureLeftSideSensor = AdafruitDHT2('22', Monitor.LEFTSIDEAIRSENSOR)
    def initpHSensor(self):
        self.pHReader = pHReader()

    def initUnderWaterSensor(self):
        pass





    def die(self):
        self.isDead = True