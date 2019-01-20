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

def takePictures():
    print("First picture is about to be taken")
    wait(1)
    pic1 = takePicture()
    beep(0.1, 1200)
    beep(0.1, 1200)
    print("Second picture is about to be taken")
    wait(2)
    pic2 = takePicture()
    beep(0.1, 1200)
    beep(0.1, 1200)
    return pic1, pic2

def sepia():
    pic = takePicture()
    for pix in getPixels(pix):
        setBlue(pix, 40)
    savePicture(pic, "sepia.gif")


def tempoChange():
    aList = []

    for x in range(30):
        p = takePicture()
        pic = takePicture()
        aList.append(p)
        wait(.1)
        
    savePicture(aList, "tempoChange.gif")


def Fade():
    x = 0
    Pics = []
    for t in range(0,10):
        pic = takePicture()
        turnLeft(0.5, 0.2)
        Pics = Pics + [pic]
        x = x+1
    newGIF = []
    for x in range(0,len(Pics)):
        p = Pics[x]
        for pixel in getPixels(p):
            r = getRed(pixel)
            g = getGreen(pixel)
            b = getBlue(pixel)
            setRed(pixel, r-((255/len(Pics))*x))
            setGreen(pixel,g-((255/len(Pics))*x))
            setBlue(pixel,b-((255/len(Pics))*x))
        newGIF = newGIF + [p]
    savePicture(newGIF, 'fade.gif')


def crossFade():
    pic1, pic2 = takePictures()
    picList = []
    picList.append(pic2)
    for i in range(1, 6):
        pic3 = copyPicture(pic1)
        num = i / 5
        num2 = 1 - num
        print(num, "complete")
        for x in range(getWidth(pic1)):
            for y in range(getHeight(pic1)):
                pix1 = getPixel(pic1, x, y)
                pix2 = getPixel(pic2, x, y)
                r, g, b = getRGB(pix1)
                r2, g2, b2 = getRGB(pix2)
                pix3 = getPixel(pic3, x, y)
                r3, g3, b3 = ((r * num + r2 * num2),(g * num + g2 * num2),(b * num + b2 * num2))
                setRGB(pix3, r3, g3, b3)
        picList.append(pic3)
    picList.append(pic1)

    savePicture(picList, "crossfade.gif")

