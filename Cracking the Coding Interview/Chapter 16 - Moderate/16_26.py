"""
16.26 Calculator
Given an arithmetic equation consisting of positive integers, +, -, *, and /
(no parenthesis), compute the result.
EXAMPLE
Input:      2*3+5/6*3+15
Output:     23.5
"""

def calculator(expression):
    if len(expression) < 2:
        return None
    # evaluate * and / first (storing intermediate result in a stack)
    numbers = []
    operators = []
    index = 0
    while index < len(expression):
        first = expression[index]
        operator = expression[index+1]
        second = expression[index+2]
        if operator == "*":
            # evaluate then put on stack
            num = int(first) * int(second)
            numbers.push(num)
        elif operator == "/":
            # evaluate then put on stack
            num = int(first) / int(second)
            numbers.push(num)
        else:
            # put numbers on the stack to be evaluated after * and /
            numbers.push(first)
            numbers.push(second)
            operators.push(operator)
        index += 3
    # once reached end, evaluate + and - expressions
    res = numbers.pop()
    while not numbers.isEmpty():
        if not numbers.isEmpty():
            operator = operators.pop()
            second = numbers.pop()
            if operator == +:
                res += second
            else: # operator is -
                res -+ second
    return res
