



class MotorController:
    def __init__(self, motorView, motor, appData):
        self.motorView = motorView
        self.motor = motor
        self.appData = appData

    def updateMode(self, mode):
        if(mode != self.appData.MANUAL):
            self.environmentManual(True,False)
        else:
            self.environmentManual(False,True)

    def environmentManual(self, cycle, manuals):
        for cycles in self.motorView.cycleArray:
            if(cycle):
                cycles.Show(True)
            else:
                cycles.Hide()
        for manual in self.motorView.manualArray:
            if(manuals):
                manual.Show(True)
            else:
                manual.Hide()
