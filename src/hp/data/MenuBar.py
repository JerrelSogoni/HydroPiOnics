

class MenuBar:
    def __init__(self):
        self.MANUAL = "MANUAL"
        self.TIMER = "TIMER"
        self.mode = self.MANUAL

    def setMode(self, mode):
            self.mode = mode

    def getMode(self):
            return self.mode
