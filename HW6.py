#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using only this semester's course materials in collaboration with my partner Onyekachi Offor

from Myro import *
init("com12")
def turn():
    state = heads()
    if state == True:
        setLED("left","on")
        wait(0.5)
        setLED("left", "off")
        turnLeft(1,2)
    elif state == False:
        setLED("right","on")
        wait(0.5)
        setLED("right", "off")
        turnRight(1,2)

def findColor(pic):
    red_count = 0
    green_count = 0
    blue_count = 0
    counter = 0
    for pixel in getPixels(pic):
        rgb = getRGB(pixel)
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        red_count = red_count + red
        green_count = green_count + green
        blue_count = blue_count + blue
        counter = counter + 1
    red_avg = red_count / counter
    blue_avg = blue_count / counter
    green_avg = green_count / counter
    if red_avg > blue_avg and green_avg > blue_avg:
        return "yellow"
    elif green_avg > red_avg and green_avg > blue_avg:
        return "green"
    elif red_avg > green_avg and red_avg > blue_avg:
        return "red"
    elif green_avg > 100 and blue_avg > 100 and red_avg > 100:
        return "white"
                
def stopLight():
    x = True
    while x:
        p = takePicture()
        show(p)
        light = findColor(p)
        if light == "green":
            forward(1,2)
            stopLight()
        elif light == "yellow":
            forward(0.5,2)
            stopLight()
        elif light == "red":
            x = False
            stop()
            beep(1,800)
        elif light == "white":
            turn()
            stopLight()