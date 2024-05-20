#!/usr/bin/python3
def read_file(isfile):
    with open(isfile) as f:
        for line in f:
            print(line, end="")
