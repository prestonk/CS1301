#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using this semester's course materials

from Myro import *

init("com12")

def getValues(numSamples):
    numSamples = int(numSamples)
    if numSamples == 1:
        a = getLight("center")
        return a
    else:
        a = []
        for x in xrange(numSamples):
            a.append(getLight("center"))
            turnLeft(1, .25)
    return a

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def printStatistics(a):
    avg = sum(a)/len(a)
    maxi = max(a)
    mini = min(a)
    count = 0
    for x in a:
        if even(x):
            count = count + 1
    print("The average of this list is ",avg," the max is ",maxi," the min is ",mini," and the number of even numbers is ", count)
