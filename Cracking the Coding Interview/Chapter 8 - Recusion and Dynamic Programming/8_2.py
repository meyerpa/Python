"""
Robot in a Grid
Imagine a robot sitting on the upper left corner of grid with r rows and c
columns. The robot can only move in two directions, riht and down, but certain
cells are "off limits" such that the robot cannot step on them. Design an
algorithm to find a path for the robot from the top left to the bottom right.
"""

import numpy as np


class Grid:
    """holds true and false if can visit there"""
    def __init__(self, nRow, nCol):
        self.__grid = np.ones([nRow, nCol], dtype=bool)

    def markOffLimits(self, point):
        self.__grid[point.getRow(), point.getCol()] = False

    def canVisit(self, point):
        if point.getRow() >= self.__grid.shape[0]:
            return False
        if point.getCol() >= self.__grid.shape[1]:
            return False
        return self.__grid[point.getRow(), point.getCol()]

class Point:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col

    def getCol(self):
        return self.__col

    def getRow(self):
        return self.__row

    def __eq__(self, other):
        return self.getCol()==other.getCol() and self.getRow()==other.getRow()

    def __str__(self):
        return "(" + str(self.getRow()) + ", " + str(self.getCol()) + ")"

    def __repr__(self):
        return self.__str__()

NCOL = 4
NROW = 4

# create 4x4 grid
model = Grid(NCOL + 1, NROW + 1)
model.markOffLimits(Point(0, 1))
model.markOffLimits(Point(2, 0))


def findPath(path, final):
    # print(path)
    current = path[-1]
    # check if at last spot
    if current == final:
        return path
    if not model.canVisit(current):
        return -1
    else:
        # check if can find path going down
        path.append(Point(current.getRow(), current.getCol() + 1))
        down = findPath(path, final)
        # print(str(currRow)+","+str(currCol))
        # print(path)
        if down != -1:
            return down
        path = path[:-1]                # get rid of failed down path
        # if cannot go down, try moving to right
        path.append(Point(current.getRow() + 1, current.getCol()))
        right = findPath(path, final)
        if right != -1:
            return right
        else:
            return -1


def findPathHelper(finalCol, finalRow):
    return findPath([Point(0, 0)], Point(finalCol, finalRow))


path = findPathHelper(4, 4)
print(path)
