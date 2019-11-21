from random import random, randrange
from math import sqrt

def tri_bulle(tableau):
    for j in range(len(tableau)-1):
        for i in range(len(tableau)-1):
            if tableau[i] > tableau[i+1]:
                a = tableau[i]
                tableau[i] = tableau[i+1]
                tableau[i+1] = a
    return tableau

b = [6,5,4,3,2,1]
print(tri_bulle(b))
