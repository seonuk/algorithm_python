import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
length = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(length)

answer = 0
while start <= end:

    h = (start + end) // 2

    total = 0

    for l in length:
        if l > h:
            total += l - h

    if total >= M:
        answer = h
        start = h + 1
    if total < M:
        end = h - 1

print(answer)