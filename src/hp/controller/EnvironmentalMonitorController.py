
class EnvironmentalMonitorController:
    def __init__(self, enviromentalMonitorView, environmentalMonitorModel, appData):
        self.environmentalMonitorView = enviromentalMonitorView
        self.environmentalMonitorModel = environmentalMonitorModel
        self.appData = appData
    def processHumidityStartValue(self,sliderValue):
        self.environmentalMonitorModel.humidityStartValue = sliderValue.GetValue()
        self.environmentalMonitorView.humidityRangeStartValue.SetValue(sliderValue.getValue)
        if(self.environmentalMonitorModel.humidityEndValue < sliderValue.getValue()):
            self.environmentalMonitorModel.humidityEndValue = sliderValue.GetValue()
            self.environmentalMonitorView.humidityRangeEndValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorView.humidityRangeEndSlider.SetValue(sliderValue.getValue())

    def processHumidityEndValue(self,sliderValue):
        if(not(sliderValue.getValue() < self.environmentalMonitorModel.humidityStartValue)):
            self.environmentalMonitorView.humidityRangeEndValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorModel.humidityEndValue = sliderValue.GetValue()

    def processTemperatureStartValue(self,sliderValue):
        self.environmentalMonitorModel.airTempStartValue = sliderValue.getValue()
        self.environmentalMonitorView.temperatureRangeStartValue.SetValue(sliderValue.getValue())
        if(self.environmentalMonitorModel.airTempEndValue < sliderValue.getValue()):
            self.environmentalMonitorModel.airTempEndValue = sliderValue.GetValue()
            self.environmentalMonitorView.temperatureRangeEndValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorView.temperatureRangeEndSlider.SetValue(sliderValue.getValue())
    def processTemperatureEndValue(self,sliderValue):
        if(not(sliderValue.getValue() < self.environmentalMonitorModel.airTempStartValue)):
            self.environmentalMonitorView.temperatureRangeEndValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorModel.airTempEndValue = sliderValue.GetValue()
    def processPHStartValue(self,sliderValue):
        self.environmentalMonitorModel.phStartValue = sliderValue.getValue()
        self.environmentalMonitorView.pHLevelStartValue.SetValue(sliderValue.getValue())
        if(self.environmentalMonitorModel.phEndValue < sliderValue.getValue()):
            self.environmentalMonitorModel.phEndValue = sliderValue.GetValue()
            self.environmentalMonitorView.phLevelEndValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorView.pHRangeEndSlider.SetValue(sliderValue.getValue())
    def processPHEndValue(self,sliderValue):
        if (not (sliderValue.getValue() < self.environmentalMonitorModel.phStartValue)):
            self.environmentalMonitorView.pHLevelStartValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorModel.phEndValue = sliderValue.GetValue()
    def processUnderwaterStartValue(self,sliderValue):

        self.environmentalMonitorModel.underwaterTempStartValue = sliderValue.getValue()
        self.environmentalMonitorView.underwaterTemperatureRangeStartValue.SetValue(sliderValue.getValue())
        if(self.environmentalMonitorModel.underwaterTempEndValue < sliderValue.getValue()):
            self.environmentalMonitorModel.underwaterTempEndValue = sliderValue.GetValue()
            self.environmentalMonitorView.underwaterTemperatureRangeEndValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorView.underwaterTemperatureRangeEndSlider.SetValue(sliderValue.getValue())
    def processUnderwaterEndValue(self,sliderValue):
        if (not (sliderValue.getValue() < self.environmentalMonitorModel.underwaterTempStartValue)):
            self.environmentalMonitorView.underwaterTemperatureRangeStartValue.SetValue(sliderValue.getValue)
            self.environmentalMonitorModel.underwaterTempEndValue = sliderValue.GetValue()

    def updateMode(self, mode):
        if(mode != self.appData.ENVIRONMENTAL):
            self.EnvironmentalMode(False)
        else:
            self.EnvironmentalMode(True)


    def EnvironmentalMode(self, bool):
        for sliders in self.environmentalMonitorView.sliderArray:
            if(bool):
                sliders.Show(True)
            else:
                sliders.Hide()
        for text in self.environmentalMonitorView.staticEnvironmentArray:
            if(bool):
                text.Show(True)
            else:
                text.Hide()
        for inputs in self.environmentalMonitorView.environmentInputArray:
            if(bool):
                inputs.Show(True)
            else:
                inputs.Hide()





