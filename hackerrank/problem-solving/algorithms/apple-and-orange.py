#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    locationStartingPoint = s
    locationEndingPoint = t
    appleTreeLocation = a
    orangeTreeLocation = b
    appleLocations = []
    orangeLocations = []

    for apple in apples:
        appleLocations.append(appleTreeLocation + apple)
    for orange in oranges:
        orangeLocations.append(orangeTreeLocation + orange)
    
    appleCount = 0
    for location in appleLocations:
        if (location >= locationStartingPoint and location <= locationEndingPoint):
            appleCount = appleCount + 1
    
    orangeCount = 0
    for location in orangeLocations:
        if (location >= locationStartingPoint and location <= locationEndingPoint):
            orangeCount = orangeCount + 1
    
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
