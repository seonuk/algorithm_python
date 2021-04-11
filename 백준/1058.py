from sys import stdin

input = stdin.readline

n = int(input().rstrip())

friends = []

for _ in range(n):
    friends.append(list(input().rstrip()))


def dfs(adj, visited, node, count):
    if count >= 3:
        return 0
    answer =  0
    for i, v in enumerate(adj[node]):
        if not v:
            continue
        if not visited[i]:
            visited[i] = True
            dfs(adj, visited, node, count + 1)
print(n, friends)