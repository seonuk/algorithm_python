import sys
import math

times = int(sys.stdin.readline().rstrip())

for _ in range(times):
    result = 0

    x, y = map(int, sys.stdin.readline().rstrip().split())
    remain = 0
    distance = y - x

    if distance <= 3:
        print(distance)
        continue

    if distance % 2 != 0:
        remain = 1

    distance = distance // 2
    n = 0

    while (n * (n + 1)) // 2 <= distance:
        n += 1
    else:
        n -= 1

    remain += distance - ((n * (n + 1)) // 2)
    result = 2 * n

    result += math.ceil(remain / n)

    print(result)



# 절반으로 나눈다
    # 소수점이 나올 경우 아래로 결과 + 1
    # 안나올 경우 결과 + 0

# n * (n + 1) / 2 <= 등차수열 합, 절반의 수보다 크지 않은 수를 찾는다
    # 결과는 n이 딱 떨어질 경우  (n + 0) * 2
    # 아닐 경우(n + 1) * 2