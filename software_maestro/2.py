def main():
    p, n, h = map(int, input().rstrip().split())

    user = [[] for _ in range(p + 1)]

    for _ in range(n):
        pc, time = map(int, input().rstrip().split())

        user[pc].append(time)

    for l in user:
        l.sort()

    for i, times in enumerate(user[1:]):
        result = 0
        remainTime = h

        for time in times:
            if remainTime >= time:
                result += time * 1000
                remainTime -= time
        print(i+1, result)

if __name__ == "__main__":
    main()