import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.cos(x)


def derivative(x, y):
    # x : np array
    # y : np array
    # Compute forward difference estimate for the derivative for array of N
    # points and values of the function at those points.  The two 1-D arrays
    # must be the same size.
    dy = y[1:] - y[:-1]             # compute y[i+1] - y[i] difference
    dx = x[1:]-x[:-1]               # compute x[i+1] - x[i] difference
    return dy / dx


# Set the step size based on limits
a = 0
b = 4 * np.pi
N = 100
h = (b - a) / N

x = np.arange(a, b, h)
y = f(x)          # Since we are using numpy, this will compute as array
yPrime = derivative(x, y, N)  # yPrime will have N-1 elements

# Add plotting commands
plt.plot(x[0:N - 1], y[0:N - 1], 'r-', label="y(x) = cos(x)")
plt.plot(x[0:N - 1], yPrime[0:N - 1], 'b*', label="dydx")

sin = np.sin(x)
plt.plot(x[:N-1], -sin[:N-1], color="m", label="-sin(x)")

plt.legend()
plt.xlabel("x")
plt.ylabel("y(x) and dy/dx")
plt.show()
