import threading
import time
import wx
from ThirdPartyAPIs.UnderwaterTemperatureReader.Temperature import Temperature
class MonitorWaterTempThreading(threading.Thread):
    def __init__(self, monitorController):
        super(MonitorWaterTempThreading, self).__init__()
        self.monitorController = monitorController
        self.isDead = False
        self.initWaterTemperature()
        self.start()

    def run(self):
        while(self.isDead != True):
            try:
                waterTemp = self.waterTemperature.read_temp()
                self.monitorController.setWaterTemperature(waterTemp)
                wx.Yield()
                time.sleep(10)
                self.monitorController.updateWaterTemperatureView()
            except:
                time.sleep(5)
                continue

    def initWaterTemperature(self):
        self.waterTemperature = Temperature()

    def die(self):
        self.isDead = True
