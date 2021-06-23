#Written by Stuart Anderson
#simple Dice roller program
#takes number of die sides
#returns result
import random


#Dice roller        
def roll(self,x):
    return random.randint(1,x)

#Dice roller with exploding dice
def rollx(self,x):
    r = roll(x)
    if r == x:
        return r + self.rollx(x)
    else:
        return r
