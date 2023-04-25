# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that when given an array, it returns the minimum and maximum values

from static_array import StaticArray


def min_max(arr: StaticArray) -> tuple:
    min_value = arr[0]  # sets first value as minimum value
    max_value = arr[0]  # sets first value as maximum value
    for i in range(StaticArray.length(arr)):  # iterates through the array
        if min_value > arr[i]:
            min_value = arr[i]  # determines if the number is minimum by reviewing against first number
        if max_value < arr[i]:
            max_value = arr[i]  # determines if the number is maximum by reviewing against first number
    return min_value, max_value  # returns the minimum and maximum
