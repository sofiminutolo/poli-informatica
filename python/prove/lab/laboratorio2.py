'''a = int(input("inserisci un numero: "))
b = int(input("inserisci un altro numero: "))
somma = a + b
differenza = a - b
prodotto = a*b
media = (a + b)/ 2
distanza = abs(differenza)
M = max(a,b)
m = min(a,b)
print(f"Somma = {somma :>7} \ndifferenza = {differenza} \nprodotto = {prodotto :>4} \nmedia = {media :>7} \ndistanza = {distanza :>4} \n M = {M :>10} \n m = {m :>10}")'''

'''numero = input("inserisci un numero di 5 cifre ")
for i in numero :
    print(i)'''

'''auto = int(input("Prezzo dell'auto? "))
km = int(input("Km percorsi in un anno? "))
carburante = float(input("Prezzo del carburante? "))
efficienza = float(input("Litri di benzina per 100km? "))
valore = int(input("Valore dell'auto dopo 5 anni? "))

spesa= auto + (((efficienza * km)/ 100)* carburante * 5) - valore
print(f"L'auto in 5 anni ti è costata {spesa}€!")'''

'''import math
q1 = float(input("Carica della prima particella: "))
q2 = float(input("Carica della seconda particella: "))
r = float(input("Distanza tra le cariche: "))
Fc = (q1*q2)/(4* math.pi * 8.854* pow(10,(-12)) * pow(r,2)) 
print(f"La forza di Coulomb tra le cariche è : {Fc}!")'''

'''parola = input("Scrivi una parola: ")
if len(parola) >= 6 :
    print(f"{parola[:round(len(parola)/2)]} ... {parola[(-round(len(parola)/2)):]}")'''

'''cell = input("Scrivi un numero di telefono: ")
a = cell[:3]
b = cell[3:6]
c = cell[6:]
print(f"({a}){b}-{c}")'''

