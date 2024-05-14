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
    new = ""
    for i in text:
        if i == " " and len(new_text) == 0:
            continue
        elif i == " " and new_text[-1] in "\n":
            continue
        new_text += i
        if i in ".?:!":
            new_text += "\n\n"

    print(new_text, end="")
