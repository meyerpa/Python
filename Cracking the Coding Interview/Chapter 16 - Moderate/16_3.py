"""
16.3 Intersection
Given two straight line segments (represented as a start point and an end
point), compute the point of intersections, if any.
"""


from sys import maxint

def intersections(line1, line2):
    if line1 == line2:
        return maxint
    # parallel lines with different starting points do not intersect
    elif getSlope(line1) == getSlope(line2):
        return 0
    # gets x value for intersection of lines and checks that falls within
    # the line segmment
    intersectX = getIntersectX(line1, line2)
    # check if x value falls within each line segment
    if containsX(line1, intersectX) and containsX(line2, intersectX):
        return 1
    else:
        return 0

def getSlope(line):
    # assuming line contains two points
    x1, y1 = line.getP1()
    x2, y2 = line.getP2()
    slope = (y2 - y1) / (x2 - x1)
    return slope

def getIntercept(line):
    m = getSlope(line)
    x, y = line.getP1()
    # find y-intercept using y = mx + b -> b = mx - y
    b = m*x - y
    return b

def getIntersectX(line1, line2):
    m1 = getSlope(line1)
    m2 = getSlope(line2)
    b1 = getIntercept(line1)
    b2 = getIntercept(line2)
    # get x-value for intersection
    offsetY = b1 - b2
    intersectX = OffsetY / (m1 - m2)
    return intersectX

def containsX(line, x):
    """Returns whether or not the line contains the X value"""
    x1 = line.getP1()[0]
    x2 = line.getP2()[0]
    if (x1 > x and x2 < x) or (x1 < x and x2 > x):
        return True
    else:
        return False
