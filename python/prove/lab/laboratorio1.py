'''inizio1 = int(input("A che ora inizia il primo appuntamento? "))
fine1 = int(input("A che ora finisce il primo appuntamento? "))
inizio2 = int(input("A che ora inizia il secondo appuntamento? "))
fine2 = int(input("A che ora finisce il secondo appuntamento? "))
if inizio1 > inizio2 :
    s = inizio1
else :
    s = inizio2
if fine1 < fine2 :
    e = fine1
else :
    e = fine2
if s < e :
    print("Gli appuntamenti si sovrappongono")
else :
    print("Gli appuntamenti non si sovrappongono")'''

'''mese = int(input("Numero del mese? "))
giorno = int(input("Numero del giorno? "))
if mese in[1,2,3] :
    stagione = "inverno" 
elif mese in[4,5,6] :
    stagione = "primavera"
elif mese in[7,8,9] :
    stagione = "estate"
elif mese in[10,11,12] :
    stagione = "autunno"
if mese %3 ==0 and giorno >= 21 :
    if stagione == "inverno" :
        stagione = "primavera"
    elif stagione == "primavera" :
        stagione = "estate"
    elif stagione == "estate" :
        stagione = "autunno"
    else :
        stagione = "inverno"
print(stagione)'''

'''km = float(input("Quanti chilometri hai percorso? "))
volte = int(input("Quante volte sei andato al lavoro? "))
distanza = float(input("Quanto dista il luogo dove lavori da casa? "))
percentuale1 = (distanza * volte * 100) / km
percentuale2 = 100 - percentuale1
print("La percentuale di utilizzo della macchina per andare al lavoro è", percentuale1)
print("La percentuale di volte che la macchina è stata usata per altri scopi è", percentuale2)'''

'''a = int(input("Numero di blocchi in una riga? "))
b = int(input("Numero di blocchi in una colonna? "))
inizio = input("Colore di partenza? ")
pari = int(round(b/2))
if b %2== 0 :
    for b in range(0,pari) :
        if inizio == "nero" :
            print("NB"*a)
            print("BN"*a)
        if inizio == "bianco" :
            print("BN"*a)
            print("NB"*a)
else :
    for b in range(0, int((b-1)/2)) :
        if inizio == "nero" :
            print("NB"*a)
            print("BN"*a)
        if inizio == "bianco" :
            print("BN"*a)
            print("NB"*a)
    for b in range(int(b-1),b) :
        if inizio == "nero" :
            print("NB"*a)
        elif inizio == "bianco" :
            print("BN"*a)'''

'''print("viva l'informatica cazzo!!!!!!")'''

'''numeri = [1,2,3,4,5,6,7,8,9,10]
tot = sum(numeri)
print(tot)'''

'''tot = 1
for i in range(1,10):
    tot *= i
print(tot)'''

'''sofia = "sofia"
for lettere in sofia :
    print(lettere)'''

'''liquidità = 1
saldo = int(1000)
interesse = int(5)
for i in range(3):
    liquidità = saldo * ((100+interesse)/100)
    saldo = liquidità
    print(liquidità)'''


"""sofia = "sofia"
l = len(sofia)
print("+","--"*l,"+")
print("|  ",sofia,"   |")
print("+","--"*l,"+")
print("    v")
print("  /)/)")
print("( . .)")
print("( づ♡)")"""

'''numeri = [1,2,3,4,5,6,7,8]
lettere = ["a","b","c","d","e","f","g","h"]
for i in range(8) :
    print(numeri[i])
    print(lettere[i])

print("01010")
for i in range(2):
    print("10101") 
    print("01010")'''  

'''print("-"*100)'''

'''print("0"*100)'''



