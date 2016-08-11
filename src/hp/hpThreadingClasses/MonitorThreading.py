import threading
from ThirdPartyAPIs.Adafruit_Python_DHT.examples.AdafruitDHT2 import AdafruitDHT2
from ThirdPartyAPIs.MinipHBFW.BeagleBone.pHReader import pHReader
import ThirdPartyAPIs.UnderwaterTemperatureReader.Temperature as Temperature
from data.Monitor import Monitor
class MonitorThreading(threading.Thread):
    def __init__(self,monitorController):
        super(MonitorThreading, self).__init__()
        self.monitorController = monitorController
        self.isDead = False
        self.initAirTemperature()
        self.initpHSensor()


    def run(self):
        while(self.isDead != True):
            try:
                humidtyR, temperatureR = self.airTemperatureRightSideSensor.getHumidityandTemp()
                humidtyL, temperatureL = self.airTemperatureLeftSideSensor.getHumidityandTemp()
                humidityAvg, tempAvg = self.averageHumidityAndTemp(humidtyR,humidtyL,temperatureR,temperatureL)
                self.monitorController.setHumidity(humidityAvg)
                self.monitorController.setTemperature(tempAvg)
                self.monitorController.updateAirHumidityView()
            except:
                continue




    def initAirTemperature(self):
        self.airTemperatureRightSideSensor = AdafruitDHT2('22', Monitor.RIGHTSIDEAIRSENSOR)
        self.airTemperatureLeftSideSensor = AdafruitDHT2('22', Monitor.LEFTSIDEAIRSENSOR)
    def initpHSensor(self):
        self.pHReader = pHReader()

    def getWaterTemperature(self):
        return Temperature.read_temp()
    def averageHumidityAndTemp(self,humidityR,humidityL,tempR,tempL):
        humidityAvg = (humidityR + humidityR)/2
        tempAvg = (tempR + tempL)/2
        return humidityAvg, tempAvg





    def die(self):
        self.isDead = True