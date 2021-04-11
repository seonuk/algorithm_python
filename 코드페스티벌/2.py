from sys import stdin

input = stdin.readline

n = int(input().rstrip())
locations = list(map(int, list(input().rstrip())))
distance = [1] + [0 for _ in range(n - 1)]

for i, v in enumerate(distance):
    if i + 1 >= n:
        continue

    if locations[i + 1]:    # 도착 가능
        distance[i + 1] += v

    if i + 2 >= n:
        continue

    if locations[i + 2]:
        distance[i + 2] += v

print(distance[-1])from sys import stdin

input = stdin.readline

n = int(input().rstrip())
locations = list(map(int, list(input().rstrip())))
distance = [1] + [0 for _ in range(n - 1)]

for i, v in enumerate(distance):
    if i + 1 >= n:
        continue

    if locations[i + 1]:    # 도착 가능
        distance[i + 1] += v

    if i + 2 >= n:
        continue

    if locations[i + 2]:
        distance[i + 2] += v

print(distance[-1])