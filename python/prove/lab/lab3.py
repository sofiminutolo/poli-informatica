'''import math
if 1 == 1 :
    print("uguali")
if 1 == 1.0 :
    print("uguali")
if 2.0 == math.sqrt(2) :
    print("uguali")
if 1 == '1' :
    print("uguali")
if 'ciao' == 'Ciao' :
    print("uguali")
else :
    print("Diversi")'''

'''a = input("scrivi qualsiasi cosa ")
if a.isalnum() :
    print("La stringa contiene lettere e numeri")
if a.islower() :
    print("La stringa contiene solo lettere minuscole")
if a.isupper() :
    print("La stringa contiene solo lettere maiuscole")
if a.isalpha() :
    print("La stringa ha solo lettere")
if a.isdigit() :
    print("La stringa contiene solo numeri")
if a[:1] in['A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] :
    print("La stringa inizia con una lettera maiuscola ")
if a[-1:] is(".") :
    print("La stringa termina con un punto")'''

'''a = input("Scrivi una sequenza lunga a piacere di DNA contenente 'A' 'C' 'T' 'G': ")
b = input("Scrivi una sequenza di dna di sole tre lettere: ")
if b in a :
    print("La sequenza è contenuta nel dna")
    posizione = a.find(b)
    print(f"La frequenza compare per la prima volta nella posizione {posizione}")
    volte = a.count(b)
    print(f"La sequenza compare {volte} volte")'''

"""parola = input("Scrivi una frase: ")
contrario = (parola[::-1]) 
print(parola[::-1])
for i in contrario :
    if i.isupper() :
        print(i)"""

"""numero = int(input("Inserisci un numero: "))
primo = True
for i in range(2,numero) :
    if numero %i == 0 :
        primo = False
        break
if primo == False :
    print(f"Il numero {numero} non è primo!")
if primo == True :
    print(f"Il numero {numero} è primo!")"""

"""numero = int(input("Scegli un numero: "))    
for a in range(1,numero + 1 ) :
    primo = True
    if a > 1 :
        for b in range(2, a) :
            if (a % b) == 0:
                primo = False
                break
        if primo == True:
            print(a)"""   
     

"""def printWindow(parola, lunghezza, winLen):
    for a in range(lunghezza) :
        b = a + winLen
        if len(parola[a:b]) == winLen:
            print(parola[a:b])
parola = input("Scrivi una parola: ")
lunghezza = len(parola)
for i in range(len(parola)):
    printWindow(parola, lunghezza,i+1)"""


    
"""numero = "0"
prec = None
while numero != "" :
    numero = input("inserisci un numero: ")
    if numero != "" :
        n = int(numero)
prec = numero      
for i in len(numero):
    if prec == numero :
        print(prec)"""

#AIUTO
"""import random
inizio = random.randrange(10,101)
giocatore = random.randrange(0,2)
stupido = random.randrange(0,2)
bigle = 0
print(f"Il sacchetto contiene {inizio} bigle!")
if giocatore == 0 :
    print("Sei tu il primo a giocare!")
elif giocatore == 1 : 
    print("Il primo a giocare è il computer!")    
if stupido == 0 :
    print("Il computer giocherà in modo stupido")
elif stupido == 1 : 
    print("Il computer ti farà il culo")    
if giocatore == 1 and stupido == 0 :
    while inizio != 0 :
        if round(inizio) <= 2  :
            bigle = 1
            inizio = inizio - bigle
            print("Il computer estrae una biglia!")
            print(inizio)
            giocata = int(input("Quante bigle estrai? "))
            inizio = inizio - giocata
            print(inizio)
            if inizio == 0 :
                if giocata == 1 :
                    print("Vince il computer! ")
                else : 
                    print("Hai vinto!!")
        else :
            bigle= random.randrange(1, round(inizio/2))
            print(f"il computer estrae {bigle} bigle!")
            inizio = inizio - bigle
            print(inizio)
            giocata = int(input("Quante bigle estrai? "))
            inizio = inizio - giocata
            print(inizio)
if giocatore == 0 and stupido == 0 :
    while inizio != 0 :
        if round(inizio) <= 2  :
            bigle = 1
            inizio = inizio - bigle
            print("Il computer estrae una biglia!")
            print(inizio)
            giocata = int(input("Quante bigle estrai? "))
            inizio = inizio - giocata
            print(inizio)
            if inizio == 0 :
                if giocata == 1 :
                    print("Vince il computer! ")
                else : 
                    print("Hai vinto!!")
        else :
            giocata = int(input("Quante bigle estrai? "))
            inizio = inizio - giocata
            print(inizio)
            bigle= random.randrange(1, round(inizio/2))
            print(f"il computer estrae {bigle} bigle!")
            inizio = inizio - bigle
            print(inizio)"""
            
    