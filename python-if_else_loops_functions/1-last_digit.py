#!/usr/bin/python3
import random
def last_digit(num):
    last_digit_unsigned = abs(num) % 10
	return -last_digit_unsigned if (num < 0) else last_digit_unsigned

if number > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
else:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0")
