import wx
from controller.HydroPiOnicsController import *



class MenuBarController:
    def __init__(self, menuBarModel, menuBarView, appGUI):
        self.menuBarModel = menuBarModel
        self.menuBarView = menuBarView
        self.appGUI = appGUI
        self.initActionListners()

    def initActionListners(self):
        tempHydroController = self.appGUI.getGUIController()
        self.appGUI.Bind(wx.EVT_MENU, tempHydroController.onClose, self.menuBarView.getExitItem() )
        pass

