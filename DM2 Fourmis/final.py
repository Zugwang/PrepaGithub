from random import random, randrange
from math import sqrt
from cmath import polar


def factoriel(a):   #Q1 oui on peut ecrire un programme testant tous les chemins
    rep = 1         #seulement l'executer prendrait trop de ressource
    for i in range(1,a+1):
        rep *= i
    return rep

#pour n = 100
# n!= 93326215443944152681699238856266700490715968264381621468592963895217599993
#2991560894146397615651828625369792082722375825118521091686400000000000000000000
#00000


def villes_aleatoires(n): #Q2
    tableau = []
    for i in range(n):
        tableau.append((random(),random()))
    return tableau

def chemin_aleatoire(tableau_villes): #Q3
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

def distance(point1, point2): #Q4
    dist = sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return dist

def matrice_des_distances(tableau_villes): #Q5
    matrice = [[0] * len(tableau_villes) for i in range(len(tableau_villes))]
    for i in range(len(tableau_villes)):
        for j in range(len(tableau_villes)):
            matrice[i][j] = (distance(tableau_villes[i],tableau_villes[j]))
    return matrice

def longueur(matrice,chemin): #Q6
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

def tri_bulle(tableau): #Q8
    for j in range(len(tableau)-1):
        for i in range(len(tableau)-1):
            if tableau[i] > tableau[i+1]:
                a = tableau[i]
                tableau[i] = tableau[i+1]
                tableau[i+1] = a
    return tableau


def moyenne_affixe(tableau): #Q10
    x = 0
    y = 0
    for i in range(len(tableau)):
        x += tableau[i][0]
        y += tableau[i][1]
    x /= len(tableau)
    y /= len(tableau)
    return (x,y)

def arguments_et_indices(tableau_villes): #Q11
    rep = []
    point_m = moyenne_affixe(tableau_villes)
    for i in range(len(tableau_villes)):
        x = tableau_villes[i][0] - point_m[0]
        y = tableau_villes[i][1] - point_m[1]
        angle = polar(x + y*1j)
        rep.append((angle[1],i))
    return rep

def heuristique_geometrique(tableau_villes): #Q12
    arguments = arguments_et_indices(tableau_villes)
    list_indice = []
    arguments_range = tri_bulle(arguments)
    for i in range(len(arguments_range)):
        list_indice.append(arguments_range[i][1])

    return list_indice

def algorithme_glouton(matrice_de_distances): #Q13
    liste_villes_non_visitees = []
    for i in range(1,len(matrice_de_distances)):
        liste_villes_non_visitees.append(i)
    chemin = [0]
    for i in range(len(matrice_de_distances)):
        derniere_ville = chemin[len(chemin)-1]
        distance_min = 2
        min_i = 0
        for j in range(len(liste_villes_non_visitees)):
            if distance_min > matrice_de_distances[derniere_ville][liste_villes_non_visitees[j]]:
                distance_min = matrice_de_distances[derniere_ville][liste_villes_non_visitees[j]]
                min_i = liste_villes_non_visitees[j]
        if not (liste_villes_non_visitees == []):
            liste_villes_non_visitees.remove(min_i)
            chemin.append(min_i)

    return chemin




def algorithme_glouton_complique(tableau_villes): #Q13 ne pas prendre en compte
    liste_villes_non_visitees = []                #(change juste d'entrée)
    for i in range(1,len(tableau_villes)):
        liste_villes_non_visitees.append(i)
    chemin = [0]
    for i in range(len(tableau_villes)):
        distance_min = 2
        min_i = 0
        derniere_ville = chemin[len(chemin)-1]
        for j in range(len(liste_villes_non_visitees)):
            if distance_min > distance(tableau_villes[derniere_ville],tableau_villes[liste_villes_non_visitees[j]]):
                distance_min = distance(tableau_villes[derniere_ville],tableau_villes[liste_villes_non_visitees[j]])
                min_i = liste_villes_non_visitees[j]
        if not (liste_villes_non_visitees == []):
            liste_villes_non_visitees.remove(min_i)
            chemin.append(min_i)
    return chemin

def somme(tableau): #Q14
    sum = tableau[0]
    for i in range(1,len(tableau)):
        sum += tableau[i]
    return sum

def choix_pondere_entier(poids): #Q15 (ne fonctionne qu'avec des entiers)
    denominateur = somme(poids)
    tirage = randrange(denominateur)
    ancien = 0
    for i in range(len(poids)):
        if tirage < (poids[i] + ancien):
            return i
        ancien += poids[i]

def choix_pondere(poids): #Q15
    a = 0


def depose_pheromones(distances, pheromones, chemin): #Q16
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

def evapore_pheromones(pheromones,evaporation): #Q17
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= evaporation
    return evaporation

def fourmi(distances, pheromones, alpha, beta): #Q18 ne fonctionne pas a cause de Q15
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
