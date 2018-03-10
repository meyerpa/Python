"""
16.24 Pairs with Sum
Design an algorithm to ffind all pairs of integers within an array which sum
to a specified value.
"""

def pairs(l, value):
    """Return pairs of values within the list that sum to value."""
    if len(l) < 2:
        return []
    # assert the list is sorted O(nlog(n))
    l.sorted()
    # have pointer at beggining and one at end, and move towards each other
    # until reach sum O(n)
    first  = 0
    last = len(l) - 1
    pairs = []
    while first < last:
        if l[first] + l[last] == 0:
            pairs.append((first, last))
        elif l[first] + l[last] < 0:
            first += 1
        else:
            last -= 1
    return pairs
