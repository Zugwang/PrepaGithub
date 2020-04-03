# -*- coding: utf-8 -*-
from random import random, choice, randrange
from tkinter import Tk, ALL, mainloop, Canvas
from math import sin, cos, pi, atan2, sqrt

DEGAZ = 0.05            # quantité de masse expulsé au dégazage
ACCELERATION = 0.02     # constante d'accélération impulsée au dégazage
VITESSE = 0.1          # constante de vitesse
TEMPS = 1/100           # temps entre 2 affichages
TRANSFERT = 0.01        # constante de vitesse de transfert de masse
EPSILON = 1e-9          # taille de la plus petite entité
DIMENSION = 700         # taille de la fenêtre


MATIERE = -1
ANTIMATIERE = 1
etats_existants = [MATIERE, ANTIMATIERE]

#%% ECRIRE LES PROGRAMMES DEMANDES APRES CETTE LIGNE

def vecteur(x,y):
    return [x,y]

def ajoute(point,vecteur):
    return [point[0]+vecteur[0], point[1]+vecteur[1]]

def multiplie(scalaire,vecteur):
    return [scalaire*vecteur[0], scalaire*vecteur[1]]

def distance(point1,point2):
    return sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

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
    rayon_min = rayonMax/10

    while len(entites) < n:
        print("len : ",len(entites))
        test_reussi = 0

#        position_test = vecteur(rayon(entite_test) + (1-rayon(entite_test))*random(), rayon(entite_test) + (1-rayon(entite_test))*random())
#        rayon_test =  rayonMax/10 + random()*0.9*rayonMax
#        entite_test = [position_test, vecteur(0,0), rayon_test, choice(etats_existants) , None]

        while not test_reussi:
            rayon_test =  rayon_min + random()*0.9*rayonMax
            entite_test = [vecteur(0,0), vecteur(0,0), rayon_test, choice(etats_existants) , None]
            for i in range(100):
                position_test = vecteur(rayon(entite_test) + (1-2*rayon(entite_test))*random(), rayon(entite_test) + (1-2*rayon(entite_test))*random())

                test_reussi = 1
                print("test : ",i)
                entite_test[0] = position_test
                for j in range(len(entites)):
                    if collision(entites[j],entite_test):
                        test_reussi = 0
                if test_reussi:
                    entites.append(entite_test)
                    break
                rayonMax = rayon_test


def couleur(entite):
    rayonMax = 0.2
    rayonMin = rayonMax/10
    if joueur(entite) != None:
        return "white"
    elif nature(entite) == MATIERE:
        a = (rayon(entite) - rayonMin ) / (rayonMax - rayonMin)
        a *= 16
        a = str(hex(int(16 - a)))
        a = a[-1]
        string = "#"+a+"00"
        return string
    else:
        a = (rayon(entite) - rayonMin ) / (rayonMax - rayonMin)
        a *= 16
        a = str(hex(int(a)))
        a = a[-1]
        string = "#04"+a
        return string

def deplacement(entites):
    for i in range(len(entites)):
        position_finale = ajoute(position(entites[i]), multiplie(VITESSE, vitesse(entites[i]) ) )
        if   position_finale[0] < rayon(entites[i]):
            entites[i][1] = [-entites[i][1][0],entites[i][1][1] ]
            position_finale[0] = rayon(entites[i])
        elif position_finale[0] > 1-rayon(entites[i]):
            entites[i][1] = [-entites[i][1][0],entites[i][1][1] ]
            position_finale[0] = 1-rayon(entites[i])

        if position_finale[1] < rayon(entites[i]):
            entites[i][1] = [entites[i][1][0],-entites[i][1][1] ]
            position_finale[1] = rayon(entites[i])
        elif position_finale[1] > 1-rayon(entites[i]):
            entites[i][1] = [entites[i][1][0],-entites[i][1][1] ]
            position_finale[1] = 1-rayon(entites[i])

        entites[i][0] = position_finale

def masse_de_rayon(rayon):
    return rayon**2

def rayon_de_masse(masse):
    return sqrt(masse)

def change_rayon(entite, rayon):
    entite[2] = rayon

def change_masse(entite, masse):
    entite[2] = rayon_de_masse(masse)

def accelere(entite,angle,intensite):
    entite[1][0] -= (intensite/masse(entite) * ACCELERATION * cos(angle) )
    entite[1][1] -= (intensite/masse(entite) * ACCELERATION * sin(angle) )

def degaze(entites,entite,angle):
    masse_ret = masse(entite)*DEGAZ
    if masse_ret < EPSILON:
        return entites

    entite[2] -= rayon_de_masse(masse_ret)
    position_x = entite[0][0] + (rayon(entite)+rayon_de_masse(masse_ret)) * cos(angle)
    position_y = entite[0][1] + (rayon(entite)+rayon_de_masse(masse_ret)) * sin(angle)

    entites.append([[position_x,position_y], [-vitesse(entite)[0],-vitesse(entite)[1] ], rayon_de_masse(masse_ret), nature(entite), None])


    accelere(entite,angle,masse_ret)
    accelere(entites[-1],angle+pi,masse_ret)

def mais_ou_sont_mes_boules(entites,joueur):
    for i in range(len(entites)):
        if str(entites[i][4]) == str(joueur):
            return entites[i]


def taille_interface(entite1,entite2):
    r = min(rayon(entite1),rayon(entite2))
    R = max(rayon(entite1),rayon(entite2))
    distance12 = distance(entite1[0],entite2[0])
    if distance12 < R-r:
        return 4*r

    p = (R + r + distance12)/2
    h = 2*sqrt(p*(p-R)*(p-r)*(p-distance12)) / distance12

    if distance12 > R:
        return 2*h
    else:
        return 4*r - 2*h

def transfert(entites):
    entites.sort(key = rayon)
    for i in range(1,len(entites)):
        for j in range(0,i):
            if collision(entites[i],entites[j]):
                transfert_th = TRANSFERT * taille_interface(entites[i],entites[j])
                if transfert_th < 0:
                    transfert_ef = 0
                elif transfert_th > masse(entites[j]):
                    transfert_ef = masse(entites[j])
                else:
                    transfert_ef = transfert_th

                entites[j][2] = sqrt(entites[j][2]**2 - transfert_ef)

                angle = atan2(vitesse(entites[i])[1],vitesse(entites[i])[0])
                accelere( entites[i],angle,transfert_ef*norme(entites[j][1]) )


                if  nature(entites[i]) == nature(entites[j]):
                    entites[i][2] =  sqrt(entites[i][2]**2 + transfert_ef)
                else:
                    entites[i][2] =  sqrt(entites[i][2]**2 - transfert_ef)


    a = 0
    for i in range(len(entites)):
        if masse(entites[i]) < EPSILON:
            entites[i] = 0
            a += 1
    for i in range(a) : entites.remove(0)







#%% ECRIRE LES PROGRAMMES DEMANDES AVANT CETTE LIGNE
def cree_fenetre():
    fenetre = Tk()
    surfaceDeDessin = Canvas(fenetre, width=DIMENSION, height = DIMENSION)
    surfaceDeDessin.pack()

    entites = [[[0.5, 0.5], [0,0], 0.15, MATIERE, 0]]
    print(entites)
    initialise_entites(entites, 50, 0.2)
    print(entites)

    def affichage(v_victoire):
        surfaceDeDessin.delete(ALL)
        for i in range(len(entites)):
            xmin = ( position(entites[i])[0]-rayon(entites[i]) ) * DIMENSION
            xmax = ( position(entites[i])[0]+rayon(entites[i]) ) * DIMENSION
            ymin = ( position(entites[i])[1]-rayon(entites[i]) ) * DIMENSION
            ymax = ( position(entites[i])[1]+rayon(entites[i]) ) * DIMENSION
            surfaceDeDessin.create_oval(xmin,ymin,xmax,ymax,fill = couleur(entites[i]))

        if v_victoire == 1:
            surfaceDeDessin.create_rectangle(100,100,DIMENSION-100,DIMENSION-100,fill = "green")

        elif v_victoire == -1:
            surfaceDeDessin.create_rectangle(100,100,DIMENSION-100,DIMENSION-100,fill = "red")



    def victoire(entites):
        if mais_ou_sont_mes_boules(entites,0) == None:
            return -1
        elif len(entites) == 1:
            return 1
        else:
            return 0


    def pas_de_jeu():
        deplacement(entites)
        transfert(entites)
        v_victoire = victoire(entites)
        affichage(v_victoire)
        surfaceDeDessin.after(int(TEMPS*1000),pas_de_jeu)

    def click(event):
        entite = mais_ou_sont_mes_boules(entites,0)
        x1,y1 = position(entite)
        x2,y2 = event.x/DIMENSION, event.y/DIMENSION
        degaze(entites, entite, atan2(y2-y1,x2-x1))
        return

    surfaceDeDessin.bind('<Button-1>', click)
    pas_de_jeu()
    mainloop()

#%% NE RIEN ECRIRE APRES CETTE LIGNE
cree_fenetre()
