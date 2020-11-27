import sys

s = int(sys.stdin.readline())

def isometricSum(num):
    result = (num*(num+1))/2

    return int(result)


for i in range(1, s+1):
    if isometricSum(i) > s:
        answer = i - 1
        break
    elif isometricSum(i) is s:
        answer = i
        break

print(answer)
