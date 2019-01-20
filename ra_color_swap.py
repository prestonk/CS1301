#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using only this semester's course materials


from Myro import *


a = makePicture("RA_colorswap_source.jpg")

def changeColor(img):
    for pix in getPixels(img):
        red = getRed(pix)
        green = getGreen(pix)
        blue = getBlue(pix)
        if red > green and red > blue:
            setGreen(pix, 255)
            setRed(pix, 0)
            setBlue(pix, 0)
        if green > blue and green > red:
            setBlue(pix, 255)
            setGreen(pix, 0)
            setRed(pix, 0)
        if blue > red and blue > green:
            setRed(pix, 255)
            setGreen(pix, 0)
            setBlue(pix, 0)
    savePicture(img, "new_picture.jpg")