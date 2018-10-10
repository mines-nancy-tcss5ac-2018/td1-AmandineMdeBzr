def solve(n):
    res=0
    nb=2**n
    while nb>=10:
        p,r=divmod(nb,10)
        res+=r
        nb=p
    res+=nb
    return res

assert solve(15) == 26
print(solve(1000))


# Meth 2

def solve_16(n):
    nombre=2**n
    somme_chiffres=0
    for chstr in str(nombre):
        somme_chiffre+=int(chstr)
    return somme_chiffres


## Probleme 22

f = open('p022_names.txt','r')
alpha=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def solve_22():
    for line in f:
        namescore=0
        liste = line.split(',')
        L=sorted(liste)
        for position,name in enumerate(L):
            res=0
            for lettre in str(name):
                indice=0
                while not(lettre==alpha[indice]):
                    indice+=1
                res+= indice
            namescore+=res*position
        return(namescore)

## Probleme 55
def est_palindromic(nb):
    res=False
    if nb<10:
        res=True
    elif 10<nb<100:
        if str(nb)[0]==str(nb)[1]:
            res=True
    elif 100<nb<1000:
        if str(nb)[0]==str(nb)[2]:
            res=True
    elif 1000<nb<10000:
        if str(nb)[0]==str(nb)[3] and str(nb)[1]==str(nb)[2]:
            res=True
    return res

def add(nombre):
    L=[]
    inverse=0
    for nb in str(nombre):
        L.append(int(nb))
    for i in reversed(L):
        inverse=inverse*10+i
    return inverse+nombre
    
def nb_lychrel():
    res=0
    i=0
    for nombre in range(10,10001):
        while i<50 and est_palindromic(nombre)==False:
            i=i+1
            nombre=add(nombre)
        if est_palindromic(nombre)==False:
            res+=1
    return res
