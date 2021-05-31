n = int(input())

def a(count):
    print("a")
    if count == 1:
        return set(["()"])
    if count == 2:
        return set([""])
    result = set()

    for r in a(count - 1):
        result.add('(' + r + ')')
        result.add('()' + r)
        result.add(r +'()')

    return result

print(list(a(n)))

# 1 ()
# 2 (()), ()()
# 3 n - 2 n -1