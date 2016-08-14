

class Motor:
    MAXPOWER = 255
    NOPOWER = 0
    def __init__(self):
        self.ventMotorCycleOn = None
        self.ventMotorCycleOff = None
        self.intakeMotorCycleOn = None
        self.intakeMotorCycleOff = None
        self.exhaustMotorCycleOn = None
        self.exhaustMotorCycleOff = None
