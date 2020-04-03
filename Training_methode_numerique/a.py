"""a = 0.1

a = a**2

print(a)

a = a ** (1/2)

print(a)
"""

def nouvelle_grille(n):
    a = [0,0]
    b = [a] * n
    return b

def nouvelle_grille2(n):
    a = []
    for i in range(n):
        a.append(None)
    return a

def u():
    for i in range(1):
        print("a")

az = type(range(7))
a = nouvelle_grille2(4)
print(a)
a[3] = 242.123456
print(a)

b = 1 + 4*1j
c = 1 + 4*1j

print(id(None))
print(id(a[3]))
print(id(242.123456))
print(id(b))
print(id(c))
print(az)

u()
