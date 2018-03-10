"""
16.6 Smallest Difference
Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-ngative) difference. Return the difference.
EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
Output: 3. That is the pair {11, 8}
"""

import sys as sys

def smallestDiff(l1, l2):
    """Returns the smallest non-negative difference between the lists"""
    # assert that the lists are not empty
    if len(l1) == 0 or len(l2) == 0:
        return -1
    # STEP #1 - Sort the arrays
    l1.sort()
    l2.sort()
    # have pointer in each list
    curr2 = l2[0]
    minimum = sys.maxsize
    i = 0
    for element in l1:
        # iterate through l2, while l2 is less than l1's element
        # when the element in l2 is larger, go to the next larger element in l1
        while l2[i] < element and i < len(l2):
            if element - l2[i] < minimum:
                minimum = element - l2[i]
            i += 1 # go to next element in l2
    return minimum

ex1 = [1, 3, 15, 11, 2]
ex2 = [23, 127, 235, 19, 8]
print(smallestDiff(ex1, ex2))
