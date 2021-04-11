from sys import stdin

input = stdin.readline

readingPreference = {
    "W": 0,
    "O": 5,
    "Y": 10
}
preference = {}
readingInfo = []
genre = []
contents = []

userPreference = list(map(float, input().rstrip().split()))

for i, g in enumerate(['A', 'B', 'C', 'D', 'E']):
    preference[g] = userPreference[i]

n, m = map(int, input().rstrip().split())

for _ in range(n):
    readingInfo.extend(list(input().rstrip()))

for _ in range(n):
    genre.extend(list(input().rstrip()))

for i in range(len(readingInfo)):
    contents.append((readingInfo[i], genre[i], i // m, i % m))

contents.sort(key=lambda x: (-readingPreference[x[0]], -preference[x[1]], x[2], [3]))

for c in contents:
    if not c[0] == 'W':
        print(c[1], preference[c[1]], c[2], c[3])