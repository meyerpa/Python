"""
16.15 Mastermind
The Game of Master Mind is played as follows:
The computer has four slots, each slot will contain a ball that is red (R),
yellow (Y), green (G), or blue (B). For example, the computer might have
RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot #4 if blue).

You, the user, are trying to guess the solution. You might, for example,
guess YRGB.

When you guess the correct color for the correct slot, you get a "hit".
If you guess a color that exists but is in the wrong slot, you get a
"pseudo-hit". Note that a slot that is a hit can never count as a pseudo-hit.

For example, fi the actual solution is RGBY and you guess GGRR, you have one
hit and one pseudo-hit. Write a method that, give a guess and and a solution,
returns the number of hits and pseudo-hits.
"""

def getHits(guess, solution):
    """Returns the number of hit and pseudo-hits given a guess (string), and
    solution (string)."""
    if len(guess) != len(solution):
        return -1

    guessHits = {
        "R": 0,
        "G": 0,
        "B": 0,
        "Y": 0
    }

    solHits = {
        "R": 0,
        "G": 0,
        "B": 0,
        "Y": 0
    }

    hits = 0
    pseudohits = 0
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            hits += 1
        elif solHits[guess[i]] > 0:     # check if solution had color in other place
            pseudohits += 1             # have a pseudohit
            solHits[guess[i]] -= 1      # get rid of letter in solution
        elif guessHits[solution[i]] > 0:
            pseudohits += 1
            guessHits[solution[i]] -= 1
        else:                           # not found, so store count
            solHits[solution[i]] += 1
            guessHits[guess[i]] += 1
    return (hits, pseudohits)
