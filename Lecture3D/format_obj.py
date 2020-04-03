from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

from numpy import array

def list_obj(fileName):
    fichier = open(fileName,"r")
    ligne = fichier.readline()
    tableau_v = []
    tableau_f = []
    tableau_final = []
    while(ligne[0] != "v"):
        ligne = fichier.readline()

    while(ligne == "v"):
        a = ligne.split()
        a.remove("v")
        tableau_v.append(a)
        ligne = fichier.readline()

        for i in range(len(tableau_v)):
            for j in range(len(tableau_v[0])):
                tableau_v[i][j] = float ( tableau_v[i][j] )

    while(ligne[0] != "f"):
        ligne = fichier.readline()

    while(ligne != "" or ligne != "\n"):
        a = ligne.split()
        if len(a)==0:
            break
        a.remove("f")
        test = []
        for i in range(len(a)):
            test.append(int(float(a[i][0])))

        tableau_f.append(test)
        ligne = fichier.readline()
    tableau_final = tableau_f
    for i in range(len(tableau_f)):
        for j in range(len(tableau_f[0])):
            tableau_final[i][j] = tableau_v[ tableau_f[i][j] - 1]

    return tableau_final

def affiche_fichier(fileName):
    faces3D = list_obj(fileName)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.add_collection3d(Poly3DCollection(faces3D))
    plt.show()

def affiche(faces3D):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.add_collection3d(Poly3DCollection(faces3D))
    plt.show()

def normalise(faces3Dor):
    faces3D = faces3Dor
    maximumx = 0
    maximumy = 0
    maximumz = 0
    minimumx = 0
    minimumy = 0
    minimumz = 0
    for i in range(len(faces3D)):
        for j in range(len(faces3D[0])):
            if faces3D[i][j][0] > maximumx:
                maximumx = faces3D[i][j][0]
            if faces3D[i][j][1] > maximumy:
                maximumy = faces3D[i][j][1]
            if faces3D[i][j][2] > maximumz:
                maximumz = faces3D[i][j][2]

            if faces3D[i][j][0] < minimumx:
                minimumx = faces3D[i][j][0]
            if faces3D[i][j][1] < minimumy:
                minimumy = faces3D[i][j][1]
            if faces3D[i][j][2] < minimumz:
                minimumz = faces3D[i][j][2]

    for i in range(len(faces3D)):
        for j in range(len(faces3D[0])):
            faces3D[i][j][0] -= minimumx
            faces3D[i][j][1] -= minimumy
            faces3D[i][j][2] -= minimumz

    return faces3D

affiche_fichier("citrouille.obj")
