import wx
from data.HydroPiOnicsM import HydroPiOnicsM
from gui.HydroPiOnicsView import HydroPiOnicsView
class HydroPiOnicsController:
    def __init__(self, hydroModel, hydroView):
        self.hydroModel = hydroModel
        self.hydroView = hydroView

    def setName(self, name):
        self.hydroModel.set
