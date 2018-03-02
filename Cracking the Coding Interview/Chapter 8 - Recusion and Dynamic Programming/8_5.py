"""
8.5 Recursive Multiply
Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations
"""

def recursiveMult(x, y):
    # could add x, y times
    # but going to add x bitshift to the left (multiply by two) (n>>2)
    if y == 1:
        return x
    remainder = x if (y & 1) == 1 else 0
    x = x << 1          # multiply x by two
    y = y >> 1          # divide y by two
    # adding on x again if y is odd
    return recursiveMult(x, y) + remainder

print(recursiveMult(4, 7))
