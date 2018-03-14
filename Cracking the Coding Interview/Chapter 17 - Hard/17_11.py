"""
17.11 Word Distance
You have a large text file containing words. Given any two words, find the
shortest distance (in terms of number of words) between them in the file.
If the operation will be repeated many times for the same file (but different
pairs of words), can you optimize your solution?
"""
import math as math

wordLocations = {}

def storeFile(file):
    """stores the location of each word in word locations"""
    for loc, word in enumerate(file):
        if word in wordLocations:
            wordLocations[word].append(loc)
        else:
            wordLocations[word] = [loc]

def wordDistance(word1, word2, locations):
    "Returns the minimum distance between word1 and word2"
    # return -1 if either word wasn't in the file
    if (not word1 in locations) or (not word2 in locations):
        return -1
    distance = sys.maxsize      # initialize distance
    p1 = 0
    p2 = 0
    while p1 < len(locations[word1]) or p2 < len(locations[word2]):
        currentDistance = math.abs(locations[word1][p1] - locations[word2][p2])
        distance = math.min(distance, currentDistance)
        if locations[word1][p1] < locations[word2][p2]:
            p1 += 1
        else:
            p2 += 1

    # iterate to end of list1 if not there
    while p1 < len(locations[word1]):
        currentDistance = math.abs(locations[word1][p1] - locations[word2][p2])
        distance = math.min(distance, currentDistance)
        p1 += 1

    # iterate to end of list2 if not there
    while p2 < len(locations[word2]):
        currentDistance = math.abs(locations[word1][p1] - locations[word2][p2])
        distance = math.min(distance, currentDistance)
        p1 += 1
    
    return distance
