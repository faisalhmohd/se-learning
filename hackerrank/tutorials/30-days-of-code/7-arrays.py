if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    print(' '.join([str(n) for n in arr]))