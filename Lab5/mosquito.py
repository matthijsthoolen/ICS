#!/usr/bin/python

import numpy as np
from globalFunctions import decision, decisionLogarithmic
import math 

class mosquito:

    # 0 = not infected = grey, 1 = infected = black
    colorList = ['#ECEAE5','black']

    def __init__(self, x, y, t, infected, hungry, age):
        """ Set the basic parameters for the mosquito """
        self.x = x
        self.y = y
        self.t = t
        self.infected = infected
        self.hungry = hungry  # 0 not hungry, 1 hungry
        self.age = age
        self.oviposition = 0

    def getColor(self):
        return self.colorList[self.infected]


    def checkDeath(self,maxAge):
        # If mosquito dies False
        if decisionLogarithmic(self.age / float(maxAge)):
            return False

        return True

    def step(self, maxX, maxY, t):
        """ Move the mosquito to a new place. Return tuple.  """

        # If already moved this T, stay in this cell
        if self.t >= t:
            return (self.x, self.y)
        else:
            # move in a random direction (hor., vert. or diag.), and do step
            # if it is stays within boundaries
            newY = self.y + np.random.randint(2) -1 
            newX = self.x + np.random.randint(2) -1 
            if 0 <= newY < maxY:
                self.y = newY
            if 0 <= newX < maxX:
                self.x = newX
                
        self.t = t
        self.age += 1

        # return tuple of new location
        return (self.x, self.y)

    def getToHumanStep(self, x, y):
        """ We found a human in the neighbourhoud, go to it """
        self.x = x
        self.y = y
        self.t = t
        self.age += 1
        return (self.x, self.y)
