import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

cache = [0 for _ in range(len(arr) + 1)]

def getMaxSize(arr):
    lenght = len(arr)

    if lenght == 2:
        return max(arr[0], arr[1])
    if lenght == 1:
        return arr[0]
    if cache[lenght] != 0:
        return cache[lenght]

    cache[lenght] = max(getMaxSize(arr[1:]), getMaxSize(arr[2:]) + arr[0])
    return cache[lenght]

print(getMaxSize(arr[:]))