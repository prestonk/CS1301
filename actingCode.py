#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment with my partners Haley Howard and Sevana Ohanian, using this semester's course materials

from Myro import *
from Graphics import *
from random import *
init("/dev/tty.Fluke2-0461-Fluke2")

#scene 1 - comes out of the door (aka mouse hole)
def mouseHole():

    forward(1,2)
    turnLeft(0.5,1)
    forward(1,2)
    stop()
#scene 2
def hallway():

    turnLeft(1,.2)
    wait(0.5)
    turnRight(1,.2)
    wait(0.5)
    forward(0.5,3)
#scene 3
def hallwayTwo():

    forward(1, 8)
#scene 4
def seesCat():

    forward(1,5)
    backward(1,3)
    turnBy(-90,"deg")
#scene 6
def playing():

    forward(1,3)
    turnBy(270,"deg")
    backward(1,3)
    turnBy(-90,"deg")
    forward(1,3)



