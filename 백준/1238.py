from sys import stdin
import heapq

input = stdin.readline
INF = 1000000000000
n, m, x = map(int, input().rstrip().split())

edges = [[] for _ in range(n + 1)]
distance = [0] + [INF for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().rstrip().split())

    edges[a].append((t, b))


def findMinCost(startNode, dist, dest):

    q = [(0, startNode)]
    dist[startNode] = 0

    while q:
        t, d = heapq.heappop(q)

        if distance[d] < t:
            continue

        for nt, nn in edges[d]:
            if nt + t < dist[nn]:
                dist[nn] = nt + t
                heapq.heappush(q, (nt + t, nn))

    return dist[dest]

if __name__ == "__main__":
    findMinCost(x, distance, 0)
    answer = 0

    for i in range(1, n + 1):
        d = [0] + [INF for _ in range(n)]

        answer = max(answer, findMinCost(i, d, x) + distance[i])


print(answer)
