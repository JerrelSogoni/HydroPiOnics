
from ThirdPartyAPIs.Adafruit_Motor_HAT_Python_Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

VENTMOTOR = 1
INTAKEMOTOR = 2
EXHAUSTMOTOR = 4
WATERAIRPUMP = 3

class Motor:
    def __init__(self):

        self.ventMotorCycleOn = "0"
        self.ventMotorCycleOff = "0"
        self.isVentMotorOn = False
        self.ventCycleOffUnits = 's'
        self.ventCycleOnUnits = 's'
        self.intakeMotorCycleOn = "0"
        self.intakeMotorCycleOff = "0"
        self.isIntakeMotorOn = False
        self.intakeCycleOffUnits = 's'
        self.intakeCycleOnUnits = 's'
        self.exhaustMotorCycleOn = "0"
        self.exhaustMotorCycleOff = "0"
        self.isExaustMotorOn = False
        self.exhaustCycleOffUnits = 's'
        self.exhaustCycleOnUnits = 's'
        self.isWaterAirPumpOn = False
        self.motorObject = Adafruit_MotorHAT(addr=0x60)
        self.ventFan = self.motorObject.getMotor(VENTMOTOR)
        self.intakeFan = self.motorObject.getMotor(INTAKEMOTOR)
        self.exhaustFan = self.motorObject.getMotor(EXHAUSTMOTOR)
        self.waterAirPump = self.motorObject.getMotor(WATERAIRPUMP)



