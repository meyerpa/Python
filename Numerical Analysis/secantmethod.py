"""
Description: Secant method
"""

__author__ = "Paige Meyer"
__date__ = "09/12/2016"

from math import exp, cos,pi

##def funct(num):
##    return exp(num) + (2**-num) + (2 * cos(num)) - 6

##def funct(num):
##    return cos(num) - num

def funct(x):
    return (1 - (1+x)**-360) / 135
    
def secant(p0, p1, tol):
    q0 = funct(p0)
    q1 = funct(p1)
    p = p1 - q1*(p1 - p0) / (q1 - q0)
    if abs(p1 - p0) <= tol:
        return p
    else:
        print(p)
        return secant(p1, p, tol)

def main():
    print("Final Answer: " + str(secant(8, 9, 10**-2)))

if __name__ == "__main__":
    main()
print("Program ended")

