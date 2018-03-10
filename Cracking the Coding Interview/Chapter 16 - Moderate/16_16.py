"""
16.16 Sub Sort
Given an array of integers, write a method to find indicies m and n such that
if you sorted elements m through n, the entire array would be sorted.
Minimize n - m (that is, find the smallest such sequence).
EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7 12, 6, 7, 16, 18, 19
Output: (3, 9)
"""

def needToSort(l):
    """Returns the indexes of the list (m, n) that need to be sorted for the
    list to be sorted."""
    i = 0           # index of where left ends
    # find left based on the first ordered sequence
    while i < len(l) and l[i+1] > l[i]:
        i += 1
    # check that the list wasn't already ordered
    if i == len(l):
        return (0, 0)
    # find right based on the last ordered sequence
    j = len(l)              # index where right starts
    while j > i and l[j] > l[j-1]:=
        i -= 1
    left = l[:i]            # left ordered sequence
    right = l[j:]           # right ordered sequence
    middle = [i:j]          # middle unordered sequence
    m = i - 1
    n = len(l) - j
    middleMin = min(middle)
    # shift over m while max(left) > min(middle)
    while left[m] > middleMin:
        m -= 1
    # shift over n while min(left) < max(middle)
    middleMax = max(middle)
    i=0
    while middleMax < left[i]:
        i += 1
        n -= 1
    return (m, n)
