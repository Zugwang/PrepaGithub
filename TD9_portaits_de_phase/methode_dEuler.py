from matplotlib.pyplot import plot, show
from random import random
from math import *

def trace_graphe(f,a,b,pas):
    x = []
    y = []
    while a < b:
        x.append(a)
        y.append(f(a))
        a += pas

    plot(x,y,"ro")
    show()

def aleatoire():
    x = []
    y = []

    for i in range(50): x.append(random()*10)
    for i in range(50): y.append(random()*10)
    plot(x,y,"ro")
    show()


def euler(F, a, b, y0, n):
    listeTemps = [a]
    listeY = [y0]
    h = (b-a)/(n-1)
    for i in range(1,n):
        listeY.append(listeY[-1] + F(listeTemps[-1],listeY[-1]) * h)
        listeTemps.append(listeTemps[-1]+h)
    return listeTemps, listeY

def somme_listes(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

def produit_liste_scalaire(list, reel):
    rep = []
    for i in range(len(list)):
        rep.append( list[i] * reel )
    return rep

def euler_vectorielle(F, a, b, y0, n):
    listeTemps = [a]
    listeY = [y0]
    h = (b-a)/(n-1)
    for i in range(1,n):
        deltaY = produit_liste_scalaire(F(listeTemps[-1], listeY[-1]), h)
        listeY.append(somme_listes(listeY[-1], deltaY))
        listeTemps.append(listeTemps[-1] + h)
    return listeTemps,listeY
#6

def euler_vectorielle_CI(F, a, b, tableau_CI, n):
    rep = []
    for i in range(len(tableau_CI)):
        listeTemps = [a]
        listeY = [tableau_CI[i]]
        h = (b-a)/(n-1)
        for i in range(1,n):
            deltaY = produit_liste_scalaire(F(listeTemps[-1], listeY[-1]), h)
            listeY.append(somme_listes(listeY[-1], deltaY))
            listeTemps.append(listeTemps[-1] + h)
        rep.append(listeY)
    return rep,listeTemps

def question6(F):
    A = [ [-1,-1], [-1,1], [1,-1], [1,1] ]
    for i in range(len(A)):
        T,U = euler_vectorielle(F, 0, 10, A[i], 1000)
        U0 = []
        for i in range(len(U)): U0.append(U[i][0])
        U1 = []
        for i in range(len(U)): U1.append(U[i][1])
        plot(U0, U1)
    show()

def question6_9():
    F = lambda t,u: [ u[0]+3*u[1], -3*u[0] + u[1] ]
    A = [ [-1,-1], [-1,1], [1,-1], [1,1] ]


#t,y = euler(lambda t,y: -2*t*y,0,5,1,10000)


#T,U = euler_vectorielle(F, 0, 10, [1,1], 1000)

F = lambda t,u: [ u[0]+3*u[1], -3*u[0] + u[1] ]

G = lambda t,u : [ u[1], (-6.28/5)*u[1] - 39.42*sin(u[0]) ]

question6(G)


"""
T,U = euler_vectorielle(G, 0, 10, 1, 1000)

plot(T,U)
show()



F = lambda t,u: [ u[0]+3*u[1], -3*u[0] + u[1] ]

U0 = []
for i in range(len(U)): U0.append(U[i][0])
U1 = []
for i in range(len(U)): U1.append(U[i][1])
plot(U0, U1)

show()

"""
#trace_graphe(lambda x:x**2, 3, 10000, 1)

#aleatoire()
