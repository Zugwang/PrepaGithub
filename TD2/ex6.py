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







#f
