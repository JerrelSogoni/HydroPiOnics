
class Pump:
    RESTOPLANTPIN = 5
    PLANTDRAINPIN = 6
    RESDRAINPIN = 12
    def __init__(self):
        self.isResToPlantOn = None
        self.isPlantDrainOn = None
        self.isResDrainOn = None
        self.isDrainingOn = None
