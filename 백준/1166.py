from sys import stdin

input = stdin.readline
n, l, w, h = map(int, input().rstrip().split())

start = 0
mid = min(l, w, h) / 2
end = min(l, w, h)

for _ in range(1000 ** 3):
    num = (l / mid) * (w / mid) * (h / mid)

    if num == n:
        print(mid)
        break

    if num > n:
        start = mid
    else:
        end = mid

    mid = (start + end) / 2
else:
    print(mid)