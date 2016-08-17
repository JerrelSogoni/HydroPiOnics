from hpThreadingClasses.MotorFanThreading import MotorFanThreading

class MotorController:
    def __init__(self, motorView, motor, appData):
        self.motorView = motorView
        self.motor = motor
        self.appData = appData
        self.threadlist = []
        self.ventFanThreading = None
        self.intakeFanThreading = None
        self.exhaustFanThreading = None
        self.waterAirThreading = None
        self.threadlist.append(self.exhastFanThreading, self.intakeFanThreading, self.exhaustFanThreading,   self.waterAirThreading)

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
        if(self.appData.running == self.appData.ON):
            self.startExhaust()


    def processExhaustFanCycleOn(self,event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        if(cycleOnValue.isdigit()):
            self.motor.exhaustMotorCycleOn = cycleOnValue
            print cycleOnValue
        else:
            self.motor.exhaustMotorCycleOn = 0
            cycleOn.SetValue("0")
            print "0"

        if(self.appData.running == self.appData.ON):
            self.startExhaustCycle()

    def processExhaustFanCycleOff(self,event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        if(cycleOffValue.isdigit()):
            self.motor.exhaustMotorCycleOff = cycleOffValue
            print cycleOffValue
        else:
            self.motor.exhaustMotorCycleOff = 0
            cycleOff.SetValue("0")

        if(self.appData.running == self.appData.ON):
            self.startExhaustCycle()

    def processExhaustFanCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnExaustFan.GetString(index)
        self.motor.exhaustCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startExhaustCycle()

    def processExhaustFanCycleOffUnits(self,event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.motorView.cycleOffExaustFan.GetString(index)
        self.motor.exhaustCycleOffUnits = cycleOffUnit
        if(self.appData.running == self.appData.ON):
            self.startExhaustCycle()




    def processVentFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isVentMotorOn = check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startVent()

    def processVentFanCycleOn(self,event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        if(cycleOnValue.isdigit()):
            self.motor.ventMotorCycleOn = cycleOnValue
        else:
            self.motor.ventMotorCycleOn = 0
            cycleOn.SetValue("0")

        if(self.appData.running == self.appData.ON):
            self.startVentCycle()

    def processVentFanCycleOff(self,event):
        cycleOff = event.getEventObject()
        cycleOffValue = cycleOff.GetValue()
        if (cycleOffValue.isdigit()):
            self.motor.ventMotorCycleOff = cycleOffValue
        else:
            self.motor.ventMotorCycleOff = 0
            cycleOff.SetValue("0")

        if(self.appData.running == self.appData.ON):
            self.startVentCycle()

    def processVentFanCycleOnUnits(self,event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnVentFan.GetString(index)
        self.motor.ventCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startVentCycle()
    def processVentFanCycleOffUnits(self,event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.motorView.cycleOffVentFan.GetString(index)
        self.motor.ventCycleOffUnits = cycleOffUnit
        if(self.appData.running == self.appData.ON):
            self.startVentCycle()
    def processIntakeFanCheckbox(self,event):
        check = event.GetEventObject()
        self.motor.isIntakeMotorOn = check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startIntake()

    def processIntakeFanCycleOn(self,event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        if(cycleOnValue.isdigit()):
            self.motor.intakeMotorCycleOn = cycleOnValue
        else:
            self.motor.intakeMotorCycleOn = 0
            cycleOn.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startIntakeCycle()
    def processIntakeFanCycleOff(self,event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        if(cycleOffValue.isdigit()):
            self.motor.intakeMotorCycleOff = cycleOffValue
        else:
            self.motor.intakeMotorCycleOff = 0
            cycleOff.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startIntakeCycle()
    def processIntakeFanCycleOnUnits(self,event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.motorView.cycleOnIntakeFan.GetString(index)
        self.motor.intakeCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startIntakeCycle()
    def processIntakeFanCycleOffUnits(self,event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.motorView.cycleOffIntakeFan.GetString(index)
        self.motor.intakeMotorCycleOff = cycleOffUnit
        if(self.appData.running == self.appData.ON):
            self.startIntakeCycle()
    def processWaterAirPumpCheckBox(self,event):
        check = event.GetEventObject()
        self.motor.isWaterAirPumpOn = check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startWaterAirPump()

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

    def convertTimeToSeconds(self, cycleTime, cycleUnit):
        if(cycleUnit == 's'):
            return cycleTime
        elif(cycleUnit == 'm'):
            return cycleTime * 60
        else:
            return cycleTime * 3600
    def startMotor(self,motor, status, thread, mode, cycleOn, cycleOff):
        if((status is False) and (thread is not None) and (mode is self.appData.MANUAL)):
            print "Die"
            thread.die()
            thread = None

        elif(status and (thread is None) and (mode is self.appData.MANUAL)):
            thread = MotorFanThreading(motor)
        elif ((status is False) and (thread is not None) and (mode is self.appData.TIMER or mode is self.appData.ENVIRONMENTAL)):
            thread.changeCycleOn(cycleOn)
            thread.changeCycleOff(cycleOff)
        elif (status and (thread is None) and ((mode is self.appData.TIMER or mode is self.appData.ENVIRONMENTAL))):
            thread = MotorFanThreading(motor,cycleOn= cycleOn,cycleOff= cycleOff, cycle = True)
    def startExhaustCycle(self):
        self.startMotor(self.motor.exhaustFan, self.motor.isExaustMotorOn,
                        self.exhaustFanThreading, self.appData.Mode,
                        self.convertTimeToSeconds(self.motor.exhaustMotorCycleOn, self.motor.exhaustCycleOnUnits),
                        self.convertTimeToSeconds(self.motor.exhaustMotorCycleOff, self.motor.exhaustCycleOffUnits))
    def startVentCycle(self):
        self.startMotor(self.motor.ventFan, self.motor.isVentMotorOn,
                        self.ventFanThreading, self.appData.Mode,
                        self.convertTimeToSeconds(self.motor.ventMotorCycleOn, self.motor.ventCycleOnUnits),
                        self.convertTimeToSeconds(self.motor.ventMotorCycleOff, self.motor.ventCycleOffUnits))
    def startIntakeCycle(self):
        self.startMotor(self.motor.intakeFan, self.motor.isIntakeMotorOn,
                        self.intakeFanThreading, self.appData.Mode,
                        self.convertTimeToSeconds(self.motor.intakeMotorCycleOn, self.motor.intakeCycleOnUnits),
                        self.convertTimeToSeconds(self.motor.intakeMotorCycleOff, self.motor.intakeCycleOffUnits))
    def startExhaust(self):
        self.startMotor(self.motor.exhaustFan, self.motor.isExaustMotorOn,
                        self.exhaustFanThreading, self.appData.Mode,
                        None, None)
    def startIntake(self):
        self.startMotor(self.motor.intakeFan, self.motor.isIntakeMotorOn,
                        self.exhaustFanThreading, self.appData.Mode,
                        None, None)
    def startVent(self):
        self.startMotor(self.motor.ventFan, self.motor.isVentMotorOn,
                        self.exhaustFanThreading, self.appData.Mode,
                        None, None)
    def startWaterAirPump(self):
        self.startMotor(self.motor.waterAirPump, self.motor.isWaterAirPumpOn,
                        self.exhaustFanThreading, self.appData.Mode,
                        None, None)



    def killMotors(self):

        if(self.ventFanThreading is not None):
            self.ventFanThreading.die()
        if(self.intakeFanThreading is not None):
            self.intakeFanThreading.die()
        if(self.exhaustFanThreading is not None):
            self.exhaustFanThreading.die()
        if(self.waterAirThreading is not None):
            self.waterAirThreading.die()






