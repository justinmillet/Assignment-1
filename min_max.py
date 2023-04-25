# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that when given an array, it returns the minimum and maximum values


import random
from static_array import *


def Min_Max(arr):
    # Assign the first value of array to min and max variable
    min = arr[0]
    max = arr[0]
    # traverse the array
    for i in arr:
        # if the current element is less than min than change min value to current value
        if (min > i):
            min = i
        # if the current element is greater than max than change max value to current value
        if max < i:
            max = i
    # return the min and max value
    return (min, max)
