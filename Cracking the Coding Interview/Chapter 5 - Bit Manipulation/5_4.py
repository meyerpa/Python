"""
5.4 Next Number
Given a positive integer, print the next smallest and next largest number that
have the same number of 1 bits in their binary representation.
-------------------------------------------------------------------------
Example
Input: 9 (or 1001)
Output: 10 (or 1010) and 6 (or 0110)
"""

def next_largest(x):
    # Find the first '01' search R->L, swap those for a '01'
    # and bubble down/right all 1's to the right of the swap
    ct_0 = 0
    ct_1 = 0
    found = False
    while x > 0 and not found:
        # check if '01'
        if (x & 1) == 1  and (x & 2) == 0:
            # flip to 10
            x = (x+2) & ~1
            found = True
        elif (x & 1) == 1:
            ct_1 += 1
        else:
            ct_0 += 1
        if not found:
            x = x >> 1  # move over one bit to the left
    # check that found 01
    if not found:
        return 0
    # shift number over the amount shifted before
    x = x << (ct_0 + ct_1)
    # print(bin(x))
    # mask for 1's taken out before
    mask = ~(~0 << ct_1)
    # print(bin(mask))
    x = x | mask
    return x

def next_smallest(x):
    # Find first '10' search R->L, swap those for a '01'
    # and bubble up/left ones ot the right of the swap
    ct_0 = 0
    ct_1 = 0
    found = False
    while x > 0 and not found:
        # check if '10'
        if (x & 1) == 0  and (x & 2) == 2:
            # flip to 01
            x = (x+1) & ~2
            found = True
        elif (x & 1) == 1:
            ct_1 += 1
        else:
            ct_0 += 1
        if not found:
            x = x >> 1  # move over one bit to the left
    # check that found a '10'
    if not found:
        return 0
    # shift number over the amount shifted before
    print(bin(x))
    x = x << (ct_0 + ct_1)
    print(ct_0 + ct_1)
    # mask for 1's taken out before
    mask = ~(0<<ct_1) << ct_0               # TODO: FIX
    print(bin(mask))
    x = x | -mask
    return x

"""NOTE: WRONG as 0<<5 still would be 0, not 000000"""

ex = 19
print('number')
print(bin(ex))
print('next_largest')
print(bin(next_largest(ex)))
print('next_smallest')
print(bin(next_smallest(ex)))
