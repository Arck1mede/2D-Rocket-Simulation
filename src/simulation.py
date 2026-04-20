from physics import *
from physicsEngine import PhysicsEngine

class Simulation:
    
    def __init__(self) -> None:
        self.totalSimulationTime = 30 
        self.physicsEngine = PhysicsEngine()
        self.timeStep = TIME_STEP
        self.rocketPositionsOverTime = []
        self.rocketVelocitiesOverTime = []
        self.rocketAccelerations = []
        self.rocketFuels = []
        
    def runSimulation(self) -> None:
        numSteps = int(self.totalSimulationTime / TIME_STEP)
        for _ in range(numSteps):
            self.physicsEngine.applyPhysics()
            
            if (self.physicsEngine.rocket.position[1] <= 0) or (self.physicsEngine.rocket.fuelMass <= 0):
                break
            
            self.rocketPositionsOverTime.append(np.copy(self.physicsEngine.rocket.position))
            self.rocketVelocitiesOverTime.append(np.copy(self.physicsEngine.rocket.velocity))
            self.rocketAccelerations.append(np.copy(self.physicsEngine.rocket.acceleration))
            self.rocketFuels.append(np.copy(self.physicsEngine.rocket.fuelMass))