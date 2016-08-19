import wx

class HydroPiOnicsController:
    def __init__(self, hydroModel, hydroView, appGUI):
        self.hydroModel = hydroModel
        self.hydroView = hydroView
        self.appGUI = appGUI
        self.initActionListener()
        self.electronicRelayEnvironmentC = None
        self.environmentalMonitorC = None
        self.motorC = None
        self.menuBarC = None
        self.pumpC = None
        self.monitorC = None
        self.workspaceController = None


    def initActionListener(self):
        self.appGUI.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        dialog = wx.MessageDialog(self.appGUI, message="Are you sure you want to quit?", caption="Caption", style=wx.YES_NO,
                                  pos=wx.DefaultPosition)
        response = dialog.ShowModal()

        if (response == wx.ID_YES):
            self.appGUI.Destroy()
        else:
            event.StopPropagation()
    def setMode(self,mode):
            self.hydroModel.setMode(mode)
            self.motorC.updateMode(mode)
            self.electronicRelayEnvironmentC.updateMode(mode)
            self.environmentalMonitorC.updateMode(mode)
            self.setRun(self.hydroModel.OFF)
            self.menuBarC.menuBarView.stop.Check(True)





    def setRun(self,run):
        self.hydroModel.setRunning(run)
        self.workspaceController.setSystemStatus(run)
        self.workspaceController.updateSystemStatus()
        if(run == self.hydroModel.ON):
            self.checkPumps()
            self.checkMotors()
            self.checkRelay()


        else:
            self.pumpC.killPumps()
            self.motorC.killMotors()
            self.electronicRelayEnvironmentC.killAll()

    def setElectronicRelayEnvironmentC(self, electronicRelayEnvironmentC):
        self.electronicRelayEnvironmentC = electronicRelayEnvironmentC
    def setEnvironmentalMonitorC(self, environmentalMonitorC):
        self.environmentalMonitorC = environmentalMonitorC
    def setMotorC(self, motorC):
        self.motorC = motorC
    def setMenuBarC(self, menuBarC):
        self.menuBarC = menuBarC
    def setPumpC(self, pumpC):
        self.pumpC = pumpC
    def setMonitorC(self, monitorC):
        self.monitorC = monitorC
    def setWorkspaceController(self, workspaceController):
        self.workspaceController = workspaceController

    def checkPumps(self):
        if(self.pumpC.pumpData.isResToPlantOn):
            self.pumpC.startResToPlant()
        if(self.pumpC.pumpData.isPlantDrainOn):
            self.pumpC.startPlantDrain()
        if(self.pumpC.pumpData.isResDrainOn):
            self.pumpC.startResDrain()
        if(self.pumpC.pumpData.isDrainingOn):
            self.pumpC.startDrainOut()


    def checkMotors(self):
        print self.hydroModel.Mode
        if(self.hydroModel.Mode == self.hydroModel.MANUAL):
            if(self.motorC.motor.isExaustMotorOn):
                self.motorC.startExhaust()
            if(self.motorC.motor.isVentMotorOn):
                self.motorC.startVent()
            if(self.motorC.motor.isIntakeMotorOn):
                self.motorC.startIntake()
        if(self.motorC.motor.isWaterAirPumpOn):
            self.motorC.startWaterAirPump()
        if((self.hydroModel.Mode == self.hydroModel.TIMER) or (self.hydroModel.Mode == self.hydroModel.ENVIRONMENTAL)):
            self.motorC.startExhaustCycle()
            self.motorC.startVentCycle()
            self.motorC.startIntakeCycle()
    def checkRelay(self):
        if(self.hydroModel.Mode == self.hydroModel.MANUAL):
            if(self.electronicRelayEnvironmentC.electronicRelayModel.isAirFilterOn):
                self.electronicRelayEnvironmentC.startAirFilterManual()
            if(self.electronicRelayEnvironmentC.electronicRelayModel.isLedOn):
                self.electronicRelayEnvironmentC.startLedManual()
            if(self.electronicRelayEnvironmentC.electronicRelayModel.isAirHeaterOn):
                self.electronicRelayEnvironmentC.startHeaterManual()
            if(self.electronicRelayEnvironmentC.electronicRelayModel.isWaterHeaterOn):
                self.electronicRelayEnvironmentC.startUnderwaterManual()
            if(self.electronicRelayEnvironmentC.electronicRelayModel.isHumidifierOn):
                self.electronicRelayEnvironmentC.startHumidifierManual()
        elif(self.hydroModel.Mode == self.hydroModel.TIMER):
            self.electronicRelayEnvironmentC.startAirFilterCycle()
            self.electronicRelayEnvironmentC.startLedCycle()
            self.electronicRelayEnvironmentC.startHeaterCycle()
            self.electronicRelayEnvironmentC.startUnderwaterCycle()
            self.electronicRelayEnvironmentC.startHumidifierCycle()
        else:
            self.electronicRelayEnvironmentC.startAirFilterCycle()
            self.electronicRelayEnvironmentC.startLedCycle()
            self.electronicRelayEnvironmentC.startHeaterEvironmental(self.environmentalMonitorC.environmentalMonitorModel.airTempStartValue,
                                                                     self.environmentalMonitorC.environmentalMonitorModel.airTempEndValue, self.monitorC.monitorModel)

            self.electronicRelayEnvironmentC.startUnderwaterEnvironmental(self.environmentalMonitorC.environmentalMonitorModel.underwaterTempStartValue,
                                                                     self.environmentalMonitorC.environmentalMonitorModel.underwaterTempEndValue, self.monitorC.monitorModel)

            self.electronicRelayEnvironmentC.startHumidifierEnvironmental(self.environmentalMonitorC.environmentalMonitorModel.humidityStartValue,
                                                                          self.environmentalMonitorC.environmentalMonitorModel.humidityEndValue, self.monitorC.monitorModel)











