import threading
import time
from ThirdPartyAPIs.MinipHBFW.BeagleBone.pHReader import pHReader
class MonitorPHThreading(threading.Thread):
    def __init__(self, monitorController):
        super(MonitorPHThreading, self).__init__()
        self.monitorController = monitorController
        self.isDead = False
        self.initPHSensor()
        self.start()
    def run(self):
        while(self.isDead != True):
            phLevel = self.getPHLevel()
            if(phLevel != self.monitorController.getPHLevel()):
                self.monitorController.setPHLevel(phLevel)
                self.monitorController.updatePHView()
            time.sleep(10)



    def initPHSensor(self):
        self.pHReader = pHReader()
    def getPHLevel(self):
        sample = self.pHReader.read()
        return self.pHReader.calc_ph(sample)




