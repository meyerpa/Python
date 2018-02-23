"""
Description: Newton's method
"""
__author__ = "Paige Meyer"
__date__ = "09/12/2016"

def f(x):
    return ((12*1000)/x)*(1-(1+(x/12))**-360) - 135000
def fPrime(x):
    return (-(12000)/x**2)*(1-(1+(x/12))**-360) + ((12000)/x)*(1+30*(1+(x/12))**-361)

def newton(p0, tol):
    p = p0 - f(p0) / fPrime(p0)
    print(p)
    if abs(p - p0) <= tol:
        return 1
    else:
        return 1 + newton(p, tol)

def main():
    a = float(input("Please enter a starting number: "))
    b = float(input("Please enter an ending number: "))
    print("Final Answer: " + str(newton((a+b)/2, 10**-5)))

if __name__ == "__main__":
    main()
print("Program ended")
