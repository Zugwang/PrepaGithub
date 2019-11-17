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
