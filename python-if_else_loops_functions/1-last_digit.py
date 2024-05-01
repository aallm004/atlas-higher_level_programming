#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

    print(f"Last digit of {number} is {last_digit(number)}" end=' ')

if last_digit(number) > 5:
    print("and is greater than 5")
elif last_digit(number) == 0:
    print(f"and is 0")
else last_digit(number) < 6:
    print(f"and is less than 6 and not 0")
