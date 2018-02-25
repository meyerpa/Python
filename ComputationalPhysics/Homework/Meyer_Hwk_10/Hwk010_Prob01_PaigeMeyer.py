# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:19:01 2017

@author: Paige
"""

import numpy as np
import matplotlib.pyplot as plt


def is_even(x):
    """Returns true if x is even, and False if x isn't.
    """
    if x % 2 == 0:
        return True
    else:
        return False


def vin(t):
    """Finds the input voltage at a certain time t.
    """
    result = -1     # default to have result to be negative 1
    if is_even(np.floor(2*t)):
        result = 1
    return result


def func(x, t):
    # Note: this accesses a variable not defined within the function,
    # a variable called RC
    dy_dt = (1/RC) * (vin(t)-x[0])
    return np.array([x[1], dy_dt])


def rk4(f, x0, t):
    """Returns Fourth Order Runge-Kutta Appoximation for derivative
    
    parameters
    ----------
    f : function pointer
        The pointer to the derivative
    x0 : Numpy array
        initial condition
    t : Numpy array
        Times would like to evaluate at. Assumes equal spacing.
        
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
        # step
        h = time - lasttime
        
        # values to sum later
        k1 = h * f(x, lasttime)
        k2 = h * f(x + (k1/2), lasttime + (h/2))
        k3 = h * f(x + (k2/2), lasttime + (h/2))
        k4 = h * f(x + k3, lasttime + h)
        
        # calculate next value using runge-kutta order 4 method
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
a = 0.0             # start time
b = 10.0            # end time
RC = 0.01           # time constant
h = RC / 10         # time step

# initial values
V_out0 = 0          # initial output
V_in0 = vin(a)      # initial input
times = np.arange(a, b, h)              # time array

# find vin
v_vin = np.vectorize(vin)
v_ins = v_vin(times)

# RC = 0.01
dV_out_dt0 = (1/RC) * (V_in0-V_out0)    # initial derivative
x_not = np.array([V_out0, dV_out_dt0])  # initial condition
rk4_0_01 = rk4(func, x_not, times)      # values

# RC = 0.1
RC = 0.1                                # RC change
dV_out_dt0 = (1/RC) * (V_in0-V_out0)    # initial derivative
x_not = np.array([V_out0, dV_out_dt0])  # initial condition
rk4_0_1 = rk4(func, x_not, times)       # values 

# RC = 1.0
RC = 1.0                                # RC change       
dV_out_dt0 = (1/RC) * (V_in0-V_out0)    # initial derivative
x_not = np.array([V_out0, dV_out_dt0])  # initial condition                       # RC change
rk4_1 = rk4(func, x_not, times)         # values 

# plotting 
plt.plot(times, v_ins, label="Vin")
plt.plot(times, rk4_0_01[:, 0], label="RC = 0.01")
plt.plot(times, rk4_0_1[:, 0], label="RC = 0.10")
plt.plot(times, rk4_1[:, 0], label="RC = 1.00")

# format plot
plt.legend()
plt.grid()
plt.title("Runge-Kutta Order Four")
plt.xlabel("Time")
plt.ylabel("Ouput Voltage")
plt.show()

"""Well... I must have calculated the voltage wrong somehow.
The low-ass filter should allow a wave that looks similar 
to a sawtooth wave, but that isn't what I'm seeing here.
If I used 

    dy_dt = (1/RC) * (vin(t)-x[0])
    return np.array([x[1], dy_dt])
    
within func, I get a sawtooth wave, but it is offset by 1.
I believe I'm calculating the derivative wrong, and I'm not quite
sure how to fix it. 

"""
