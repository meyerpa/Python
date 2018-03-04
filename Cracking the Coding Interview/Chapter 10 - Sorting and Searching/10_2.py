"""
10.2 Group Anagrams
Write a method to sort an array of strings so that all the anagrams are next
to each other.
"""


def sortArrayString(a):
    """Returns list with anagrams grouped together"""
    # Insertion Sort-like method
    # iterate through a, and move anagrams together
    ctAnagrams = 0
    for i, string in enumerate(a):
        # look at remaining string for anagrams, and insert the value at the
        # next element (shifted by the number of anagrams found)
        for j in range(i, len(a)):
            if isAnagram(string, a[i]):
                ctAnagrams += 1
                a[i+ctAnagrams], a[j] = a[j], a[i+ctAnagrams]   # swap values
        ctAnagrams = 0     # restart counter
    return a


def isAnagram(a, b):
    """
    Return whether a is an anagram of b
    """
    # dictionary counting the times each letter is seen
    countTimes = {
        "a": 0,
        "b": 0,
        "c": 0,
        ...
        .
        .
    }
    # count characters in a
    for char in a:
        countTimes[char] += 1
    # remove one count for each character in b
    for char in b:
        countTimes[b] -= 1
    # retunr True that each letter in countTimes is 0
    return all(countTimes.values() == 0)
