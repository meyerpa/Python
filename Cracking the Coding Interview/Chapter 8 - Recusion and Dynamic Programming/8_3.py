"""
8.3 Magic Index
A magic index in an array A[0...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find a
magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
"""
# initial -- shitty
def shittyFindMagicIndex(A):
    index = [i for i, x in enumerate(A) if i == x]
    return -1 if index==[] else index[0]

A = [-6, -5, 0, 1, 4, 18, 19]
#index = findMagicIndex(A)
#print(index)

# binary search on sorted array

def findMagicIndex(A, offset = 0):
    if A == []:
        return -1
    index = len(A) // 2
    # check if index is the correct
    if A[index] == index + offset:
        return index + offset
    # check that searching the left side would be feasible
    if A[index] >= 0:
        # recurse on the left side
        left = findMagicIndex(A[:index], offset)
        if left != -1:
            return left
    # check that searching the right side is feasible
    if A[index] < offset + len(A):
        return findMagicIndex(A[index+1:], offset + index + 1)
    return -1

print(findMagicIndex(A))
