"""
16.13 Bisect Squares
Given two squares on a two-dimensional plane, find a line that would cut these
two squares in half. Assume that the top and bottom sides of the square run
parallel to the x-axis.
"""

# Note, each line must right through each square's center.

def findLine(square1, square2):
    """Return the line (string) that cuts square1 and square 2 in half."""
    # find center of square 1
    x1 = (square1.point1()[0] + square1.point2()[0]) / 2
    y1 = (square1.point1()[1] + square1.point2()[1]) / 2

    # find center of square 2
    x2 = (square2.point1()[0] + square2.point2()[0]) / 2
    y2 = (square2.point1()[1] + square2.point2()[1]) / 2

    # if x's are the same, vetical line
    if x1 == x2:
        if y1 == y2:
            return -1
        else:
            return "x = " + str(x1)

    # find line that runs through the centers
    # slope is rise over run (y2 -y1) / (x2 - x1)
    m = (y2 - y1) / (x2 - x1)

    # find y-intercept
    # y = mx + b -> b = y - mx
    b = y1 - (m * x2)

    return "y = " + str(m) + "x + " + str(b)
