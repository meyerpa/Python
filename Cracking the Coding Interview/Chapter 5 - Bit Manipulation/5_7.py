"""
5.7 Pairwise Swap
Write a program to swap odd and even bits in an integer with as few instructions
as possible (e.g., bi 0 and bit 1 are swapped, bit 2 and bit 3 are swapped,
and so on).
"""

def swap_even_odd(x):
    even_mask = int("aaaaaaaa", 16)            # 101010
    odd_mask =  int("55555555", 16)            # 010101
    new_even = (x & odd_mask) << 1             # shift odd to even spot
    new_odd = (x & even_mask) >> 1             # shift even to odd spot
    return (new_even | new_odd)                # return even with odd

ex = 42
print(bin(ex))
print(bin(swap_even_odd(ex)))
