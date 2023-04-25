# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that receives three strings and returns a modified string of the same length

import random
from static_array import *


def transform_string(source: str, s1: str, s2: str) -> str:
    result = ""
    for char in source:  # loops through the characters in the string
        if char in s1:
            result += s2[s1.index(char)]  # places a character from the source in s1, to the index in s2
        elif char.isupper():
            result += " "  # replaces uppercase characters letters with a space
        elif char.islower():
            result += "#"  # replaces lowercase letters with a "#"
        elif char.isdigit():
            result += "!"  # replaces numbers with a "!"
        else:
            result += "="  # replaces anything else with "="
    return result
