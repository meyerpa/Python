"""
Description: False Position method
"""

__author__ = "Paige Meyer"
__date__ = "09/12/2016"

from math import cos,pi

def funct(x):
    return cos(x) - x

def falsePosition(p0, p1, tol):
    q0 = funct(p0)
    q1 = funct(p1)
    p = p1 - q1*(p1 - p0) / (q1 - q0)
    q = funct(p)
    if q1*q < 0:
        p1 = p0
        q1 = q0
    print(p)
    if abs(p - p1) <= tol:
        return 2
    else:
        return 1 + falsePosition(p1, p, tol)

def main():
    print("Final Answer: " + str(falsePosition(.5, pi/4, 10**-5)))

if __name__ == "__main__":
    main()
print("Program ended")
