"""def fattoriale(valore):
    risultato = valore
    if valore == 0:
        risultato = 1
    else :
        for i in range(valore -1, 1, -1) :
            risultato = risultato * i 
    return risultato    

numero = int(input("Inserisci un numero: "))    
print(fattoriale(numero))"""

"""def scatola(parola) :
    a = len(parola)
    b = "*" * (a +6)
    print(b)
    print(f"<3 {parola} <3")
    print(b)
parola = input("Scrivi qualsiasi cosa: ")
print(scatola(parola))"""

#string split e maxsplit
stringa = "domenica,vado,al,salame,non,vedo,l',ora,sia,domenica" 
lista2 = list(stringa) # rende una lista la stringa
lista = stringa.split(',')
stringa3 = "<3" .join(lista2)
print(lista)
stringa2 = "suca" .join(lista) # sostituisce la virgola con " "
posizione= lista.index('domenica')
"""elemento = lista.pop() """# ti dAA l'ultimo elemento della lista
# per partire da destra uso la r split
lis = stringa.rsplit(',', maxsplit= 2)

print(stringa2)
print(stringa3)
print(posizione)