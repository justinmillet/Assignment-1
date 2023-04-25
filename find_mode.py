# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that when given an array, it returns the minimum and maximum values

from static_array import StaticArray


def find_mode(arr: StaticArray) -> tuple:
    length = len(arr)  # determines the length of the array
    if length == 1:  # if the length of the array is 1, it will return 1
        return arr[0], 1
    mode = arr[0]
    frequency = 1
    count = 1
    for i in range(1, length):  # iterates over the array
        if arr[i] == arr[i - 1]:  # compares each value
            count += 1  # increases the count by 1 if the current value is equal to the previous value
        else:
            if count > frequency:  # determines if the count is greater than the frequency
                frequency = count  # sets the frequency equal to the count
                mode = arr[i - 1]  # sets mode equal to the array length minus 1
            count = 1  # sets the count equal to 1
    if count > frequency:
        frequency = count
        mode = arr[length - 1]  # returns the tuple of the values

    return mode, frequency
