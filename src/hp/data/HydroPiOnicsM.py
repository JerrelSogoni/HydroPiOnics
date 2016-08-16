import wx

class HydroPiOnicsM:

    def __init__(self):
        self.ON = "ON"
        self.OFF = "OFF"
        self.MANUAL = "MANUAL"
        self.TIMER = "TIMER"
        self.ENVIRONMENTAL = "ENVIRONMENTAL"
        self.running = self.OFF 
        self.Mode = self.MANUAL
    def setRunning(self, running):
        self.running = running
    def getRunning(self):
        return self.running
    def setMode(self, mode):
        self.Mode = mode
    def getMode(self):
        return self.Mode
    def getON(self):
        return self.ON
    def getOFF(self):
        return self.OFF
    def getMANUAL(self):
        return self.MANUAL
    def getTIMER(self):
        return self.TIMER
    def getENVIROMENTAL(self):
        return self.ENVIRONMENTAL


