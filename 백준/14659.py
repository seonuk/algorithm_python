import sys

N = int(sys.stdin.readline().rstrip())

heights = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0

while heights:

    index = heights.index(max(heights))

    answer = max(answer, len(heights) - 1 - index)

    heights = heights[:index]

print(answer)