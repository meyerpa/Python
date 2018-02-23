'''Free Cubic Spline'''
from __future__ import print_function
import math

def f(x):
    return math.log(x)
def fprime(x):
    return 1/x

x = [1.0, (4.0/3), (5.0/3), 2.0]
y = [f(num) for num in x]
n = len(x) - 1

n= len(x)
b = [0]*n
c = [0]*n
d = [0]*n
h = [1]*n
for i in range(n-1):
    h[i] = x[i+1] - x[i]

alpha = [0]*n
alpha[0] = 3*(y[1]-y[0])/h[0] - 3* FPO
for i in range(1, n-1):
    num = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])
    alpha[i] = num
# need to tri-diagonalize
l = [1]*n
u = [0]*n
z = [0]*n
c = [0]*n
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
for i in range(len(x)-1):
    print(str(y[i])+ " + " + str(b[i]) + "x + " + str(c[i])+ "x^2 + " + str(d[i])+ "x^3" , end=",\t")
    print("for " + str(x[i]) + " < x < " + str(x[i+1])) 

