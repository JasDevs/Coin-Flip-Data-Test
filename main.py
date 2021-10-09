import random as r
import time as t

def coin_toss(times_to_test):
    heads = 0
    tails = 0
    for _ in range(times_to_test): 
        value=bool(r.getrandbits(1))
        if value == True: 
            heads += 1
        else: 
            tails += 1
    return heads, tails

def display_data(heads, tails):
    print(f"""
        |================|
        Heads was flipped: {heads} times, {heads*100//(heads+tails)}% of the time
        Tails was flipped: {tails} times, {tails*100//(heads+tails)}% of the time
        |================|
    """)

while True:
     times_to_test = int(input("Coins to flip: "))

     start = t.process_time()
     heads, tails = coin_toss(times_to_test)
     end = t.process_time()
     seconds = end-start;
     print(f"took: {seconds} seconds.\n");
     display_data(heads, tails)
     
