import matplotlib.pyplot as plt
import numpy as np
from simulation import Simulation
from physics import *
from metrics import Metrics
from matplotlib.animation import FuncAnimation

class Visualization:
    
    def __init__(self):
        self.simulation = Simulation()
        self.metrics = Metrics()
    
    def runSimulation(self):
        self.simulation.runSimulation()
    
    def getSimulationTime(self, values: list):
        return np.arange(len(values)) * TIME_STEP
    
    def createPositionVisualization(self):        
        plt.rcParams['font.family'] = 'monospace'
        xRocketPositions, yRocketPositions = [pos[0] for pos in self.simulation.rocketPositionsOverTime], [pos[1] for pos in self.simulation.rocketPositionsOverTime]
        
        plt.plot(xRocketPositions, yRocketPositions, color='#5d275d', label='Position', linewidth=1.2)
        plt.title("Position Metric")
        plt.grid(alpha=0.2)
        plt.xlabel("Horizontal Distance")
        plt.ylabel("Altitude")
        plt.legend(loc='upper left')
        plt.show()
        
    def createMagnitudeVisualization(self):
        speed = [getVectorLength(velocity) for velocity in self.simulation.rocketVelocitiesOverTime]
        accMagnitude = [getVectorLength(acc) for acc in self.simulation.rocketAccelerations]
        
        avgFuelConsumptionRate = self.metrics.getAvgFuelConsumptionRate(self.simulation.rocketFuels)
        avgMassOverTime = self.metrics.getAvgMassOverTime(self.simulation.rocketFuels, self.simulation.physicsEngine.rocket.dryMass)
        totalDistTravelled = self.metrics.getTotalDistanceTravelled(self.simulation.rocketPositionsOverTime)

        plt.plot(self.getSimulationTime(speed), speed, color='#ef7d57', label='Velocity', linewidth=1.2)
        plt.plot(self.getSimulationTime(accMagnitude), accMagnitude, color='#ffcd75', label='Acceleration', linewidth=1.2)
        plt.plot(self.getSimulationTime(self.simulation.rocketFuels), self.simulation.rocketFuels, color='#73eff7', label='Fuel', linewidth=1.2)
        
        plt.text(0, 170, s=f"Avg. Fuel Consumption Rate: {np.round(avgFuelConsumptionRate, 2)}")
        plt.text(0, 160, s=f"Avg. Mass Over Time: {np.round(avgMassOverTime, 2)}")
        plt.text(0, 150, s=f"Total Distance Travelled: {np.round(totalDistTravelled, 2)}")
        
        plt.title("Metrics")
        plt.grid(alpha=0.2)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.legend(loc='upper left')
        plt.show()

visualization = Visualization()
visualization.runSimulation()
visualization.createPositionVisualization()
visualization.createMagnitudeVisualization()

fig, ax = plt.subplots()

xRocketPositions, yRocketPositions = [pos[0] for pos in visualization.simulation.rocketPositionsOverTime], [pos[1] for pos in visualization.simulation.rocketPositionsOverTime]
maxAltitude = max(yRocketPositions)

scatterPlot = ax.scatter(xRocketPositions[0], yRocketPositions[0], s=20)
engineCutoffFrame = visualization.simulation.rocketFuels.index(min(visualization.simulation.rocketFuels))

altitudeText = ax.text(x=max(xRocketPositions) * 0.05, y=max(yRocketPositions) * 0.9, s="")
speedText = ax.text(x=max(xRocketPositions) * 0.05, y=max(yRocketPositions) * 0.85, s="")
fuelRemainingText = ax.text(x=max(xRocketPositions) * 0.05, y=max(yRocketPositions) * 0.8, s="")

ax.set_title("Rocket Position Over Time")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_xlim(0, max(xRocketPositions) * 1.1)
ax.set_ylim(0, max(yRocketPositions) * 1.1)
ax.grid(alpha=0.2)

def update(frame):
    x = xRocketPositions[:frame+1]
    y = yRocketPositions[:frame+1]
    
    data = np.stack([x, y]).T
    scatterPlot.set_offsets(data)
        
    currentVelocity = visualization.simulation.rocketVelocitiesOverTime[frame]
    velocitySpeed = getVectorLength(currentVelocity)
    currentAltitude = yRocketPositions[frame]
    
    altitudeText.set_text(f"Current Altitude: {np.round(currentAltitude, 2)}")
    speedText.set_text(f"Current Speed: {np.round(velocitySpeed, 2)}")
    fuelRemainingText.set_text(f"Current Fuel: {np.round(visualization.simulation.rocketFuels[frame], 2)}")

    if velocitySpeed < 100.0:
        scatterPlot.set_color('#257179')
    else:
        scatterPlot.set_color('#ef7d57')
    
    if frame == engineCutoffFrame:
        ax.axhline(y=maxAltitude, color='#b13e53', linestyle='--', label='Max. Altitude Reached')
        ax.legend(loc='upper right')
    
ani = FuncAnimation(fig=fig, 
                    func=update, 
                    frames=len(visualization.simulation.rocketFuels), 
                    interval=50, 
                    repeat=False, 
                    blit=False)
plt.show()