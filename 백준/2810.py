import sys

N = int(sys.stdin.readline().rstrip())

seats = sys.stdin.readline().rstrip()

if 'LL' in seats:
    print(len(seats.replace("LL", 'S'))+1)
else:
    print(len(seats))
