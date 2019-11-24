from random import random, randrange
from math import sqrt
from villes import villes_aleatoires, longueur, chemin_aleatoire, distance
from cmath import polar
from bulles import tri_bulle

def somme(tableau):
    sum = tableau[0]
    for i in range(1,len(tableau)):
        sum += tableau[i]
    return sum

def choix_pondere(poids):
    denominateur = somme(poids)
    tirage = randrange(denominateur)
    ancien = 0
    for i in range(len(poids)):
        if tirage < (poids[i] + ancien):
            return i
        ancien += poids[i]

def depose_pheromones(distances, pheromones, chemin):
