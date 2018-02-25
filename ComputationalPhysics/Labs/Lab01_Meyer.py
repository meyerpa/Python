# -*- coding: utf-8 -*-

"""
__author__="Paige Meyer"
__date__="01/11/2017"
__version__=1.1
PHYS 350 - Computational Physics
Lab 1
Description: This lab creates a random walk and graphs the walk.
"""

from numpy import empty,absolute
from random import random
from matplotlib.pyplot import plot, xlim, ylim, show, title

'''
----------------------------------------------------
Part 1
----------------------------------------------------
'''

step_size = 1           # size of each step
n_timesteps = 100      # number of steps

def coord(step):
    """Return positive or negative step 50 percent change each
    
    Randomly returns either a negative step 50% of the time
    or a positive step the other 50% of the time.
    
    Parameters
    ----------
    step : double, float, or integer of the step size
        
    """
    # return negative 1/2 time
    if random() < 0.5:
        return -1*step
    # return positve the other 1/2 time
    else:
        return step


def random_walk(x_pos, y_pos, step_size=1, start_x=0.0, start_y=0.0):
    """Creates random walk with in x and y with step_size
    
    Returns two numpy arrays containting floats one for the 
    x-coordinate and the other for the y-coordinate with 
    random walks. Each walk consists of steps filling 
    both numpy arrays with steps of step_size. Defaulted
    to start at (0,0), but can be changed through parameters.
    
    Parameters
    ----------
    x_pos : numpy array 
        Values in array are overwitten with each step in the 
            x-direction
    y_pos : numpy array
        Values in array are overwitten with each step in the
            y-direction
    step_size : int, float, or double
        Indicates the size of the step for the walk
    start_x : float or double
        Starting x-value of the walk
    start_y : float or double
        Starting y-value of the walk
    
    """
    # ensure will not run into index error
    assert(x_pos.size==y_pos.size)
    
    current_x_pos = start_x
    current_y_pos = start_y
    
    # set intial positions in array
    x_pos[0] = current_x_pos
    y_pos[0] = current_y_pos
    
    # loop through each value stepping forward by step_size
    # or backward 50% of the time and write to the arrays.
    for i in range(1,x_pos.size):
        current_x_pos += coord(step_size)
        current_y_pos += coord(step_size)
        x_pos[i] = current_x_pos
        y_pos[i] = current_y_pos
    return (x_pos,y_pos)
    

# Create empty arrays to store positions
x_pos = empty(n_timesteps)
y_pos = empty(n_timesteps)
# call random walk
x_pos,y_pos = random_walk(x_pos, y_pos, step_size)

# print final x and y positions
print("Ending x and y positions: ({}, {})".format(x_pos[-1], y_pos[-1]))

'''
----------------------------------------------------
Part 2 - Questions
----------------------------------------------------
1. Ensure the first element in the both arrays are 0, since that is
     the origin. This can be done by typing in x_pos[0] and y_pos[0]
     to the IPython console, or opening Variable Explorer and looking
     under the value of x_pos and y_pos to see that it displays 
     array([0., ...]).
2. The plot does look as expected. It jumps up or down by one each
    time, and at times it has continued positive or negative step 
    size.
3. A new window pops up where individual cells in the array are 
    able to be clicked and edited
4. I went to the IPython subwindow and typed in y_pos[49], since 
    it is zero-based.
5. Could type y_pos[40] = 1000 in the IPython console or in the 
    variable explorer window right clicked an array then clicked
    edit then select a cell and change the value within the cell.
'''

'''
----------------------------------------------------
Part 3
----------------------------------------------------
'''

plot(x_pos,y_pos)               # plot walk
plot(x_pos[-1],y_pos[-1], "ro") # plot endpoint
# center plot on origin and scale to positions
max_x = max(absolute(x_pos))    # maximum x value
max_y = max(absolute(y_pos))    # maximum y value
xlim(-1*max_x, max_x)           # change x limit
ylim(-1*max_y, max_y)           # change y limit
title("One random walk")
show()

'''
----------------------------------------------------
Extra credit 1- Second random walk
----------------------------------------------------
Note:I'm using the walk from the previous sections as the
first walk
'''

# Create new empty arrays to store second walker positions
x_pos2 = empty(n_timesteps)
y_pos2 = empty(n_timesteps)
# call random walk
x_pos2,y_pos2 = random_walk(x_pos2, y_pos2, step_size)

plot(x_pos,y_pos)                   # plot first walk
plot(x_pos[-1],y_pos[-1], "ro")     # plot first endpoint
plot(x_pos2,y_pos2, "m")            # plot second walk
plot(x_pos2[-1],y_pos2[-1], "ro")   # plot second endpoint

# update maximums if the new one is larger
new_x_max = max(absolute(x_pos2))   # maximum x value 2
if new_x_max > max_x:
    max_x = new_x_max
new_y_max = max(absolute(y_pos2))   # maximum x value 2
if new_y_max > max_y:
    max_y = new_y_max
    
# set limits
xlim(-1*max_x, max_x)               # change x limit
ylim(-1*max_y, max_y)               # change y limit

title("Two random walks")
show()

'''
----------------------------------------------------
Extra Credit 2
----------------------------------------------------
Question:
    Stop the program immediate after you create the empty arrays
    and comment on the values stored in thsoe arrays right after 
    they are created. 
---------------------------------------------------
Answer:
    This can be done by setting a breakpoint. To set a breakpoint,
    navigate the cursor to the line you want the breakpoint.
    Click Debug->Set/Clear Breakpoint. This sents an unconditional
    breakpoint. A conditional breakpoint can be done similarly, but
    clicking Debug->Set/Edit conditional breakpoint then a 
    condtional to break in the code can by typed in such as
    max_x < 0. Then, the breakpoint will execute only when 
    max_x is negative.
'''

