nomi = open("C:\\poli\\informatica\\python\\nomi.txt", "r", encoding="utf-8")
paroleita = open("C:\\poli\\informatica\\python\\paroleita.txt", "r", encoding="utf-8")

tutteparole= set()
insiemenomi = set()
alfabeto = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", "r","s","t","u","v","w","x","y","z"]

for nome in nomi:
    insiemenomi.add(nome.rstrip("\n").lower())

storpiate = dict.fromkeys(insiemenomi)

for parola in paroleita:
    tutteparole.add(parola.rstrip("\n").lower())    


for nome in insiemenomi:
    for lettera in nome :
        for valore in alfabeto :
            nuova = valore
            storpiata = nome.replace(lettera,nuova)
            setstorpiate = storpiate[nome]
            if setstorpiate == None:
                setstorpiate = set
                storpiate[nome] = setstorpiate
            if storpiata in tutteparole:
                setstorpiate.add(storpiata)
print(storpiate)