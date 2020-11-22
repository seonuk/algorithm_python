import sys

n, m = map(int, sys.stdin.readline().strip().split())

answer = 0
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    min_value = min(row)

    answer = max(answer, min_value)

print(answer)