def init_tab(n):
    t = [0,0]
    for i in range(n-1):
        t.append(1)
    return t

def first_true(i,t):
    for j in range(i,len(t)):
        if t[j] == 1:
            return j

    return len(t)

def all_true(t):
    tr = []
    for i in range(len(t)):
        if t[i] == 1:
            tr.append(i)
    return tr

def del_mutiple_of(t,p):
    for i in range(2*p,len(t),p):
        t[i] = 0
    return t

def del_mutiple_of2(t,p):
    for i in range(p*p,len(t),p):
        t[i] = 0
    return t

def crible_eratosthene(n):
    t = init_tab(n)
    u = []
    a = 0
    u = 0
    while(a != len(t)):
        a = first_true(a+1,t)

        del_mutiple_of(t,a)

    print(all_true(t))

    return t


crible_eratosthene(200)
#t_ = [0, 0, 1, 1, 0, 0, 1, 1]

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

def apply(f,t):
    reponse = f(t[0],t[1])
    for i in range(2,len(t)+1):
        reponse += f(reponse,t[i])
    return reponse

    return t

def somme_t(t):
    return apply((lambda a,b:a+b),t)




t = [1,3,6]

print(somme_t(t))
