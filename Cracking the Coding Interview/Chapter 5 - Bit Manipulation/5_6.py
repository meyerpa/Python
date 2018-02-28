"""
5.6 Conversion
Write a function to determine the number of bits you would need to flip
to convert integer A to integer B.
------------------------------------------------------------------
Example
Input: 29 (or 11101), 15 (or 01111)
Output: 2
"""

def ct_bits_flip(a, b):
    # Note, assume these are the same length??
    ct = 0
    diff = a ^ b # a exclusive or b, should be 1 if bits are different
    while diff > 0:
        ct += diff & 1
        diff = diff >> 1  # shift diff over one bit
    return ct

print(ct_bits_flip(29, 15))
