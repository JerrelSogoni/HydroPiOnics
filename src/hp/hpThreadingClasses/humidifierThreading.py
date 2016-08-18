import threading
import RPi.GPIO as GPIO
import time
import data.ElectronicRelayEnviroment as ElectronicRelayEnvironment
import data.HydroPiOnicsM as appData
import data.Monitor as monitor
GPIO.setmode(GPIO.BCM)
class humidifierThreading(threading.Thread):
    def __init__(self,humidityLow = None, humidityHigh = None,cycleOn = None,cycleOff = None,mode= None):
        super(humidifierThreading, self).__init__()
        self.isDead = False
        self.humidityLow = humidityLow
        self.humidityHigh = humidityHigh
        self.cycleOn = cycleOn
        self.cycleOff = cycleOff
        self.mode = mode
        self.isOn = False
        self.start()

    def run(self):

        try:
            self.pin = ElectronicRelayEnvironment.HUMIDIFIERPIN
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH)
            if(self.mode == appData.TIMER):
                while(not self.isDead):
                    GPIO.output(self.pin, GPIO.LOW)
                    print "Humidifier On for " + str(self.cycleOn)
                    time.sleep(self.cycleOn)
                    print "Humidifier Off for " + str(self.cycleOff)
                    GPIO.output(self.pin, GPIO.HIGH)
                    time.sleep(self.cycleOff)
            elif(self.mode == appData.ENVIRONMENTAL):
                while(not self.isDead):
                    if(monitor.humidity < self.humidityLow):
                        if(not self.isOn):
                            GPIO.output(self.pin, GPIO.LOW)
                            self.isOn = True
                        else:
                            continue
                    else:
                        GPIO.output(self.pin, GPIO.HIGH)
                        self.isOn = False
            else:
                GPIO.output(self.pin, GPIO.LOW)
                while(not self.isDead):
                    continue
        except:
            print "Error in Humidifier"
            self.die()


    def changeHumidLow(self, humidLow):
        self.humidityLow = humidLow
    def changeHumidHigh(self, humidHigh):
        self.humidityHigh = humidHigh

    def die(self):
        print "Humidifer Off"
        self.isDead = True
        GPIO.output(self.pin, GPIO.HIGH)









