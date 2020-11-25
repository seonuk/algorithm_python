import sys
from collections import deque

board = []
count = 0

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        print(i,j)
        if board[i][j] is '0':
            print('he')
            count = count + 1

            queue = deque([(i, j)])

            while queue:
                i_index, j_index = queue.popleft()

                for k in range(4):
                    nn = dn[k] + i_index
                    nm = dm[k] + j_index

                    if 0 <= nn < N and 0 <= nm < M and board[nn][nm] is '0':
                        board[nn][nm] = 1

                        queue.append((nn,nm))

print(count)
