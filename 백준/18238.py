import sys

str = sys.stdin.readline().strip()

answer = 0
point = ord('A')

for c in str:
    distance = abs(point - ord(c))
    answer += min(abs(26 - distance), abs(distance))
    point = ord(c)

print(answer)