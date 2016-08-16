
class PumpController:
    def __init__(self, pumpView, pumpData, appData):
        self.pumpView = pumpView
        self.pumpData = pumpData
        self.appData = appData
    def processResToPlantCheckbox(self, checkboxValue):
        self.pumpData.isResToPlantOn = checkboxValue.getValue()
    def processPlantDrainCheckbox(self,checkboxValue):
        self.pumpData.isPlantDrainOn = checkboxValue.getValue()
    def processResDrainCheckbox(self,checkboxValue):
        self.pumpData.isResDrainOn = checkboxValue.getValue()


