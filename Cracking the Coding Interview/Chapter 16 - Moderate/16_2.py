"""
16.2 Word Frequencies
Design a method to find the frequency of occurrences of any given word
in a book. What if we were running this algorithm multiple times?
"""

def setFrequencies(book):
    """Returns the number of occurrences of the word in a book"""
    try:
        wordCount
    except NameError:
        global wordCount = {}
    finally:
        for word in book:
            if word.lower() not in wordCount:
                wordCount[word.lower()] = 1
            else:
                wordCount[word.lower()] += 1

    return wordCount


def getCount(wordCount, word):
    if word in wordCount:
        return wordCount[word]
    else:
        return 0

freq = setFrequencies(book)
occurrences = getcount(freq, word)
