#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    timePhase = s[-2:]
    hour = int(s[0:2])
    if (timePhase == 'AM'):
        if (hour == 12):
            return '00' + s[2:-2]
        else: 
            return s[:-2]
    elif (timePhase == 'PM'):
        if (hour == 12):
            return '12' + s[2:-2]
        else:
            twentyFourHour = hour + 12
            return str(twentyFourHour) + s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
