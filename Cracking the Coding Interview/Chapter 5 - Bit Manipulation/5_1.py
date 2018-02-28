"""
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i
and j. Write a method to insert M into N such that M stars at bit j and ends at
bit i. You can assume that there are at least 5 bits between j and i. You would
not, for example have j=3 and i=2, because M could not fully fit between bit 3
and bit 2.
----------------------------------------------------------
Example:
Input:  N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
"""

def insert(M, N, i, j):
    """insert M into N such that M starts at j, and ends at i"""
    """parameters
            M, N: integers
            j, i: integers
        output
            N : binary string
    """
    # separate into two masks one for the leading digits (>j) and the other
    # mask for the trailing digits <i. Combine both masks the clear out
    # the inserted number digits
    # move the inserted number over i digits and combine together

    leading_mask = N & (~0 << i)
    trailing_mask = ~(~0 << i)
    mask = leading_mask | trailing_mask
    
    N = N & mask

    # shift M by the offset, i
    insert_number = M << i
    new_number = (N | insert_number)

    return bin(new_number)


N = int('10000000000', 2)
M = int('10011', 2)
i = 2
j = 6
ans = insert(M, N, i, j)
print(ans)
