import wx



class MenuBarController:
    def __init__(self, menuBarView, appGUI):
        self.menuBarView = menuBarView
        self.appGUI = appGUI
        self.HydroController = self.appGUI.getGUIController()
        self.fileManager = None
        self.initActionListners()

    def initActionListners(self):
        self.appGUI.Bind(wx.EVT_MENU, self.HydroController.onClose, self.menuBarView.getExitItem() )
        self.appGUI.Bind(wx.EVT_MENU, self.giveModeToController, self.menuBarView.getManualItem())
        self.appGUI.Bind(wx.EVT_MENU, self.giveModeToController, self.menuBarView.getTimerItem())
        self.appGUI.Bind(wx.EVT_MENU, self.giveModeToController, self.menuBarView.getEnvironmentalItem())
        self.appGUI.Bind(wx.EVT_MENU, self.giveRunToController, self.menuBarView.start)
        self.appGUI.Bind(wx.EVT_MENU, self.giveRunToController, self.menuBarView.stop)
        self.appGUI.Bind(wx.EVT_MENU, self.aboutMeLaunch, self.menuBarView.aboutMeItem)
        # self.appGUI.Bind(wx.EVT_MENU, self.giveFileFunction, self.menuBarView.saveItem)

    def aboutMeLaunch(self, event):
        dialog = wx.MessageDialog(self.appGUI, message="Application made by Jerrel Sogoni in the Summer of 2016",
                                  caption="About Me", style= wx.OK,
                                  pos=wx.DefaultPosition)
        response = dialog.ShowModal()


    def giveFileFunction(self, event):
        self.fileManager.save()
    def giveRunToController(self, event):
        item = self.menuBarView.FindItemById(event.GetId())
        run = item.GetText()
        self.HydroController.setRun(run)

    def giveModeToController(self, event):
        item = self.menuBarView.FindItemById(event.GetId())
        mode = item.GetText()
        self.HydroController.setMode(mode)
    def initDefaultValue(self):
        self.HydroController.setRun(self.HydroController.hydroModel.OFF)
        self.HydroController.setMode(self.HydroController.hydroModel.MANUAL)
    def setFileManager(self,fileManager):
        self.fileManager = fileManager





