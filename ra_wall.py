from Myro import *

init("com10")

def avoidWalls():
    for t in timer(60):
        x = getObstacle(1)
        if x > 200:
            turnLeft(1,1)
        elif x < 200:
            forward(1,1)
    beep(1,850)
    turnRight(1,3)
    beep(1,800)
    turnLeft(1,3)
    beep(1,1000)

avoidWalls()