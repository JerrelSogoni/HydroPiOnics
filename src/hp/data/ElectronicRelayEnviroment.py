
class ElectronicRelayEnvironment:
    AIRFILTERPIN = 4
    LEDPIN = 13
    AIRHEATERPIN = 16
    WATERHEATERPIN = 19
    HUMIDIFIERPIN = 20

    def __init__(self):
        self.isAirFilterOn = False
        self.isLedOn = False
        self.isAirHeaterOn = False
        self.isWaterHeaterOn = False
        self.isHumidifierOn = False
        self.airFilterFanCycleOn = "0"
        self.airFilterFanCycleOff = "0"
        self.airFilterFanCycleOnUnits = 's'
        self.airFilterFanCycleOffUnits = 's'
        self.humidifierFanCycleOn = "0"
        self.humidifierFanCycleOff = "0"
        self.humidifierFanCycleOnUnits = 's'
        self.humidifierFanCycleOffUnits = 's'
        self.airHeaterFanCycleOn = "0"
        self.airHeaterFanCycleOff = "0"
        self.airHeaterFanCycleOnUnits = 's'
        self.airHeaterFanCycleOffUnits = 's'
        self.ledCycleOn = "0"
        self.ledCycleOff = "0"
        self.ledCycleOnUnits = 's'
        self.ledCycleOffUnits = 's'
        self.underWaterHeaterCycleOn = "0"
        self.underWaterHeaterCycleOff = "0"
        self.underWaterHeaterCycleOnUnits = 's'
        self.underWaterHeaterCycleOffUnits = 's'








