import wx

class HydroPiOnicsM:

    def __init__(self):
        self.ON = "RUNNING"
        self.OFF = "OFF"
        self.running = self.OFF
    def setRunning(self, running):
        self.running = running
    def getRunning(self):
        return self.running


