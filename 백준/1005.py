from sys import stdin, setrecursionlimit

setrecursionlimit(1000*1000)

input = stdin.readline

t = int(input().rstrip())

def getTotalBuildingTime(node, graph, totalTime, buildingTime):
    if not graph[node]:
        return buildingTime[node]

    if totalTime[node] == -1:
        totalTime[node] = max(map(lambda x: getTotalBuildingTime(x, graph, totalTime, buildingTime), graph[node])) + buildingTime[node]

    return totalTime[node]

for _ in range(t):
    n, k = map(int, input().rstrip().split())

    buildingTime = [0] + list(map(int, input().rstrip().split()))
    totalTime = [-1 for _ in range(n + 1)]

    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        a, b = map(int, input().rstrip().split())

        graph[b].append(a)

    target = int(input().rstrip())

    print(getTotalBuildingTime(target, graph, totalTime, buildingTime))
