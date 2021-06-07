#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxScore = scores[0]
    maxScoreChangedTimes = 0
    minScore = scores[0]
    minScoreChangedTimes = 0
    
    for score in scores:
        if (score > maxScore):
            maxScore = score
            maxScoreChangedTimes = maxScoreChangedTimes + 1
        elif (score < minScore):
            minScore = score
            minScoreChangedTimes = minScoreChangedTimes + 1
    
    return [maxScoreChangedTimes, minScoreChangedTimes]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
