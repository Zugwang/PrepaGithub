def matrice_vide(n,m):
    return [[None] * n for i in range(m)]

def matrice_des_distances_2_mots(mot1,mot2):
    distance = matrice_vide(len(mot1),len(mot2))
    for i in range(len(mot1)):
        distance[0][i] = i
    for i in range(len(mot2)):
        distance[i][0] = i

    

print(matrice_vide(3,5))
