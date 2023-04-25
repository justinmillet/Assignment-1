# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that receives a static array and corts them in non-ascending order

from static_array import StaticArray


def count_sort(arr: StaticArray) -> StaticArray:
    max = -int(10 ** 100)  # sets the max value in the StaticArray
    min = int(10 ** 100)  # sets the min value in the StaticArray
    for i in range(arr.size()):  # iterates through to determine size, max and min
        if max < arr.get[i]:
            max = arr.get[i]
        if min > arr.get[i]:
            min = arr.get[i]
    max = max - min  # accommodates for negative values
    max += 1
    count = StaticArray(max)  # sets the array count
    for i in range(arr.size()):  # iterate through the array and stores the size
        value = count.get(arr.get[i] - 1)
        count.set(arr.get(i) - min, value + 1)
    for i in range(1, max):  # finds the sum of the count
        count.set(i, count.get(i) + count.get(i - 1))
    final = StaticArray(arr.size())  # starts the final array in non-ascending order
    i = arr.size() - 1
    while i >= 0:
        index = count.get(arr.get(i) - min) - 1
        final.set(arr.size() - index - 1, arr.get(i))
        count.set(arr.get(i) - min, count.get(arr.get(i) - min) - 1)
        i -= 1
    return final
