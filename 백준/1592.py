import sys

n, m, l = map(int, sys.stdin.readline().rstrip().split())

gamers = [0 for _ in range(n)]
count = 0
i = 0

while gamers[i] + 1 < m:
    gamers[i] += 1
    count += 1

    i = (i + l) % n if gamers[i] % 2 != 0 else (i - l) % n

print(count)
