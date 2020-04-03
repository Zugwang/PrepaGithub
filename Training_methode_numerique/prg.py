from matplotlib.pyplot import plot, show, grid
from numpy import linspace, cos, sin
#from math import cos

def methode_des_trapeze(f,a,b,n):
    p = (b-a)/n
    integrale = (f(b)-f(a))/2
    for i in range(n):
        integrale += f(a+i*p)
    return integrale*p
"""
g =lambda x: x
gp = methode_des_trapeze(g,1,10,10**7)
a = 0.5
for i in range(10):
    a += 0.5 + i

print(a)

x = linspace(0,30, 200)

plot(x,g(x))
print(gp)
#plot(x,gp(x))"""


def dichotomie(f,a,b,p):
    fa,fb = f(a),f(b)
    assert a < b and fa*fb < 0

    while b-a > p:
        m = (b+a)/2
        fm = f(m)

        if fm*fa < 0:
            b,fb = m,fm
        else:
            a,fa = m,fm
    return (b+a)/2
"""
f = lambda x: +x - 1
x = linspace(-10,10, 200)
x0 = dichotomie(f,-10,10,10e-10)
plot(x,f(x))
print(x0)
plot(x0,0,"ro")
"""

def newton(f,fp,x,epsilon):
    t = x+2*epsilon
    a = 0

    print(a,t,x)
    while abs(t-x) > epsilon:
        a += 1
        t = x
        x = x-f(x)/fp(x)
        print(a," t= ",t," x= ",x)
    return x
"""
f = lambda x: 2*x - 6
fp = lambda x: 2
x = linspace(-10,10, 200)
x0 = newton(f,fp,10,10e-10)
plot(x,f(x))
print(x0)
grid()
plot(x0,0,"ro")
"""



"""
h = 10**-4

f = lambda x:cos(x)
fp = lambda x0:( f(x0+h) - f(x0-h) ) / (2*h)
x = linspace(0,30, 200)
y = f(x)
yp = fp(x)
oui = -sin(x)

plot(x,oui)
plot(x,yp)
plot(x,y)"""







show()
