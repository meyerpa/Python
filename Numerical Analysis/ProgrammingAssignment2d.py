# Adaptive Quadrature with Simpson's Rule
def f(x):
    return 5 / (1 + x**4)

def simp(start, end):
    simp = float(end-start)/6 * (f(start) + (4 * f(float(start+end)/2)) + f(end))
    return simp

def adaptiveQuad(a, b, epsilon, level = 1):
    Sab = simp(a, b)
    Sa = simp(a, float(a+b)/2)
    Sb = simp(float(a+b)/2, b)
    if abs(Sab - Sa - Sb) < 15* epsilon:
        print("Sab " + str(Sab) + " returned on level: " + str(level))
        return Sab
    else:
        return adaptiveQuad(a, (a+b)/2, epsilon/2, level+1) + \
                       adaptiveQuad((a+b)/2, b, epsilon/2, level+1)


a = 0.0
b = 1.0
ct = 1
epsilon = 10**-5
print("Final Answer " + "{:.5f}".format(adaptiveQuad(a, b, epsilon)))
