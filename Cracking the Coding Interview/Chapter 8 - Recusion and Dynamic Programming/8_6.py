"""
8.6 Towers of Hanoi
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks
of different sizes which can slide onto any tower. The puzzle starts with
disks sorted in ascending order of size from top to bottom. (i.e. each disk
sits on top of an even larger one). You have the following constraints:
    (1) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto another tower.
    (3) A disk cannot be placed on top of a smaller dis.
Write a program to move the disks from the first tower to the last using stacks.
"""

def solveHanoi(stackOne, stackTwo, stackThree):
    """Will move disks from stackOne two stackThree"""
    if len(stackOne) == 0 and len(stackTwo) == 0:
        return True
    if len(stackOne) != 0:
        if (stackOne.peek() < stackTwo.peek() or len(stackTwo) == 0):
            disk = stackOne.pop()
            stackTwo.push(disk) # put disk on stackTwo
        if (stackOne.peek() > stackTwo.peek()):
            if stackTwo.peek() < stackThree.peek():
                stackThree.append(stackTwo.pop())
