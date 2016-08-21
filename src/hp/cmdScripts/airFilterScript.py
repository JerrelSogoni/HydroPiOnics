import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)




def main(cycleOn,cycleOnUnits, cycleOff, cycleOffUnits ):
    pin = 4
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    cycleOn = convertTimeToSeconds(cycleOn, cycleOnUnits)
    cycleOff = convertTimeToSeconds(cycleOff, cycleOffUnits)
    try:
        while(True):
            GPIO.output(pin, GPIO.LOW)
            print "AirFilter On for " + str(cycleOn) + " seconds"
            time.sleep(cycleOn)
            GPIO.output(pin, GPIO.HIGH)
            print "AirFilter for " + str(cycleOff) + " seconds"
            time.sleep(cycleOff)
            continue
    except KeyboardInterrupt:
            GPIO.output(pin, GPIO.HIGH)










def convertTimeToSeconds(cycleTime, cycleUnit):
    if (cycleUnit == 's'):
        return float(cycleTime)
    elif (cycleUnit == 'm'):
        return cycleTime * 60.0
    else:
        return cycleTime * 3600.0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4]))