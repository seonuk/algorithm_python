import sys

charset = sys.stdin.readline().rstrip()

for i in "UCPC":
    if i in charset:
        charset = charset[charset.index(i):]
    else:
        print("I hate UCPC")
        break
else:
    print('I love UCPC')


