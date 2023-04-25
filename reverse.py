# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that when given an array, it returns the minimum and maximum values

from static_array import StaticArray


def reverse(arr: StaticArray) -> None:
    front = 0  # sets the first number equivalent to 0
    end = arr._size - 1  # sets the last number to the array size minus 1
    while front < end:
        num = arr.get(front)  # gets the first number
        arr.set(front, arr.get(end))  # sets the first number at the end
        arr.set(end, num)
        end -= 1  # takes one from the end
        front += 1  # adds one to the front
    return
