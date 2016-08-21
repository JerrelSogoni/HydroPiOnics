import time
import sys
import os
sys.path.insert(0, os.getcwd()[0:len(os.getcwd()) - 10] )
from ThirdPartyAPIs.MinipHBFW.BeagleBone.pHReader import pHReader
from ThirdPartyAPIs.UnderwaterTemperatureReader.Temperature import Temperature
from ThirdPartyAPIs.Adafruit_Python_DHT.examples.AdafruitDHT2 import AdafruitDHT2
from data.Monitor import Monitor

def main( ):
    airTemperatureRightSideSensor = AdafruitDHT2('22', Monitor.RIGHTSIDEAIRSENSOR)
    airTemperatureLeftSideSensor = AdafruitDHT2('22', Monitor.LEFTSIDEAIRSENSOR)
    waterTemperature = Temperature()




    try:
        while(True):
            try:
                humidtyR, temperatureR = airTemperatureRightSideSensor.getHumidityandTemp()
                humidtyL, temperatureL = airTemperatureLeftSideSensor.getHumidityandTemp()
                humidityAvg, tempAvg = averageHumidityAndTemp(humidtyR, humidtyL, temperatureR, temperatureL)
                waterTemp = waterTemperature.read_temp()
                phReader = pHReader()
                phLevel = getPHLevel()

                print "Humidity Left : " + str(humidtyL) + " %"
                print "Humidity Right : " + str(humidtyR) + " %"
                print "Avg Humidity : " + str(humidityAvg) + " %"
                print
                print
                print "Temperature Left : " + str(temperatureL) + " F"
                print "Temperature Right : " + str(temperatureR) + " F"
                print "Avg Temperature : " + str(tempAvg) + " F"
                print
                print
                print "Underwater temp: " + str(waterTemp) + " F"
                print
                print
                print "PH LEVEL : " + str(phLevel)
                time.sleep(10)
                continue
            except:
                print "read failure re-reading"
                time.sleep(5)
                continue
    except KeyboardInterrupt:
            print "done"






def averageHumidityAndTemp(humidityR, humidityL, tempR, tempL):
            humidityAvg = (humidityR + humidityL) / 2
            tempAvg = (tempR + tempL) / 2
            return humidityAvg, tempAvg


def getPHLevel():
    sample = pHReader.read()
    return pHReader.calc_ph(sample)


if __name__ == '__main__':
	main()