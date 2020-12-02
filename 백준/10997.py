import sys

N = int(sys.stdin.readline())


if N == 1:
    print('*')
else:
    for i in range(8 * N - 3):
        idx = i - 1

        if idx % 4 == 0 and idx < (N // 2):
            num = idx // 4
            stars = '* ' * num + '*' * ((4 * N - 3) - 2*(2*num - 1)) + ' *' * (num - 1)
            print(stars)




