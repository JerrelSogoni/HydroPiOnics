
class ElectronicRelayEnvironmentController:
    def __init__(self, electronicRelayView, electronicRelayModel, appData):
        self.electronicRelayView = electronicRelayView
        self.electronicRelayModel = electronicRelayModel
        self.appData = appData



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

    def processAirFilterFanCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isAirFilterOn = check.GetValue()
        print check.GetValue()
    def processAirFilterCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.airFilterFanCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.airFilterFanCycleOn = 0
            cycleOn.SetValue("0")

    def processAirFilterCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.airFilterFanCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.airFilterFanCycleOff = 0
            cycleOff.SetValue("0")

    def processAirFilterCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnAirFilterFan.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.airFilterFanCycleOnUnits = cycleOnUnit

    def processAirFilterCycleOffUnits(self, event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffAirFilterFan.GetString(index)
        print cycleOffUnit
        self.electronicRelayModel.airFilterFanCycleOffUnits = cycleOffUnit
    def processAirHeaterCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isAirHeaterOn = check.GetValue()
        print check.GetValue()
    def processAirHeaterCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.airHeaterFanCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.airHeaterFanCycleOn = 0
            cycleOn.SetValue("0")
    def processAirHeaterCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.airHeaterFanCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.airHeaterFanCycleOff = 0
            cycleOff.SetValue("0")
    def processAirHeaterCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnAirHeaterFan.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.airHeaterFanCycleOnUnits = cycleOnUnit

    def processAirHeaterCycleOffUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffAirHeaterFan.GetString(index)
        print cycleOffUnit
        self.electronicRelayModel.airHeaterFanCycleOffUnits = cycleOffUnit
    def processLedCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isLedOn = check.GetValue()
        print check.GetValue()
    def processLedCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.ledCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.ledCycleOn = 0
            cycleOn.SetValue("0")

    def processLedCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.ledCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.ledCycleOff = 0
            cycleOff.SetValue("0")

    def processLedCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnLed.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.ledCycleOnUnits = cycleOnUnit

    def processLedCycleOffUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffLed.GetString(index)
        print cycleOffUnit
        self.electronicRelayModel.ledCycleOffUnits = cycleOffUnit

    def processUnderwaterHeaterCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isWaterHeaterOn = check.GetValue()
        print check.GetValue()
    def processUnderwaterHeaterCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.underWaterHeaterCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.underWaterHeaterCycleOn = 0
            cycleOn.SetValue("0")
    def processUnderwaterHeaterCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.underWaterHeaterCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.underWaterHeaterCycleOff = 0
            cycleOff.SetValue("0")

    def processUnderwaterHeaterCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnunderwater.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.underWaterHeaterCycleOnUnits = cycleOnUnit

    def processUnderwaterHeaterCycleOffUnits(self, event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffunderwater.GetString(index)
        self.electronicRelayModel.underWaterHeaterCycleOffUnits = cycleOffUnit
        print cycleOff
    def processHumidifierCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isHumidifierOn = check.GetValue()
        print check.GetValue()
    def processHumidifierCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.humidifierFanCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.humidifierFanCycleOn = 0
            cycleOn.SetValue("0")
    def processHumidifierCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.humidifierFanCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.humidifierFanCycleOff = 0
            cycleOff.SetValue("0")

    def processHumidifierCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnAirHumidFan.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.humidifierFanCycleOnUnits = cycleOnUnit

    def processHumidifierCycleOffUnits(self, event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffAirHumidFan.GetString(index)
        self.electronicRelayModel.humidifierFanCycleOffUnits = cycleOffUnit
        print cycleOff






