import sys

n, s = map(int, sys.stdin.readline().rstrip().split())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

i, j = 0, 1
answer = 100000
partialSum = numbers[0]

while i < j and j <= len(numbers):
    if partialSum >= s:
        answer = min(answer, j - i)
        partialSum -= numbers[i]
        i += 1
    else:
        if j == len(numbers):
            break
        partialSum += numbers[j]
        j += 1

print(answer if answer != 100000 else 0)