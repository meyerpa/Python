"""
10.3  Search in a Rotated Array
Given a sorted array of n integers that has been rotated an unknown number of
times, write code to find an element in the array. You may assume that the
array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8 (the index of 5 in the array)
"""

def getMiddle(high, low = 0):
    middle = (high + low) / 2
    return middle

def getIndex(a, num):
    """Returns the index of num in a"""
    # Want to do a binary search-like technique for this
    high = len(a) - 1
    low = 0
    return getIndexHelper(a, num, high, low)


def getIndexHelper(a, num, high, low=0):
    if low > high:
        return -1
    mid = a[getMiddle(high, low)]
    left = a[low]
    right = a[high]
    if mid == num:
        return getMiddle(high, low)
    if left < mid:  # left is normal
        if num < mid and num > left:
            return getIndexHelper(a, num, mid-1, low)
        else:
            return getIndexHelper(a, num, high, mid + 1)
    elif right >  mid:  # right is normal
        if num > mid and num < right:
            return getIndexHelper(a, num, high, mid + 1)
        else:
            return getIndexHelper(a, num, mid - 1, high)
    elif left == mid: # number just repeats
        # search right first, then return
        res = getIndexHelper(a, num, high, mid+1)
        if res != -1:
            return res
        return getIndexHelper(a, num, mid-1, low)
