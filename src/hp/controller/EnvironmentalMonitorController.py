
class EnvironmentalMonitorController:
    def __init__(self, enviromentalMonitorView, environmentalMonitorModel, appData):
        self.environmentalMonitorView = enviromentalMonitorView
        self.environmentalMonitorModel = environmentalMonitorModel
        self.appData = appData
    def processHumidityStartValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        self.environmentalMonitorModel.humidityStartValue = sliderValue
        self.environmentalMonitorView.humidityRangeStartValue.SetValue(str(sliderValue))
        if(self.environmentalMonitorModel.humidityEndValue < sliderValue):
            print "changing end"
            self.environmentalMonitorModel.humidityEndValue = sliderValue
            self.environmentalMonitorView.humidityRangeEndValue.SetValue(str(sliderValue))
            self.environmentalMonitorView.humidityRangeEndSlider.SetValue(sliderValue)

    def processHumidityEndValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        if(sliderValue > self.environmentalMonitorModel.humidityStartValue):
            self.environmentalMonitorView.humidityRangeEndValue.SetValue(str(sliderValue))
            self.environmentalMonitorModel.humidityEndValue = sliderValue
        else:
            slider.SetValue(self.environmentalMonitorModel.humidityEndValue)


    def processTemperatureStartValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        self.environmentalMonitorModel.airTempStartValue =  sliderValue
        self.environmentalMonitorView.temperatureRangeStartValue.SetValue(str(sliderValue))
        if(self.environmentalMonitorModel.airTempEndValue <sliderValue):
            self.environmentalMonitorModel.airTempEndValue = sliderValue
            self.environmentalMonitorView.temperatureRangeEndValue.SetValue(str(sliderValue))
            self.environmentalMonitorView.temperatureRangeEndSlider.SetValue(sliderValue)
    def processTemperatureEndValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        if(sliderValue > self.environmentalMonitorModel.airTempStartValue):
            self.environmentalMonitorView.temperatureRangeEndValue.SetValue(str(sliderValue))
            self.environmentalMonitorModel.airTempEndValue = sliderValue
        else:
            slider.SetValue(self.environmentalMonitorModel.airTempEndValue)
    def processPHStartValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        self.environmentalMonitorModel.phStartValue = sliderValue
        self.environmentalMonitorView.pHLevelStartValue.SetValue(str(sliderValue))
        if(self.environmentalMonitorModel.phEndValue < sliderValue):
            self.environmentalMonitorModel.phEndValue = sliderValue
            self.environmentalMonitorView.phLevelEndValue.SetValue(str(sliderValue))
            self.environmentalMonitorView.pHRangeEndSlider.SetValue(sliderValue)
    def processPHEndValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        if (sliderValue > self.environmentalMonitorModel.phStartValue):
            self.environmentalMonitorView.pHLevelStartValue.SetValue(str(sliderValue))
            self.environmentalMonitorModel.phEndValue = sliderValue
        else:
            slider.SetValue(self.environmentalMonitorModel.phEndValue)
    def processUnderwaterStartValue(self,event):
        slider = event.GetEventObject()
        sliderValue = slider.GetValue()
        self.environmentalMonitorModel.underwaterTempStartValue = sliderValue
        self.environmentalMonitorView.underwaterTemperatureRangeStartValue.SetValue(str(sliderValue))
        if(self.environmentalMonitorModel.underwaterTempEndValue < sliderValue):
            self.environmentalMonitorModel.underwaterTempEndValue = sliderValue
            self.environmentalMonitorView.underwaterTemperatureRangeEndValue.SetValue(str(sliderValue))
            self.environmentalMonitorView.underwaterTemperatureRangeEndSlider.SetValue(sliderValue)
    def processUnderwaterEndValue(self,event):
        slider= event.GetEventObject()
        sliderValue = slider.GetValue()
        if (sliderValue > self.environmentalMonitorModel.underwaterTempStartValue):
            self.environmentalMonitorView.underwaterTemperatureRangeStartValue.SetValue(str(sliderValue))
            self.environmentalMonitorModel.underwaterTempEndValue = sliderValue
        else:
            slider.SetValue(self.environmentalMonitorModel.underwaterTempEndValue)

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






