#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    results = []
    for i in range(len(arr)):
        results.append(sum(num for j, num in enumerate(arr) if not i == j))
    print(min(results), max(results))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
