#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, and referred to http://stackoverflow.com/questions/20449427/input-integers-python and http://stackoverflow.com/questions/17470883/how-to-round-to-two-decimal-places-in-python-2-7

def machToFPS():
    machs = int(input("Type speed in machs."))
    conversion = 1116.4370079
    fps = machs * conversion
    print(machs,"machs is",fps,"feet per second")

def sqPyramidVolume():
    l = int(input("Length of base"))
    h = int(input("Height of Pyramid"))
    v = (l*l*h)/3
    print("The pyramid's volume is", v)

def makeChange():
    cents = int(input("Amount of money"))
    dollars = cents // 100
    cents2 = cents % 100
    quarters = cents2 // 25
    cents3 = cents2 % 25
    dimes = cents3 // 10
    cents4 = cents3 % 10
    nickels = cents4 // 5
    pennies = cents4 % 5
    print(cents,"cents makes",dollars,"dollars,",quarters,"quarters,",dimes,"dimes,",nickels,"nickels, and",pennies,"pennies")

#have to look up rounding to one decimal
def PPIIndex():
    weight = int(input("What is your weight in pounds?"))
    height = int(input("What is your height in inches?"))
    ppi = weight / height * 1.125
    ppi2 = round(ppi,1)
    print("Your corrected PPI is",ppi2)
