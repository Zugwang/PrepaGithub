from math import sqrt

graine = 0
def change_graine(entier):
    global graine
    graine = entier
    return

def cree_generateur(uneGraine):
    graine1 = uneGraine
    graine1 = graine1**2

    #print(graine1)

    graine1 //= 10**5
    graine1 %= 10**10
    return graine1


def aleatoire():
    global graine
    graine1 = graine
    graine1 = graine1**2

    #print(graine1)

    graine1 //= 10**5
    graine1 %= 10**10
    graine = graine1

def flottant_aleatoire():
    for i in range(0,10):
        aleatoire()
    return graine/(10**10)

def entier_aleatoire_entre_bornes(entierMin,entierMax):
    oui = entierMax - entierMin + 1
    result = oui * flottant_aleatoire()
    result += entierMin
    result //= 1
    return result

def teste_generateur(f, n, a = None, b = None):
    if (a == None and b == None):
        for i in range(0,n):
            print(f())
    else:
        for i in range(0,n):
            print(f(a,b))





change_graine(4242424242)

print(graine)

teste_generateur(entier_aleatoire_entre_bornes, 4, 1, 6)
#print(entier_aleatoire_entre_bornes(42,69))

##############################################################################################

graine = 0
def change_graine(entier):
    global graine
    graine = entier
    return

def aleatoire2():
    a = 1103515245
    c = 12345
    m = 2**31

    global graine
    graine1 = graine
    graine1 *= a
    graine1 += c
    graine1 %= m
    graine = graine1

def flottant_aleatoire2():
    aleatoire2()
    return graine/(2**31)

change_graine(4242424242)
aleatoire2()
for i in range(0, 10):
    print(flottant_aleatoire2())
    print(flottant_aleatoire2())
