'''Runge-Kutta Order Four Method'''
def frange(x, y, jump):
    tmplist = []
    while x <= y:
        tmplist.append(x)
        x += jump        
    return tmplist

def f(t, y):
    return -t * y + 4*t/y

def w(ti,wi, h):
    k1 = h*f(ti,wi)
    k2 = h*(f(ti+(h/2),wi+k1/2))
    k3 = h*(f(ti+(h/2),wi+k2/2))
    k4 = h*(f(ti+h, wi+k3))
    return wi + (1/6) * (k1+ 2* k2 + 2*k3 + k4)


a = 0.0
b = 1.0
h = 0.1
w0 = 1.0
print(frange(a+h, b, h)[-1])
for i in frange(a+h, b, h):
    #print(i)
    w0 = w(i-h, w0, h)
print("t{:.3f}: {}".format(b,w0))
w1 = w0
h = 0.01
w0 = 1.0
print(frange(a+h, b+h, h)[-1])
for i in frange(a+h, b+h, h):
    #print(i)
    w0 = w(i-h, w0, h)
print("t{:.3f}: {}".format(b,w0))
from math import exp
def y(t):
    return (4 - 3*exp(-(t**2)))**.5
diff1 = y(1.0)-w1
diff01 = y(1.0)-w0
print("frac. diff: " + str(diff1/diff01))
