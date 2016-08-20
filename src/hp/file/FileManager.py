import wx
import json

ISON = 'Status'
MODE = 'Mode'
MOTOR = 'Motors'
VENT = 'Vent'
VON = 'VentCycleOn'
VONUNITS = 'VentCycleOnUnits'
VOFF = 'VentCycleOff'
VOFFUNITS = 'VentCycleOffUnits'
EXHAUST = 'Exhaust'
EON = 'ExhaustCycleOn'
EONUNITS = 'ExhaustCycleOnUnits'
EOFF = 'ExhaustCycleOff'
EOFFUNITS = 'ExhaustCycleOffUnits'
INTAKE = 'Intake'
ION = 'IntakeCycleOn'
IONUNITS = 'IntakeCycleOnUnits'
IOFF = 'IntakeCycleOff'
IOFFUNITS = 'IntakeCycleOffUnits'
WATERAIR = 'WaterAir'
PUMPS = 'Pumps'
RESTOPLANT = 'ResToPlant'
PLANTTORES = 'PlantToRes'
RESTODRAIN = 'ResToDrain'
DRAINOUT = 'DrainOut'
RELAY = 'Relay'
AIRFILTER = 'AirFilter'
AIRFON = 'AirfilterCycleOn'
AIRFONUNITS = 'AirfilterCycleOnUnits'
AIRFOFF = 'AirfilterCycleOff'
AIRFOFFUNITS = 'AirfilterCycleOffUnits'
HUMIDIFIER = 'Humidifier'
HUMIDON = 'HumidifierCycleOn'
HUMIDONUNITS = 'HumidifierCycleOnUnits'
HUMIDOFF = 'HumidifierCycleOff'
HUMIDOFFUNITS = 'HumidifierCycleOffUnits'
HUMIDRANGELOW = 'HumidifierRangeLow'
HUMIDRANGEHIGH = 'HumidifierRangeHigh'
LED = 'Led'
LEDON = 'LedCycleOn'
LEDONUNITS = 'LedCycleOnUnits'
LEDOFF = 'LedCycleOff'
LEDOFFUNITS = 'LedCycleOffUnits'
AIRHEATER = 'AirHeater'
AIRHON = 'AirHeaterCycleOn'
AIRHONUNITS = 'AirHeaterCycleOnUnits'
AIRHOFF = 'AirHeaterCycleOff'
AIRHOFFUNITS = 'AirHeaterCycleOffUnits'
AIRHRANGELOW = 'AirHeaterRangeLow'
AIRHRANGEHIGH = 'AirHeaterRangeHigh'
UNDERWATERHEATER = 'UnderwaterHeater'
UNDERON = 'UnderwaterCycleOn'
UNDERONUNITS = 'UnderwaterCycleOnUnits'
UNDEROFF = 'UnderwaterCycleOff'
UNDEROFFUNITS = 'UnderwaterCycleOffUnits'
UNDERRANGELOW = 'UnderwaterRangeLow'
UNDERRANGEHIGH = 'UnderwaterRangeHigh'
PHRANGELOW = 'PHRangeLow'
PHRANGEHIGH = 'PHRangeHigh'
class FileManager:
    def __init__(self, appController):
        self.appController = appController
        self.appModel = self.appController.hydroModel
        self.motorController = self.appController.motorC
        self.motor = self.motorController.motor
        self.motorView = self.motorController.motorView
        
        self.relayController = self.appController.electronicRelayEnvironmentC
        self.electronicRelayModel = self.relayController.electronicRelayModel
        self.electronicRelayView = self.relayController.electronicRelayView
        
        self.environmentalController = self.appController.environmentalMonitorC
        self.environmentalMonitorModel = self.environmentalController.environmentalMonitorModel
        self.environmentalMonitorView = self.environmentalController.environmentalMonitorView
        self.pumpController = self.appController.pumpC
        
        self.pumpView = self.pumpController.pumpView
        self.pumpData = self.pumpController.pumpData
        self.workspaceController = self.appController.workspaceController

        
        
        self.currentSaveLocation = None
    def open(self):
        try:
            openFileDialog = wx.FileDialog(self, "Save As", "", "",
                                           "Json files (*.json)|*.json",
                                           wx.FD_OPEN)

        except:
            print "Error in Opening"

    def save(self):
        try:
            if(self.appModel.Saved == False):

                self.saveFileDialog = wx.FileDialog(self.appController.appGUI, "Save As", "", "",
                                               "Json files (*.json)|*.json",
                                                   wx.FD_SAVE )
                self.saveFileDialog.ShowModal()
                self.filePath = self.saveFileDialog.GetPath()
                self.saveFileDialog.Destroy()
                with open(self.filePath + ".json", 'w') as file:
                    json.dump(self.constructSaveJson(), file)
                self.currentSaveLocation = self.saveFileDialog.GetPath()
        except:
            print "error in save"



    def saveAs(self):
        pass

    def constructSaveJson(self):
        self.data = {}
        #turn off everything
        isAppOn = self.appModel.running
        appMode = self.appModel.Mode
        print "saving"
        self.data.update({ISON: isAppOn},{MODE:appMode})
        # constant checkboxes no matter what mode
        self.data.update({EXHAUST: self.motor.isExaustMotorOn},
                         {RESTOPLANT: self.pumpModel.isResToPlantOn},
                         {PLANTTORES: self.pumpModel.isPlantDrainOn},
                         {RESTODRAIN: self.pumpModel.isResToPlantOn},
                         {DRAINOUT: self.pumpModel.isDrainingOn})
        if(appMode == self.appModel.MANUAL ):
            self.saveManualState(self.data)

        elif(appMode == self.appModel.TIMER):
            self.saveCycleState(self.data)
        else:
            self.saveEnvironmentalState(self.data)
        return self.data


    def saveManualState(self, data):
        # motors
        data.update({MOTOR: {{VENT: self.motor.isVentMotorOn},
                    {INTAKE:    self.motor.isIntakeMotorOn},
                    {WATERAIR: self.motor.isWaterAirPumpOn}}})
        # relay

        data.update({RELAY: {{AIRFILTER: self.electronicRelayModel.isAirFilterOn},
                    {LED: self.electronicRelayModel.isLedOn},
                    {AIRHEATER: self.electronicRelayModel.isAirHeaterOn },
                    {UNDERWATERHEATER: self.electronicRelayModel.isWaterHeaterOn},
                    {HUMIDIFIER: self.electronicRelayModel.isHumidifierOn }}})


    def saveCycleState(self,data):
        data.update({RELAY: {{AIRFON : self.electronicRelayModel.airFilterFanCycleOn},
                             {AIRFONUNITS: self.electronicRelayModel.airFilterFanCycleOnUnits},
                             {AIRFOFF: self.electronicRelayModel.airFilterFanCycleOff },
                             {AIRFOFFUNITS: self.electronicRelayModel.airFilterFanCycleOffUnits },
                             {HUMIDON: self.electronicRelayModel.humidifierFanCycleOn},
                             {HUMIDONUNITS: self.electronicRelayModel.humidifierFanCycleOnUnits},
                             {HUMIDOFF: self.electronicRelayModel.humidifierFanCycleOff},
                             {HUMIDOFFUNITS: self.electronicRelayModel.humidifierFanCycleOffUnits },
                             {LEDON: self.electronicRelayModel.ledCycleOn },
                             {LEDONUNITS: self.electronicRelayModel.ledCycleOnUnits },
                             {LEDOFF: self.electronicRelayModel.ledCycleOff },
                             {LEDOFFUNITS: self.electronicRelayModel.ledCycleOffUnits},
                             {AIRHON: self.electronicRelayModel.airHeaterFanCycleOn},
                             {AIRHONUNITS: self.electronicRelayModel.airHeaterFanCycleOnUnits},
                             {AIRHOFF: self.electronicRelayModel.airHeaterFanCycleOff},
                             {AIRHOFFUNITS: self.electronicRelayModel.airHeaterFanCycleOffUnits },
                             {UNDERON: self.electronicRelayModel.underWaterHeaterCycleOn },
                             {UNDERONUNITS: self.electronicRelayModel.underWaterHeaterCycleOnUnits },
                             {UNDEROFF: self.electronicRelayModel.underWaterHeaterCycleOff},
                             {UNDEROFFUNITS: self.electronicRelayModel.underWaterHeaterCycleOffUnits}}})

    def saveEnvironmentalState(self, data):
        self.saveMotorCycle(data)
        data.update({RELAY: {{AIRFON : self.electronicRelayModel.airFilterFanCycleOn},
                             {AIRFONUNITS: self.electronicRelayModel.airFilterFanCycleOnUnits},
                             {AIRFOFF: self.electronicRelayModel.airFilterFanCycleOff },
                             {AIRFOFFUNITS: self.electronicRelayModel.airFilterFanCycleOffUnits },
                             {HUMIDRANGELOW: self.environmentalMonitorModel.humidityStartValue},
                             {HUMIDRANGEHIGH: self.environmentalMonitorModel.humidityEndValue},
                             {LEDON: self.electronicRelayModel.ledCycleOn },
                             {LEDONUNITS:self.electronicRelayModel.ledCycleOnUnits },
                             {LEDOFF: self.electronicRelayModel.ledCycleOff },
                             {LEDOFFUNITS: self.electronicRelayModel.ledCycleOffUnits},
                             {AIRHRANGELOW: self.environmentalMonitorModel.airTempStartValue},
                             {AIRHRANGEHIGH : self.environmentalMonitorModel.airTempEndValue },
                             {UNDERRANGELOW : self.environmentalMonitorModel.underwaterTempStartValue},
                             {UNDERRANGEHIGH: self.environmentalMonitorModel.underwaterTempEndValue},
                             {PHRANGELOW : self.environmentalMonitorModel.phStartValue},
                             {PHRANGEHIGH : self.environmentalMonitorModel.airTempEndValue}}})

    def saveMotorCycle(self,data):
        data.update({MOTOR: {{VON: self.motor.ventMotorCycleOn },
                             {VONUNITS: self.motor.ventMotorCycleOnUnits},
                             {VOFF: self.motor.ventMotorCycleOff},
                             {VOFFUNITS: self.motor.ventMotorCycleOffUnits},
                             {EON: self.motor.exhaustMotorCycleOn},
                             {EONUNITS: self.motor.exhaustCycleOnUnits},
                             {EOFF : self.motor.exhaustMotorCycleOff},
                             {EOFFUNITS: self.motor.exhaustCycleOffUnits},
                             {ION: self.motor.intakeMotorCycleOn},
                             {IONUNITS: self.motor.intakeCycleOnUnits},
                             {IOFF: self.motor.intakeMotorCycleOff},
                             {IOFFUNITS: self.motor.intakeCycleOffUnits}}})
