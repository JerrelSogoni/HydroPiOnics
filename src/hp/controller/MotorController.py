


class MotorController:
    def __init__(self, motorView, motor, appData):
        self.motorView = motorView
        self.motor = motor
        self.appData = appData

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
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        if(cycleOnValue.isdigit()):
            self.motor.exhaustMotorCycleOn = cycleOnValue
            print cycleOnValue
        else:
            self.motor.exhaustMotorCycleOn = 0
            cycleOn.SetValue(0)
            print "0"

    def processExhaustFanCycleOff(self,event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        if(cycleOffValue.isdigit()):
            self.motor.exhaustMotorCycleOff = cycleOffValue
            print cycleOffValue
        else:
            self.motor.exhaustMotorCycleOff = 0
            cycleOff.SetValue(0)


    def processExhaustFanCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnExaustFan.GetString(index)
        self.motor.exhaustCycleOnUnits = cycleOnUnit


    def processExhaustFanCycleOffUnits(self,event):
        cycleOff = event.GetEventObject()
        index = event.GetCurrentSelection()
        cycleOffUnit = self.motorView.cycleOffExaustFan.GetString(index)
        self.motor.exhaustCycleOffUnits = cycleOffUnit



    def processVentFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isVentMotorOn = check.GetValue()
    def processVentFanCycleOn(self,event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        if(cycleOnValue.isdigit()):
            self.motor.ventMotorCycleOn = cycleOnValue
        else:
            self.motor.ventMotorCycleOn = 0
            cycleOn.SetValue(0)

    def processVentFanCycleOff(self,event):
        cycleOff = event.getEventObject()
        cycleOffValue = event.GetValue()
        if (cycleOffValue.isdigit()):
            self.motor.ventMotorCycleOff = cycleOffValue
        else:
            self.motor.ventMotorCycleOff = 0
            cycleOff.SetValue(0)

    def processVentFanCycleOnUnits(self,event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnVentFan.GetString(index)
        self.motor.ventCycleOnUnits = cycleOnUnit
    def processVentFanCycleOffUnits(self,event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.motorView.cycleOffVentFan.GetString(index)
        self.motor.ventCycleOffUnits = cycleOffUnit
    def processIntakeFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isIntakeMotorOn = check.GetValue()
    def processIntakeFanCycleOn(self,event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        if(cycleOnValue.isdigit()):
            self.motor.intakeMotorCycleOn = cycleOnValue
        else:
            self.motor.intakeMotorCycleOn = 0
            cycleOn.SetValue(0)
    def processIntakeFanCycleOff(self,event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        if(cycleOffValue.isdigit()):
            self.motor.intakeMotorCycleOff = cycleOffValue
        else:
            self.motor.intakeMotorCycleOff = 0
            cycleOff.SetValue(0)
    def processIntakeFanCycleOnUnits(self,event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnIntakeFan.GetString(index)
        self.motor.intakeCycleOnUnits = cycleOnUnit
    def processIntakeFanCycleOffUnits(self,event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.motorView.cycleOffIntakeFan.GetString(index)
        self.motor.intakeMotorCycleOff = cycleOffUnit
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

