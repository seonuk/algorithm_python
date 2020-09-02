import sys
import heapq

m, n= map(int, sys.stdin.readline().split())

INF = int(1e9)

board = []

for _ in range(n):
    row = list(map(int, list(sys.stdin.readline().rstrip())))
    board.append(row)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

distance = [[INF for _ in range(m)] for _ in range(n)]

q = [(0, 0, 0)]         # (w, x, y)

heapq.heapify(q)
distance[0][0] = 0

while q:
    current = heapq.heappop(q)

    w, x, y = current[0], current[1], current[2]


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        d = distance[x][y] + board[nx][ny]

        if d < distance[nx][ny]:
            distance[nx][ny] = d
            heapq.heappush(q, (d,nx,ny))
print(distance[n-1][m-1])

