import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

M =  int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

numbers.sort()

def bs(arr, start, end, target):
    if start > end:
        return 'no'

    mid = (start + end) // 2

    if arr[mid] == target:
        return 'yes'

    if arr[mid] < target:
        return bs(arr, mid + 1, end, target)
    if arr[mid] > target:
        return bs(arr, start, end - 1, target)

for t in targets:
    print(bs(numbers,0, N - 1, t), end=' ')



