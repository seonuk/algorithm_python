import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

weights = map(int, sys.stdin.readline().rstrip().split())
arr = [0 for _ in range(11)]
result = 0
for w in weights:
    arr[w] += 1

for i in arr:
    n -= i
    result += i * n

print(result)
