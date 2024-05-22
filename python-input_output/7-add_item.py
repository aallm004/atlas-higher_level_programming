#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file =__import__("6-load_from_json_file").load_from_json_file
try:
    i = load_from_json_file("add_items.json")
except:
    i = []
for x in range(1, len(sys.argv)):
    i.append(sys.argv[x-1])
save_to_json_file(i, "add_item.json")
