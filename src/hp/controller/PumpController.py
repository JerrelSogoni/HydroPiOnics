
class PumpController:
    def __init__(self, pumpView, pumpData, appData):
        self.pumpView = pumpView
        self.pumpData = pumpData
        self.appData = appData
    def processResToPlantCheckbox(self, event):
        check = event.GetEventObject()
        print "ResTo Plant CLicked"
        self.pumpData.isResToPlantOn = check.getValue()
    def processPlantDrainCheckbox(self,event):
        check = event.GetEventObject()
        print "PlantDrain clicked"
        self.pumpData.isPlantDrainOn = check.getValue()

    def processResDrainCheckbox(self,event):
        check = event.GetEventObject()
        print "ResDrain clicked"
        self.pumpData.isResDrainOn = check.getValue()


