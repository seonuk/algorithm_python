from sys import stdin, setrecursionlimit

input = stdin.readline
def dfs(adj, visited, node):
    if visited[node]:
        return 0

    visited[node] = True
    for v in adj[node]:
        if not visited[v]:
            dfs(adj, visited, v)

    return 1

if __name__ == "__main__":
    setrecursionlimit(1000 * 1000)
    n, m = map(int, input().rstrip().split())

    adj = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    answer = 0

    for _ in range(m):
        i, j = map(int, input().rstrip().split())
        adj[i].append(j)
        adj[j].append(i)

    for startNode in range(1, n + 1):
        answer += dfs(adj, visited, startNode)

    print(answer)
