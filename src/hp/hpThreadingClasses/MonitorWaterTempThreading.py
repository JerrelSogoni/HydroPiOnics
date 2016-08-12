import threading
import wx
from ThirdPartyAPIs.UnderwaterTemperatureReader.Temperature import Temperature
class MonitorWaterTempThreading(threading.Thread):
    def __init__(self, monitorController):
        super(MonitorWaterTempThreading, self).__init__()
        self.monitorController = monitorController
        self.isDead = False
        self.start()

    def run(self):
        while(self.isDead != True):
            waterTemp = Temperature.read_temp()
            wx.Yield()
            self.monitorController.setWaterTemperature(waterTemp)
            self.monitorController.updateWaterTemperatureView()

    def die(self):
        self.isDead = True
