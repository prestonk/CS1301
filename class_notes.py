myList = [ -5, 1, 22, 5, 3 ]

def findAvg(aList):
    a = 0
    count = 0
    for x in aList:
        a = x + a
        count = count + 1
    a = a / count
    return a

ans = findAvg(myList)

print(ans)