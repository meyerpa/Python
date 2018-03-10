"""
16.11 Diving Board
You are building a diving board by placing a bunch of planks of wood end-to-end.
There are two types of planks, one of length shorter and one of length longer.
You must use exactly K planks of wood. Write a method to generate all possible
lengths for the diving board.
"""

def getLengths(shorter, longer, k):
    all_short = k * shorter
    diff = longer-shorter
    lengths = [all_short + (diff * i) for i in range(k + 1)]
    return lengths

ex = getLengths(1, 2, 4)
print(ex)
