#Import
from random import uniform
from character import Character
from army import Army
import csv
import numpy as np

#def
def calc_All_Moral(listOfArmy):
    total = float(0.0)
    for army in listOfArmy:
        total += army.get_total_moral()
    return total

# -- MAIN --
#writer = csv.writer(open("C:/Users/eg785934/Desktop/characters.csv", "w"))
character_list = []
army_list = []
with open("./characters.csv", "r") as monfichier:
    reader = csv.reader(monfichier)
    next(reader) # In order to skip ['name', 'first name', 'age', 'profession', 'morale value']
    for row in reader:
        # print(row)
        c = Character(row[0], row[1], row[2], row[3], row[4])
        character_list.append(c)
        army_list.append(Army(c, uniform(20,100)))

somme = float(0)
for i in army_list:
    somme += i.get_total_moral()

# print "Total army : ",somme

# NUMPY
armyMoral = np.array([20,100,55, 60, 75])
chefMoral = np.array([0.97, 2, 1.3, 1.5, 0.1])
matrix = armyMoral.dot(chefMoral)
#print armyMoral
#print chefMoral
print matrix

# Perceptron
input = np.array([[0,0], [0,1], [1,0], [1, 1]])
output = np.array([0,0,0,1])

E = np.zeros((10,10))

for w1 in range(-5, 5):
    for w2 in range(-5, 5):
        for i in range(len(input)):
            y = (w1*input[i][0]) + (w2*input[i][1])
            if(y <= 0):
                y = 0
            else:
                y = 1
            t = output[i]
            E[w1+5, w2+5] += (1./2.) * (y-t)**2

print E









