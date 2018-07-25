#!/bin/python3

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    sum = -9*6
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if tmp > sum:
                sum = tmp
    print(sum)