"""vs1 = {5:4 , 9:2, 10:9}

def vettoratore(diz) :
    lista = []
    for i in range(max(diz)+1):
        lista.append(0)
    for i in diz :
        lista[i] = diz[i]  
    return lista  
def sparse_array_sum(a, b):
    lista1 = vettoratore(a)
    lista2 = vettoratore(b)
    lista3 = []
    for i,v in enumerate(lista1) :
      lista3.append(v + lista2[i]) 
    return lista3, lista1, lista2

def main():
    a = {5:4 , 9:2, 10:9}
    b = {3:7, 8:4, 10:5}
    liste = sparse_array_sum(a, b)
    print(liste)
        
main()"""

# censura
testo = open("C:\\poli\\informatica\\python\\prove\\parolacce.txt", "r", encoding= "UTF-8")
testo2 = open("C:\\poli\\informatica\\python\\prove\\canzone.txt", "r", encoding= "UTF-8")
censurata = open("censurata.txt", "w", encoding="UTF-8")
canzone = testo2.read()
parole_canzone = canzone.split()
parole_censurate = []
righe = testo.readlines()
parolacce = set()

for parola in righe :
    parolacce.add(parola.strip())

testo.close()

for v in parole_canzone :
    if (v.strip()).lower() in parolacce:
        parole_censurate.append("*"* len(v))
    else :
        parole_censurate.append(v)
censurata.write(" ".join(parole_censurate))        