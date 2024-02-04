# conteggio vocali
"""frase = input("Scrivi una frase: ")
def count_vowels(frase) :
    vocali = 0
    for i in frase :
        if i in ("AEIOUaeiou"):
            vocali = vocali +1
    print(vocali)        

count_vowels(frase)"""

# conteggio parole
"""frase = input("Scrivi una frase: ")
def count_words(frase) :
    prev = None
    parole = 1
    for i in frase.strip() :
        if i == " " and prev != " " :
            parole = parole + 1
        prev = i    
    print(parole)      

count_words(frase)"""

# Solidi geometrici
"""import math
r = float(input("Raggio: "))
h = float(input("Altezza: "))
def sphere_volume(r):
    V = (4* math.pi * r**3 ) / 3
    print(V)

def sphere_surface(r):
    S = 4 * math.pi * r**2
    print(S)

def cylinder_volume(r, h):
    V = math.pi * r**2 * h
    print(V)    

def cylinder_surface(r, h):
    S = (2 * math.pi * r * h) + (r**2 * math.pi)
    print(S)

def cone_volume(r, h):
    V = (math.pi * r**2 * h)/ 3
    print(V)   

def cone_surface(r, h):
    S = math.pi * r * (math.sqrt(h**2 + r**2)+r) 
    print(S)    

sphere_volume(r)
sphere_surface(r)
cylinder_volume(r, h)
cylinder_surface(r, h)
cone_volume(r, h)
cone_surface(r, h)"""

# saldo bancario
"""anni = int(input("numero anni: "))
Si = int(input("saldo iniziale: "))
i = int(input("tasso d' interesse: "))

def soldi(anni, Si, i) :
    for h in range(anni) :
        Totale = Si * ((i + 100)/ 100)
        Si = Totale
    print(Totale)

soldi(anni, Si, i)"""

# ONG
"""figli = int(input("Numero figli: "))
reddito = int(input("Reddito annuale: "))
def sussidio(figli, reddito) :
    soldi = 0
    if 30000 <= reddito < 40000 and figli >= 3 :
        soldi = 1000 * figli
    elif 20000 <= reddito < 30000 and figli >= 2 :
        soldi = 1500 * figli
    elif reddito < 20000 :
        soldi = 2000 * figli
    else :
        print("La famiglia non è elegibile per il sussidio")            
    print(f"Il sussidio è di {soldi}€")
sussidio(figli, reddito)""" 

# numeri romani
"""def convertitore(s) :
    valore = 0
    for i in s :
        if i == "I" :
            valore = 1
        if i == "V" :
            valore = 5
        if i == "X" :
            valore = 10
        if i == "L" :
            valore = 50
        if i == "C" :
            valore = 100
        if i == "D" :
            valore = 500
        if i == "M" :
            valore = 1000 
    return valore          
totale = 0
s = input("Inserisci numero romano: ")
valore = 0
prec = 0
for i in s[:2] :
        convertitore(s)
        prec = convertitore(s)
for i in s[1:] :
    convertitore(s)
    if len(s) == 1 or prec >= valore :
        totale = totale + valore
        prec = convertitore(s)
    else :
        differenza = valore - prec
        totale = totale - differenza
    print(totale)"""    

# resistenza aerodinamica
"""v = float(input("Velocità dell'auto (m/s): "))
def resistenza(v):
    d = 1.23 # kg/m^3
    A = 2.5 # m^2
    Cd = 0.2 # coeff resistenza aerodinamica
    Fd = 0.5 * d * v**2 * A * Cd
    return Fd

def potenza(v):
    Fd = resistenza(v)
    P = Fd * v
    return P

def cavalli(v) :
    P = potenza(v)
    Hp = P / 745.7
    return Hp

print(f"la forza di resistenza è {resistenza(v)} N, la potenza sviluppata è {potenza(v)} W = a {cavalli(v)} cavalli")"""

# Filo elettrico
"""import math
AWG = int(input("Calibro del filo: "))
l = float(input("Lunghezza del filo: "))
def diameter(AWG):
    d = 0.127 * 92 ** (( 36- AWG)/ 39)
    return d

def copper_wire_resistance(l, AWG):
    rho = 1.678 * 10**(-8)
    R = (rho*l*4)/ (math.pi * diameter(AWG)**2)
    return R 

def aluminium_wire_resistance(l, AWG):
    rho = 2.82 * 10**(-8)
    R = (rho*l*4)/ (math.pi * diameter(AWG)**2)
    return R

print(f"La resistenza del filo di rame è {copper_wire_resistance(l, AWG)} ohm\nLa resistenza del filo d'alluminio è {aluminium_wire_resistance(AWG,l)} ohm")"""
