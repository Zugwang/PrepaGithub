from random import random, randrange
from math import sqrt
from villes import villes_aleatoires, longueur, chemin_aleatoire, distance, matrice_des_distances
from cmath import polar
from bulles import tri_bulle

def somme(tableau):
    sum = tableau[0]
    for i in range(1,len(tableau)):
        sum += tableau[i]
    return sum

def choix_pondere_entier(poids):
    denominateur = somme(poids)
    tirage = randrange(denominateur)
    ancien = 0
    for i in range(len(poids)):
        if tirage < (poids[i] + ancien):
            return i
        ancien += poids[i]

def choix_pondere(poids):
    

def depose_pheromones(distances, pheromones, chemin):
    LONGUEUR = longueur(distance,chemin)
    pheromones = [[0] * len(distances) for i in range(len(distances))]
    for i in range(len(chemin)):
        if i == len(chemin)-1:
            v1 = 0
            v2 = i
        else:
            v1 = chemin[i]
            v2 = chemin[i+1]
        pheromones[v1][v2] = distance[v1][v2] / LONGUEUR

def evapore_pheromones(pheromones,evaporation):
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= evaporation
    return evaporation

def fourmi(distances, pheromones, alpha, beta):
    chemin = [0]
    liste_villes_non_visitees = []
    for i in range(1,len(distances)):
        liste_villes_non_visitees.append(i)
    print(liste_villes_non_visitees)
    for i in range(len(distances)):
        t_poids = []
        derniere_ville = chemin[len(chemin)-1]
        for j in range(len(liste_villes_non_visitees)):
            print(derniere_ville,"/////:",liste_villes_non_visitees[j])
            print(distances[0][1])
            print(distances[derniere_ville][liste_villes_non_visitees[j]])
            t_poids[j] = ( ( (pheromones[derniere_ville][liste_villes_non_visitees[j]]) ** alpha)
                         * (distances[derniere_ville][liste_villes_non_visitees[j]] ** beta) )
        prochaine_ville = choix_pondere_entier(t_poids)
        chemin.append(prochaine_ville)
        liste_villes_non_visitees.remove(prochaine_ville)
    return chemin

a = villes_aleatoires(4)
b = matrice_des_distances(a)
print(len(b))
cheminc = chemin_aleatoire(a)

pheromone__ = [[0] * len(b) for i in range(len(b))]

chemin_f = fourmi(b,pheromone__,2,1)

print(chemin_f)
