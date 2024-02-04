try:
    testo = open("testo.txt", "r", encoding= "utf-8")
    righe_testo = testo.readlines()
    testo.close()

except IOError :
    print("File non trovato. fine del programma")   
    exit(-1)  
try :
    obsoleto = open("obsoleto.txt", "r", encoding="utf-8")
    righe_obsoleto = obsoleto.readlines()
    obsoleto.close()
    parola_nuova = {}
    for linee in righe_obsoleto:
        lista_linee = linee.strip().split()
        parola_nuova[lista_linee[0]]=[]
        parola_nuova[lista_linee[0]].append(lista_linee[1])
        parola_nuova[lista_linee[0]].append(0)
except IOError :
    print("File non trovato. fine del programma")   
    exit(-1) 

try :
    nuovo_testo = open("nuovotesto.txt", "w", encoding="utf-8")
except IOError :
    print("File non trovato. fine del programma")   
    exit(-1)

conta_parole = 0
for riga in righe_testo :
    parola_riga = riga.strip().spbblit()
    conta_parole += len(parola_riga)

    for parola in parola_nuova.keys():   