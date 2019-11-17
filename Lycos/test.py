t = [1,1,1,4,4,3,3,2]

def compte(n,t):
    a = 0
    for i in range(0, len(t)):
        if t[i] == n:
            a += 1
    return a

def compte_first(n,t):
    a = 0
    for i in range(0, len(t)):
        if t[i] == n:
            return i
    return none

def somme(t):
    somme = t[0]
    for i in range(1,len(t)):
        print(somme)
        somme += t[i]
    return somme

def compte_indice(n,t):
    a = []
    for i in range(0, len(t)):
        if t[i] == n:
            a.append(i)
    return a

print(compte_indice(4,t))
#print(compte_first(3,t))
