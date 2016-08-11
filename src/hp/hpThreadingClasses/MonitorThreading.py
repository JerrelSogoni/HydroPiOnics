import threading
import time
from src.hp.ThirdPartyAPIs.Adafruit-Motor-HAT-Python-Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

isDead = False
mh = Adafruit_MotorHAT(addr=0x60)
class MonitorThreading(threading.Thread):



    def turnOffMotors(self):
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    atexit.register(turnOffMotors)