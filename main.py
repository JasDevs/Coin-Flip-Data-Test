import random as r
import time as t

heads, tails = 0,0

timesToTest = int(input("Coins to flip: "))

def coinToss():
    global timesToTest
    for _ in range(timesToTest): 
        global heads,tails
        value=r.randint(1,2)
        if (value==1): 
            heads+=1
        else: 
            tails+=1

def displayData():
    print("")
    print(("|================|"))
    print("Heads was flipped: ", "{:,}".format(heads),"time(s),",int(heads/timesToTest*100),"% of the time")
    print("Tails was flipped: ", "{:,}".format(tails),"time(s),",int(tails/timesToTest*100),"% of the time")
    print("|================|")
    print("")

while True:
     coinToss()
     displayData()
     heads,tails,value = 0,0,0
     timesToTest = int(input("Coins to flip: "))
     