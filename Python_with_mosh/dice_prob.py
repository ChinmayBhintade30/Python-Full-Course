#rolling 2 dice at a time
#create a roll function which will always generate 2 random number in tuple form 

#as we know --> the values of dice are 1 to 6 

#return the first no and second no in tuple  () or directly using , 

import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first, second)
    

#we have created a class named Dice which has the function roll 

dice = Dice()
#we created a object and given the value of class
print(dice.roll())
#accesing the object and roll function using , operator







