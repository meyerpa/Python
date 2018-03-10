"""
16.5 Factorial Zeros
Write an algorithm which computes the number of trailing zeros in n factorial.
"""

from math import ceiling, log

def trailingZeros(n):
    """Returns the number of trailing zeros in n factorial"""
    zeros = 0
    for i in range(1, ceiling(log(n, 5))):
        zeros += n // (5**i)
    return zeros
