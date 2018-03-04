"""
10.5 Sparse Search
Given a sorted array of strings that is interspersed with empty strings, write
a method to find the location of a given string.
EXAMPLE
Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4
"""

def findString(x, string):
    """Returns the index string is in list x."""
    high = len(x) - 1
    low = 0
    mid = (high + low) / 2


def findStringHelper(x, string, low, high):
    # didn't find variable in list
    if low > high:
        return -1
    check = (low + high) / 2   # variable to represent current check for empty strings
    addEach = 1
    while x[check] == "":
        check += addEach
        # go through lower
        if check > high:
            check = mid
            addEach = -1
        if check == 0:
            return -1
    # check if current same as string, if so return index
    if x[check] == string:
        return low
    # if larger, search left half
    elif x[check] > string:
        return findStringHelper(x, string, low, check - 1)
    # if lower, search right half
    else:
        return findStringHelper(x, string, check + 1, high)
