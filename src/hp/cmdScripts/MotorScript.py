import sys
import time
import os

sys.path.insert(0, os.getcwd()[0:len(os.getcwd()) - 10] )
from ThirdPartyAPIs.Adafruit_Motor_HAT_Python_Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from hpThreadingClasses.MotorFanThreading import MotorFanThreading

VENTMOTOR = 1
INTAKEMOTOR = 2
EXHAUSTMOTOR = 4
WATERAIRPUMP = 3
motorObject = Adafruit_MotorHAT(addr=0x60)
ventFan = motorObject.getMotor(VENTMOTOR)
intakeFan = motorObject.getMotor(INTAKEMOTOR)
exhaustFan = motorObject.getMotor(EXHAUSTMOTOR)
waterAirPump = motorObject.getMotor(WATERAIRPUMP)



def main(cycleOn1,cycleOn1Units, cycleOff1, cycleOff1Units,
         cycleOn2,cycleOn2Units, cycleOff2, cycleOff2Units,
         cycleOn3,cycleOn3Units, cycleOff3, cycleOff3Units ):
    cycleOn1 = convertTimeToSeconds(cycleOn1, cycleOn1Units)
    cycleOff1 = convertTimeToSeconds(cycleOff1, cycleOff1Units)
    cycleOn2 = convertTimeToSeconds(cycleOn2, cycleOn2Units)
    cycleOff2 = convertTimeToSeconds(cycleOff2, cycleOff2Units)
    cycleOn3 = convertTimeToSeconds(cycleOn3, cycleOn3Units)
    cycleOff3 = convertTimeToSeconds(cycleOff3, cycleOff3Units)
    try:
        while(True):
            WaterPumpThread = MotorFanThreading(waterAirPump)
            VentThread = MotorFanThreading(ventFan, cycleOn = cycleOn1, cycleOff = cycleOff1, cycle = True )
            IntakeThread = MotorFanThreading(intakeFan, cycleOn=cycleOn2, cycleOff=cycleOff2, cycle=True)
            ExhaustThread = MotorFanThreading(exhaustFan, cycleOn=cycleOn3, cycleOff=cycleOff3, cycle=True)
            time.sleep(2147483647)
            continue
    except KeyboardInterrupt:
        VentThread.die()
        IntakeThread.die()
        ExhaustThread.die()
        WaterPumpThread.die()
        sys.exit()
        print "bye"



def convertTimeToSeconds(cycleTime, cycleUnit):
    cycleTime = float(cycleTime)
    if (cycleUnit == 's'):
        return cycleTime
    elif (cycleUnit == 'm'):
        return cycleTime * 60.0
    else:
        return cycleTime * 3600.0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1], sys.argv[2],sys.argv[3],
                  sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7]
                  ,sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12]))