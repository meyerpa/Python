"""
16.4 Tic Tac Win
Design an algorithm to figure out if someone has won a game of tic-tac-toe.
"""

players = ['O', 'X']

def hasOne(tacGame):
    """Input tacGame list of lists"""
    # if board is empty
    if len(tacGame) == 0:
        return True
    # check if three 'X's or 'O' in the row
    for row in tacGame:
        if (row[0] in players) and rowSame(row):
            return True
    # check if columns are the same
    for i in len(tacGame[0]):
        if col[0][i] in players and colSame(tacGame, i):
            return True
    # the last hope is the diagonal is the same element
    # check fist diagonal
    if tacGame[0][0] in players and diagonalSame(tacGame):
        return True
    return tacGame[len(tacGame)][0] in players and diagonal2Same(tacGame)


def rowSame(row):
    if len(row) == 0:
        return True
    first = row[0]
    return all([element == first for element in row])

def colSame(game, i):
    if len(game) == 0:
        return True
    first = game[0][i]
    return all([game[j][i] == first for j in range(len(game))])

def diagonal1Same(game):
    """Returns if the downward diagonal is the same element."""
    length = len(game)
    # if game is 0x0, return True
    if length == 0:
        return True
    # check downward diagonal
    first = game[0][0]
    sameDown = all([game[i][i] == first for i in range(length)])
    return sameDown

def diagonal2Same(game):
    """Returns if the upward diagonal is the same element."""
    length = len(game)
    # if game is 0x0, return True
    if length == 0:
        return True
    # check first
    first = game[length][0]
    sameUp = all([game[length-i][i] == first for i in range(length)])
    return sameUp
