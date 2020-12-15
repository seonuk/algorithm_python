import sys

x = int(sys.stdin.readline().rstrip())

cache = [0 for _ in range(30001)]

def dp(num):
    if num == 1:
        return 0

    numbers = []
    if num % 5 == 0:
        if cache[num // 5] == 0:
            cache[num // 5] = dp(num // 5)

        numbers.append(cache[num // 5])

    if num % 3 == 0:
        if cache[num // 3] == 0:
            cache[num // 3] = dp(num // 3)
        numbers.append(cache[num // 3])

    if num % 2 == 0:
        if cache[num // 2] == 0:
            cache[num // 2] = dp(num // 2)
        numbers.append(cache[num // 2])

    if cache[num - 1] == 0:
        cache[num - 1] = dp(num - 1)
    numbers.append(cache[num - 1])

    cache[num] = min(numbers) + 1

    return cache[num]

print(dp(x))