def solution(s):
    length = len(s)
    answer = length

    for i in range(1, (length // 2) + 1):

        zipStr = ''
        previousStr = s[0:i]
        count = 1

        for j in range(i, length - i + 1, i):

            if previousStr == s[j:j + i]:
                count += 1
            else:
                if count == 1:
                    zipStr += previousStr
                else:
                    zipStr += str(count) + previousStr

                count = 1
                previousStr = s[j:j + i]

        else:
            if count != 1:
                zipStr += str(count) + previousStr + s[j + i:]

            else:
                zipStr += s[j:]

        if len(zipStr) < answer:
            answer = len(zipStr)

    return answer