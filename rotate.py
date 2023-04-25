# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that rotates an array based on the number of position

from static_array import StaticArray


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    length = arr.length  # defines the length of the array
    result = StaticArray(length, arr[0])  # defines the length of the StaticArray
    for i in range(length):  # iterates through the array
        j = (i + steps) % length  # j becomes equal to i plus the steps and index's the length at j
        result[j] = arr[i]
    return result
