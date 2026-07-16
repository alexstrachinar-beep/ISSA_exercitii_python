#ex1
def ex1(n):
    if n == 1:
        return [0]

    sir = [0,1]
    while len(sir) < n:
        urm = sir[-1]+sir[-2]
        sir.append(urm)
    return sir

#print(ex1(10))

#ex2
def if_prim(a):
    if a==1:
        return False
    if a==2:
        return True
    for i in range(2,a//2+1):
        if(a%i==0):
            return False
    return True

def ex2(a):
    rez = []
    for x in a:
        if if_prim(x):
            rez.append(x)
    return rez
#print (ex2([1,2,3,4,5, 6, 7]))

#ex3
import math
def ex3(a):
    drepte_unice = set()
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            p1 = a[i]
            p2 = a[j]
            if p1==p2:
                continue
            x1, y1 =p1
            x2, y2 =p2

            m = y2-y1
            n = x2-x1
            p = x2*y1 - x1*y2

            g = math.gcd(abs(m),abs(n),abs(p))

            if g!=0:
                m//=g
                n//=g
                p//=g

            if m<0 or (m == 0 and n<0) or (m == 0 and p<0):
                m,n,p = -m,-n,-p

        drepte_unice.add(m,n, p)
    return list(drepte_unice)

#ex4
def ex4(a, b):
    intersectie = []
    for x in a:
        if x in b and not in intersectie:
            intersectie.append(x)

    reuniune = []
    for x in a:
        if x not in reuniune:
            reuniune.append(x)
    for x in b:
        if x not in reuniune:
            reuniune.append(x)

    dif_ab = []
    for x in a:
        if x not in b and x not in dif_ab:
            dif_ab.append(x)

    dif_ba = []
    for x in b:
        if x not in a and x not in dif_ba:
            dif_ba.append(x)

    return intersectie, reuniune, dif_ab, dif_ba

#ex5
def ex5(a, b):
    rez = []
    def backtrack(start, cale_curenta):
        if len(cale_curenta)==b:
            rez.append(tuple(cale_curenta))
            return None
        for i in range(len(a)):
            cale_curenta.append(a[i])
            backtrack(i+1, cale_curenta)
            cale_curenta.pop()

    backtrack(0, [])
    return rez
#a = [1, 2, 3, 4]
#b = 3
#print(ex4(a, b))

#ex6
def ex6(*a,b):
    frecvente = {}
    for lista in a
        elemente = set(lista)
        for elem in elemente:
            frecvente[elem] = frecvente.get(elem, 0) + 1

    rez = [elem for elem, frecv in frecvente.items() if frecv == b]
    return rez

#ex7
def ex7(*siruri, x=1, flag=True):
    liste_rezultat = []

    for sir in siruri:
        lista_curenta = []
        for char in sir:
            cod_ascii = ord(char)

            if flag:
                if cod_ascii % x == 0:
                    lista_curenta.append(char)
            else:
                if cod_ascii % x != 0:
                    lista_curenta.append(char)

        liste_rezultat.append(lista_curenta)

    return tuple(liste_rezultat)
