from character import Character

class Army:
    def __init__(self, chef, moral):
        self.chef = chef
        self.moral = float(moral)

    def getChef(self):
        return self.chef

    def getMoral(self):
        return  self.moral

    def setChef(self, chef):
        self.chef = chef

    def setMoral(self, moral):
        self.moral = moral

    def __str__(self):
        return "Chef : " + self.chef + " et le moral est de " + self.moral + "."

    def get_total_moral(self):
        return float(self.moral * self.chef.boostDeMoral)
