import wx

class HydroPiOnicsController:
    def __init__(self, hydroModel, hydroView, appGUI):
        self.hydroModel = hydroModel
        self.hydroView = hydroView
        self.appGUI = appGUI
        self.initActionListener()


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
        print self.hydroModel.getMode()

