# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 20:12:53 2017

@author: Paige Meyer

Desciption: Finds the position in an oscillating
pendulum.
"""

import numpy as np
import matplotlib.pyplot as plt


def func(x, t, Omega=1.0, C=1.0, l=1.0):
    """Returns the derivative of the function
    
    parameters
    ---------
    x : numpy array
        Current values, first being the value, second is derivative.
    t : float
        The time
    Omega : float, optional
        The constant driving the angular speed. The default is 1.0
    C : float, optional
        The constant ___. The default is 1.0
    l : float, optional
        The length of the pendulum. the default is 1.
        
    returns
    -------
    deriv : numpy array
        The derivative of the current values based on 
        d^2Theta / dt^2 = -(g/l)*sin(Theta) + C*cos(Theta)*sin(Omega*t)
    """
    theta = x[0]        # theta is the current value
    g = -9.8            # Force of gravity
    # calculate the second deriviative
    d2Theta_dt2 = - (g/l)*np.sin(theta) + C*np.cos(theta)*np.sin(Omega*t)
    return np.array([x[1], d2Theta_dt2])


def diff(f, x, initial = np.array([]), **kwargs):
    """Retuns the difference in Energy at the boundary condition 
    
    Note: times should define an array of times called times,
    and a function that gives the derivative called func.  
    """
    values = rk4(f, initial, x)
    return values[-1, 0]


def secant_solver(f, x0, x1, tol=1e-15, n_max=100, n=1, **kwargs):
    """Finds root (0) of function 0 with initial 
    """
    f0 = f(x0, **kwargs)
    f1 = f(x1, **kwargs)
    # ensure will not have divide by zero error
    if np.abs(f1-f0) < tol:
        delta = np.abs(x1 - x0)             # difference
        print("Returning early", np.abs(f1-f0))
        return (n, x1, delta)
    
    # compute new x
    x = x1 - f1*(x1 - x0) / (f1 - f0)
    delta = np.abs(x - x1)                  # difference
    
    # if new x is within tolerence, return otherwise do again
    if delta < tol or n > n_max:
        return (n, x, delta)
    else:
        return secant_solver(f, x1, x, tol, n_max, n+1, **kwargs)

    
def rk4(f, x0, t, **kwargs):
    """Returns Fourth Order Runge-Kutta Appoximation for derivative
    
    parameters
    ----------
    f : function pointer
        The pointer to the derivative
    x0 : Numpy array
        initial condition
    t : Numpy array
        Times would like to evaluate at. Assumes equal spacing.
    **kwargs : keyword arguments
        The keyword aguments needed for the function f
        
    returns
    -------
    xlist: numpy array
        Fourth Order Runge-Kutta numerical approximation for derivative.
    """
    # Pass in the function for dx/dt, the initial value, x0, and an array
    # of times and return an array of x values for those times.
    x = x0        # track the current value of x
    xlist = x  # Create an array of x values at all times
    lasttime = t[0]

    for time in t[1:]:
        # This loop needs to compute h based on time and lasttime
        # (since it isn't automatically "known" to the euler function)
        h = time - lasttime
        k1 = h * f(x, lasttime, **kwargs)
        k2 = h * f(x + (k1/2), lasttime + (h/2), **kwargs)
        k3 = h * f(x + (k2/2), lasttime + (h/2), **kwargs)
        k4 = h * f(x + k3, lasttime + h, **kwargs)
        x = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        # Add x to the xlist array.  To do this, we have to over-write the
        # xlist array using vstack (which stacks the arrays in 'rows' or
        # vertical stacks).  Since x is a scalar, we have to
        # convert it into an array first, and then 'stack' it.
        xlist = np.vstack((xlist, x))

        # Update the lasttime variable so it is ready for the next loop.
        lasttime = time

    return xlist

# Set up limits and step number
Omega0 = 0.0         # starting position
dOmega_dt = 0.0      # starting derivative
C = 2                # in 1/seconds^2
l = 0.10             # length in meters
Omega = 1e-14         # driving frequency in Hertz
a = 0.0              # start time in seconds
b = 100.0            # end time in seconds
N = 10000            # steps
h = (b - a) / N      # step size

# initial conditions
xa = np.array([Omega, dOmega_dt])
times = np.arange(a, b, h)
rk = rk4(func, xa, times, Omega=Omega, l=l, C=C)

# print final value
print("Final value", rk[-1, 0])

# plotting commands part a
plt.plot(times, rk[:, 0], label="rk4")
plt.title("Omega={:}, l={:}, and C={:}".format(Omega, l, C))
plt.ylabel("height (meters)")
plt.xlabel("time (seconds)")
plt.legend()
plt.show()


# Part b
C = 2                # in 1/seconds^2
l = 0.10             # length in meters
Omega = 50           # driving frequency in Hertz

# initial conditions
xa = np.array([Omega, dOmega_dt])
rk = rk4(func, xa, times, Omega=Omega, l=l, C=C)

# print final value
print("Final value", rk[-1, 0])

# plotting commands part a
plt.plot(times, rk[:, 0], label="rk4")
plt.title("Omega={:}, l={:}, and C={:}".format(Omega, l, C))
plt.ylabel("height (meters)")
plt.xlabel("time (seconds)")
plt.legend()
plt.show()
