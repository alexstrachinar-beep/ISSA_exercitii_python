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
