


import wx.lib.buttons
from gui.HydroPiOnicsView import HydroPiOnicsView
from data.HydroPiOnicsM import HydroPiOnicsM
from controller.HydroPiOnicsController import HydroPiOnicsController
from gui.MenuBarView import MenuBarView
from data.MenuBar import MenuBar
from controller.MenuBarController import MenuBarController
from gui.MonitorView import MonitorView
from data.Monitor import Monitor
from controller.MonitorController import MonitorController
from gui.WorkspaceView import WorkspaceView


def create(parent):
    return HydroPiOnics(parent)

class HydroPiOnics(wx.Frame):

    def _init_ctrls(self, prnt):
        pass




    def __init__(self, parent):

        self.initFrameMVC()
        self.initMenuBarMVC()
        self.initMonitorMVC()
        self.initWorkspaceMVC()
        self._init_ctrls(parent)
    def initFrameMVC(self):
        self.gui = HydroPiOnicsView(self)
        self.guiModel =  HydroPiOnicsM()
        self.guiController = HydroPiOnicsController(self.guiModel, self.gui, self)
    def initMenuBarMVC(self):
        self.menuView = MenuBarView()
        self.SetMenuBar(self.menuView)
        self.menuModel = MenuBar()
        self.menuController = MenuBarController(self.menuModel, self.menuView, self)
    def initMonitorMVC(self):
        self.monitorView = MonitorView(self)
        self.monitorModel = Monitor()
        self.monitorController = MonitorController(self.monitorModel, self.monitorView, self)
    def initMotorMVC(self):
        pass
    def initRelayMVC(self):
        pass
    def initWorkspaceMVC(self):
        self.workspaceView = WorkspaceView(self)
    def getGUIController(self):
        return self.guiController
    # def OnCheckBox12Checkbox(self, event):
    #     event.Skip()
    #
    # def OnManualToggleButtonLeftDclick(self, event):
    #     event.Skip()
    #
    # def OnCheckBox3Checkbox(self, event):
    #     event.Skip()
    #
    # def OnExhaustFanCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnWaterAirCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnMixToPlantCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnPlanToMixCheckboxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnMixToDrainCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnTemperatureRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnHumidityRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnPHLevelStartValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnPhLevelEndValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnPHRangeStartSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnPHRangeEndSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnWaterAirPowerSliderCommandScroll(self, event):
    #     event.Skip()
    #
    # def OnCycleOnWaterAirPumpValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOffWaterAirPumpValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOnMixToPlantValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnCycleOffMixToPlantValueTextEnter(self, event):
    #     event.Skip()
    #
    # def OnDrainSystemCheckBoxCheckbox(self, event):
    #     event.Skip()
    #
    # def OnCycleOnWaterPumpChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOffWaterPumpChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOffPlantMixCycleChoice(self, event):
    #     event.Skip()
    #
    # def OnCycleOnPlantMixCycleChoice(self, event):
    #     event.Skip()
    #
    # def OnCheckPHCheckBoxCheckbox(self, event):
    #     event.Skip()
    # def initPage(self, parent):
    #     pass
    # def initMotor(self, parent):
    #     pass
    # def initRelay(self, parent):
    #     pass


if __name__ == '__main__':
    app = wx.App()
    frame = create(None)
    frame.Show()

    app.MainLoop()
