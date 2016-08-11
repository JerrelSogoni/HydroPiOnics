import sys
from hpThreadingClasses.MonitorThreading import MonitorThreading
class MonitorController:
    def __init__(self, monitorModel, monitorView, appGUI):
        self.monitorModel = monitorModel
        self.monitorView = monitorView
        self.appGUI = appGUI
        self.monitorThreading = MonitorThreading(self)

