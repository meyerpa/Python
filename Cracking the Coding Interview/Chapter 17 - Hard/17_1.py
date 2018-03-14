"""
17.1 Add Without Plus
Write a function that adds two numbers. You should not use + or any arithmetic
operators.
"""

def add(num1, num2):
    """Returns the sum of num1 and num2"""
    # see which numbers are both 1, and carry those to the left
    carry = (num1 & num2) << 1
    # see which numbers are 0, 1 or 0,0 and leave same
    xor = num1 ^ num2
    res = carry | xor
    while (carry & xor) != 0: # do this until don't have two ones
        num1 = carry
        num2 = xor
        # see which numbers are both 1, and carry those to the left
        carry = (num1 & num2) << 1
        # see which numbers are 0, 1 or 0,0 and leave same
        xor = num1 ^ num2
        res = carry | xor
    return res


print(add(15, 15))
