#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"IV": 4, "IX": 9, "XL": 40,
             "XC": 90, "CD": 400, "CM": 900,
             "I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}
    result = 0
    if isinstance(roman_string, str):
        for i in roman:
            while i in roman_string:
                result += roman.get(i)
                roman_string = roman_string.replace(i, "", 1)
    return result
