#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    
    try:
        print_el = 0
        for element in my_list:
            print(element, end='')
            print_el += 1

    except IndexError:
            print(f"An error occurred: {element}")
    print()
    return print_el
