import heapq


def solution(food_times, k):
    answer = 0
    cycle = len(food_times)
    hq = []

    for i, el in enumerate(food_times):
        heapq.heappush(hq, (el, i))

    minTimes = hq[0][0]
    total = 0

    while cycle * minTimes <= k:
        k -= cycle * minTimes
        total += minTimes

        while hq and hq[0][0] - total == 0:
            heapq.heappop(hq)

        if hq:
            cycle = len(hq)
            minTimes = hq[0][0] - total
        else:
            return -1

    hq.sort(key=lambda x: x[1])

    return hq[k % cycle][1] + 1