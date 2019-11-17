from random import randrange


def point_domino(domino):
    somme = domino[0] + domino[1]
    return somme

def inverse_domino(domino):
    v = (domino[1], domino[0])
    return v

def generation_ensemble_domino():
    domino = []
    for i in range(6):
        for j in range(i+1):
            domino.append((i+1,j+1))
            #print(i+1,j+1)
    return domino

def somme_ensemble_domino(ensemble_domino):
    domino= 0
    for i in range(len(ensemble_domino)):
        domino += ensemble_domino[i][0] + ensemble_domino[i][0]
    return domino

def trouver_domino(domino,ensemble_domino):
    for i in range(len(ensemble_domino)):
        if(a[i][0] == domino[0] and a[i][1] == domino[1]) or (a[i][0] == domino[1] and a[i][1] == domino[0]):
            return i

def trouver_domino_max(ensemble_domino):
    max = 0
    maxi = 0
    for i in range(len(ensemble_domino)):
        if point_domino(ensemble_domino[i]) > max:
            max = point_domino(ensemble_domino[i])
            maxi = i
    return i

def accoller_domino(ensemble_domino,face):
    v = []
    for i in range(len(ensemble_domino)):
        if(ensemble_domino[i][0] == face or ensemble_domino[i][1] == face):
            v.append(ensemble_domino[i])

    return v
def face_train(train):
    v = (train[0][0],train[len(train)-1][1])
    return v


def est_un_train(ensemble_domino):
    for i in range(len(ensemble_domino)-1):
        if ensemble_domino[i][1] != ensemble_domino[i+1][0]:
            return 0
    return 1

def supprimer_domino_ensemble(ensemble_domino,indice):
    ensemble_domino[indice] = ensemble_domino[len(ensemble_domino)-1]
    ensemble_domino.pop()

def pioche_domino(ensemble_domino,nombre_domino):
    v = []
    while(len(v) < nombre_domino ):
        i = randrange(len(ensemble_domino))
        v.append( ensemble_domino[i] )
        supprimer_domino_ensemble(ensemble_domino,i)
    return v

def nouvelle_partie()



u = (3,2)
print(inverse_domino(u))
a = generation_ensemble_domino()
print(trouver_domino((6,5),a))
print(accoller_domino(a,3))
e = [ (1,2), (2,5), (3,5), (3,3), (3,42) ]

print(e)
print(pioche_domino(e,2))
print(e)
