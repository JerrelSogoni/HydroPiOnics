#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

from src.hp.ThirdPartyAPIs.Adafruit_Python_DHT.examples import AdafruitDHT
#testing
def main():
    GPIO.setmode(GPIO.BCM)

    # init list with pin numbers

    #pinList = [21,20, 4, 5, 6, 7, 8, 9]
    pinList = [20]

    # loop through pins and set mode and state to 'low'

    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    # time to sleep between operations in the main loop

    SleepTimeL = 14400

    # main loop

    try:
     # GPIO.output(20, GPIO.LOW)
     # print "ONE"
     # time.sleep(SleepTimeL);
     # GPIO.output(21, GPIO.LOW)
     # print "TWO"
     # time.sleep(SleepTimeL);
     # GPIO.output(4, GPIO.LOW)
     # print "THREE"
     # time.sleep(SleepTimeL);
     # GPIO.output(5, GPIO.LOW)
     # print "FOUR"
     # time.sleep(SleepTimeL);
      isOn = False
      while True:
        try:
            humidity1, temp1 = AdafruitDHT2.main('22',22)
            humidity2, temp2 = AdafruitDHT2.main('22',23)
            time.sleep(1)
            avgH = (humidity1 + humidity2) / 2
            if(avgH >= 50 and isOn):
                GPIO.output(20, GPIO.HIGH)
                isOn = False
                print "Humidity Reached now turning Off"
            elif(avgH < 50 and isOn == False):
                GPIO.output(20,GPIO.LOW)
                isOn = True
                print "Humidity lower than 50 humifier activated"
            else:
                print "Is Humidifier On?: " + str(isOn)
        except:
            time.sleep(1)
            continue
      #GPIO.output(7, GPIO.LOW)
      #print "SIX"
      #time.sleep(SleepTimeL);
      #GPIO.output(8, GPIO.LOW)
      #print "SEVEN"
      #time.sleep(SleepTimeL);
      #GPIO.output(9, GPIO.LOW)
      #print "EIGHT"
      #time.sleep(SleepTimeL);
      GPIO.cleanup()
      print "Good bye!"

    # End program cleanly with keyboard
    except KeyboardInterrupt:
      print "  Quit"
    
      # Reset GPIO settings
      GPIO.cleanup()


    # find more information on this script at
    # http://youtu.be/oaf_zQcrg7g
if __name__ == '__main__':
    main()
