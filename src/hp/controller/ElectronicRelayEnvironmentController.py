
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
        print mode
        if(mode == self.appData.ENVIRONMENTAL):
            self.cycleOrEnvironmentalMode(True, True)
        elif(mode == self.appData.TIMER):
            self.cycleOrEnvironmentalMode(True, False)
        else:
            self.cycleOrEnvironmentalMode(False, False)

    def cycleOrEnvironmentalMode(self, cycles, environment):
        for cycles in self.electronicRelayView.cycleArray:
            if(cycles):
                cycles.Show(True)
            else:
                cycles.Hide()
        for environment in self.electronicRelayView.environmentalArray:
            if(environment):
                environment.Show(True)
            else:
                environment.Hide()

