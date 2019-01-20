#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment with my partners Haley Howard and Sevana Ohanian, using this semester's course materials

from Myro import *
from Graphics import *
from random import *
init("/dev/tty.Fluke2-0461-Fluke2")
setPicSize("small")

def scene1(x):
    scene1 = []
    beep(1,800)
    for t in timer(x):
        y = takePicture()
        scene1.append(y)
        wait(.1)
    beep(1,800)
    savePicture(scene1, "scene1.gif")
def scene2(x):
    scene2 = []
    beep(1,800)
    time = 0
    for t in timer(x):
        y = takePicture()
        scene2.append(y)
        wait(.1)
    beep(1,800)
    savePicture(scene2, "scene2.gif")
def scene3(x):
    scene3 = []
    beep(1,800)
    time = 0
    for t in timer(x):
        forward(1)
        y = takePicture()
        scene3.append(y)
        wait(.5)
        time = time + .5
    stop()
    savePicture(scene3, "scene3.gif")
    beep(1,800)
def scene4(x):
    scene4 = []
    beep(1,800)
    for t in timer(x):
        y = takePicture()
        scene4.append(y)
        wait(.1)
    beep(1,800)
    savePicture(scene4, "scene4.gif")
def scene5(x):
    scene5 = []
    beep(1,800)
    for t in timer(x):
        turnLeft(.5,.05)
        y = takePicture()
        scene5.append(y)
        turnRight(.5,.05)
        y = takePicture()
        scene5.append(y)
        turnLeft(.5,.05)
        y = takePicture()
        scene5.append(y)
        turnRight(.5,.05)
        y = takePicture()
        scene5.append(y)
    beep(1,800)
    savePicture(scene5, "scene5.gif")
def scene6(x):
    scene6 = []
    beep(1,800)
    for t in timer(x):
        y = takePicture()
        scene6.append(y)
        wait(.1)
    beep(1,800)
    savePicture(scene6, "scene6.gif")

def scene7(x):
    scene7 = []
    beep(1,800)
    for t in timer(x):
        y = takePicture()
        scene7.append(y)
        wait(.1)
    beep(1,800)
    savePicture(scene7, "scene7.gif")
#scene1(10)
#scene2(8)
#scene3(10)
#scene4(12)
#scene5(12)
#scene6(15)
