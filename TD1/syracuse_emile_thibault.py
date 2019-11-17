# -*- coding: utf-8 -*-
#from pylab import plot, show
#from matplotlib import pylab
from pylab import show, plot

def suite_syracuse(inputNumber):
    if inputNumber%2 ==  0:
        result = inputNumber/2
    else:
        result = (3 * inputNumber + 1)

    return result

def graphic(firstTerm, rangMax):
    u = firstTerm
    for i in range(rangMax):
        plot(i,u,"ro")
        u = suite_syracuse(u)
    show()

def longueur_de_vol(firstTerm):
    n = 0
    u = firstTerm
    while(u != 1):
        u = suite_syracuse(u)
        n += 1
    return n

def hauteur_de_vol(firstTerm):
    a = firstTerm
    u = firstTerm
    while(u != 1):
        u = suite_syracuse(u)
        if( a < u ):
            a = u
    return a

def le_plus_grand(entierMax,a_maximiser):
    if(a_maximiser ==  "hauteur"):
        maxK = 0
        for i in range(1,entierMax+1):
            k = hauteur_de_vol(i)
            if (maxK < k):
                maxI = i
                maxK = k
        return maxI
    elif(a_maximiser == "longueur"):
        maxK = 0
        for i in range(1,entierMax+1):
            k = longueur_de_vol(i)
            if (maxK < k):
                maxI = i
                maxK = k
        return maxI

print(longueur_de_vol(17), "\n",hauteur_de_vol(17), "\n",le_plus_grand(17, "hauteur"), "\n", le_plus_grand(17,"longueur") )
graphic(17,20)
