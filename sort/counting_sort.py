def counting_sort(numbers, scope):
    count = [0] * (scope + 1)
    sorted_number = []

    for i in numbers:
        count[i] += 1

    for i, v in enumerate(count):
        for _ in range(v):
            sorted_number.append(i)

    return sorted_number



if __name__ == "__main__":
    numbers = [2,2,2,1,4,3,3,3,5,6,7,8,8,8,8,10,9,6,7,7,6]
    print("입력", numbers)
    print("출력", counting_sort(numbers,10))

