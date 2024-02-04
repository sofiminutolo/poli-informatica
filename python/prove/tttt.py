chimica = open("C:\\poli\\informatica\\testarello.txt" , "r", encoding="UTF-8")
parole_testo = set()

for riga in chimica :
    riga = riga.lower()
    parole = riga.split()
    for v in parole :
        if v.isalpha():
            parole_testo.add(v)


n_parole = len(parole_testo)

print(f"Il testo ha {n_parole} parole diverse")