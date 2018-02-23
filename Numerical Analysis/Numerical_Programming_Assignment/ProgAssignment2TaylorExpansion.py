from __future__ import print_function
from sympy import *
from math import factorial
import numpy as np
import matplotlib.pyplot as plt

def maximum(funct, start, end):
    functderivative = diff(funct, x)
    zeros = solve(functderivative,x)
    zeros = [zero for zero in zeros if start<zero<end]
    tmpmax = funct.subs(x, start)
    if funct.subs(x, end) > tmpmax:
        tmpmax = funct.subs(x, end)
    for num in zeros:
        if funct.subs(x, num) > tmpmax:
            tmpmax = funct.subs(x, num)
    return tmpmax

x = symbols("x") # define x to be a symbol
#functions and derivatives
f = ln(x)
fprime1 = diff(ln(x), x)
fprime2 = diff(fprime1, x)
fprime3 = diff(fprime2, x)
fprime4 = diff(fprime3, x)
fprime5 = diff(fprime4, x)
fprime6 = diff(fprime5, x)

# Taylor Series approximations of ln(x)
P0 = f.subs(x, 1)
P1 = f + fprime1*(x-1)
P2 = P1 + fprime2* (x-1)**2 /factorial(2)
P3 = P2 + fprime3* (x-1)**3 /factorial(3)
P4 = P3 + fprime4* (x-1)**4 /factorial(4)
P5 = P4 + fprime5* (x-1)**5 /factorial(5)
print("P0(x) = " + str(P0))
print("P1(x) = " + str(P1))
print("P2(x) = " + str(P2))
print("P3(x) = " + str(P3))
print("P4(x) = " + str(P4))
print("P5(x) = " + str(P5))

#print approximations and errors
print("P0(1.5) = " + str(P0.subs(x, 1.5)), end=" ")
print("with maximum error: " + str(abs(maximum(fprime1, 1, 1.5)*(1.5-1)**1/factorial(1))))
print("P1(1.5) = " + str(P1.subs(x, 1.5)), end=" ")
print("with maximum error: " + str(abs(maximum(fprime2, 1, 1.5)*(1.5-1)**2/factorial(2))))
print("P2(1.5) = " + str(P2.subs(x, 1.5)), end=" ")
print("with maximum error: " + str(abs(maximum(fprime3, 1, 1.5)*(1.5-1)**3/factorial(3))))
print("P3(1.5) = " + str(P3.subs(x, 1.5)), end=" ")
print("with maximum error: " + str(abs(maximum(fprime4, 1, 1.5)*(1.5-1)**4/factorial(4))))
print("P4(1.5) = " + str(P4.subs(x, 1.5)), end=" ")
print("with maximum error: " + str(abs(maximum(fprime5, 1, 1.5)*(1.5-1)**5/factorial(5))))
print("P5(1.5) = " + str(P5.subs(x, 1.5)), end=" ")
print("with maximum error: " + str(abs(maximum(fprime6, 1, 1.5)*(1.5-1)**6/factorial(6))))

# set axis labels
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.set_ylim([-4, 2])
# add in first line
x_1 = np.arange(0.001, 2, 0.00001);
f = lambdify( (x), P0 )
f = np.vectorize(f)
plt.plot(x_1, f(x_1), linewidth="2", color="red", label="P0")
f1 = lambdify( (x), P1 )
f1 = np.vectorize(f1)
plt.plot(x_1, f1(x_1), linewidth="1.5", color="blue", label="P1")
f2 = lambdify( (x), P2 )
f2 = np.vectorize(f2)
plt.plot(x_1, f2(x_1), linewidth="1.5", color="cyan", label="P2")
f3 = lambdify( (x), P3 )
f3 = np.vectorize(f3)
plt.plot(x_1, f3(x_1), linewidth="1.5", color="green", label="P3")
f4 = lambdify( (x), P4 )
f4 = np.vectorize(f4)
plt.plot(x_1, f4(x_1), linewidth="1.5", color="black", label="P4")
f5 = lambdify( (x), P5 )
f5 = np.vectorize(f5)
plt.plot(x_1, f5(x_1), linewidth="1.5", color="magenta", label="P5")
# add legend
plt.legend(loc='best')
plt.title('Taylor Expansion for ln(x)')
plt.show()
