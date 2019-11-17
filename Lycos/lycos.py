# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:40:16 2019

@author: Laurent
"""



#import lycosetat
NORD, EST, SUD, OUEST = 0,1,2,3

class Etat:
    def __init__(self):        
        self.direction = EST
        self.ligne = None
        self.colonne = None
        self.porteObjet = False
        
        self.nbLignes = None
        self.nbColonnes = None
        self.plateau = None
        self.cailloux = None
        
lycosetat = Etat()

from random import randrange
def affiche_etat():
    for i in range(len(lycosetat.plateau)):
        for j in range(len(lycosetat.plateau[0])):
            if lycosetat.plateau[i][j]==1:
                print("#", end="")
            elif lycosetat.ligne == i and lycosetat.colonne == j:
                if lycosetat.porteObjet:
                    print("R", end="")
                else:
                    print("r", end="")
            elif lycosetat.plateau[i][j]==-1:
                print("$", end="")
            else:
                print(" ", end="")
        print()
            
    print("direction:",["NORD", "EST", "SUD", "OUEST"][lycosetat.direction])

def initialise0():
    lycosetat.direction = EST
    lycosetat.ligne = 2
    lycosetat.colonne = 2
    lycosetat.porteObjet = False
    
    lycosetat.nbLignes = 5
    lycosetat.nbColonnes = 5
    lycosetat.plateau = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    lycosetat.cailloux = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    for i in range(lycosetat.nbLignes):
        lycosetat.plateau[i][0] = 1
        lycosetat.plateau[i][-1] = 1
    for j in range(lycosetat.nbColonnes):
        lycosetat.plateau[0][j] = 1
        lycosetat.plateau[-1][j] = 1
    


def initialise1():
    lycosetat.direction = EST
    lycosetat.ligne = 10
    lycosetat.colonne = 2
    lycosetat.porteObjet = False
    
    lycosetat.nbLignes = 20
    lycosetat.nbColonnes = 20
    lycosetat.plateau = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    lycosetat.cailloux = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    for i in range(lycosetat.nbLignes):
        lycosetat.plateau[i][0] = 1
        lycosetat.plateau[i][-1] = 1
    for j in range(lycosetat.nbColonnes):
        lycosetat.plateau[0][j] = 1
        lycosetat.plateau[-1][j] = 1
    lycosetat.plateau[10][10+randrange(9)]=-1

def verifie1():
    return lycosetat.plateau[10][2]==-1

def initialise2():
    lycosetat.direction = EST
    lycosetat.ligne = 10
    lycosetat.colonne = 2
    lycosetat.porteObjet = False
    
    lycosetat.nbLignes = 20
    lycosetat.nbColonnes = 20
    lycosetat.plateau = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    lycosetat.cailloux = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    for i in range(lycosetat.nbLignes):
        lycosetat.plateau[i][0] = 1
        lycosetat.plateau[i][-1] = 1
    for j in range(lycosetat.nbColonnes):
        lycosetat.plateau[0][j] = 1
        lycosetat.plateau[-1][j] = 1
    for k in range(1+randrange(8)):        
        lycosetat.plateau[10][3+k]=-1
    
def verifie2():
    return lycosetat.plateau[10][2]<0 and all(lycosetat.plateau[i][j]>=0 for i in range(lycosetat.nbLignes) for j in range(lycosetat.nbColonnes) if i!=10 or j !=2)
    
def initialise3():
    lycosetat.direction = EST
    lycosetat.ligne = 1
    lycosetat.colonne = 2
    lycosetat.porteObjet = False
    
    lycosetat.nbLignes = 5
    lycosetat.nbColonnes = 20
    lycosetat.plateau = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    lycosetat.cailloux = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    for i in range(lycosetat.nbLignes):
        lycosetat.plateau[i][0] = 1
        lycosetat.plateau[i][-1] = 1
    for j in range(lycosetat.nbColonnes):
        lycosetat.plateau[0][j] = 1
        lycosetat.plateau[-1][j] = 1
        lycosetat.plateau[2][j] = 1
        
    lycosetat.plateau[2][-2] = 0
    lycosetat.plateau[3][1]=-1

def verifie3():
    return lycosetat.plateau[1][2]==-1

def initialise4():
    lycosetat.direction = EST
    lycosetat.ligne = 1
    lycosetat.colonne = 2
    lycosetat.porteObjet = False
    
    lycosetat.nbLignes = 5
    lycosetat.nbColonnes = 20
    lycosetat.plateau = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    lycosetat.cailloux = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    for i in range(lycosetat.nbLignes):
        lycosetat.plateau[i][0] = 1
        lycosetat.plateau[i][-1] = 1
    for j in range(lycosetat.nbColonnes):
        lycosetat.plateau[0][j] = 1
        lycosetat.plateau[-1][j] = 1
        lycosetat.plateau[2][j] = 1
        
    lycosetat.plateau[2][-2] = 0
    lycosetat.plateau[3][1]=-1

def verifie4():
    return lycosetat.porteObjet and all(lycosetat.plateau[i][j]>=0 for i in range(lycosetat.nbLignes) for j in range(lycosetat.nbColonnes))


def initialise5():
    lycosetat.direction = EST
    lycosetat.ligne = 1
    lycosetat.colonne = 1
    lycosetat.porteObjet = False
    
    lycosetat.nbLignes = 5
    lycosetat.nbColonnes = 20
    lycosetat.plateau = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    lycosetat.cailloux = [[0 for j in range(lycosetat.nbColonnes)] for i in range(lycosetat.nbLignes)]
    for i in range(lycosetat.nbLignes):
        lycosetat.plateau[i][0] = 1
        lycosetat.plateau[i][-1] = 1
    for j in range(lycosetat.nbColonnes):
        lycosetat.plateau[0][j] = 1
        lycosetat.plateau[-1][j] = 1
        lycosetat.plateau[2][j] = 1
        
    lycosetat.plateau[2][-2] = 0
    for i in range(randrange(5, 10)):
        u,v = 0, 0
        while lycosetat.plateau[u][v]!=0:
            u,v = randrange(lycosetat.nbLignes), randrange(lycosetat.nbColonnes)
        lycosetat.plateau[u][v]=-1

def verifie5():
    def compte_voisins(i,j):
        return (lycosetat.plateau[i-1][j]==-1)+(lycosetat.plateau[i+1][j]==-1)+(lycosetat.plateau[i][j-1]==-1)+(lycosetat.plateau[i][j+1]==-1)
        
    c = [0]*5
    
    for i in range(lycosetat.nbLignes):
        for j in range(lycosetat.nbColonnes):
            if lycosetat.plateau[i][j]==-1:
                c[compte_voisins(i,j)]+=1
    return not lycosetat.porteObjet and c[0]==0 and c[1]==2 and c[3]==0 and c[4]==0 and c[1]+c[2] == -sum(lycosetat.plateau[i][j] for i in range(lycosetat.nbLignes) for j in range(lycosetat.nbColonnes) if lycosetat.plateau[i][j]<0)
def suivante(i,j):
    if lycosetat.direction==NORD:
        i-=1
    elif lycosetat.direction==SUD:
        i+=1
    elif lycosetat.direction==EST:
        j+=1
    else:
        j-=1
    return i,j


def avance():
    if not peut_avancer():
        affiche_etat()
        raise Exception("Ne peut avancer")
    lycosetat.ligne, lycosetat.colonne = suivante(lycosetat.ligne, lycosetat.colonne)
    lycosetat.cailloux[lycosetat.ligne][lycosetat.colonne]+=1

def pivote_a_droite():
    lycosetat.direction = (lycosetat.direction +1)%4

def peut_avancer():
    l1, c1 = suivante(lycosetat.ligne, lycosetat.colonne)
    try:
        return lycosetat.plateau[l1][c1]<=0
    except:
        return False
    
def prend_objet():
    if lycosetat.porteObjet:
        affiche_etat()
        raise Exception("Ne peut porter qu'un objet à la fois")
    else:
        if presence_objet():        
            lycosetat.porteObjet = 1
            lycosetat.plateau[lycosetat.ligne][lycosetat.colonne]+=1
        else:
            affiche_etat()
            raise Exception("Pas d'objet sur la case")

def presence_objet():
    return lycosetat.plateau[lycosetat.ligne][lycosetat.colonne]<0

def pose_objet():
    if not lycosetat.porteObjet:
        affiche_etat()
        raise Exception("Ne porte pas d'objet")

    lycosetat.plateau[lycosetat.ligne][lycosetat.colonne]-=1
    lycosetat.porteObjet = False
 
def compte_cailloux():
    return lycosetat.cailloux[lycosetat.ligne][lycosetat.colonne]