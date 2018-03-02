"""
7.1 Deck of Cards
Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.
"""

import random as random

# Objects, card, deck (has 52 cards), blackjack (game that uses one deck, assuming not casino-style with multiple decks)

class Suit:
    def __init__(self, suit):
        self.__suit = suit

    def get(self):
        return self.__suit

class Card:
    """Holds information about card--suit and number. Aces are low."""
    def __init__(self, suit, number):
        self.__suit = suit
        self.__number = number

    def getSuit(self):
        return self.__suit

    def getNumber(self):
        return self.__number

    def get(self):
        return str(self.__number) + str(self.__suit)

class BlackjackCard(Card):
    def isAce(self):
        return self.getNumber() == 1

    def isFaceCard(self):
        return self.getNumber() > 10

    def getValues(self):
        if self.isAce() == 1:
            return [1, 11]
        if self.isFaceCard():
            return [10]
        else:
            return [self.getNumber()]


class Deck:
    """Holds 52 different cards--assuming no Jokers"""
    def __init__(self):
        self.__cards = []
        self.__current_card = 0
        suits = [Suit('heart'), Suit('spade'), Suit('diamond'), Suit('clover')]
        numbers = range(1, 14)
        for i in numbers:
            for suit in suits:
                self.__cards.append(Card(suit, i))

    def shuffle(self):
        """Randomizes deck"""
        self.__cards = random.shuffle(self.__cards)

    def next(self):
        """Returns -1 if no cards left in the deck"""
        if self.__current_card >= len(self.__cards):
            return "-1"
        return self.__cards[self.__current_card]

    def cards_left(self):
        return len(self.__cards)-self.__current_card

class Hand:
    def __init__(self):
        self.__cards = []
        self.__score = 0

    def addCard(self, card):
        self.__cards.append(card)
        self.updateScore(card)          # TODO -- implement score based on game

    def updateScore(card):
        self.score += card.getValue()

    def getScore(self):
        return self.__score

class BlackjackHand(Hand):
    def __init__(self):
        super(BlackjackHand, self).__init__()
        self.__possibleScores = []

    def updateScore(card):
        scores = card.getValues() #assuming is BlackjackCard, so returns list of scores
        for possibleScore in self.__possibleScores:
            for score in scores:
                self.__possibleScores.append(score + possibleScore)

    def getScore(self):
        threshold = 21
        max_score = 0
        for score in self.__possibleScores:
            if score > max_score and score <= threshold:
                max_score = score
            if score == threshold:
                break
        return max_score
