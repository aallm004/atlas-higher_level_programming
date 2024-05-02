#!/usr/bin/python3
def print_last_digit(number):
    if number == "abcdefghijklmnopqrstuvwxyz":
        print("Error")
    else:
        print(number[-1], end="")
        return(number[-1])