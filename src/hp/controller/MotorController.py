



class MotorController:
    def __init__(self, motorView, motor, appData):
        self.motorView = motorView
        self.motor = motor
        self.appData = appData

    def updateMode(self, mode):
        if(mode != self.appData.MANUAL):
            self.cycleMode(True)
        else:
            self.cycleMode(False)

    def cycleMode(self, bool):
        for cycles in self.motorView.cycleArray:
            if(bool):
                cycles.Show(True)
            else:
                cycles.Hide()
