"""
17.2 Shuffle
Write a method to shuffle a deck of cards. It must be a perfect shuffle
--in other words, each of the 52! permutations of the deck has to be equally
likely. Assume that you are given a random number generator which is perfect.
"""

class Card:
    def __init__(self, num, suit):
        self.__number = num
        self.__suit = suit


class Deck:
    def __init__(self):
        suits = ["Hearts", "Spades", "Diamond", "Club"]
        nums = range(1, 14)
        self.__deck = []
        for suit in suits:
            for num in nums:
                self.__deck.append(Card(num, suit))

    def shuffle(self):
        self.__deck = self.shuffleHelper(self.__deck)

    def shuffleHelper(self, deck):
        if len(deck) < 2:
            return deck
        index = rng(len(deck))
        if index == len(deck) - 1:
            other = self.shuffleHelper(deck[0:index])
        else:
            other = self.shuffleHelper(deck[0:index] + deck[index+1:])
        return other.append(deck[index])


def shuffle():
    """Return a deck that is shuffled perfectly (randomized)."""
    deck = Deck()
    deck.shuffle()
    return deck
