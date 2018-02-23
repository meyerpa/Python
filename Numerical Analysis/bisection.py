"""
Description: Bisection method
"""
__author__ = "Paige Meyer"
__date__ = "09/30/2016"

from math import log10

def f(x):
    return x**5 + 5 *(x**4) - 8 * (x**3)+5*(x**2)-11*x+7

def bisection(a, b, tol, n):
    print("x"+str(n)+ ": " + str((a+b)/2))
    if f((a+b)/2) == 0  or abs((b - a)/2) < tol:
        #ignore the line below, convoluted (just wanted certain decimal places)
        eval("print(\"x: %." + str(-int(log10(tol))) + "f\" % float((a+b)/2.0))")
        return 0
    else:
        if f((a+b)/2) < 0:
            a = (a+b)/2
        else:
            b = (a+b)/2
        return 1 + bisection(a, b, tol, n+1)

def main():
    a = float(input("Please enter a starting value of x: "))
    b = float(input("Please enter an ending value of x: "))
    if f(a)* f(b) > 0:
        a = float(input("Please enter a starting value of x: "))
        b = float(input("Please enter an ending value of x: "))
    #switch a and b based on postive or negative f(x) values
    if f(a) > 0:
        a,b = b,a
    print("Final Answer took: " + str(bisection(a, b, 10**-10, 0)) + " times")

if __name__ == "__main__":
    main()
print("Program ended")
