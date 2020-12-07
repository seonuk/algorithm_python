import sys
import heapq as hq
N, K = map(int, sys.stdin.readline().rstrip().split())

arrayA = list(map(int, sys.stdin.readline().rstrip().split()))
arrayB = list(map(lambda x: -int(x), sys.stdin.readline().rstrip().split()))


hq.heapify(arrayA)
hq.heapify(arrayB)

for _ in range(K):
    elementA = hq.heappop(arrayA)
    elementB = hq.heappop(arrayB)

    elementB = -elementB
    if elementA < elementB:
        hq.heappush(arrayA, elementB)
    else:
        hq.heappush(arrayA, elementA)
        break

print(sum(arrayA))