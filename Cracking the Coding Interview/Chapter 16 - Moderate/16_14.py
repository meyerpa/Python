"""
16.14 Best Line
Given a two-dimensional graph with points on it, find a line which passes
the most number of points.
"""

allLines = dict()

def bestLine(points):
    """Returns the line intersecting the most points."""
    if len(points) < 2:
        return -1
    for i in range(len(points)):
        for j in range(i, len(points)):
            # find line connecting the two points
            line = connect(points[i], points[2])
            # if the line exists, add a point to the line, if it doens't
            # have two points to the line
            if line.getInfo() in allLines:
                allLines[line.getInfo()] += 1
    # iterate through all the lines to find the maximum
    maxLine = None
    maxCount = 0
    for line, count in allLines.items():
        if count > maxCount:
            maxCount = count        # update maximum counter
            maxLine = line          # update maximum line
    return maxLine


def connect(p1, p2):
    """Return the line connecting p1 and p1. Returns -1 if more than one line
    exists."""
    # check if p1 == p2
    if p1 == p2:
        return -1
    # check that x's are not the same
    if p1.x() == p2.x():
        return Line(sys.maxsize, p1.x())
    # find slope
    m = (p2.y() - p1.y()) / (p2.x() - p1.x())
    # find intercept y = mx + b -> b = y - mx
    b = p1.y() - (m * p1.x())

    # create and return a line
    return Line(m, b)

class Line:
    def __init__(self, slope, intercept):
        self.__m = slope
        self.__b = intercept

    def getSlope(self):
        return self.__m

    def getIntercept(self):
        return self.__b

    def getInfo(self):
        """Return tuple of slope and intercept."""
        return (self.getSlope(), self.getIntercept())
