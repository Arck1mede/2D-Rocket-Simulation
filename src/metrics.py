import numpy as np
import math
from physics import *

class Metrics:
    
    @staticmethod
    def getTotalDistanceTravelled(position):
        totalDistance = []
        
        for i in range(len(position) - 1):
            dist = math.dist(position[i], position[i + 1])
            totalDistance.append(dist)
            
        return sum(totalDistance)
    
    @staticmethod
    def getAvgFuelConsumptionRate(fuelList: list):
        if not fuelList: return
        fuelRates = []
        
        for i in range(len(fuelList) - 1):
            rate = (fuelList[i] - fuelList[i + 1]) / TIME_STEP
            fuelRates.append(rate)
        return np.mean(fuelRates)
    
    @staticmethod
    def getAvgMassOverTime(fuelMassesList: list, dryMass):
        massesOverTime = []
        
        for fuelMass in fuelMassesList:
            massAtPointInTime = dryMass + fuelMass
            massesOverTime.append(massAtPointInTime)
            
        return np.mean(massesOverTime)