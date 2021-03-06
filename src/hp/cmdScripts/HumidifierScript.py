import sys
import os
sys.path.insert(0, os.getcwd()[0:len(os.getcwd()) - 10] )
import RPi.GPIO as GPIO
import time
from ThirdPartyAPIs.Adafruit_Python_DHT.examples.AdafruitDHT2 import AdafruitDHT2
from data.Monitor import Monitor
GPIO.setmode(GPIO.BCM)




def main(cycleOn,cycleOnUnits, cycleOff, cycleOffUnits, mode , limit):
    pin = 20
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    airTemperatureRightSideSensor = AdafruitDHT2('22', Monitor.RIGHTSIDEAIRSENSOR)
    airTemperatureLeftSideSensor = AdafruitDHT2('22', Monitor.LEFTSIDEAIRSENSOR)
    on = False
    try:
        if(int(mode) == 0):
            cycleOn = convertTimeToSeconds(cycleOn, cycleOnUnits)
            cycleOff = convertTimeToSeconds(cycleOff, cycleOffUnits)
            while(True):
                GPIO.output(pin, GPIO.LOW)
                print "Heater On for " + str(cycleOn) + " seconds"
                time.sleep(cycleOn)
                GPIO.output(pin, GPIO.HIGH)
                print "Heater Off for " + str(cycleOff) + " seconds"
                time.sleep(cycleOff)
                continue
        else:
            while (True):
                try:
                    humidtyR, temperatureR = airTemperatureRightSideSensor.getHumidityandTemp()
                    humidtyL, temperatureL = airTemperatureLeftSideSensor.getHumidityandTemp()
                    humidityAvg, tempAvg = averageHumidityAndTemp(humidtyR, humidtyL, temperatureR, temperatureL)
                    print "Avg Humidity: " + str(humidityAvg)
                    if (humidityAvg < int(limit)):
                        if (not on):
                            GPIO.output(pin, GPIO.LOW)
                            on = True
                        else:
                            time.sleep(5)
                            continue
                    else:
                        GPIO.output(pin, GPIO.HIGH)
                        on = False
                        time.sleep(5)
                        continue
                    print "Humidity is" + str(on)
                except:
                    time.sleep(5)
                    continue

    except KeyboardInterrupt:
            GPIO.output(pin, GPIO.HIGH)










def convertTimeToSeconds(cycleTime, cycleUnit):
    cycleTime = float(cycleTime)
    if (cycleUnit == 's'):
        return cycleTime
    elif (cycleUnit == 'm'):
        return cycleTime * 60.0
    else:
        return cycleTime * 3600.0


def averageHumidityAndTemp(humidityR, humidityL, tempR, tempL):
    humidityAvg = (humidityR + humidityL) / 2
    tempAvg = (tempR + tempL) / 2
    return humidityAvg, tempAvg

if __name__ == '__main__':
	sys.exit(main(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4], sys.argv[5], sys.argv[6]))