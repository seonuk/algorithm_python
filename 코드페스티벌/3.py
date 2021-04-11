from sys import stdin

input = stdin.readline

n = int(input().rstrip())
space = []
size = [-1]
length = 1

def isSquare(l, board, i, j):
    squareSum = 0

    for a in range(i, i + l):
        squareSum += sum(board[a][j: j + l])
    if squareSum == l * l:
        return True
    return False

for _ in range(n):
    space.append(list(map(int, list(input().rstrip()))))

while size[-1] != 0:
    count = 0
    for i in range(n - (length - 1)):
        for j in range(n - (length - 1)):
            if isSquare(length, space, i, j):
                count += 1

    length += 1
    size.append(count)

print("total:", sum(size[1:-1]))
for i, v in enumerate(size[1:-1]):
    print("size["+str(i+1) + "]:", v)

