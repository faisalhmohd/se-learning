#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveResult = 0
    negativeResult = 0
    zerosResult = 0
    for number in arr:
        if (number == 0):
            zerosResult = zerosResult + 1
        elif (number > 0):
            positiveResult = positiveResult + 1
        else:
            negativeResult = negativeResult + 1
    print("{0:.6f}".format(positiveResult/len(arr)))
    print("{0:.6f}".format(negativeResult/len(arr)))
    print("{0:.6f}".format(zerosResult/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
