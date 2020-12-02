import sys

N = int(sys.stdin.readline().rstrip())
points = []
answer = 0

for _ in range(N):
    points.append(int(sys.stdin.readline().rstrip()))

points.reverse()

previous = points[0]

for i, current in enumerate(points):
    if i == 0:
        continue

    if previous <= current:
        answer += current - (previous - 1)
        previous = previous - 1
    else:
        previous = current

print(answer)