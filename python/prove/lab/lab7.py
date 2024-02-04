# somma segni alterni
"""numeri = []
giusta = []
n = None
while n != "" :
    n = (input("Inserire numero : "))
    numeri.append(n)
for i in numeri[:-1] :
    n = int(i)
    giusta.append(n)
tot = 0
for i in giusta :
    if giusta.index(i)%2 == 0:
        tot = tot + i
    else :
        tot = tot -i
print(tot)"""

# lista numeri casuali
"""import random
lista = []
pari = []
indicep = []
contrario= []
n = None
for i in range(10) :
    n = random.randint(1,100)
    lista.append(n)
print(lista)
for i in lista:
    if i %2 == 0:
        pari.append(i)
    if lista.index(i) %2 ==0:
        indicep.append(i)
for i in lista[::-1]:
    contrario.append(i)
u = lista.pop()    
p = lista.pop(0)
print(f"Gli elementi di indice pari sono: {indicep}\nGli elementi pari sono: {pari}\nLa lista al contrario è: {contrario}\nil primo elemento è {p} e l'ultimo è {u}")"""

# rimuovere valore minimo
"""numeri = []
v = []
n = None
while n != "" :
    n = (input("Inserire numero : "))
    numeri.append(n)
for i in numeri[:-1] :
    n = int(i)
    v.append(n)
def remove_min(v):
    minimo = None    
    for i in v:
        if minimo == None :
            minimo = i
        if i >= minimo :
            minimo = minimo
        if i < minimo :
            minimo = i
    for i in v :
        if i == minimo :
            pos = v.index(i)
    finito = v.pop(pos)   
    print(v)      
    print(finito)          
remove_min(v)"""


def findLocalMaxima(v):
    maxl = []
    if len(v) >= 3 :
        for i in range(1, len(v) - 1) :
            if v[i-1] < v[i] and v[i] > v[i+1] :
                maxl.append(i)
    return maxl 
numeri = []
v = [3,4,2,12,6,7,9,10,2,34,12]
n = None
# while n != "" :
#     n = (input("Inserire numero : "))
#     numeri.append(n)
# for i in numeri[:-1] :
#     n = int(i)
#     v.append(n)
maxl=findLocalMaxima(v)
if maxl == [] :
    print("Non ci sono massimi locali")
print(maxl)
minDist=9999999
idxMinDist=[]    
for i in range(len(maxl)-1):
    i1 = maxl[i]
    i2 = maxl[i+1]
    dist = i2 - i1
    if dist < minDist:
        minDist= dist
        idxMinDist = [(i1,i2)]
    elif dist == minDist:
        idxMinDist.append((i1,i2))
print(idxMinDist)

# stessi elementi ????
"""a = [1,8,3,4,4,5]
b = [5,5,4,3,2,1]
def sameset(a,b):
    for i in a :
        if i in b :
            pass
        else :
            print("Le liste non sono uguali")
            break
    for i in b :
        if i in a:
            pass
        else :
            print("Le liste non sono uguali")
            break
    print("Le liste coincidono")
sameset(a,b)"""

#ordinare lista
"""import random
numeri = []
for i in range(20) :
    i = random.randint(0,100)
    numeri.append(i)
print(numeri)
numeri.sort()
print(numeri)"""

# somma senza il minimo
"""import random
numeri = []
for i in range(10) :
    i = random.randint(0,100)
    numeri.append(i)
print(numeri)
def sum_without_smallest(numeri) :
    minimo = min(numeri)
    pos = numeri.index(minimo)
    numeri.pop(pos)
    print(numeri)
    somma = 0
    for i in numeri :
        somma = somma + i
    print(somma)    
sum_without_smallest(numeri)"""

# rumore di misura
"""lista = [1,2,3,3,5]
pos = None
for v in lista :
    if v == lista[0] :
        pos = 0
        nuovo_num1 = round((v + lista[pos+1])/2)
    elif v == lista[-1]:
        pos = len(lista) -1
        nuovo_num = round((v + lista[pos-1])/2)
        lista.pop(pos)
        lista.append(nuovo_num)
    else :
        pos = pos +1
        nuovo_num= round((v + lista[pos-1] + lista[pos+1])/3)
        lista.pop(pos)
        lista.append(nuovo_num)
    lista.pop(lista[0])
    lista.insert(nuovo_num1,0)    
print(lista)"""

#parcheggi
posti = int(input("Quanti posti ha il parcheggio? "))
parcheggio = []
libero = True
for p in range(posti) :
    parcheggio.append("_")    
metà = round(posti/2)
parcheggio.pop(metà)
parcheggio.insert(metà, "X")
for p in enumerate(parcheggio):
