from random import random, randrange
from math import sqrt
from villes import villes_aleatoires


def moyenne_affixe(tableau):
    x = 0
    y = 0
    for i in range(len(tableau)):
        x += tableau[i][0]
        y += tableau[i][1]
    x /= len(tableau)
    y /= len(tableau)
    return (x,y)

def arguments_et_indices(tableau_villes):
    rep = []
    for i in range(tableau_villes):
        angle =
        rep.append((angle,i))
    return rep

    
a = villes_aleatoires(4)
print(a)
print(moyenne_affixe(a))
