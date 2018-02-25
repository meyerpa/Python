'''
Code for plotting up the inverse hyperbolic sine of a variable
u without using the built-in function.
'''

import numpy as np
import matplotlib.pyplot as plt

def f(x, u):
    return np.sinh(x) - u


def fPrime(x):
    return -np.cosh(x)


def invsinh(u, tolerance=1e-3):
    # This function, when completed will compute the arcsinh(u) using
    # Newton's method to a tolerance of 1e-12 (unless overridden).
    
    # Set initial conditions for Newton's Method search for root of
    #      sinh(x) - u = 0
    # using the fact that (d/dx)sinh(x) = cosh(x)
    x = 0
    deltax = tolerance*10
    
    # Implement Newton's Method requiring delta = x' - x be less
    # than the tolerance before returning x.
    while (np.abs(deltax) > tolerance):
        deltax = f(x, u) / fPrime(x)
        x = x + deltax

    return x

# Set up an list of points from -5 to 5 and plot up the inverse tangent
# function.
upoints = np.linspace(-10, 10, 200)

# Create arrays to store our roots and the exact answers for the inverse
# hyperbolic sine that are the same size as the number of u values we are
# checking.
xpoints = np.zeros_like(upoints)
exact = np.zeros_like(upoints)

# We must call our invsinh function for each value of u because
# it has not be designed with array arithmetic in mind.
for n in range(upoints.size):
    xpoints[n] = invsinh(upoints[n])
    exact[n] = np.arcsinh(upoints[n])

plt.plot(upoints, xpoints, marker="o", color="blue", label="Newton's Method")
plt.plot(upoints, exact, linestyle="-", color="red", label="numpy arcsinh(u)")
plt.xlabel("u")
plt.ylabel("arcsinh(u)")
plt.legend(loc='upper left')
plt.show()
