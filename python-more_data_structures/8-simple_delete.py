#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    i = False
    for k in a_dictionary:
        if k == key:
            i = True
        else:
            del a_dictionary[key]
            return(a_dictionary)
