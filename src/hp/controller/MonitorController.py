import sys
from hpThreadingClasses.MonitorThreading import MonitorThreading
class MonitorController:
    def __init__(self, monitorModel, monitorView, appGUI):
        self.monitorModel = monitorModel
        self.monitorView = monitorView
        self.appGUI = appGUI
        #self.monitorThreading = MonitorThreading(self)
        #self.monitorThreading.start()
    def updateAirHumidityView(self):
        self.monitorView.setAirTemperatureText("{:.2f} F".format(self.monitorModel.getTemperature()))
        self.monitorView.setHumidityText("{:.2f} %".format(self.monitorModel.getHumidity()))
    def setTemperature(self, temp):
        self.monitorModel.setTemperature(temp)
    def getTemperature(self):
        return self.monitorModel.getTemperature()
    def setHumidity(self, humiditiy):
        self.monitorModel.setHumidity(humiditiy)
    def getHumidity(self):
        return self.monitorModel.getHumidity()
    def setWaterTemperature(self,temperature):
        self.monitorModel.setWaterTemperature(temperature)
    def getWaterTemperature(self):
        return self.monitorModel.getWaterTemperature()



