def addition(i):
    return i + 2


def apply_function_global(t,f):
    for i in range(len(t)):
        t[i] = f(t[i])

def apply_function(t,f):
    t2 = t.copy()
    for i in range(len(t2)):
        t2[i] = f(t[i])
    return t2

def triplet_des():
    list = []
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                a = i
                b = j
                c = k
                list.append((a,b,c))
    return list

def somme_produit_triplet(t):
    somme = t[0] + t[1] + t[2]
    produit = t[0] * t[1] * t[2]
    return (somme,produit)

def fonction_finale():
    t_somme  = []
    t_produit  = []
    t_triplet = triplet_des()
    for i in range(len(t_triplet)):
        u = somme_produit_triplet(t_triplet[i])
        t_somme.append(u[0])
        t_produit.append(u[1])

    return (t_somme,t_produit)

print(fonction_finale())
