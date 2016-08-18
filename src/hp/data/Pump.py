
class Pump:
    RESTOPLANTPIN = 5
    PLANTDRAINPIN = 6
    RESDRAINPIN = 12
    def __init__(self):
        self.isResToPlantOn = False
        self.isPlantDrainOn = False
        self.isResDrainOn = False
        self.isDrainingOn = False
