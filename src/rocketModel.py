import numpy as np
from physics import *

class Rocket:
    
    def __init__(self, position, velocity, acceleration, angle, dryMass, fuelMass, maxThrust, fuelBurnRate, currentThrottle) -> None:
        self.position = position 
        self.velocity = velocity 
        self.acceleration = acceleration 
        self.angle = angle 
        
        self.dryMass = dryMass 
        self.fuelMass = fuelMass 
        self.totalMass = self.dryMass + self.fuelMass
        self.maxThrust = maxThrust 
        self.fuelBurnRate = fuelBurnRate
        self.currentThrottle = min(max(currentThrottle, 0), 1) 
    
    def rocketDirectionVector(self) -> np.array:
        return np.array([np.cos(self.angle), np.sin(self.angle)])
    
    def decreaseFuel(self, dt: float):
        self.fuelMass -= self.fuelBurnRate * dt
    
    def engineState(self) -> bool:
        return self.fuelMass > 0
    
    def thrustVector(self):
        return self.rocketDirectionVector() * self.maxThrust * self.currentThrottle
    
    @property
    def fuelPercentage(self):
        try:
            return self.fuelMass / (self.fuelMass + self.dryMass)
        except ZeroDivisionError:
            print("Denominator is 0.")
            
    def computeAltitude(self):
        return self.position[1]
    
    def getThrustForce(self):
        return self.maxThrust * self.currentThrottle