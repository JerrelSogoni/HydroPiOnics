
class ElectronicRelayEnvironmentController:
    def __init__(self, electronicRelayView, electronicRelayModel, appData):
        self.electronicRelayView = electronicRelayView
        self.electronicRelayModel = electronicRelayModel
        self.appData = appData

    def processAirFilterCheckBox(self,checkboxValue):
        self.electronicRelayModel.isAirFilterOn = checkboxValue.getValue()
    def processLedCheckbox(self,checkboxValue):
        self.electronicRelayModel.isLedOn = checkboxValue.getValue()
    def processAirHeaterCheckbox(self,checkboxValue):
        self.electronicRelayModel.isAirHeaterOn = checkboxValue()
    def processWaterHeaterCheckbox(self,checkboxValue):
        self.electronicRelayModel.isWaterHeaterOn = checkboxValue.getValue()
    def processHumidifierCheckbox(self, checkboxValue):
        self.electronicRelayModel.isHumidifierOn = checkboxValue()

    def updateMode(self,mode):
        for objects in self.electronicRelayView.objects:
            objects.Hide()
        if(mode == self.appData.ENVIRONMENTAL):
            for cycles in self.electronicRelayView.cycleArray:
                cycles.Show(True)
            for evironmental in self.electronicRelayView.environmentalHideArray:
                evironmental.Hide()
        elif(mode == self.appData.TIMER):
            for cycles in self.electronicRelayView.cycleArray:
                cycles.Show(True)
        else:
            for manuals in self.electronicRelayView.manualArray:
                manuals.Show(True)



    def initDefaultValues(self):
        self.electronicRelayModel.isAirFilterOn = False
        self.electronicRelayModel.isLedOn = False
        self.electronicRelayModel.isAirHeaterOn = False
        self.electronicRelayModel.isWaterHeaterOn = False
        self.electronicRelayModel.isHumidifierOn = False


