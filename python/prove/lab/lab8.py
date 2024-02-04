# out of range error
"""lista = [1,2,3]
for i in lista:
    v = i + lista[6]"""

# buffer
"""lista = [1,2,3,4,5]
ultimo = len(lista) - 1
for v in lista :
    if v == lista[0]:
        lista.insert(0,lista[ultimo])
        break
for v in lista :    
    if v == lista[ultimo+1]:
        lista.pop(ultimo+1)
        break  
print(lista)"""

# Dadi
"""import random
lista = []
ldl = []
for v in range(20):
    lista.append(random.randrange(1,7))
print(lista)    
for v in lista :
    if ldl == [] :
        ldl.append([v])
    else :
        vl = ldl[-1] 
        if vl[0] == v :
            vl.append(v)
        else : 
            ldl.append([v])
sz = [len(v) for v in ldl]
print(sz)
firstmax = sz.index(max(sz))
for i,v in enumerate(ldl) :
    if i == firstmax:
        print("( ",end="")
    for n in v:
        print(n,end=" ")
    if i == firstmax:
        print(") ",end="")
print()"""

def tabellatore(tbl):
    for r,row in enumerate(tbl):
        print("#%-3s|" % r, end="")
        for v in row :
            print("%5s" % v, end="")
        print() # va a capo alla fine della riga


# Tabella
tabella = []
m = 4 # rige
n = 3 # colonne
"""for i in range(n):
    riga=[]
    tabella.append(riga)
    for i in range(m):
        riga.append(0)
print(tabella)"""
for i in range(m) :
    fila = [0]*n
    tabella.append(fila)
tabellatore(tabella)        