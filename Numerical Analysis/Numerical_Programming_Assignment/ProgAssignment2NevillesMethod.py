'''
Neville's Method
'''
from __future__ import print_function
from math import log
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def funct(x):
    return log(x)

x = [1, 1.2, 1.4, 1.6, 1.8, 2.0]
y = [funct(val) for val in x]
value = 1.5
P = y
Q = np.zeros((len(x), len(x)))
Q[:, 0] = x
Q[:, 0] = y
for i in range(len(x)):
    for j in range(1,i+1):
        Q[i,j] = ((value-x[i-j])*Q[i,j-1] - (value-x[i])*Q[i-1,j-1])/(x[i]-x[i-j])
print("Q: \n" + str(Q), end="\n\n")

# set up graph
# set axis labels
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
colors = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'black']
x_range = np.arange(0.001, 2, 0.000001);
x_sym = symbols("x")
ax.set_ylim([-1, 5])

#output polynomials, values, and errors
for j in range(len(x)):
    P = 0
    print("P" + str(range(j+1)) + "(x): ", end=" ")
    num = 0
    for i in range(j+1):
        if i!= j:
            print(str(Q[i,i]) + "(x-1)**" + str(i), end=" + ")
        else:
            print(str(Q[i,i]) + "(x-1)**" + str(i))
        P += Q[i,i] * (x_sym)**i
        num += Q[i,i]*(1.5-1)**i
    print("P" + str(range(j+1)) + "(1.5): " + str(num), end=" ")
    print("with error: " +str(abs(num-log(1.5))))
    f = lambdify( (x_sym), P )
    f = np.vectorize(f)
    plt.plot(x_range, f(x_range), linewidth="2", color=colors[i], label="P"+str(range(j+1))+"(x)")
plt.legend(loc='best')
plt.title("Neville's Approximation for ln(x)")
plt.show()
