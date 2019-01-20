#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using only this semester's course materials

import string


def tallEnough(height):
    height = int(height)
    height = height / .39370
    if height > 120 and height < 190:
        return True
    else:
        return False


def whereIsWaldo(x, y):
    xguess = input("Guess Waldo's X cordinate?")
    yguess = input("Guess Waldo's Y cordinate?")
    if x == xguess and y == yguess:
        yes = "You found Waldo"
        no = "Couldn't find Waldo. Better luck next time"
        return yes
    else:
        return no

def allLetters(userString):
    userString = str(userString)
    b = ""
    for a in userString:
        if a in string.ascii_letters:
            b = b + a
    return b

def replaceLetter(aString, aLetter):
    a = input("Input a letter")
    num = 0
    counter = 0
    while num > len(aString):
        if a != aString[num]:
            num = num + 1
        else:
            counter = counter + 1
            num = num + 1
    if counter != len(aString):
        aString = aString.replace(a,aLetter)
        print(aString)
    else:
        print("Letter is not in string")
        replaceLetter(aString,aLetter)



def countUp(start,end,increment):
    while start <= end:
        print(start)
        start = start + increment
    print("Done!")
    return None



def numMountainRange(X):
    X = int(X)
    start = 1
    multi = 2 * X
    while start != X:
        print((str(start)*start).ljust((multi-start)-1),(str(start)*start))
        start = start + 1
    print(str(X)*multi)



def printTimestable():
    first = 1
    last = 10
    multi = first
    new = (last - first)/multi
    a = multi
    b = 0
    c = 0
    row = "\t""Times:"
    while b < new + 1:
        while c < new + 1:
            if(b == 0):
                if c < new:
                    row = row + "\t" + str((first + (c * a)))
            else:
                if(c == 0):
                    row = row + "\t" + str((first + ((b-1) * a)))
                else:
                    row = row + "\t" + str((first + ((c-1) * a)) * (first + ((b-1) * a)))
            c = c + 1
        print(row)
        row = ""
        b = b + 1
        c = 0




def printTimes(last):
    last = last + 1
    first = 1
    multi = first
    new = (last - first)/multi
    a = multi
    b = 0
    c = 0
    row = "\t""Times:"
    while b < new + 1:
        while c < new + 1:
            if(b == 0):
                if c < new:
                    row = row + "\t" + str((first + (c * a)))
            else:
                if(c == 0):
                    row = row + "\t" + str((first + ((b-1) * a)))
                else:
                    row = row + "\t" + str((first + ((c-1) * a)) * (first + ((b-1) * a)))
            c = c + 1
        print(row)
        row = ""
        b = b + 1
        c = 0










