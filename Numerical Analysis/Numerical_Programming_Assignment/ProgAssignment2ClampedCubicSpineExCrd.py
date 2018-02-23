'''Clamped Cubic Spline'''
from __future__ import print_function
import math

def f(x):
    return math.log(x)
def fprime(x):
    return 1/x
x = [1.0, (4.0/3), (5.0/3), 2.0]
n = len(x)-1
y = [f(num) for num in x]
FPO = fprime(x[0]) # fprime(x_0)
FPN = fprime(x[n]) # fprime(x_n)
n = len(x)
b = [0]*n; c = [0]*n; d = [0]*n; h = [1]*n
for i in range(n-1):
    h[i] = x[i+1] - x[i]

alpha = [0]*n
alpha[0] = 3*(y[1]-y[0])/h[0] - 3* FPO
alpha[n-1] = 3*FPN - 3*(y[n-1] - y[n-2])/h[n-1]
for i in range(1, n-1):
    alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])
# need to tri-diagonalize
l = [1]*n
u = [0]*n
z = [0]*n
c = [0]*n
l[0] = 2 * h[0]
u[0] = .5
z[0] = alpha[0]/l[0]

for i in range(1, n-1):
    l[i] = 2*(x[i+1] - x[i-1]) -h[i-1]*u[i-1]
    u[i] = h[i] / l[i]
    z[i] = (alpha[i] - (h[i]/l[i]))/l[i]

for i in range(1, n-1):
    l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*u[i-1]
    u[i] = h[i]/l[i]
    z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]
    
l[n-1] = 1
z[n-1] = 0
c[n-1] = 0
#calculate c, b, and d
for j in range(n-2, -1, -1):
    c[j] = z[j] - u[j]*c[j+1]
    b[j] = (y[j+1] - y[j])/h[j] - h[j]*(c[j+1]+2*c[j])/3
    d[j] = (c[j+1] - c[j])/(3*h[j])
#output
string= ""; value = 1.5
for i in range(len(x)-1):
    print(str(y[i])+ " + " + str(b[i]) + " (x-" + str(x[i]) + ") + " +
            str(c[i])+ " (x-" + str(x[i]) + ")**2 + " + str(d[i])+ " (x-" + str(x[i]) + ")**3" , end=",\t")
    print("for " + str(x[i]) + " < x < " + str(x[i+1]))
    if x[i] < value and value<= x[i+1]:
        string = "P("+str(value)+") = " + str(y[i]+ b[i] *(value -x[i]) + c[i]*(value- x[i])**2 + d[i]*(value-x[i])**3)
print(string)
