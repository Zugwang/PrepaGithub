def est_une_occurence(chaine,mot,i):
    for k in range(len(mot)):
        if mot[k] != chaine[i+k]:
            return False
    return True

def premiere_occurence(chaine,mot):
    for i in range(len(chaine) - lent(mot)+1):
        if est_une_occurence(chaine,mot,i):
            return i
    return NONE

def est_une_occurence_avec_k_erreurs(chaine,mot,i,k):
    erreur = 0
    for j in range(len(mot)):
        if mot[j] != chaine[i+j]:
            erreur += 1
        if erreur > k:
            return False
    return True

def premiere_occurence_k_erreur(chaine,mot,k):
    for i in range(len(chaine) - len(mot)+1):
        if est_une_occurence_avec_k_erreurs(chaine,mot,i,k):
            return i
    return None

def occurence_avec_moins_erreurs(chaine,mot):
    nbre_k_erreur = 0
    reponse = -1
    while nbre_k_erreur < len(mot):
        reponse = premiere_occurence_k_erreur(chaine,mot,nbre_k_erreur)
        if reponse != None:
            return reponse
        nbre_k_erreur += 1
    return None


def nbre_erreur(chaine,mot,i):
    erreur = 0
    for j in range(len(chaine) - len(mot)+1):
        if mot[j] != chaine[i+j]:
            erreur += 1
    return erreur

def occurence_avec_moins_erreurs_plus_efficace(chaine,mot):
    tab_erreur = []
    for i in range(len(chaine)):
        tab_erreur.append(nbre_erreur(chaine,mot,i))
    min = len(mot)
    min_i = 0
    for j in range(len(tab_erreur)):
        if tab_erreur[j] < min:
            min = tab_erreur[j]
            min_i = j
    return min_i


mot = "adodigado"
mot_recherche = "da"
print(occurence_avec_moins_erreurs_plus_efficace(mot,mot_recherche))
