from hpThreadingClasses.PumpDrainOutThreading import PumpDrainOutThreading
from hpThreadingClasses.PumpResToDrainThreading import PumpResToDrainThreading
from hpThreadingClasses.PumpPlantToResThreading import PumpPlantToResThreading
from hpThreadingClasses.PumpResToPlantThreading import PumpResToPlantThreading
import wx
class PumpController:

    def __init__(self, pumpView, pumpData, appData):
        self.pumpView = pumpView
        self.pumpData = pumpData
        self.appData = appData
        self.pumpResToPlant = None
        self.pumpResToDrain = None
        self.pumpPlantToRes = None
        self.pumpDrainOut = None

    def updateMode(self):
        for i in self.pumpView.threePumps:
            i.SetValue(False)
        self.pumpView.drainSystemCheckBox.SetValue(False)
        self.killPumps()

    def processResToPlantCheckbox(self, event):
        check = event.GetEventObject()
        self.pumpData.isResToPlantOn = check.GetValue()
        print check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startResToPlant()

    def startResToPlant(self):
        if((self.pumpData.isResToPlantOn is False) and (self.pumpResToPlant is not None)):
            self.pumpResToPlant.die()
            self.pumpResToPlant = None
        if(self.pumpData.isResToPlantOn and (self.pumpResToPlant is None)):
            self.pumpResToPlant = PumpResToPlantThreading()

    def processPlantDrainCheckbox(self,event):
        check = event.GetEventObject()
        self.pumpData.isPlantDrainOn = check.GetValue()
        print check.GetValue()
        if(self.appData.running == self.appData.ON):
            self.startPlantDrain()



    def startPlantDrain(self):
        if((self.pumpData.isPlantDrainOn is False) and (self.pumpResToDrain is not None)):
            self.pumpPlantToRes.die()
            self.pumpPlantToRes = None
        if (self.pumpData.isPlantDrainOn and (self.pumpResToDrain is None)):
            self.pumpPlantToRes = PumpPlantToResThreading()


    def processResDrainCheckbox(self,event):
        check = event.GetEventObject()
        self.pumpData.isResDrainOn = check.GetValue()
        print check.GetValue()
        if (self.appData.running == self.appData.ON):
            self.startResDrain()

    def startResDrain(self):
        if((self.pumpData.isResDrainOn is False)and (self.pumpResToDrain is not None) ):
            self.pumpResToDrain.die()
            self.pumpResToDrain = None
        if((self.pumpData.isResDrainOn) and (self.pumpResToDrain is None)):
            self.pumpResToDrain = PumpResToDrainThreading()


    def processDrainSystem(self, event):
        check = event.GetEventObject()
        self.pumpData.isDrainingOn = check.GetValue()
        if (self.appData.running == self.appData.ON):
            self.startDrainOut()


    def startDrainOut(self):
        if(self.pumpData.isDrainingOn is False and (self.pumpDrainOut is not None)):
            self.pumpDrainOut.die()
            self.pumpDrainOut = None
        if(self.pumpData.isDrainingOn and (self.pumpDrainOut is None)):
            if(self.pumpData.isResToPlantOn):
                self.pumpData.isResToPlantOn = False
                self.pumpView.mixToPlantCheckBox.SetValue(False)
                if(self.pumpResToPlant is not None):
                    self.pumpResToPlant.die()
                    self.pumpResToPlant = None
            if(self.pumpData.isPlantDrainOn):
                self.pumpData.isPlantDrainOn = False
                self.pumpView.planToMixCheckbox.SetValue(False)
                if(self.pumpPlantToRes is not None):
                    self.pumpPlantToRes.die()
                    self.pumpPlantToRes = None
            if(self.pumpData.isResDrainOn):
                self.pumpData.isResDrainOn = False
                self.pumpView.mixToDrainCheckBox.SetValue(False)
                if(self.pumpResToDrain is not None):
                    self.pumpResToDrain.die()
                    self.pumpResToDrain = None
            self.pumpView.mixToPlantCheckBox.Hide()
            self.pumpView.planToMixCheckbox.Hide()
            self.pumpView.mixToDrainCheckBox.Hide()
            self.pumpDrainOut = PumpDrainOutThreading(self.pumpView.threePumps)
    def killPumps(self):
        if(self.pumpResToPlant is not None):
            self.pumpResToPlant.die()
            self.pumpData.isResToPlantOn = False
            self.pumpView.mixToPlantCheckBox.SetValue(False)
        if(self.pumpResToDrain is not None):
            self.pumpResToDrain.die()
            self.pumpData.isResDrainOn = False
            self.pumpView.mixToDrainCheckBox.SetValue(False)
        if(self.pumpPlantToRes is not None):
            self.pumpPlantToRes.die()
            self.pumpData.isPlantDrainOn = False
            self.pumpView.planToMixCheckbox.SetValue(False)
        if(self.pumpDrainOut is not None):
            self.pumpDrainOut.die()
            self.pumpData.isDrainingOn = False
            self.pumpView.drainSystemCheckBox.SetValue(False)









