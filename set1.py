#ex1
import math
def ex1(*nr):
    return math.gcd(*nr)

#print(ex1(12, 24, 32))

#ex2
def ex2(a):
    vocale = 'aeiouAEIOU'
    i = 0
    for caracter in a:
        if caracter in vocale:
            i += 1
    return i
#print(ex2('alabala'))

#ex3
def ex3(a):
    spatii = ' ,.!?;'
    i=0
    for caracter in a:
        if caracter in spatii:
            i += 1
    return i

#print(ex3('ana are mere.'))

#ex4
def ex4(a,b):
    return b.count(a)
#print(ex4('ana','ana are multe ana'))

#ex5
def ex5(a):
    caractere = ['\r','\n','\t','\a','\b','\f','\v']
    for c in caractere:
        if c in a:
            return True
    return False

#ex6
def ex6(a):
    rez = []
    for i,c in enumerate(a):
        if c.isupper():
            if i>0:
                rez.append("_")
        rez.append(c.lower())
    else:
        rez.append(c)

    return "".join(rez)
#print(ex6('UpperCamelCase'))

#ex7
def ex7(char_len,*a):
    if len(a) < 2:
        return True

    for i in range(len(a)-1):
        cuv_curent = a[i].lower()
        cuv_urmator = a[i+1].lower()
        sfarsit = cuv_curent[-char_len:]
        inceput = cuv_urmator[:char_len]

        if sfarsit != inceput:
            return False
    return True

#print(ex7(2,'fazan', 'antena','nasture'))

#ex8
#--

#ex9
#--
