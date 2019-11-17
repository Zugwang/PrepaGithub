from random import randint


def etat_initial(nbreLigne):
    t = []
    j = 1
    for i in range(nbreLigne):
        t.append(j)
        j += 2
    return t

def est_gagnante(etat):
    if etat == []:
        return 0
    reponse = etat[0]
    for i in range(1, len(etat)):
        reponse = reponse^etat[i]
    if reponse == 0:
        return 1
    else:
        return 0

def affiche_etat(etat):
    for i in range(len(etat)):
        print(i,": ",end = "")
        for j in range(etat[i]):
            print("|",end = "")
        print("\n")
    if(est_gagnante(etat) == 1):
        print("Tu peux gagner")
    else:
        print("Tu peux pas gagner")

def coup_legal(etat,ligne,nombre):
    if(ligne < 0 or ligne > len(etat)-1 or nombre < 0 or nombre > etat[ligne]):
        return False
    else:
        return True

    """elif(ligne > len(etat)-1):
        return 0
    elif(nombre < 0):
        return 0
    elif(nombre > etat[ligne]):
        return 0
    else:
        return 1"""

def joue_coup(etat,ligne,nombre):
    etat[ligne] -= nombre
    if(etat[ligne] < 1):
        etat.pop(ligne)
    return etat

def strategie_libre(etat):
    while(True):
        print("Ligne:", end = "")
        jligne = int(input())
        print("Nombre:", end = "")
        jnombre = int(input())
        if coup_legal(etat,jligne,jnombre):
            coup = (jligne,jnombre)
            return coup
        print("Joue sans tricher stp")

def joue_marienbad(stratj1,stratj2):
    u = etat_initial(5)
    aquidejouer = randint(0,1)
    affiche_etat(u)
    while(not u == []):
        if(not aquidejouer):
            print("///////////////Player 1///////////////")
            coupActuel = stratj1(u)
        else:
            print("///////////////Player 2///////////////")
            coupActuel = stratj2(u)
        joue_coup(u,coupActuel[0],coupActuel[1])
        affiche_etat(u)
        aquidejouer = not aquidejouer
    print("Joueur", (not aquidejouer)+1, "a explosé son adversaire")





joue_marienbad(strategie_libre,strategie_libre)



"""
u = etat_initial(4)
print(u)
affiche_etat(u)
print(coup_legal(u,1,2))
joue_coup(u,1,3)
affiche_etat(u)
b = strategie_libre(u)
print(b)"""
