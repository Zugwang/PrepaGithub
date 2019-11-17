pas = 0.001
h = 1e-9

borneInf = 0
borneSup = 10

def fonction_f(inputNumber):
    result = -(inputNumber - 3)*(inputNumber - 5)*(inputNumber - 7)
    return result

#for i in range(borneInf, borneSup, pas):
i = borneInf
max = fonction_f(i)
min = fonction_f(i)
while(i<borneSup+pas):
    a = fonction_f(i)
    if a > max:
        max = a
    if a < min:
        min = a
    i += pas

print("Min = ", min,"   Max = ",max)

def derivee_approximation(fonction_A):

    d_fonction_A = lambda x: (fonction_A(x + h)-fonction_A(x-h))/(2*h)

    print(d_fonction_A)

    return d_fonction_A


print(derivee_approximation(fonction_f(0)))
