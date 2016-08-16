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
        print mode
        self.hydroModel.setMode(mode)
        self.motorC.updateMode(mode)
        self.electronicRelayEnvironmentC.updateMode(mode)
        self.environmentalMonitorC.updateMode(mode)



    def setElectronicRelayEnvironmentC(self, electronicRelayEnvironmentC):
        self.electronicRelayEnvironmentC = electronicRelayEnvironmentC
    def setEnvironmentalMonitorC(self, environmentalMonitorC):
        self.environmentalMonitorC = environmentalMonitorC
    def setMotorC(self, motorC):
        self.motorC = motorC




