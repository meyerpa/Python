"""
10.1 Sorted Merge
You are given two sorted arrays, A and B, where A has a large enough buffer at
the end to hold B. Write a method to merge B into A in sorted order
"""

def sortedMerge(a, b, lenA, lenB):
    currA = lenA - 1
    currB = lenB - 1
    insert = currA + currB
    # merge and a and b
    while currA >= 0 or currB >= 0:
        # check to see which is larger, and insert at end
        if a[currA] > b[currB]:
            a[insert] = a[currA]
            currA -= 1
        else:
            a[insert] = b[currB]
            currB -= 1
        insert -= 1

    # reached end of one list, and insert b into a
    while currB >= 0:
        a[insert] = currB
        currB -= 1
        insert -= 1
