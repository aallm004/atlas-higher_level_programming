#!/usr/bin/python3
def read_file(isfile):
    "reads text file and prints to stdout"
    with open(isfile) as f:
        for line in f:
            print(line, end="")
