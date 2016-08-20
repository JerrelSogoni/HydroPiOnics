import sys
import RPi.GPIO as GPIO
import time
from ThirdPartyAPIs.UnderwaterTemperatureReader.Temperature import Temperature
from data.Monitor import Monitor
GPIO.setmode(GPIO.BCM)




def main(cycleOn,cycleOnUnits, cycleOff, cycleOffUnits, mode , limit):
    pin = 19
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    cycleOn = convertTimeToSeconds(cycleOn, cycleOnUnits)
    cycleOff = convertTimeToSeconds(cycleOff, cycleOffUnits)
    waterTemperature = Temperature()

    on = False
    try:
        if(mode == 1):
            while(True):
                GPIO.output(pin, GPIO.LOW)
                print "Water Heater On for " + str(cycleOn) + " seconds"
                time.sleep(cycleOn)
                GPIO.output(pin, GPIO.HIGH)
                print "Water Heater Off for " + str(cycleOff) + " seconds"
                time.sleep(cycleOff)
                continue
        else:
            while (True):
                try:
                    temp = waterTemperature.read_temp()
                    print "Avg Underwater Temp: " + str(temp)
                    if (temp < limit):
                        if (not on):
                            GPIO.output(pin, GPIO.LOW)
                            on = True
                        else:
                            time.sleep(60)
                            continue
                    else:
                        GPIO.output(pin, GPIO.HIGH)
                        on = False
                        time.sleep(60)
                        continue
                    print "Underwater Heater is" + str(on)
                except:
                    time.sleep(5)
                    continue

    except KeyboardInterrupt:
            GPIO.output(pin, GPIO.HIGH)










def convertTimeToSeconds(self, cycleTime, cycleUnit):
    if (cycleUnit == 's'):
        return float(cycleTime)
    elif (cycleUnit == 'm'):
        return cycleTime * 60.0
    else:
        return cycleTime * 3600.0


def averageHumidityAndTemp(self, humidityR, humidityL, tempR, tempL):
    humidityAvg = (humidityR + humidityR) / 2
    tempAvg = (tempR + tempL) / 2
    return humidityAvg, tempAvg

if __name__ == '__main__':
	sys.exit(main(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4], sys.argv[5]))