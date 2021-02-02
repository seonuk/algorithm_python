import sys

ONE = 0
TWO = 1

n = int(sys.stdin.readline().rstrip())
stair = []

points = [[0, 0] for _ in range(n)]

for _ in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))


def dp(index, step):

    if index < 0:
        return 0

    if points[index][step] != 0:
        return points[index][step]

    if step == ONE:
        oneStepPoint = dp(index - 1, TWO) + stair[index]
        points[index][ONE] = oneStepPoint

        return points[index][ONE]

    if step == TWO:
        twoStepPoint = max(dp(index - 2, ONE), dp(index - 2, TWO))
        points[index][TWO] = twoStepPoint + stair[index]

        return points[index][TWO]

if __name__ == "__main__":
    print(max(dp(n - 1, ONE), dp(n - 1, TWO)))



# 14
# 100
# 100
# 0
# 100
# 100
# 0
# 100
# 100
# 0
# 100
# 100
# 0
# 100
# 100