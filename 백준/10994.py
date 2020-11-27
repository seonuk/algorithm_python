import sys

N = int(sys.stdin.readline().rstrip())

for rowNum in range(8 * N - 7):
    if rowNum % 4 == 0:
        edge = N - 1 - abs((N - 1) - (rowNum // 4))
        center = N - edge
        stars = '* ' * edge + '*' * (4 * center - 3) + ' *' * edge
        print(stars)
    elif rowNum % 2 == 0:
        center = ((abs(4 * N - 4 - rowNum) - 2) // 4) + 1
        edge = N - center

        stars = '* ' * edge + ' ' * (4 * center - 3) + ' *' * edge
        print(stars)
    else:
        print('' * (8 * N - 7), end='')
