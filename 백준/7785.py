import sys

n = int(sys.stdin.readline().rstrip())
workers = set()
for _ in range(n):
    name, act = tuple(sys.stdin.readline().rstrip().split())

    if act == 'enter':
        workers.add(name)
    else:
        workers.remove(name)

workers = list(workers)
workers.sort(reverse=True)

for w in workers:
    print(w)