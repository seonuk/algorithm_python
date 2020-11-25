import sys

N, K = map(int, sys.stdin.readline().strip().split())

q = []

for _ in range(N):
    info = tuple(map(int, sys.stdin.readline().strip().split()))

    if info[0] == K:
        target = info[1:]
    else:
        q.append(info[1:])

print(len([x for x in q if x > target]) + 1)