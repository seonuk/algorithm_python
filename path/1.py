import sys
import heapq

INF = 1e9


n, m = map(int, sys.stdin.readline().rstrip().split())

adj = [[] for _ in range(n)]
distance = [INF for _ in range(n)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    adj[s-1].append((1, e-1))

x, k = map(int, sys.stdin.readline().rstrip().split())

q = []
distance[0] = 0
heapq.heappush(q, (distance[0], 0))

while q:
    current_distance, current_node = heapq.heappop(q)

    if current_distance > distance[current_node]:
        continue

    for d, nn in adj[current_node]:
        if distance[nn] > current_distance + d:
            heapq.heappush(q, (current_distance + d, nn))
            distance[nn] = current_distance + d

print(distance[k-1] + distance[x-1])