#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_function = lambda x: replace if x == search else x

    new_list = list(map(replace_function, my_list))

    return new_list
