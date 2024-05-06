#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    printed_el = 0

    for element in my_list:
        try:
            print(element, end=' ')
            printed_el += 1
        except: IndexError
        print(f"An error occurred: {element}")
        
        print()
    return printed_el


