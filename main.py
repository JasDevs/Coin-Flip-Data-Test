import random as r
import time as t

heads, tails = 0,0

times_to_test = int(input("Coins to flip: "))

def coin_toss():
    global heads, tails
    for _ in range(times_to_test): 
        value=bool(r.getrandbits(1))
        if value == True: 
            heads += 1
        else: 
            tails += 1

def display_data():
    print(f"""
        |================|
        Heads was flipped: {heads} times, {heads*100//(heads+tails)}% of the time
        Tails was flipped: {tails} times, {tails*100//(heads+tails)}% of the time
        |================|
    """)

while True:
     coin_toss()
     display_data()
     heads,tails,value = 0,0,0
     times_to_test = int(input("Coins to flip: "))
     
