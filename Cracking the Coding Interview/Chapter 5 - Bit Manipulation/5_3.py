"""
5.3 Flip Bit to Win
You have an integer and you can flip exactly one bit from a 0 to a 1. Write code
to find the length of the longest sequence of 1s you could create.
------------------------------------------------------------------
Example
Input: 1775 (or 11011101111)
Output: 8
"""

def longest_ones_flip_bit(x):
    # track max_length, iterating over the bits, finding the maximum 1's
    # sequence flipping one bit (if needed)
    # Note that x is an integer
    max_length = 1              # even if all 0's one bit can be flipped
    curr_length = 0             # track current 1's length
    prev_length = 0             # track previous 1's length (if any)
    # iterate through bin(x) going from R to L, keeping track of max length
    while x > 0:
        if (x & 1) == 1:
            curr_length += 1
        else:
            # update max if greater
            max_length = max(curr_length + prev_length, max_length)
            # check if next number is a 1--seq of 1's separated by only one 0
            if (x & 2) == 2:
                prev_length = curr_length
            else:
                prev_length = 0
            curr_length = 0
        x = x >> 1              # update x to get next bit
        #print(curr_length)
    # update max_length again
    max_length = max(curr_length + prev_length, max_length)
    return max_length

ex = 1775
print(bin(ex))
print(longest_ones_flip_bit(ex))
