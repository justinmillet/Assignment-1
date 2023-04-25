# Author: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1
# Date: 4/24/2023
# Description: Write a function that receives a static array of integers and returns a new array object.

from static_array import StaticArray


def fizz_buzz(arr: StaticArray) -> StaticArray:
    for i in range(len(arr)):
        num = arr[i]
        if num % 3 == 0 and num % 5 == 0:
            result = "fizzbuzz"
        elif num % 3 == 0:
            result[i] = "fizz"
        elif num % 5 == 0:
            result[i] = "buzz"
    return result
