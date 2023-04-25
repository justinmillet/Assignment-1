# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that removes duplicates from an array

from static_array import StaticArray


def remove_duplicates(arr: StaticArray) -> StaticArray:
    new_arr = StaticArray(size=arr.size())  # creates a new StaticArray
    total_value = 1  # sets the value to 1 and keeps track of unique values
    new_arr[0] = arr[0]
    for i in range(1, new_arr.size()):  # iterates through the array
        if not arr[i] == arr[i - 1]:  # starts at second element
            total_value += 1  # adds 1 value for a unique element in the array
            new_arr[i] = arr[i]
        end_arr = StaticArray(total_value)  # creates the end array
        end_index = 0  # indexes it at value 0
    for i in range(new_arr.size()):  # iterates through the array to find unique values
        if new_arr[i] is not None:  # determines the array is not none
            end_arr[end_index] = new_arr[i]
            end_index += 1  # adds 1 to the array
    return end_arr
