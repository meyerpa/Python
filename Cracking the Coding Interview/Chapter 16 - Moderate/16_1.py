"""
16.1 Number Swapper
Write a function to swap a number in place (that is, without temporary
variables).
"""

def swapInPlace(x, y):
    """Returns x and y swapped in place"""
    y = y - x           # set y to be the difference between the numbers
    x = y + x           # update x to be y
    y = x - y           # update y to x
    return x, y


def swapInPlace2(x, y):
    """Returns x and y swapped in place"""
    # This algorithms does a inplace swap using xor
    y = x ^ y          # y is the xor of x and y
    x = x ^ y          # update x to initial y
    y = x ^ y          # update x to initial x
