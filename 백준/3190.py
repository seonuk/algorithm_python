import sys

APPLE = -1


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

dn = [0, 1, 0, -1] #r, d, l, u
dm = [1, 0, -1, 0]

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

board = [[-2 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(lambda num: int(num) - 1, sys.stdin.readline().rstrip().split())
    board[x][y] = APPLE

l = int(sys.stdin.readline().rstrip())
lArr = []

for _ in range(l):
    x, c = map(lambda a: str(a) if a.isalpha() else int(a), sys.stdin.readline().rstrip().split())
    lArr.append((x, c))
lArr.sort(reverse=True)

time = 0
length = 1
direction = RIGHT
head = (0, 0)
board[0][0] = 0

while True:

    length += 1
    time += 1

    nn = head[0] + dn[direction]
    nm = head[1] + dm[direction]

    if nn < 0 or nn >= n or nm < 0 or nm >= n:
        break

    if board[nn][nm] > time - length:
        break

    if board[nn][nm] != APPLE:
        length -= 1

    head = (nn, nm)
    board[nn][nm] = time


    if lArr and lArr[-1][0] == time:
        t, d = lArr.pop()
        if d == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4



print(time)
