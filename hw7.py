#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using only this semester's course materials in collaboration with my partner Onyekachi Offor



from Myro import *


init(com12)



def overlay(new_pic):
    pic = takePicture()
    n_pic = makePicture(new_pic)
    n_width = getWidth(n_pic)
    n_height = getHeight(n_pic)
    width = getWidth(pic)
    height = getHeight(pic)
    if n_width > width and n_height > height:
        for x in range(0,width):
            for y in range(0,height):
                n_pix = getPixel(n_pic, x, y)
                pix = getPixel(pic, x, y)
                r, g, b = getRGB(n_pix)
                setRGB(pix, (r,g,b))
    elif width > n_width and height > n_height:
        for x in range(0,n_width):
            for y in range(0,n_height):
                n_pix = getPixel(n_pic, x, y)
                pix = getPixel(pic, x, y)
                r, g, b = getRGB(n_pix)
                setRGB(pix, (r,g,b))
    else:
        print("One picture must be smaller than the other for the overlay function to work properly")
    show(pic)


def multipleExposure():
    frame1 = takePicture()
    turnRight(1,1)
    frame2 = takePicture()
    turnRight(1,1)
    frame3 = takePicture()
    frame1 = makePicture(frame1)
    frame2 = makePicture(frame2)
    frame3 = makePicture(frame3)
    width = getWidth(frame1)
    height = getHeight(frame1)
    for x in range(0,width):
        for y in range(0,height):
            pix1 = getPixel(frame1, x, y)
            pix2 = getPixel(frame2, x, y)
            pix3 = getPixel(frame3, x, y)
            r1,g1,b1 = getRGB(pix1)
            r2,g2,b2 = getRGB(pix2)
            r3,g3,b3 = getRGB(pix3)
            r_avg = (r1 + r2 + r3)/3
            g_avg = (g1 + g2 + g3)/3
            b_avg = (b1 + b2 + b3)/3
            setRGB(pix1, (r_avg, g_avg, b_avg))
    show(frame1)




def seeingRed(picture):
    pic = makePicture(picture)
    for pixel in getPixels(pic):
        red = getRed(pixel)
        green = getGreen(pixel)
        blue = getBlue(pixel)
        setGreen(pixel, green*0.5)
        setBlue(pixel, blue*0.5)
        setRed(pixel, red*2)
    show(pic)


def greenscreen(background,sprite):
    sprite =makePicture(sprite)
    background =makePicture(background)
    width = getWidth(sprite)
    height = getHeight(sprite)
    for x in range(0, width):
        for y in range(0, height):
            pixel = getPixel(sprite, x, y)
            red = getRed(pixel)
            green = getGreen(pixel)
            blue = getBlue(pixel)
            if green > 150 and red<100 and blue< 100:
                replace = getPixel(background, x, y)
                setColor(pixel, getColor(replace))     
    show(sprite)

def BlackAndWhite(picture):
    pic = makePicture(picture)
    for pixel in getPixels(pic):
        red = getRed(pixel)
        green = getGreen(pixel)
        blue = getBlue(pixel)
        value = (red+ green+ blue)/3
        setBlue(pixel, value)
        setGreen(pixel, value)
        setRed(pixel, value)    
    show(pic)