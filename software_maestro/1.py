import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    skills = input().rstrip().split()
    n = int(input().rstrip())

    adj = defaultdict(list)
    indegree = {}

    for s in skills:
        indegree[s] = 0

    for _ in range(n):
        a, b = input().rstrip().split()

        adj[a].append(b)
        indegree[b] += 1

    st = [k for k in indegree.keys() if indegree[k] == 0]
    print(adj)
    while st:
        root = st.pop()

        print(dfs(adj, root))

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visit:
            visit.append(node)

            stack.extend(graph[node])
            if not graph[node]:
                return visit
    return visit

if __name__ == "__main__":
    main()