"""
10.4 Sorted Search, No Size
You are given an array-like data structure Listy which lacks a size method.
It does, however, have an elementAt(i) method that returns the element at index
i in O(1) time. If i is beyond the bounds of the data structure, it returns -1.
(For this reason, the data structure only supports positive integers). Given
a Listy which contains sorted, positive integers, find the index at which an
element x occurs. If x occurs multiple times, you may return any index.
"""

def find(x, num):
    """Returns the index which num is at in list x."""
    current = 0
    firstElem = x.elementAt(current)
    if firstElem == -1 or firstElem == num:
        return firstElem
    return findHelper(x, num, current, 1) # search through remainder of Listy

def findHelper(x, num, prev, index):
    if x[index] == num:
        return index
    # if previous and index are one apart, element doesn't exist in the List
    if index == prev + 1:
        return -1
    # if greater, look at element half way between (binary search)
    if x[index] > num:
        findHelper(x, num, prev, (index + prev) / 2)
    # if less, then take a twice as large step as last time
    if x[index] < num:
        findHelper(x, num, index, index + 2 * (index - prev))
