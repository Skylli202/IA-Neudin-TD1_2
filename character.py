#Import


#Class
class Character:
    """Cette classe modelise les personnages de The Witcher"""

    def __init__(self, nom, prenom, age, profession, boostDeMoral):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boostDeMoral = float(boostDeMoral)

    # def __init__(self, chef):
    #     self.nom = chef.nom
    #     self.prenom = chef.prenom
    #     self.age = chef.age
    #     self.profession = chef.profession
    #     self.boostDeMoral = chef.boostDeMoral

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    def getBoostDeMoral(self):
        return self.boostDeMoral

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setAge(self, age):
        self.age = age

    def setProfession(self, profession):
        self.profession = profession

    def setBoostDeMoral(self, boostDeMoral):
        self.boostDeMoral = boostDeMoral

    def __str__(self):
        return self.prenom + " " + self.nom + ", " + self.age + " ans, " + self.profession + ", " + self.boostDeMoral + "."