"""
7.6 Jigsaw
Implement a NxN jigsaw puzzle. Design the data structures and explain an
algorithm to solve the puzzle. You can assume that you have a fitsWith method
which, when passed two puzzle edges, returns true if the two edges belong
together.
"""

from enum import Enum

# assuming 4 sides for each piece
class orientation(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

class Piece:
    def __init__(self, edges):
        self.__edges = edges
        self.__isEdge = False
        self.__is

    def getEdges(self):
        return self.__edges

    def adjacentTo()

    def fitsWith(self, other):
        """returns the edge(int) it is connected to if the two pieces belong together"""
        # TODO: Can use list comprehesion??
        for i, selfEdge in enumerate(self.getEdges()):
            for j, otherEdge in other.getEdges():
                if selfEdge.fitsWith(otherEdge):
                    return i, j
        return False   # made it here, so no edge fits together



class Edge:
    def __init__(self, ...):
        pass

    def fitsWith(self, other):
        # assuming implemented already, returns true if two edges fit together

class Jigsaw:
    def __init__(self, pieces):
        self.__pieces = pieces


    def solveJigsaw(self, peices):
        pass
