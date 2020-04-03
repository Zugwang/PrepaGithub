
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
