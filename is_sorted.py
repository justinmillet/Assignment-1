# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that receives a static array and returns an integer that describes if the array is sorted

from static_array import StaticArray


def is_sorted(arr: StaticArray) -> int:
    length = len(arr)  # sets the length equal to the length of the array
    if length == 1:  # determines if the length is only 1 value
        return 1  # returns 1 if the length is only 1 value, such as "1" or "a"
    increasing = arr[0] <= arr[1]
    for i in range(1, length):  # iterates through the array at the first index
        if increasing and arr[i - 1] > arr[i]:  # determines if the values are increasing and the array minus 1 is
            # greater than the length of the original length
            return 0
        elif not increasing and arr[i - 1] < arr[i]:  # determines if the values are decreasing by looking at the
            # length of the array minus 1 and if it is less than the original length
            return 0
        return 1 if increasing else -1
