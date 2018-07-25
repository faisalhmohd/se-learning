#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    bin = str(format(n, 'b'))
    ones = bin.split('0')
    result = 0
    for num in ones:
        if len(num) > result:
            result = len(num)
    print(result)
