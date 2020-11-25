import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []
dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]

for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))


q = deque([(0, 0)])
board[0][0] = 0

while q:

    (i, j) = q.popleft()

    for k in range(4):
        nn = i + dn[k]
        nm = j + dm[k]

        if 0 <= nn < N and 0 <= nm < M and board[nn][nm] is 1:
            board[nn][nm] = board[i][j] + 1

            q.append((nn, nm))

print(board[N-1][M-1] + 1)