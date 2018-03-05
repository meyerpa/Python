"""
10.10 Rank from Stream
Imagine you are reading in a stream of integers. Periodically, you wish to be
able to look up the rank of a number x (the number of values less than or equal
to x). Implement the data structures and algorithms to support these operations.
That is, implement the method track (int x), which is called when each number
is generated, and the method getRankOfNumber(int x), which returns the number
of values less than or equal to x (not including x itself).
EXAMPLE
Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 2
getRankOfNumber(1): 0
getRankOfNumber(3): 4
getRankOfNumber(4): 3
"""

class IntStream:
    def __init__(self, stream):
        self.__bst = BinarySearchTree()

    def trackInt(self, x):
        self.__bst.insert(x)

    def getRankOfNumber(self, x):
        return self.__bst.getRank(x)


class Node:
    def __init__(self, num):
        self.__value = num
        self.__right = None
        self.__left = None
        self.__below = 0

    def getBelow(self):
        return self.__below

    def setBelow(self, x):
        """sets below to x"""
        self.__below = x

    def incrementBelow(self):
        self.__below += 1

    def get(self):
        return self.__value

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self, x):
        self.__right = x

    def setLeft(self, x):
        self.__left = x


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(x):
        """Inserts x into the bst"""
        currNode = self.__root
        prevNode = self.__root
        while currNode != None:
            prevNode = currNode
            if x > currNode.get():
                currNode = currNode.getRight()
            else:
                currNode = currNode.getLeft()
        if prevNode != None:
            prevNode

    def getRank(x):
        return getRankHelper(self.__root, x)


    def getRankHelper(node, x):
        while node != None:
            if node.getValue() == x:
                # see if any to the right of it, and return
                while node.getRight().getValue == x:
                    node = node.getRight()
                return node.getBelow()
            elif node.getValue() > x:
                return getRankHelper(node.getRight(), x)
            else:
                return getRankHelper(node.getLeft(), x)
        return -1 ## not found, so return -1
