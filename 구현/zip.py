def solution(s):
    zipNumber = 0  # 압축된 양

    for i in range(1, (len(s) // 2 + 1)):
        index = 0
        compare = s[:i]
        counts = [0]

        while index + 2 * i <= len(s):
            index += i
            current = s[index:index + i]

            if compare == current:
                counts[-1] += 1
            else:
                compare = current
                counts.append(0)
        zipNumber = max(zipNumber, sum(counts) * i - (sum(map(a, counts))))

    return len(s) - zipNumber


def a(number):
    if number == 0:
        return 0
    number += 1
    return len(str(number))

if __name__ == "__main__":
    s = "abcabcabcabcdededededede"
    print(solution(s))


#https://programmers.co.kr/learn/courses/30/lessons/60057