import sys
import heapq

n = int(sys.stdin.readline().rstrip())

hq = []
for _ in range(n):
    number = int(sys.stdin.readline().rstrip())

    if hq and number == 0:
        print(heapq.heappop(hq)[1])
    elif not hq and number == 0:
        print(0)
    else:
        heapq.heappush(hq, (-number, number))

