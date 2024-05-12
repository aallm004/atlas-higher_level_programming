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
    Function that prints a text with 22 new lines after .?:

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
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            new += "\n\n"
        else:
            new += text[i]
    print(new, end="")
