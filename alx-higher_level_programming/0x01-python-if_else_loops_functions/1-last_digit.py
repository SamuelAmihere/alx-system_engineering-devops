#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dig = -1 * (-number % 10)
else:
    last_dig = number % 10

if last_dig != 0 and last_dig < 6:
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")
elif last_dig > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
elif last_dig == 0:
    print(f"Last digit of {number} is {last_dig} and is 0")
