"""
Description: Fixed Point Iteration method
"""
__author__ = "Paige Meyer"
__date__ = "09/12/2016"

from math import exp

##def funct(x):
##    return (2 - exp(x) + x**2) / 3

##def funct(x):
##    return (5/(x**2)) + 2
def funct(x):
    return ((12*1000)/x)*(1-(1+(x/12))**-360) - 135000

def fixedPointIteration(p0, tol):
    p = funct(p0)
    if abs(p - p0) <= tol:
        return 1
    else:
        print(p)
        return 1 + fixedPointIteration(p, tol)

def main():
    a = float(input("Please enter a starting number: "))
    b = float(input("Please enter an ending number: "))
    print("Final Answer: " + str(fixedPointIteration((a+b)/2, 10**-5)))

if __name__ == "__main__":
    main()
    print(funct(.05))
    print(funct(.10))
    print(funct(.08))
print("Program ended")
