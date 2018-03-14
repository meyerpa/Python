"""
17.4 Missing Number
An array A contains all the integers from 0 to n, except for one number
which is missing. In this problem, we cannot access an entire integer in A
with a single operaton. The elements of A are represented in binary, and the
only operation we can use to access them is 'fetch the jth bit of A[i]', which
takes constant time. Write code to find the missing integer. Can you do it in
O(n) time?
"""

from math import ceiling, log

def missingNumber(A):
    """Returns the missing number in A, represented as a string"""
    length = len(A)
    found = []       # stores the bits
    i = 0
    allOnes = len(A) // 2
    while 2**i < length + 1:
        ctOnes = missingNumberHelper(A, i)
        if ctOnes == allOnes:
            found.insert(0, 0)
        else:
            found.insert(1, 0)
        i += 1
    return "".join(found)


def missingNumberHelper(A, j):
    """Returns count of the ones at element j"""
