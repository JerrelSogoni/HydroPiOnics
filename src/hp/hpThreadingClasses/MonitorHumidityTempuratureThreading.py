import threading
import time
from ThirdPartyAPIs.Adafruit_Python_DHT.examples.AdafruitDHT2 import AdafruitDHT2
from data.Monitor import Monitor
class MonitorHumidityTemperatureThreading(threading.Thread):
    def __init__(self,monitorController):
        super(MonitorHumidityTemperatureThreading, self).__init__()
        self.monitorController = monitorController
        self.isDead = False
        self.initAirTemperature()


    def run(self):
        while(self.isDead != True):
            try:
                humidtyR, temperatureR = self.airTemperatureRightSideSensor.getHumidityandTemp()
                humidtyL, temperatureL = self.airTemperatureLeftSideSensor.getHumidityandTemp()
                humidityAvg, tempAvg = self.averageHumidityAndTemp(humidtyR,humidtyL,temperatureR,temperatureL)
                self.monitorController.setHumidity(humidityAvg)
                self.monitorController.setTemperature(tempAvg)
                self.monitorController.updateAirHumidityView()
                time.sleep(5)
            except:
                time.sleep(2)
                continue


    def initAirTemperature(self):
        self.airTemperatureRightSideSensor = AdafruitDHT2('22', Monitor.RIGHTSIDEAIRSENSOR)
        self.airTemperatureLeftSideSensor = AdafruitDHT2('22', Monitor.LEFTSIDEAIRSENSOR)
    def averageHumidityAndTemp(self,humidityR,humidityL,tempR,tempL):
        humidityAvg = (humidityR + humidityR)/2
        tempAvg = (tempR + tempL)/2
        return humidityAvg, tempAvg
    def die(self):
        self.isDead = True