#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment with my partner Elizabeth Hill, using only this semester's course materials

from Myro import *

init("com12")

win = Window()

record = open("myMovements.txt","w")

def sensor(left_light,right_light,right_obst):
    total = right_light + right_obst
    ans = left_light / total
    return ans

def keyPress(win, event):
    record = open("myMovements.txt","a")
    if event.key == "Up":
        forward(1,.1)
        a = sensor(getBright(0),getBright(2),getObstacle(2))
        a = str(a)
        b = "Forward .1 "+a+"\n"
        record.write(b)
    if event.key == "Down":
        backward(1,.1)
        a = sensor(getBright(0),getBright(2),getObstacle(2))
        a = str(a)
        b = "Backward .1 "+a+"\n"
        record.write(b)
    if event.key == "Left":
        turnLeft(1,.1)
        a = sensor(getBright(0),getBright(2),getObstacle(2))
        a = str(a)
        b = "Left .1 "+a+"\n"
        record.write(b)
    if event.key == "Right":
        turnRight(1,.1)
        a = sensor(getBright(0),getBright(2),getObstacle(2))
        a = str(a)
        b = "Right .1 "+a+"\n"
        record.write(b)
    if event.key == "b":
        beep(1,800)
        b = "Beep .1\n"
        record.write(b)
    record.close()

def collectData(record, direction):
    time = 0
    beeps = 0
    lines = 0
    record = open("myMovements.txt","r")
    for start in record.readlines():
        if start[:2] == "Ri" or start[:2] == "Le" or start[:2] == "Fo" or start[:2] == "Ba":
            time = time + .1
        elif start[:2] == "Be":
            beeps = beeps + 1
        if direction == "forward":
            if start[0] == "F":
                lines = lines + 1
        if direction == "backward":
            if start[:2] == "Ba":
                lines = lines + 1
        if direction == "right":
            if start[0] == "R":
                lines = lines + 1
        if direction == "left":
            if start[0] == "L":
                lines = lines + 1
    time = str(time)
    beeps = str(beeps)
    lines = str(lines)
    record.close()
    a = "The robot traveled for "+time+", beeping "+beeps+" times. This robot moved "+direction+" a total of "+lines+" times."
    return a

def replay(record):
    record = open("myMovements.txt","r")
    for start in record.readlines():
        if start[:2] == "Fo":
            forward(1,.1)
        if start[:2] == "Ba":
            backward(1,.1)
        if start[:2] == "Ri":
            turnRight(1,.1)
        if start[:2] == "Le":
            turnLeft(1,.1)
        if start[:2] == "Be":
            beep(1,800)
    record.close()





onKeyPress( keyPress )