from hpThreadingClasses.ElectronicThreading import ElectronicThreading
import MotorController as calculate
class ElectronicRelayEnvironmentController:
    def __init__(self, electronicRelayView, electronicRelayModel, appData):
        self.electronicRelayView = electronicRelayView
        self.electronicRelayModel = electronicRelayModel
        self.appData = appData
        self.airFilterThreading = None
        self.airHeaterThreading = None
        self.underwaterHeaterThreading = None
        self.humidifierThreading = None
        self.ledThreading = None
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
        if(self.appData.running == self.appData.ON):
            self.startAirFilterManual()

    def processAirFilterCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.airFilterFanCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.airFilterFanCycleOn = 0
            cycleOn.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startAirFilterCycle()



    def processAirFilterCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.airFilterFanCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.airFilterFanCycleOff = 0
            cycleOff.SetValue("0")

        if (self.appData.running == self.appData.ON):
            self.startAirFilterCycle()


    def processAirFilterCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnAirFilterFan.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.airFilterFanCycleOnUnits = cycleOnUnit
        if (self.appData.running == self.appData.ON):
            self.startAirFilterCycle()


    def processAirFilterCycleOffUnits(self, event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffAirFilterFan.GetString(index)
        print cycleOffUnit
        self.electronicRelayModel.airFilterFanCycleOffUnits = cycleOffUnit
        if (self.appData.running == self.appData.ON):
            self.startAirFilterCycle()


    def processAirHeaterCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isAirHeaterOn = check.GetValue()
        print check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startHeaterManual()

    def processAirHeaterCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.airHeaterFanCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.airHeaterFanCycleOn = 0
            cycleOn.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startHeaterCycle()

    def processAirHeaterCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.airHeaterFanCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.airHeaterFanCycleOff = 0
            cycleOff.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startHeaterCycle()
    def processAirHeaterCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnAirHeaterFan.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.airHeaterFanCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startHeaterCycle()

    def processAirHeaterCycleOffUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffAirHeaterFan.GetString(index)
        print cycleOffUnit
        self.electronicRelayModel.airHeaterFanCycleOffUnits = cycleOffUnit
        if(self.appData.running == self.appData.ON):
            self.startHeaterCycle()
    def processLedCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isLedOn = check.GetValue()
        print check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startLedManual()
    def processLedCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.ledCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.ledCycleOn = 0
            cycleOn.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startLedCycle()

    def processLedCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.ledCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.ledCycleOff = 0
            cycleOff.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startLedCycle()

    def processLedCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnLed.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.ledCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startLedCycle()

    def processLedCycleOffUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffLed.GetString(index)
        print cycleOffUnit
        self.electronicRelayModel.ledCycleOffUnits = cycleOffUnit
        if(self.appData.running == self.appData.ON):
            self.startLedCycle()

    def processUnderwaterHeaterCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isWaterHeaterOn = check.GetValue()
        print check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startUnderwaterManual()
    def processUnderwaterHeaterCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.underWaterHeaterCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.underWaterHeaterCycleOn = 0
            cycleOn.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startUnderwaterCycle()
    def processUnderwaterHeaterCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.underWaterHeaterCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.underWaterHeaterCycleOff = 0
            cycleOff.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startUnderwaterCycle()

    def processUnderwaterHeaterCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnunderwater.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.underWaterHeaterCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startUnderwaterCycle()

    def processUnderwaterHeaterCycleOffUnits(self, event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffunderwater.GetString(index)
        self.electronicRelayModel.underWaterHeaterCycleOffUnits = cycleOffUnit
        print cycleOff
        if(self.appData.running == self.appData.ON):
            self.startHeaterCycle()
    def processHumidifierCheckbox(self, event):
        check = event.GetEventObject()
        self.electronicRelayModel.isHumidifierOn = check.GetValue()
        print check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startHumidifierManual()
    def processHumidifierCycleOn(self, event):
        cycleOn = event.GetEventObject()
        cycleOnValue = cycleOn.GetValue()
        print cycleOnValue
        if(cycleOnValue.isdigit()):
            self.electronicRelayModel.humidifierFanCycleOn = int(cycleOnValue)
        else:
            self.electronicRelayModel.humidifierFanCycleOn = 0
            cycleOn.SetValue("0")
            if (self.appData.running == self.appData.ON):
                self.startHumidifierCycle()
    def processHumidifierCycleOff(self, event):
        cycleOff = event.GetEventObject()
        cycleOffValue = cycleOff.GetValue()
        print cycleOffValue
        if(cycleOffValue.isdigit()):
            self.electronicRelayModel.humidifierFanCycleOff = int(cycleOffValue)
        else:
            self.electronicRelayModel.humidifierFanCycleOff = 0
            cycleOff.SetValue("0")
        if(self.appData.running == self.appData.ON):
            self.startHumidifierCycle()

    def processHumidifierCycleOnUnits(self, event):
        cycleOn = event.GetEventObject()
        index = cycleOn.GetCurrentSelection()
        cycleOnUnit = self.electronicRelayView.cycleOnAirHumidFan.GetString(index)
        print cycleOnUnit
        self.electronicRelayModel.humidifierFanCycleOnUnits = cycleOnUnit
        if(self.appData.running == self.appData.ON):
            self.startHumidifierCycle()

    def processHumidifierCycleOffUnits(self, event):
        cycleOff = event.GetEventObject()
        index = cycleOff.GetCurrentSelection()
        cycleOffUnit = self.electronicRelayView.cycleOffAirHumidFan.GetString(index)
        self.electronicRelayModel.humidifierFanCycleOffUnits = cycleOffUnit
        print cycleOffUnit
        if(self.appData.running == self.appData.ON):
            self.startHumidifierCycle()


    def startADeviceManual(self, pin):
        if(pin == self.electronicRelayModel.AIRFILTERPIN ):
            self.airFilterThreading = ElectronicThreading(pin, mode= self.appData.MANUAL, appData = self.appData)
        elif(pin == self.electronicRelayModel.AIRHEATERPIN):
            self.airHeaterThreading = ElectronicThreading(pin, mode=self.appData.MANUAL)
        elif(pin == self.electronicRelayModel.WATERHEATERPIN):
            self.underwaterHeaterThreading = ElectronicThreading(pin, mode=self.appData.MANUAL)
        elif(pin == self.electronicRelayModel.LEDPIN):
            self.ledThreading = ElectronicThreading(pin, mode=self.appData.MANUAL)
        elif(pin == self.electronicRelayModel.HUMIDIFIERPIN):
            self.humidifierThreading = ElectronicThreading(pin, mode=self.appData.MANUAL, appData = self.appData)
    def startADeviceCycle(self, pin, cycleOn, cycleOff):

        if (pin == self.electronicRelayModel.AIRFILTERPIN):
            self.airFilterThreading = ElectronicThreading(pin, mode=self.appData.TIMER,cycleOn = cycleOn,cycleOff = cycleOff)
        elif (pin == self.electronicRelayModel.AIRHEATERPIN):
            self.airHeaterThreading = ElectronicThreading(pin, mode=self.appData.TIMER, cycleOn = cycleOn,cycleOff = cycleOn)
        elif (pin == self.electronicRelayModel.WATERHEATERPIN):
            self.underwaterHeaterThreading = ElectronicThreading(pin, mode=self.appData.TIMER, cycleOn = cycleOn,cycleOff = cycleOff)
        elif (pin == self.electronicRelayModel.LEDPIN):
            self.ledThreading = ElectronicThreading(pin, mode=self.appData.TIMER, cycleOn = cycleOff,cycleOff = cycleOff)
        elif (pin == self.electronicRelayModel.HUMIDIFIERPIN):
            self.humidifierThreading = ElectronicThreading(pin, mode=self.appData.TIMER, cycleOn = cycleOn,cycleOff = cycleOff)
    def startADeviceEvironmental(self, pin, rangeLow, rangeHigh):
        if(pin == self.electronicRelayModel.AIRHEATERPIN):
            self.airHeaterThreading = ElectronicThreading(pin, mode=self.appData.ENVIRONMENTAL, rangeLow = rangeLow, rangeHigh = rangeHigh)
        elif (pin == self.electronicRelayModel.WATERHEATERPIN):
            self.underwaterHeaterThreading = ElectronicThreading(pin, mode=self.appData.ENVIRONMENTAL, rangeLow = rangeLow, rangeHigh = rangeHigh)
        elif (pin == self.electronicRelayModel.HUMIDIFIERPIN):
            self.humidifierThreading = ElectronicThreading(pin, mode=self.appData.ENVIRONMENTAL,rangeLow = rangeLow, rangeHigh = rangeHigh)


    def startAirFilterManual(self):
        self.startADeviceManual(self.electronicRelayModel.AIRFILTERPIN)
    def startAirFilterCycle(self):
        self.startADeviceCycle(self.electronicRelayModel.AIRFILTERPIN,
                               cycleOn=calculate.convertTimeToSeconds(self.electronicRelayModel.airFilterFanCycleOn, self.electronicRelayModel.airFilterFanCycleOnUnits),
                               cycleOff=calculate.convertTimeToSeconds(self.electronicRelayModel.airFilterFanCycleOff, self.electronicRelayModel.airFilterFanCycleOffUnits))
    def startHeaterManual(self):
        self.startADeviceManual(self.electronicRelayModel.AIRHEATERPIN)
    def startHeaterCycle(self):
        self.startADeviceCycle(self.electronicRelayModel.AIRHEATERPIN,
                               cycleOn=calculate.convertTimeToSeconds(self.electronicRelayModel.airHeaterFanCycleOn, self.electronicRelayModel.airHeaterFanCycleOnUnits),
                               cycleOff=calculate.convertTimeToSeconds(self.electronicRelayModel.airHeaterFanCycleOff, self.electronicRelayModel.airHeaterFanCycleOffUnits))
    def startHeaterEvironmental(self, rangeLow, rangeHigh):
        self.startADeviceCycle(self.electronicRelayModel.AIRHEATERPIN, rangeLow= rangeLow, rangeHigh = rangeHigh)

    def startLedManual(self):
        self.startADeviceManual(self.electronicRelayModel.LEDPIN)
    def startLedCycle(self):
        self.startADeviceCycle(self.electronicRelayModel.LEDPIN,
                               cycleOn=calculate.convertTimeToSeconds(self.electronicRelayModel.ledCycleOn, self.electronicRelayModel.ledCycleOnUnits),
                               cycleOff=calculate.convertTimeToSeconds(self.electronicRelayModel.ledCycleOff, self.electronicRelayModel.ledCycleOffUnits))

    def startUnderwaterManual(self):
        self.startADeviceManual(self.electronicRelayModel.WATERHEATERPIN)
    def startUnderwaterCycle(self):
        self.startADeviceCycle(self.electronicRelayModel.WATERHEATERPIN,
                               cycleOn=calculate.convertTimeToSeconds(self.electronicRelayModel.underWaterHeaterCycleOn, self.electronicRelayModel.underWaterHeaterCycleOnUnits),
                               cycleOff=calculate.convertTimeToSeconds(self.electronicRelayModel.underWaterHeaterCycleOff, self.electronicRelayModel.underWaterHeaterCycleOffUnits))
    def startUnderwaterEnvironmental(self, rangeLow, rangeHigh):
        self.startADeviceCycle(self.electronicRelayModel.WATERHEATERPIN, rangeLow=rangeLow, rangeHigh=rangeHigh)
    def startHumidifierManual(self):
        self.startADeviceManual(self.electronicRelayModel.HUMIDIFIERPIN)
    def startHumidifierCycle(self):
        self.startADeviceCycle(self.electronicRelayModel.HUMIDIFIERPIN,
                               cycleOn=calculate.convertTimeToSeconds(self.electronicRelayModel.humidifierFanCycleOn, self.electronicRelayModel.humidifierFanCycleOnUnits),
                               cycleOff=calculate.convertTimeToSeconds(self.electronicRelayModel.humidifierFanCycleOff, self.electronicRelayModel.humidifierFanCycleOffUnits))
    def startHumidifierEnvironmental(self, rangeLow, rangeHigh):
        self.startADeviceCycle(self.electronicRelayModel.HUMIDIFIERPIN, rangeLow=rangeLow, rangeHigh=rangeHigh)










