import wx



class MenuBarController:
    def __init__(self, menuBarView, appGUI):
        self.menuBarView = menuBarView
        self.appGUI = appGUI
        self.HydroController = self.appGUI.getGUIController()

        self.initActionListners()

    def initActionListners(self):
        self.appGUI.Bind(wx.EVT_MENU, self.HydroController.onClose, self.menuBarView.getExitItem() )
        self.appGUI.Bind(wx.EVT_MENU, self.giveModeToController, self.menuBarView.getManualItem())
        self.appGUI.Bind(wx.EVT_MENU, self.giveModeToController, self.menuBarView.getTimerItem())
        self.appGUI.Bind(wx.EVT_MENU, self.giveModeToController, self.menuBarView.getEnvironmentalItem())
        self.appGUI.Bind(wx.EVT_MENU, self.giveRunToController, self.menuBarView.start)
        self.appGUI.Bind(wx.EVT_MENU, self.giveRunToController, self.menuBarView.stop)

    def giveRunToController(self, event):
        item = self.menuBarView.FindItemById(event.GetId())
        run = item.GetText()
        print run
        self.HydroController.setRun(run)

    def giveModeToController(self, event):
        item = self.menuBarView.FindItemById(event.GetId())
        mode = item.GetText()
        self.HydroController.setMode(mode)
    def initDefaultValue(self):
        self.HydroController.setRun(self.HydroController.hydroModel.OFF)
        self.HydroController.setMode(self.HydroController.hydroModel.MANUAL)





