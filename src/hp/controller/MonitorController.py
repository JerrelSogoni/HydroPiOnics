import sys
from hpThreadingClasses.MonitorHumidityTemperatureThreading import MonitorHumidityTemperatureThreading
from hpThreadingClasses.MonitorWaterTempThreading import MonitorWaterTempThreading
from hpThreadingClasses.MonitorPHThreading import MonitorPHThreading
class MonitorController:
    def __init__(self, monitorModel, monitorView, appGUI):
        self.monitorModel = monitorModel
        self.monitorView = monitorView
        self.appGUI = appGUI
        self.monitorHumidityTempThreading = MonitorHumidityTemperatureThreading(self)
        self.monitorWaterTempThreading = MonitorWaterTempThreading(self)
        self.monitorPHThreading = MonitorPHThreading(self)



    def updateAirView(self):
        self.monitorView.setAirTemperatureText("{:.2f} F".format(self.monitorModel.getTemperature()))

    def updateHumidityView(self):
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
    def updateWaterTemperatureView(self):
        self.monitorView.setWaterTempText(str(self.monitorModel.getWaterTemperature()))
    def setPHLevel(self,ph):
        self.monitorModel.setPHLevel(ph)
    def getPHLevel(self):
        return self.monitorModel.getPHLevel()
    def updatePHView(self):
        self.monitorView.setPHText(str(self.monitorModel.getPHLevel()))


