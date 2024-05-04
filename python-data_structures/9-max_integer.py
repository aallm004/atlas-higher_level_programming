#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return "None"
    res = 0
    for i in my_list:
        if i >= res:
            res = i
    return res


