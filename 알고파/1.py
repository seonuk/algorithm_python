import sys

answer = 0
current = 0
for _ in range(10):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    current -= n
    current += m

    answer = max(answer, current)

print(answer)