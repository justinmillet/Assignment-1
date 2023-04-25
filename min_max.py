# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that when given an array, it returns the minimum and maximum values

from static_array import StaticArray


def min_max(arr: StaticArray) -> ():
    if StaticArray.length(arr) == 0:
        return None, None
    min_value = arr[0]
    max_value = arr[0]
    for i in range (StaticArray.length(arr)):
        if min_value > arr[i]:
            min_value = arr[i]
        if max_value < arr[i]:
            max_value = arr[i]
    return min_value, max_value
