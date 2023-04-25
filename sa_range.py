# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that receives two integers and returns a StaticArray

from static_array import StaticArray


def sa_range(start: int, end: int) -> StaticArray:
    sa = StaticArray(abs(end - start) + 1)  # creates the sa object and determines the length as (end-start) plus 1
    increasing = end > start
    index = 0
    value = start
    while value != end:  # loops from start to end
        sa.set(index, value)  # sets the index to the value
        index += 1  # adds 1 to the index
        if increasing:
            value += 1  # increases the value by 1 if increasing
        else:
            value -= 1  # decreases the value by 1 if decreasing
    sa.set(index, value)
    return sa  # returns the StaticArray
