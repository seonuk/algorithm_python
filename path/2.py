import sys
import heapq

INF = 1e9

n, m, c = map(int, sys.stdin.readline().rstrip().split())

adj = [[] for _ in range(n)]
distance = [INF for _ in range(n)]


for _ in range(m):
    s, e, d = map(int, sys.stdin.readline().rstrip().split())

    adj[s - 1].append((d, e - 1))

q = []
distance[c - 1] = 0
heapq.heappush(q, (0, c - 1))

while q:
    currentDistance, currentNode = heapq.heappop(q)

    if distance[currentNode] < currentDistance:
        continue

    for d, nn in adj[currentNode]:
        total = d + currentDistance

        if total < distance[nn]:
            distance[nn] = total
            heapq.heappush(q, (total, nn))

count = 0
max_distance = -1
for v in distance:
    if v < INF:
        count += 1
        max_distance = max(max_distance, v)

print(count - 1, max_distance)