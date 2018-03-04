"""
10.9 Sorted Matrix Searching
Given an M x N matrix in which each row and each
column is sorted in ascending order, write a method to find an element.
"""

def findElement(matrix, num):
    """Returns the column and row of the number in the matrix"""
    lowRow = 0
    lowCol = 0
    highRow = matrix.shape[0]
    highCol = matrix.shape[1]
    if matrix.isEmpty():
        return -1
    return findElementHelper(matrix, num, lowRow, highRow, lowCol, highCol)


def findElementHelper(matrix, num, lowRow, highRow, lowCol, highCol):
    if lowRow > highRow or lowCol > highCol:
        return -1
    midRow = (lowRow + highRow) // 2
    midCol = (lowCol + highCol) // 2
    if matrix[midRow, midCol] == num:
        return (midRow, midCol)
    # if less, search previous half
    elif matrix[midRow, midCol] < num:
        findElementHelper(matrix, num, lowRow, midRow - 1, lowCol, midCol - 1)
    # if more, search latter half
    else:
        findElementHelper(matrix, num, midRow+1, highRow, midCol+1, highCol)
