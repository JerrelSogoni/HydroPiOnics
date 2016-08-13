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
            try:
                phLevel = self.getPHLevel()
                if(phLevel != self.monitorController.getPHLevel()):
                    self.monitorController.setPHLevel(phLevel)
                    self.monitorController.updatePHView()
                time.sleep(10)
            except:
                print "Error in PH Sensor, re-reading in 5 seconds"
                time.sleep(5)
                continue


    def initPHSensor(self):
        self.pHReader = pHReader()
    def getPHLevel(self):
        print "fine"
        sample = self.pHReader.read()
        return self.pHReader.calc_ph(sample)




