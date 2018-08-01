#!/bin/python3

import sys

def bubble_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swaps += 1
        if swaps == 0:
            return 0, arr
    return swaps, arr

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

no_swaps, array = bubble_sort(a)
print('Array is sorted in', no_swaps, 'swaps.')
print('First Element:', array[0])
print('Last Element:', array[len(array) - 1])