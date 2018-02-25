'''
This program solves a three coupled first order DE of the form
  dx/dt=f(x,y,z,t) dy/dt=g(x,y,z,t), dz/dt=h(x,y,z,t)
using fourth-order Runge Kutta (RK4).
'''
import numpy as np
import matplotlib.pyplot as plt
from fourth_order_rk import rk4


# This defines the derivatives
def f(x, t, sigma=10, r=28, b=8/3):
    """
    Calculate the derivatives for the problem in the lab.

    Parameters
    ----------

    x : list or array
        The "positions" x0, x1, and x2 at which to calculate the derivatives.
    t : float
        Time at which to calculate the derivatives.
    sigma : int, optional
        Constant for Lorenz Equation, Optional. The Default is 10.
    r : int, optional
        Lorenz Equation constant. The default is 28.
    b : int, optional
        Lorenz Equation constant. The default is 8/3rds.

    Returns
    -------

    derivs : array
        The derivatives of x0, x1 and x2 as a numpy array.
    """
    dx0 = sigma * (x[1] - x[0])
    dx1 = r * x[0] - x[1] - x[0] * x[2]
    dx2 = x[0] * x[1] - b * x[2]

    derivs = np.array([dx0, dx1, dx2])
    return derivs


# These parameters specify the interval over which
# the calculations are to be done.
a = 0.
b = 50.
N = 10000

# This is the initial condition x0=x(a). Either list the dtype explicitly
# as float, as done below, or make the entries floating point numbers
# instead of integers.
x0 = np.array([0, 1, 0], dtype=float)

# Define the times we will be solving for x(t) at
t = np.linspace(a, b, num=N)

# This is the function call for the Runge Kutta routine
xvals = rk4(f, x0, t)
x0vals = xvals[:, 0]
x1vals = xvals[:, 1]
x2vals = xvals[:, 2]

# This takes the FFT of the data x[2] vs t
c = np.fft.rfft(x2vals)

# Plot the results

# Allow subplots' labels to show up without overlapping.
fig = plt.figure()
fig.set_tight_layout(True)

# Plot x0, x1, and x2 as functions of time
plt.subplot(3, 1, 1)
plt.plot(t, x0vals, color='r', label='x0')
plt.plot(t, x1vals, color='g', label='x1')
plt.plot(t, x2vals, color='b', label='x2')
plt.xlabel('Time')
plt.ylabel('x0,x1,x2')
plt.legend()

# Plot x0(t) versus x2(t)
plt.subplot(3, 1, 2)
plt.plot(x0vals, x2vals)
plt.xlabel('x0')
plt.ylabel('x2')

# format plot limits
xlo = 0                                 # lower x-axis
xhi = 5500                              # upper x-axis
ylo = 0                                 # lower y-axis
yhi = np.max((np.abs(c)**2)[1:])        # set y upper limit to be max.


# Plot the DFT of the x2(t) to examine periodicity (add the lines once
# you have computed the FFT)
# Plot the DFT of the x2(t) to examine periodicity
plt.subplot(3, 1, 3)
plt.axis([xlo, xhi, ylo, yhi])
plt.plot(np.abs(c)**2)
plt.xlabel('frequency (in terms of fundamental 1/' + str(b) + ')')
plt.ylabel('fft of x2')

plt.show()
