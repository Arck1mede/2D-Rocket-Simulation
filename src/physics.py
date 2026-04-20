import numpy as np

AIR_DENSITY = 1.225 
DRAG_COEFFICIENT = 0.75 
TIME_STEP = 0.1 
AREA = 0.1 
GRAVITY_CONSTANT = 9.81 

def addVectors(first: np.array, second: np.array):
    return first + second

def subtractVectors(first: np.array, second: np.array):
    return first - second

def multiplyVecByNum(vec: np.array, num: int):
    return vec * num

def getVectorLength(vec: np.array):
    if vec is None: return
    return np.linalg.norm(vec)

def normalizeVector(vec: np.array):
    if vec is None or getVectorLength(vec) == 0: return
    return vec / getVectorLength(vec)

def getAcceleration(force, mass):
    return force / mass

def getDragMagnitude(speed):
    return 0.5 * AIR_DENSITY * speed**2 * DRAG_COEFFICIENT * AREA

def gravityForce(mass):
    return mass * GRAVITY_CONSTANT