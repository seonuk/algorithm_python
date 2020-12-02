import sys
import heapq

N = int(sys.stdin.readline().rstrip())
tips = []
realTips = []
answer = 0

for _ in range(N):
    tip = int(sys.stdin.readline().rstrip())
    tips.append(tip)

    currentTip = tip - len(tips) - 1
    lastIndexTip = currentTip - (N - len(tips) - 2)

    realTips.append(lastIndexTip)


heapq.heapify(realTips)

i = 0
while realTips:
    t = heapq.heappop(realTips)

    if t + i > 0:
        answer += t + i

    i += 1

print(answer)