import sys
import heapq

s = list(map(str, sys.stdin.readline().rstrip()))

heapq.heapify(s)

result = 0
resultStr = ''
for i in s:

    if not i.isalpha():
        result += int(i)
    else:
        resultStr += i

print(resultStr + str(result))

