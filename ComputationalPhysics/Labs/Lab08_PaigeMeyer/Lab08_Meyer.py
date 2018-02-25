# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:09:46 2017

@author: Paige Meyer
@description Code for finding the roots of functions using the 
secant method. This also approximates the maximum wavelength times
temperature given by Wien's displacement law.
"""

import numpy as np
import matplotlib.pyplot as plt


def funct(x):
    # Note this function has three roots at
    # -1, (2)^.5, and -(2)^.5
    return np.exp(-x**2) * (x**3 + x**2 - 2*x - 2)


def wiens_law(x):
    return np.exp(x) * (x - 5) + 5


def secant_solver(f, x0, x1, tol=1e-15, n_max=100, n=1):
    # print("x0", x0)
    # print("x1", x1)
    f0 = f(x0)
    f1 = f(x1)
    # ensure will not have divide by zero error
    # print("tol:", tol)
    # print("f1", f1)
    #print("f0", f0)
    #print("abs", np.abs(f1-f0))
    if np.abs(f1-f0) < tol:
        delta = np.abs(x1 - x0)             # difference
        return (n, x1, delta)
    
    # compute new x
    x = x1 - f1*(x1 - x0) / (f1 - f0)
    delta = np.abs(x - x1)                  # difference
    
    # if new x is within tolerence, return otherwise do again
    if delta < tol or n > n_max:
        return (n, x, delta)
    else:
        return secant_solver(f, x1, x, tol, n_max, n+1)

# Part 1 and Two 
print("e^(-x^2) * (x^3 + x^2 - 2^x - 2)...")

# Set up an list of points from -10 to 10 and plot the function.
xpoints = np.linspace(-2, 3, 200)
ypoints = funct(xpoints)
plt.plot(xpoints, ypoints)
plt.grid()
plt.title("e^(-x^2) * (x^3 + x^2 - 2^x - 2)")
plt.ylim(-.5, .5)
plt.show()


# Secant Method
tol = 1e-5
a = 0
b = 1
max_times = 100
ans = secant_solver(funct, a, b, tol=10e-5, n_max = max_times)
print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
    + "with difference {0:.6f} ".format(ans[2]))


''' Part 2
Note that the roots are mentioned in comments in funct

To find root two called with a = 0 and b = 1 as shown below
    tol = 1e-5
    a = 0
    b= 1
    max_times = 100
    ans = secant_solver(funct, a, b, tol, max_times)
    print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
        + "with difference {0:.6f} ".format(ans[2]))
Output: 1 secant call(s) gave 1.41421356 as answer with difference 0.000000 
Program ended

    
To find negative root two called with a = -1.3 and b = -1.6 as shown below
    tol = 1e-5
    a = -1.3
    b = -1.6
    max_times = 100
    ans = secant_solver(funct, a, b, tol, max_times)
    print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
        + "with difference {0:.6f} ".format(ans[2]))
Output: 1 secant call(s) gave -1.41421356 as answer with difference 0.000000 
Program ended
    
To find negative one called with a = 0  and b = -0.8 as shown below
    tol = 1e-5
    a = 0
    b = -0.8
    max_times = 100
    ans = secant_solver(funct, a, b, tol, max_times)
    print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
        + "with difference {0:.6f} ".format(ans[2]))
Output: 1 secant call(s) gave -1.00000000 as answer with difference 0.000003 
Program ended

'''


# Part 3 - Wien's Law for Blackbody Radiation
print("Wien's Law in Part 3...")

x = np.linspace(0, 6, 400)
y = wiens_law(x)
plt.plot(x, y)
plt.grid()
plt.title("Wien's Law Function")
plt.show()

# Secant Method

tol = 1e-5
max_times = 100

# a = 5, b = 6
a = 5
b = 6
ans = secant_solver(wiens_law, a, b, tol, max_times)
print("a = {}, b = {}".format(a, b))
print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
    + "with difference {0:.6f} ".format(ans[2]))

# a = 4, b = 3
a = 4
b = 5
ans = secant_solver(wiens_law, a, b, tol, max_times)
print("a = {}, b = {}".format(a, b))
print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
    + "with difference {0:.6f} ".format(ans[2]))

# a = 3.9, b = 4.1
# This doesn't find a root becuase there is a turning point near here
# The turning point is between 3.9 and 4, so the approximated slope
# is an incorrect representation, since the slope is approximately horizontal.
a = 3.9
b = 4.1
ans = secant_solver(wiens_law, a, b, tol, max_times)
print("a = {}, b = {}".format(a, b))
print("{0:} secant call(s) gave {1:.8f} as answer ".format(ans[0], ans[1])
    + "with difference {0:.6f} ".format(ans[2]))


# a = 4, b = 3
a = 4
b = 5
ans = secant_solver(wiens_law, a, b, tol, max_times)
x = ans[1]
# Know x = hc / (lambda * k_B * T)
# so lambda*T = hc / (x * k_B) = 0.014388 K / x
lambda_T = 1.4388e-5 / x    # In Kelvin
print("\nlambda * T: ", lambda_T)
# this reult is very close to the expect 2.8977729 * 1-^-3 values
# which suggests this code is similar
