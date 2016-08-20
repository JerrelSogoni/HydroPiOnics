

import wx
from gui.HydroPiOnicsView import HydroPiOnicsView
from data.HydroPiOnicsM import HydroPiOnicsM
from controller.HydroPiOnicsController import HydroPiOnicsController
from gui.MenuBarView import MenuBarView
from controller.MenuBarController import MenuBarController
from gui.MonitorView import MonitorView
from data.Monitor import Monitor
from controller.MonitorController import MonitorController
from gui.WorkspaceView import WorkspaceView
from data.Workspace import Workspace
from controller.WorkspaceController import WorkspaceController
from gui.MotorView import MotorView
from data.Motor import Motor
from controller.MotorController import MotorController
from gui.PumpView import PumpView
from data.Pump import Pump
from controller.PumpController import PumpController
from gui.EnvironmentalMonitorView import EvironmentalMonitorView
from data.EnvironmentalMonitor import EnvironmentalMonitor
from controller.EnvironmentalMonitorController import EnvironmentalMonitorController
from gui.ElectronicRelayEnviromentView import  ElectronicRelayEnviromentView
from data.ElectronicRelayEnviroment import ElectronicRelayEnviroment
from controller.ElectronicRelayEnvironmentController import ElectronicRelayEnvironmentController
from file.FileManager import FileManager



def create(parent):
    return HydroPiOnics(parent)

class HydroPiOnics(wx.Frame):

    def _init_ctrls(self, prnt):
        pass




    def __init__(self, parent):
        try:
            self.initFrameMVC()
            self.initMenuBarMVC()
            self.initWorkspaceMVC()
            self.initMonitorMVC()
            self.initMotorMVC()
            self.initPumpMVC()
            self.initEnvironmentalMonitorMVC()
            self.initElectronicRelayEnvironmentMVC()
            self.giveControllersToMainController()
            self.initDefaultMode()


        except KeyboardInterrupt:
            print "Shutting Down"
            self.guiController.killSystem()
        except:
            print "Error Occured"



        self._init_ctrls(parent)
    def initFrameMVC(self):
        self.gui = HydroPiOnicsView(self)
        self.guiModel =  HydroPiOnicsM()
        self.guiController = HydroPiOnicsController(self.guiModel, self.gui, self)
    def initMenuBarMVC(self):
        self.menuView = MenuBarView()
        self.SetMenuBar(self.menuView)
        self.menuController = MenuBarController(self.menuView, self)

    def initMotorMVC(self):
        self.motorView = MotorView(self.workspaceView)
        self.motorModel = Motor()
        self.motorController = MotorController(self.motorView,self.motorModel, self.guiModel)
        self.motorView.initController(self.motorController)
        self.motorView.initListeners()
    def initPumpMVC(self):
        self.pumpView = PumpView(self.workspaceView)
        self.pumpModel = Pump()
        self.pumpController = PumpController(self.pumpView, self.pumpModel, self.guiModel)
        self.pumpView.initController(self.pumpController)
        self.pumpView.initListeners()
    def initWorkspaceMVC(self):
        self.workspaceView = WorkspaceView(self)
        self.workspaceModel = Workspace()
        self.workspaceController = WorkspaceController(self.workspaceView, self.workspaceModel, self.guiModel)
        self.workspaceView.initController(self.workspaceController)
    def initMonitorMVC(self):

        self.monitorView = MonitorView(self)
        self.monitorModel = Monitor()
        self.monitorController = MonitorController(self.monitorModel, self.monitorView, self)

    def getGUIController(self):
        return self.guiController
    def initEnvironmentalMonitorMVC(self):
        self.environmentalMonitorView = EvironmentalMonitorView(self.workspaceView)
        self.environmentalMonitorModel = EnvironmentalMonitor()
        self.environmentalMonitorController = EnvironmentalMonitorController(self.environmentalMonitorView, self.environmentalMonitorModel, self.guiModel)
        self.environmentalMonitorView.initController(self.environmentalMonitorController)
        self.environmentalMonitorView.initListners()
    def initElectronicRelayEnvironmentMVC(self):
        self.electronicRelayView = ElectronicRelayEnviromentView(self.workspaceView)
        self.electronicRelayModel = ElectronicRelayEnviroment()
        self.electronicRelayController = ElectronicRelayEnvironmentController(self.electronicRelayView, self.electronicRelayModel, self.guiModel)
        self.electronicRelayView.initController(self.electronicRelayController)
        self.electronicRelayView.initListeners()
        self.environmentalMonitorController.setElectronicRelayController(self.electronicRelayController)

    def giveControllersToMainController(self):
        self.guiController.setElectronicRelayEnvironmentC(self.electronicRelayController)
        self.guiController.setEnvironmentalMonitorC(self.environmentalMonitorController)
        self.guiController.setMotorC(self.motorController)
        self.guiController.setMenuBarC(self.menuController)
        self.guiController.setPumpC(self.pumpController)
        self.guiController.setMonitorC(self.monitorController)
        self.guiController.setWorkspaceController(self.workspaceController)
    def initDefaultMode(self):
        self.menuController.initDefaultValue()


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
