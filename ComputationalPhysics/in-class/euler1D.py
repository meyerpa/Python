"""
Code for solving a first order differential equation using Euler's Method in 1D.

We are trying to design this code using arrays in the euler routine so that
it can more easily handle multi-dimensional data.
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def func(x, t):
    # This is dx/dt = -x
    return -x**3 + np.sin(t)


def euler(f, x0, t):
    # Pass in the function for dx/dt, the initial value, x0, and an array
    # of times and return an array of x values for those times.
    x = x0        # track the current value of x
    xlist = x  # Create an array of x values at all times
    lasttime = t[0]

    for time in t[1:]:
        # This loop needs to compute h based on time and lasttime
        # (since it isn't automatically "known" to the euler function)

        # Using the Euler method, compute the new x based on derivative
        # at lastime.  WARNING: For future compatibility with 'x' being
        # potentially an array, please use x=x + stuff format instead of
        # x += stuff format.
        h = time - lasttime
        x = x + f(x, time) * h

        # Add x to the xlist array.  To do this, we have to over-write the
        # xlist array using vstack (which stacks the arrays in 'rows' or
        # vertical stacks).  Since x is a scalar, we have to
        # convert it into an array first, and then 'stack' it.
        xlist = np.vstack((xlist, x))
        lasttime = time

        # Update the lasttime variable so it is ready for the next loop.

    return xlist


# Set up limits and step number
a = 0.
b = 10.
N = 1000
h = (b - a) / N

# Initial condition (PLEASE DEFINE xa as an array with one element for now)
xa = np.array([0.])    # x(a) = 1.
t = np.arange(a, b, h)
x = euler(func, xa, t)

# ADD THE COMMANDS NEEDED TO PLOT THE FUNCTION x(t) [INCLUDE PROPER LABELS]
plt.plot(t, x)
plt.grid()
plt.title("Euler's Method")
plt.show()

# THESE COMMANDS ARE FOR 3D PLOTTING TO BE USED LATER, DO NOT ACTIVATE UNTIL
# TOLD TO. :)
# Make a 3D scatter plot to show the position versus time
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(t, x[:, 0], x[:, 1], c='g', marker='o')
# ax.set_xlabel('t')
# ax.set_ylabel('x(t)')
# ax.set_zlabel('y(t)')
# plt.show()      # This plot is interactive, try moving it around by dragging it.
