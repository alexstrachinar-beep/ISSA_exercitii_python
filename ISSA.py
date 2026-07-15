
# ex5
#print(len(str(2 ** 1024)))
# ex6
def myfunc(a,b,c):
    x = [a,b,c]
    return sorted(x)[-1]
#print(myfunc(5,7,1))

#ex7
def myfunc2(x,y,op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y

#print(myfunc2(2,3, '+'))

#ex8
def myfunc3(a):
    v = []
    k = 0
    while a != 0:
        v.append(a%10)
        a //= 10
        k+=1

    for i in range(k//2):
        if(v[i]!=v[k-i-1]):
            return False
    return True
#print(myfunc3(534))

#ex9
def myfunc4(a):
    for i in range(2,a//2):
        if(a%i==0):
            return False
    return True
#print(myfunc4(8))

#ex10
def myfunc5(a):
    for element in a:
        print(element)

#myfunc5([5, 6, 7, 8, 9, 0])

#ex11
def myfunc6(a):
    minim = min(a)
    maxim = max(a)
    media_arit = (minim+maxim)/2
    media_geo = (minim*maxim)**0.5
    return media_arit, media_geo
#print(myfunc6([5, 6 ,7, 8]))

#ex12
def myfunc7(a):
    mij = len(a)//2
    prima_jum = a[:mij]
    a_doua_jum = a[mij:]
    maxim = max(prima_jum)
    minim = min(a_doua_jum)
    return maxim, minim
#print(myfunc7([1,2,3,4,5,6,7,8,9]))

#ex13
def myfunc8(a):
    rez = []
    for nr in a:
        if (myfunc3(nr)):
            s=str(nr)
            if(len(s)%2==0):
                rez.append(s)

    return rez
#print(myfunc8([1,222,312,444,56765,66,77,8,9]))

#ex14
def myfunc9(a):
    minim = min(a)
    maxim = max(a)
    poz_min = a.index(minim)
    poz_max = a.index(maxim)
    start = min(poz_min, poz_max)
    stop = max(poz_min, poz_max)
    return a[start:stop+1]

#print(myfunc9([1,2,3,4,5,6,7,8,9]))

#ex15
def myfunc10(a):
    diag = []
    n = len(a)
    for i in range(n)
        diag.append(a[i][i])
    diag.sort(reverse=True)
    return diag
