import wx



class MenuBarController:
    def __init__(self, menuBarModel, menuBarView, appGUI):
        self.menuBarModel = menuBarModel
        self.menuBarView = menuBarView
        self.appGUI = appGUI
        self.HydroController = self.appGUI.getGUIController()
        self.initActionListners()

    def initActionListners(self):
        self.appGUI.Bind(wx.EVT_MENU, self.HydroController.onClose, self.menuBarView.getExitItem() )
        self.menuBarView.getMenuMode().Bind(wx.EVT_MENU, self.giveModeToController)

    def giveModeToController(self, event):
        item = self.menuBarView.FindItemById(event.GetId())
        mode = item.GetText()
        self.HydroController.setMode(mode)
        return mode




