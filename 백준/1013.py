import sys
import re

t = int(sys.stdin.readline().rstrip())
regex = re.compile('(100+1+|01)+')
for _ in range(t):
    print( 'YES' if regex.fullmatch(sys.stdin.readline().rstrip()) else 'NO')
