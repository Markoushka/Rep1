class Human:
    def __init__(self, name, ves):
        self.name = name
        self.ves = ves

    def showInfo(self):
        print("Name:", self.name, "ves:", self.ves)

class Brain(Human):
    def __init__(self, name, ves):
        super().__init__(name, ves)

class Leg(Human):
    def __init__(self, name, ves):
        super().__init__( name, ves)

class Heart(Human):
    def __init__(self, name, ves):
        super().__init__(name, ves)

myBrain = Brain("Brain", 1)
myBrain.showInfo()

myLeg = Leg("Leg", 5)
myLeg.showInfo()

myHeart = Heart("Heart", 0.2)
myHeart.showInfo()