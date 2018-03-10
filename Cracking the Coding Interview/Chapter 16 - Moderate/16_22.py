"""
16.22 Langton's Ant
An ant is sitting on an infinite grid of white and black squares. It initially
faces right. At each step, it does the follwing:
    (1) At a white square, flit the color of the square, turn 90 degrees right
        (clockwise), and move forward one unit.
    (2) At a black square, flip the color of the square, turn 90 degrees left
        (counter-clockwise), and move forward one unit
Write a program to simulate the first K moves that the ant makes and pring the
final board as a grid. Note that you are not provided with the data structure to
represent the grid. This si something you must design yourself. Teh only input
to your method is K. You should print the final grid and return nothing. The
method signature might be something like void printKMoves(int K).
"""

class Facing:
    """Implement a class for facing certain ways, and turn right, left"""
    def __init__(self, initial):
        # 0 -> Up, 1 -> Right, 2 -> Down, 3 -> left
        self.__pos = 0

    def isUp(self):
        return self.__pos == 0


class Position:
    """Stores information related to position"""
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def moveFoward(self, facing):
        if facing.isRight():
            self.__x += 1
        elif facing.isDown():
            self.__y -= 1
        elif facing.isLeft():
            self.__x -= 1
        else:
            self.__y += 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


class Grid:
    def __init__(self, K):
        # create a 2k by 2k grid of white and black squares

        self.__offset = k

    def isWhite(self, position):
        x = self.__offset + position.getX()
        y = self.__offset + position.getY()
        return grid[x, y] == 1

    def turnColor(self, position):
        x = self.__offset + position.getX()
        y = self.__offset + position.getY()
        grid[x, y] = not grid[x, y]

def printKMoves(K):
    """Return the grid after the walk."""
    grid = getNewGrid(K)
    current = Position(0, 0)
    face = Facing("Right")
    return printKMovesHelper(K, current, grid)


def printKMovesHelper(K, position, grid, facing):
    if K == 0:
        return grid
    """Return the grid after the walk, and updates the grid with the walk"""
    if grid.isWhite(position):          # Turn right
        facing.turnRight()
    else:
        facing.turnLeft()
    # turn color of square
    grid.turnColor(position)
    # move forward
    position.moveFoward(facing)
    return printKMovesHelper(K-1, position, grid, facing)
