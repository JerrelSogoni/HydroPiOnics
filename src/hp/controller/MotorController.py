


class MotorController:
    def __init__(self, motorView, motor, appData):
        self.motorView = motorView
        self.motor = motor
        self.appData = appData
        self.initDefaultValue()

    def updateMode(self, mode):
        if(mode != self.appData.MANUAL):
            self.environmentManual(True,False)
            self.motorView.waterAirCheckBox.Show(True)
        else:
            self.environmentManual(False,True)

    def environmentManual(self, cycle, manuals):
        for cycles in self.motorView.cycleArray:
            if(cycle):
                cycles.Show(True)
            else:
                cycles.Hide()
        for manual in self.motorView.manualArray:
            if(manuals):
                manual.Show(True)
            else:
                manual.Hide()
    def processExhaustFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isExaustMotorOn = check.GetValue()
    def processExhaustFanCycleOn(self,event):
        cycleOn = event.getEventObject()
        cycleOnValue = cycleOn.GetStringSelection()
        if(cycleOnValue.isdigit()):
            self.motor.exhaustMotorCycleOn = cycleOnValue
    def processExhaustFanCycleOnUnits(self, event):
        cycleOn = event.getEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnExaustFan.GetString(index)
        self.motor.exhaustCycleOnUnits = cycleOnUnit
    def processExhaustFanCycleOff(self,event):
        cycleOff = event.getEventObject()
        cycleOffValue = cycleOff.GetStringSelection()
        if(cycleOffValue.isdigit()):
            self.motor.exhaustMotorCycleOff = cycleOffValue

    def processExhaustFanCycleOffUnits(self,event):
        pass
    def processVentFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isVentMotorOn = check.GetValue()
    def processVentFanCycleOn(self,event):
        cycleOn = event.getEventObject()
        cycleOnValue = cycleOn.GetStringSelection()
        if(cycleOnValue.isdigit()):
            self.motor.ventMotorCycleOn = cycleOnValue
    def processVentFanCycleOff(self,event):
        pass
    def processVentFanCycleOnUnits(self,event):
        pass
    def processVentFanCycleOffUnits(self,event):
        pass
    def processIntakeFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isIntakeMotorOn = check.GetValue()
    def processIntakeFanCycleOn(self,event):
        cycleOn = event.getEventObject()
        cycleOnValue = cycleOn.GetStringSelection()
        if(cycleOnValue.isdigit()):
            self.motor.intakeMotorCycleOn = cycleOnValue
    def processIntakeFanCycleOff(self,event):
        pass
    def processIntakeFanCycleOnUnits(self,event):
        pass
    def processIntakeFanCycleOffUnits(self,event):
        pass
    def processWaterAirPumpCheckBox(self,event):
        check = event.GetEventObject()
        self.motor.isWaterAirPumpOn = check.GetValue()
    def initDefaultValue(self):
        self.motor.ventMotorCycleOn = 0
        self.motor.ventMotorCycleOff = 0
        self.motor.isVentMotorOn = False
        self.motor.ventCycleOffUnits = 's'
        self.motor.ventCycleOnUnits = 's'
        self.motor.intakeMotorCycleOn = 0
        self.motor.intakeMotorCycleOff = 0
        self.motor.isIntakeMotorOn = False
        self.motor.intakeCycleOffUnits = 's'
        self.motor.intakeCycleOnUnits = 's'
        self.motor.exhaustMotorCycleOn = 0
        self.motor.exhaustMotorCycleOff = 0
        self.motor.isExaustMotorOn = False
        self.motor.exhaustCycleOffUnits = 's'
        self.motor.exhaustCycleOnUnits = 's'
        self.motor.isWaterAirPumpOn = False

