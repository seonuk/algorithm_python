import re


def oper(num1, op, num2):
    if op == '*':
        return num1 * num2

    if op == '+':
        return num1 + num2

    if op == '-':
        return num1 - num2


def solution(expression):
    answer = 0
    operator = [
        ['*', '+', '-'],
        ['*', '-', '+'],
        ['+', '*', '-'],
        ['+', '-', '*'],
        ['-', '*', '+'],
        ['-', '+', '*']
    ]

    total = 0

    for priority in operator:
        numbers = list(map(int, re.split('[*\-\+]', expression)))
        numbers.reverse()
        op_stack = []
        num_stack = [numbers.pop()]

        for input_op in expression:
            if input_op not in operator[0]:
                continue

            while op_stack and priority.index(op_stack[-1]) >= priority.index(input_op):
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                result = oper(num1, op_stack.pop(), num2)
                num_stack.append(result)

            else:
                op_stack.append(input_op)
                num_stack.append(numbers.pop())

        while op_stack:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            result = oper(num1, op_stack.pop(), num2)

            num_stack.append(result)

        total = max(abs(num_stack[0]), total)

    return total