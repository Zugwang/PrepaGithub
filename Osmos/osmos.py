from math import sqrt
from random import random, choice, randrange

etats_existants = ["MATIERE", "ANTIMATIERE" ]

def vecteur(x,y):
    return [x,y]

def ajoute(point,vecteur):
    return [point[0]+vecteur[0], point[1]+vecteur[1]]

def norme(vecteur):
    return sqrt(vecteur[0]**2 + vecteur[1]**2)

def position(entite):
    return entite[0]

def vitesse(entite):
    return entite[1]

def rayon(entite):
    return entite[2]

def nature(entite):
    return entite[3]

def joueur(entite):
    return entite[4]

def masse(entite):
    return entite[2]**2

def collision(entite1,entite2):
    if norme([position(entite1)[0]-position(entite2)[0], position(entite1)[1]-position(entite2)[1]] ) >= rayon(entite1) + rayon(entite2):
        return False
    return True

def initialise_entites(entites, n, rayonMax):

    while len(entites) < n-1:
        test_reussi = 0
        entite_test = [vecteur(0,0), vecteur(0,0), rayonMax/10 + random()*0.9*rayonMax, choice(etats_existants) , None]
        position_test = vecteur(random(),random())
        while test_reussi == 0:
            test_reussi = 1
            entite_test[0] = position_test
            for i in range(len(entites)):
                if collision(entites[i],entite_test):
                    test_reussi = 0
        entites.append(entite_test)
    return entites

def couleur(entite):
    if joueur(entite) != None:
        return "green"
    elif nature(entite) == "MATIERE":
        return white
    else:
        return black


f = []
print(len(f))
f = initialise_entites(f,4,0.02)
print(f)
a = vecteur(1,2)
b = vecteur(1,1)
#a = ajoute(a,b)
d = [[1,3], 0, 1]
e = [[1,1], 0 ,1]
print(collision(d,e))
c = a + b

print(c)
print(norme(b))
