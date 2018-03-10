"""
16.17 Contiguous Sequence
You are given an array of integers (both positive and negative). Find the
contiguous sequence with the largest sum. Return the sum.
"""

def largestSum(a):
    """Return the largest sum in a"""
    if len(a) == 0:
        return 0
    maximum = a[0]   # current max is the first element
    total = 0
    # iterate through a, getting rid of any negative sums in front
    # and keep track of the maximum positive sum
    for element in a:
        total += element
        # update maximum, if necessary
        if total > maximum:
            maximum = total
        # reset total if negative sum
        if total < 0:
            total = 0
    return maximum
