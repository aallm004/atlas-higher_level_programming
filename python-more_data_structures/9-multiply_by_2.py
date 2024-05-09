#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult_dict = {}
    for a, b in a_dictionary.items():
        mult_dict[a] = b * 2
    return mult_dict

