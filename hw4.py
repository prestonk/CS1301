#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using this semester's course materials and http://www.phy.mtu.edu/~suits/notefreqs.html


from Myro import *

init("com12")


def trickOne():
    #fetch
    forward(1,6)
    backward(1,6)
def trickTwo():
    #chasing tail
    turnLeft(1,4)
    turnRight(.5,1)
    turnLeft(1,4.25)
def trickThree():
    #wagging tail
    for x in timer(5):
        turnLeft(1,.1)
        turnRight(1,.1)
def trickFour():
    #belly crawl
    turnRight(.25,3)
    forward(.25,2)
    turnLeft(.25,1)
    forward(.25,2)
    turnLeft(.25,1)
    forward(.25,2)
    turnLeft(.25,1)
    forward(.25,1)
def happyBday():
    #happy birthday
    beep(.5,523.25)
    beep(.5,523.25)
    beep(1,587.33)
    beep(1,523.25)
    beep(1,698.46)
    beep(1.5,659.25)

    beep(.5,523.25)
    beep(.5,523.25)
    beep(1,587.33)
    beep(1,523.25)
    beep(1,783.99)
    beep(1.5,698.46)
def happySong():
    beep(1,523.25)
    beep(1,783.99)
    beep(1,1046.50)
    beep(1,1046.50)
    beep(1,1174.66)
def okSong():
    beep(1,698.46)
    beep(1,880.00)
    beep(1,783.99)
    beep(1,987.77)
def sadSong():
    beep(1,659.25)
    beep(1,659.25)
    beep(1,587.33)
    beep(1,523.25)



def morningRoutine(x):
    if x == 1:
        trickOne()
    if x == 2:
        trickOne()
        trickTwo()
    if x == 3:
        trickOne()
        trickTwo()
        trickThree()
    if x == 4:
        trickOne()
        trickTwo()
        trickThree()
        trickFour()
    if x >= 5:
        trickOne()
        trickTwo()
        trickThree()
        trickFour()
        happyBday()

def greetMenu():
    x = input("Please give one of the following\n\n1. Small Treat\n2. Medium Treat\n3. Large Treat\n0. Exit")
    x = int(x)
    if x == 1:
        trickOne()
        trickThree()
        sadSong()
        greetMenu()
    if x == 2:
        trickOne()
        trickTwo()
        trickThree()
        okSong()
        greetMenu()
    if x == 3:
        trickOne()
        trickTwo()
        trickThree()
        trickFour()
        happySong()
        greetMenu()
    if x > 3 or x < 0:
        x = input("Entry not accepted\n\nPlease give one of the following\n\n1. Small Treat\n2. Medium Treat\n3. Large Treat\n0. Exit")
        x = int(x)
        if x == 1:
            trickOne()
            trickThree()
            sadSong()
            greetMenu()
        if x == 2:
            trickOne()
            trickTwo()
            trickThree()
            okSong()
            greetMenu()
        if x == 3:
            trickOne()
            trickTwo()
            trickThree()
            trickFour()
            happySong()
            greetMenu()
        if x > 3 or x < 0:
            greetMenu()










