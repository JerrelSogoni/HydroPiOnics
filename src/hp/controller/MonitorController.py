

class MonitorController:
    def __init__(self, monitorModel, monitorView, appGUI):
        self.monitorModel = monitorModel
        self.monitorView = monitorView
        self.appGUI = appGUI
        self.setPHText("10")

    def getPHText(self):
        return self.monitorView.pHSensor
    def getWaterTempText(self):
        return self.monitorView.waterTemperatureSensor
    def getHumidityText(self):
        return self.monitorView.humiditySensor
    def getAirTemperatureText(self):
        return self.monitorView.TemperatureSensor
    def setPHText(self,ph):
        self.monitorView.pHSensor.SetLabel(ph)
    def setWaterTempText(self,temp):
        self.monitorView.waterTemperatureSensor.SetLabel(temp)
    def setHumidityText(self,humidity):
        self.monitorView.humiditySensor.SetLabel(humidity)
    def setAirTemperatureText(self,temp):
        self.monitorView.TemperatureSensor.SetLabel(temp)