from physics import *
from rocketModel import Rocket
import numpy as np

class PhysicsEngine:
    
    def __init__(self):
        self.rocket = Rocket(np.array([0.0, 0.0]), np.array([0.0, 0.0]), acceleration=np.array([0.0, 0.0]), angle=np.pi/2, dryMass=80, fuelMass=40, maxThrust=3000, fuelBurnRate=1.5, currentThrottle=1.0)
        
    def applyPhysics(self):
        thrustVec = self.rocket.thrustVector()
        gravityVec = np.array([0, -self.rocket.totalMass * GRAVITY_CONSTANT])
        speed = getVectorLength(self.rocket.velocity)
        dragMagnitude = getDragMagnitude(speed)

        if speed > 0:
            dragDirection = -normalizeVector(self.rocket.velocity)
            dragVec = dragMagnitude * dragDirection
        else:
            dragVec = [0, 0]
        
        netForce = thrustVec + gravityVec + dragVec
        acc = netForce / self.rocket.totalMass
        self.rocket.acceleration = acc
        self.rocket.velocity += acc * TIME_STEP
        self.rocket.position += self.rocket.velocity * TIME_STEP
        self.rocket.decreaseFuel(TIME_STEP)