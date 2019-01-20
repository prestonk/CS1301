#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on this project with my partner Elizabeth Hill

import math

def quesoForFishy(balance):
    balance = float(balance)
    jars = balance / 2.98
    jars = int(jars)
    return jars

def mailboxes(n):
    n = int(n)
    timea = n*2 
    timeb = n*6
    print("Because you have run into",n,"mailbox(es), your car's life has been shortened by anywhere from",timea,"to", timeb,"months.")

def concertTicket():
    cost = float(input("How much money will the ticket(s) be?"))
    rate = float(input("What is your hourly rate in dollars?"))
    hours = cost/rate
    print("You will need to work","{0:.2f}".format(hours),"hours to afford your ticket(s)")
        
def boringInterlude(r):
    r = float(r)
    volume = (4/3)*(math.pi)*(r**3)
    return volume


def trafficJam(lanes, miles):
    miles = miles * lanes
    miles = miles * 5280
    cars = miles / 15
    return cars

def timeLeft(time):
    hours = input("How many hours does the battery last?")
    hours = int(hours)
    hours = hours*60
    percentage = int(hours/time)
    battery = hours - time
    print(percentage)
    return battery

def daffodils(flowers, neighbor, price):
    a = flowers / 12
    b = math.ceil(a)
    c = b * price
    leftover = c - neighbor
    leftover = round(leftover, 2)
    print("Your contribution is $",leftover)