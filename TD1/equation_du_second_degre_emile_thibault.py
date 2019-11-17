from math import sqrt
print("Bienvenue dans ce programme de résolution d'équations du second degré")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b*b - 4 * a * c

if (delta < 0):
    delta = -delta
    result1j = (-b - sqrt(delta)*1j)/(2*a)
    result2j = (-b + sqrt(delta)*1j)/(2*a)
    print("Les deux racines sont ", result1j, " et ", result2j)
elif (delta == 0):
    result = -b / (2*a)
    print("L'unique racine est ",result)
else:
    result1 = (-b - sqrt(delta))/(2*a)
    result2 = (-b + sqrt(delta))/(2*a)
    print("Les deux racines sont ", result1, " et ", result2)
