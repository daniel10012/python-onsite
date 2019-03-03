'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''

import random

random_num = random.randint(1,10)

r = int(input("choose a random num"))

while r != random_num:
    r = int(input("choose a random num"))

print(f"you found it !!! it was {r}")