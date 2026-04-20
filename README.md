# 🚀 2D Rocket Simulation
The project is about reproducing rocket movement by using thrust, gravity, rocket velocity, an angle theta, mass and fuel mass. After running the project, I keep track of of meaningful metrics to analyze the rocket: the position, velocity, thrust, fuel, some average metrics and the maximum altitude reached after completing burning the fuel.

## 💻 Technologies Used

* ```Numpy```

* ```Python```

* ```Math Module```

* ```Matplotlib```

## 🃏 Features

### The project is divided into three plots:

1. Position Plot: it shows the initial and last position of the rocket, measured by 'horizontal distance' on the x axis and altitude on the y axis.

2. Metrics Plot: it outlines three important metrics to gauge the rocket, namely velocity, acceleration and fuel. The metrics are shown until the simulation ends: whether it due to no fuel remaining or the rocket hits the ground.

3. Rocket Position Animation: it shows the real-time rocket position until there is no fuel left. When that happens, the maximum altitude is highlighted in red.

## 🏫 What I Learned

Here is what I learned after completing the project:

1.	Metrics: Simulations are all about physics and math mostly, therefore I had to calculate many physics-related metrics such as the total distance travelled, average metrics, rocket direction vector and thrust vector.
   
2.	FuncAnimation: I practiced more with FuncAnimation function to draw a real-time animation of the rocket: this involved updating the rocket current position as well as showing altitude, speed and remaining fuel.
   
3.	Newtonian Physics: I dove deep into the physics to understand how rockets work. They can be represented by a vector, have an acceleration, burn fuel over time and are also influenced by many things such as drag, gravity. All this had to be considered when updating physics in the project.
   
4.	Coherent Metric Units: one aspect I had to be careful with was to make sure every value I gave to each variable was consistent with all the other variables' metric units. 

## 💭 How Can It Be Improved?

- Realism: I don't consider the fact the as we move higher and higher, gravity decreases. Furthermore, I also make the assumption that the engine functions properly but, in reality, it can have failures during launch/travel.
- Improved Simulation: the real-time animation is good but I didn't add functionality for ex. stop/restart it to inspect it. This would greatly improve rocket monitoring.
- More Rockets!: it would be exciting to see many rockets launch, starting at different positions, velocities and fuels.


## 📹 Video
[Uploading 2D rocket simulation.mp4…](https://github.com/user-attachments/assets/31bac341-29ed-4336-af1c-4c7f22d31141
)
