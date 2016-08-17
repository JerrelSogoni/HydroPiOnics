
from ThirdPartyAPIs.Adafruit_Motor_HAT_Python_Library.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor


class Motor:
    def __init__(self):
        self.VENTMOTOR = 1
        self.INTAKEMOTOR = 2
        self.EXHAUSTMOTOR = 4
        self.WATERAIRPUMP = 3
        self.ventMotorCycleOn = None
        self.ventMotorCycleOff = None
        self.isVentMotorOn = None
        self.ventCycleOffUnits = None
        self.ventCycleOnUnits = None
        self.intakeMotorCycleOn = None
        self.intakeMotorCycleOff = None
        self.isIntakeMotorOn = None
        self.intakeCycleOffUnits = None
        self.intakeCycleOnUnits = None
        self.exhaustMotorCycleOn = None
        self.exhaustMotorCycleOff = None
        self.isExaustMotorOn = None
        self.exhaustCycleOffUnits = None
        self.exhaustCycleOnUnits = None
        self.isWaterAirPumpOn = None
        self.motorObject = Adafruit_MotorHAT(addr=0x60)
        self.ventFan = self.motorObject.getMotor(self.VENTMOTOR)
        self.intakeFan = self.motorObject.getMotor(self.INTAKEMOTOR)
        self.exhaustFan = self.motorObject.getMotor(self.EXHAUSTMOTOR)
        self.waterAirPump = self.motorObject.getMotor(self.WATERAIRPUMP)



