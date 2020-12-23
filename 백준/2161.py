import sys

n = int(sys.stdin.readline().rstrip())

cards = [i for i in range(n, 0, -1)]
while True:
    print(cards.pop())
    if cards:
        cards = [cards.pop()] + cards
    else:
        break
