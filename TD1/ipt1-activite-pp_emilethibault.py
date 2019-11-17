# -*- coding: utf-8 -*-
#from pylab import plot, show
from pylab import plot, show

def suiteSyracuse(inputNumber):
    if inputNumber%2 ==  0:
        result = inputNumber/2
    else:
        result = (3 * inputNumber + 1)

    return result

def graphic(firstTerm, rangMax):
    u = firstTerm
    for i in range(firstTerm,rangMax+1):
        plot(i,u,"ro")
        show()
        u = suiteSyracuse(u)

"""
Spyder Editor

This is a temporary script file.
"""
