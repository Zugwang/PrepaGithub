from random import random, randrange
from math import sqrt
from villes import villes_aleatoires, longueur, chemin_aleatoire, distance, matrice_des_distances
from cmath import polar
from bulles import tri_bulle

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
    point_m = moyenne_affixe(tableau_villes)
    for i in range(len(tableau_villes)):
        x = tableau_villes[i][0] - point_m[0]
        y = tableau_villes[i][1] - point_m[1]
        angle = polar(x + y*1j)
        rep.append((angle[1],i))
    return rep

def heuristique_geometrique(tableau_villes):
    arguments = arguments_et_indices(tableau_villes)
    rep = 0
    list_indice = []
    arguments_range = tri_bulle(arguments)
    for i in range(len(arguments_range)):
        list_indice.append(arguments_range[i][1])

    rep = longueur(tableau_villes,list_indice)
    return rep

def algorithme_glouton(matrice_de_distances):
    liste_villes_non_visitees = []
    for i in range(1,len(matrice_de_distances)):
        liste_villes_non_visitees.append(i)
    chemin = [0]
    for i in range(len(matrice_de_distances)):
        derniere_ville = chemin[len(chemin)-1]
        matrice_distance_triee = tri_bulle(matrice_de_distances)
        print(matrice_distance_triee)



    return 4




def algorithme_glouton_complique(tableau_villes):
    liste_villes_non_visitees = []
    for i in range(1,len(tableau_villes)):
        liste_villes_non_visitees.append(i)
    chemin = [0]
    print(liste_villes_non_visitees)
    for i in range(len(tableau_villes)):
        distance_min = 2
        min_i = 0
        derniere_ville = chemin[len(chemin)-1]
        print(derniere_ville)
        for j in range(len(liste_villes_non_visitees)):
            if distance_min > distance(tableau_villes[derniere_ville],tableau_villes[liste_villes_non_visitees[j]]):
                distance_min = distance(tableau_villes[derniere_ville],tableau_villes[liste_villes_non_visitees[j]])
                min_i = liste_villes_non_visitees[j]
        print("min =",min_i)
        print(liste_villes_non_visitees)
        if not (liste_villes_non_visitees == []):
            liste_villes_non_visitees.remove(min_i)
            chemin.append(min_i)
    return chemin



a = villes_aleatoires(3)
b = matrice_des_distances(a)
print(b)
#chemin_glouton = algorithme_glouton(b)
#print(chemin_glouton)

print("###########")
print(longueur(a,chemin_aleatoire(a)))
#print(longueur(a,chemin_glouton))
print(heuristique_geometrique(a))
