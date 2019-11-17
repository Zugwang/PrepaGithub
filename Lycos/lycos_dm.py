from lycos import *

def pivote_a_gauche(): #Question 1
    for i in range(0,3):
        pivote_a_droite()

def demi_tour(): #Question 1
    for i in range(0,2):
        pivote_a_droite()

def avance_de(n): #Question 2
    for i in range(0,n):
        avance()

def va_chercher1(): #Question 3
    objet = 0
    compteur = 0
    while(not objet):
        avance()
        compteur += 1
        if (presence_objet()):
            prend_objet()
            objet =1
    demi_tour()
    for i in range(0, compteur):
        avance()
    pose_objet()

def va_chercher2():  #Question 4
    compteur = 0
    u = 0
    while(peut_avancer()):
        avance()
        compteur += 1
        if (presence_objet()):
            prend_objet()
            u = 1
            demi_tour()
            for i in range(0, compteur):
                avance()
            pose_objet()
            u = 0
            demi_tour()
            compteur = 0
    demi_tour()
    for i in range(0, compteur):
        avance()
    if (u):
        pose_objet()

def avance_couloir(n):  #Question 5
    for i in range(0,n):
        if(peut_avancer()):
            avance()
        else:
            pivote_a_droite()
            if(peut_avancer()):
                avance()
            else:
                demi_tour()
                if(peut_avancer()):
                    avance()
                else:
                    if(presence_objet()):
                        prend_objet()

def avance_couloir6(): #Question 6
    fin = 0
    nmbredeplacement = 0
    while(not fin):
        if(peut_avancer()):
            avance()
            nmbredeplacement += 1
        else:
            pivote_a_droite()
            if(peut_avancer()):
                avance()
                nmbredeplacement += 1
            else:
                demi_tour()
                if(peut_avancer()):
                    avance()
                    nmbredeplacement += 1
                else:
                    if(presence_objet()):
                        prend_objet()
                        fin = 1
    avance_couloir(nmbredeplacement)
    pose_objet()

def nombre_directions(): #Question 7
    result = 0
    for i in range(0,4):
        if (peut_avancer()):
            result += 1
        pivote_a_droite()
    return result

def avance_le_plus_a_droite():  #Question 8
    stop = 1
    pivote_a_droite()
    for i in range(0,4):
        if (peut_avancer() and stop):
            avance()
            stop = 0
        elif(stop):
            pivote_a_gauche()

def avance_le_plus_a_gauche(): #Utilisé dans des tests
    stop = 1
    pivote_a_gauche()
    for i in range(0,4):
        if (peut_avancer() and stop):
            avance()
            stop = 0
        elif(stop):
            pivote_a_droite()

def avance_gauche(): #Utile pour la dernière question
    stop = 1
    for i in range(0,4):
        if (peut_avancer() and stop):
            avance()
            stop = 0
        elif(stop):
            pivote_a_gauche()


def trouve_objet_labyrinthe():  #Question 9
    asTuTrouveObjetLycos = 1
    while(asTuTrouveObjetLycos):
        avance_le_plus_a_droite()
        #affiche_etat()
        if (presence_objet()):
            prend_objet()
            asTuTrouveObjetLycos = 0

def essaye_trouve_objet_labyrinthe():  #Question 10
    asTuTrouveObjetLycos = 0
    introuvable = 0
    while(not(asTuTrouveObjetLycos) and not(introuvable)):
        if (compte_cailloux()>nombre_directions()):
            introuvable = 1
        avance_le_plus_a_droite()
        if (presence_objet()):
            prend_objet()
            asTuTrouveObjetLycos = 1

    return asTuTrouveObjetLycos

def rangement_du_couloir():  #Question 11 (utilise une fonction spécifique comprise entre les questions 8 et 9)
    bout_du_couloir = 0
    i = 0
    #a=0
    while(not bout_du_couloir):
    #while(a<100 and not bout_du_couloir):
        a += 1
        if(presence_objet()):
            prend_objet()
            demi_tour()
            for j in range(0,i):
                avance_gauche5()
            pose_objet()
            i = 0
            demi_tour()
            avance_le_plus_a_droite()
        else:
            avance_le_plus_a_droite()
            if(nombre_directions() == 1):
                bout_du_couloir = 1
            i += 1
        #print(bout_du_couloir)
        #affiche_etat()
