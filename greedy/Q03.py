import sys
import math
binaries = sys.stdin.readline().rstrip()

binaries = list(map(int, list(binaries)))

count = 0
previous = binaries[0]
for n in binaries[1:]:
    if previous != n:
        previous = n
        count += 1

print(math.ceil(count // 2))
