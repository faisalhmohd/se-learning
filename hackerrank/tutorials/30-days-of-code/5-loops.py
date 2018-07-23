#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    for i in range(10):
        print(str(n) + ' x ' + str(i+1) + ' = ' + str(n*(i+1)))