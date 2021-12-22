#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n =  int(repr(number)[-1])
if number < 6:
    if number != 0:
        print("Last digit of", number, "is", n, "and is less than 6 and not 0")
elif number > 5:
    print("Last digit of", number, "is", n, "and is greather than 5")
elif number[-1] == 0:
    print("Last digit of", number, "is", n, "and is 0")
