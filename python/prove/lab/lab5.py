# pin
"""giusto = "1234"
pin = input("Inserisci il pin di 4 cifre: ")
for i in range(2) :
    if pin == giusto :
        print("Your PIN is correct!")
        break
    if pin != giusto :
        print("Your pin is incorrect")
        pin = input("Inserisci il pin di 4 cifre: ")
for i in range(3,4) :
    if pin != giusto :
        print("Your bank card is blocked")"""

# paesi francesi
"""paese = input("Inserisci il nome di una nazione in francese: ")
if paese == "Etats-Unis" or "Pays-Bas" :
    print(f"Les {paese}")
for i in paese:
    if i in ["A","E","I","O","U"]:
        print(f"L'{paese}")
    break
else:
    for i in paese[:: -1]:
        if i == "e" :
            print(f"La {paese}")
        if i != "e" or paese == ("Belize", "Cambodge", "Cambodge", "Mozambique", "Zaïre", "Zimbabwe"):
            print(f"Le {paese}")"""

# Fattorizzazione interi
"""n = int(input("Inserisci un numero: "))
numero = 2
while n >1 :
    if n%numero == 0 : 
        print(numero)            
        n = n / numero    
    if n%numero != 0 :
        numero = numero +1
        if n%numero == 0 : 
            print(numero)            
            n = n / numero"""

# cinema
"""bigletti = 100
acquirenti = 0
while bigletti != 0 :
    comprati = int(input("Quanti bigletti desideri acquistare? (max 4) "))
    bigletti = bigletti - comprati
    print(bigletti)
    acquirenti = acquirenti + 1     
if bigletti == 0 :
    print(f"Gli acquirenti sono {acquirenti}")"""

# numeri random
"""a = 32310901
b = 1729
m = 2**24
rv = int(input("Inserisci un numero: "))
for i in range(100) :
    rn = (a * rv + b ) % m
    print(rn)
    rv = rn"""

# posizione ubriaco
"""import random
x = 0
y = 0
for i in range(101):
    sugiu = random.randrange(0,2)
    if sugiu == 0 :
        x = x + int(random.choice([1, -1]))
    if sugiu == 1 :
        y = y + int(random.choice([1, -1]))   
print(f"La posizione finale è ({x},{y})")"""

# trasformatori
Ro = 20
n = 0.01
Vs = 40
Rs = 8
for i in range(199) :
    Ps = Rs * ((n*Vs)/ n ** 2 * Ro + Rs )**2
    n = n + 0.01
    print(Ps, n)
