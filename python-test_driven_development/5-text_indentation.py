#!/usr/bin/python3
"""
This function prints a text with 22 new lines after .?:

Functions:
    def text_indentation(text):
    
Return:
    Only print
"""


def text_indentation(text):
    """
    Function that prints a text 

    Args:
        text: text used

    Raises:
        TypeError: if text is not a string

    Return:
        Only print
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    inst = text.replace(".", ".\n\n")
    inst = inst.replace(":", ":\n\n")
    inst = inst.replace("?", "?\n\n")
    p = inst.splitlines(True)
    ls_strip = []
    for linea in p:
        if linea == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(linea.lstrip())
    print("".join(ls_strip), end="")
