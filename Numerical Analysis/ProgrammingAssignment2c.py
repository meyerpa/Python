# Composite Trapezoid Rule

from math import log, pi
def f(x):
    #return 1/x
    return 5 / (1 + x**4)

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def compTrap(data):
    h = abs(data[0]-data[-1]) / len(data)
    summ = f(data[0]) + f(data[-1])
    for i in range(len(data)-2):
        summ += 2*f(data[i+1])
    return h * summ

def trap(start, end):
    h = end- start
    summ = f(start) + f(end)
    return h/2 * summ

a = 1.0
b = 2.0
h = b-a
levels = 5
epsilon = 10**-5
R11 = compTrap([a, b])
R = [[R11]]
for i in range(levels-1):
    R[0].append(.5*(R[0][-1] + h * sum([f(x) for x in list(frange(a+(h/2), b, h))])))
    h /= 2
for i in range(2, levels+1):
    R.append([])
    for j in range(levels-i+1):
        R[i-1].append((4**(i-1)*R[i-2][j+1] - R[i-2][j])/ (4**(i-1)-1))
print(R)
print("Romberg integration took R[" +str(levels)+"]["+str(levels)+"] to get {:.5f}".format(R[-1][-1]))
