import sys
from collections import deque

input = sys.stdin.readline

def main():
    n, m, e = map(int, input().rstrip().split())

    xi = deque(list(map(int, input().rstrip().split())))

    while m:
        m -= 1
        s, e = abs(xi[0] - e), abs(xi[-1] - e)

        if s > e:
            xi.popleft()
        else:
            xi.pop()

    print(xi[-1] - xi[0])




if __name__ == "__main__":
    main()