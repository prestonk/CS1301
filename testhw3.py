from Myro import*

def tallEnough(height):
    height = float(height)
    height = height / 0.39370
    if hieght <= 190 and height >= 120:
        return true
    else:
        return false

def whereIsWaldo(X,Y):
    GX = input("Guess Waldo's x-coordinate")
    GY = input("Guess Waldo's y-coordinate")
    if GX == X and GY == Y:
        return "You found Waldo"
    else:
        return "Couldn't find Waldo. Better luck next time"

def allLetters(aStr):
    index = 0
    while index > len(aStr):
        if aStr[index] != string.ascii_letters:
            aStr = aStr.replace(aStr[index],"")
            index = index + 1
        else:
            index = index + 1
    return aStr

def replaceLetter(aStr,aLet):
    X = input("")
    index = 0
    count = 0
    while index > len(aStr):
        if X != aStr[index]:
            index = index + 1
        else:
            count = count + 1
            index = index + 1
    if count != 0:
        aStr = aStr.replace(X,aLet)
        print(aStr)
    else:
        print("Letter is not in string")
        replaceLetter()

def countUp(S,E,I):
    while S != E:
        print(S)
        S = S + I
    print("Done")

def numMountainRange(x):
    y=1
    z=2*x
    while y!=x:
        print((str(y)*y).ljust((z-y)-1),(str(y)*y))
        y=y+1
    print(str(x)*z)

def printTimestable():
    index = 0
    while index != 9:
        if index == 0:
            print ("times:")


def printTimes(start,end,increment):
    diff = (end - start)/increment
    y = end
    z = increment
    i = 0
    j = 0
    line = "\t""Times:"
    while i < diff + 1:
        while j < diff + 1:
            if(i == 0):
                if j < diff:
                    line = line + "\t" + str((start + (j * z)))
            else:
                if(j == 0):
                    line = line + "\t" + str((start + ((i-1) * z)))
                else:
                    line = line + "\t" + str((start + ((j-1) * z)) * (start + ((i-1) * z)))
            j = j + 1
        print(line)
        line = ""
        i = i + 1
        j = 0