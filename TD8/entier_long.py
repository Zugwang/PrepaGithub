def conversion_base(nombre, base):
    resultat = []
    while nombre != 0:
        chiffre = nombre % base
        nombre = nombre // base
        resultat.append(chiffre)
    return resultat

def conversion10(nombre_decompose, base):
    resultat = 0
    for i in range(len(nombre_decompose)):
        resultat += nombre_decompose[i] * (base**i)
    return resultat


def addition_paul(tableau1,tableau2,base):
    a = len(tableau1)
    b = len(tableau2)

    if a > b:
        resultat = tableau1
        resultat.append(0)
        for i in range(len(tableau2)):
            resultat[i]=resultat[i]+tableau2[i]
            if resultat

def addition(nombreA, nombreB, base):
    retenue = 0
    resultat = []
    Asup = 0

    for i in range(min(len(nombreA), len(nombreB))):
        somme = nombreA[i] + nombreB[i]
        resultat.append( (somme  + retenue) % base)
        retenue = somme // base

    if len(nombreA) > len(nombreB):
        le_truc_qui_reste = nombreA
    elif len(nombreA) == len(nombreB):
        le_truc_qui_reste = nombreA+[0]
    else:
        le_truc_qui_reste = nombreB

    for i in range(min(len(nombreA), len(nombreB)), len(le_truc_qui_reste)):
        resultat.append( (le_truc_qui_reste[i]  + retenue) % base)
        retenue = (le_truc_qui_reste[i]  + retenue) // base
    while retenue != 0:
        resultat.append(retenue % base)
        retenue = retenue // base

    return resultat


def produit_chiffre(nombre,chiffre,base):
    resultat = []
    retenue = 0
    for i in range(len(nombre)):
        a = nombre[i] * chiffre
        resultat.append( (a+retenue) % base )
        retenue = (a+retenue) // base
    resultat.append( retenue )
    return resultat

def produit(nombreA,nombreB,base):
    resultat_intermediaire = []
    for i in range(len(nombreA)):
        resultat_intermediaire.append( [0]*i + produit_chiffre(nombreB,nombreA[i],base) )

    print(resultat_intermediaire)
    resultat = resultat_intermediaire[0]

    for i in range(1,len(resultat_intermediaire)):
        resultat = addition(resultat,resultat_intermediaire[i],base)

    return resultat





print( produit([1,2,3],[2,4,1],5) )
