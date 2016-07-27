

class Monitor:
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.waterTemperature = None
    def setTemperature(self, temp):
        self.temperature = temp
    def getTemperature(self):
        return self.temperature
    def setHumidity(self, humiditiy):
        self.humidity = humiditiy
    def getHumidity(self):
        return self.humidity
    def setWaterTemperature(self,temperature):
        self.waterTemperature = temperature
    def getWaterTemperature(self):
        return self.waterTemperature
