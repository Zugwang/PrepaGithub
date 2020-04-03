from random import random, randrange
from math import sqrt

def factoriel(a):   #Q1 oui on peut ecrire un programme testant tous les chemins
    rep = 1         #seulement l'executer prendrait trop de ressource
    for i in range(1,a+1):
        rep *= i
    return rep

#pour n = 100
# n!= 93326215443944152681699238856266700490715968264381621468592963895217599993
#2991560894146397615651828625369792082722375825118521091686400000000000000000000
#00000


def villes_aleatoires(n):
    tableau = []
    for i in range(n):
        tableau.append((random(),random()))
    return tableau

def chemin_aleatoire(tableau_villes):
    nbre_ville = len(tableau_villes)
    rep = []
    tampon = []
    for i in range(nbre_ville):
        tampon.append(i)
    for i in range(nbre_ville):
        u = randrange(nbre_ville-i)
        rep.append(tampon[u])
        tampon.pop(u)
    del tampon
    return rep

def distance(point1, point2):
    dist = sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return dist

def matrice_des_distances(tableau_villes):
    matrice = [[0] * len(tableau_villes) for i in range(len(tableau_villes))]
    for i in range(len(tableau_villes)):
        for j in range(len(tableau_villes)):
            matrice[i][j] = (distance(tableau_villes[i],tableau_villes[j]))
    return matrice

def longueur(matrice,chemin):
    longueur_totale = 0
    for i in range(len(chemin)):
        if i == len(chemin)-1:
            v1 = 0
            v2 = i
        else:
            v1 = chemin[i]
            v2 = chemin[i+1]
        longueur_totale += matrice[v1][v2]
    return longueur_totale

"""
a = villes_aleatoires(4)
b = matrice_des_distances(a)
print(a)
chemin = chemin_aleatoire(a)
print(chemin)
print("matrice=",matrice_des_distances(a))
print("taille=",len(matrice_des_distances(a)))
print(longueur(b,chemin))
"""
