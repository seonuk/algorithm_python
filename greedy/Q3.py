import sys

n, k = map(int, sys.stdin.readline().strip().split())

count = 0

while n != 1:
    if n % k == 0:
        n = n/k
    else:
        n = n - 1

    count = count + 1
print(count)