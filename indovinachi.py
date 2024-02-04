filep = open("C:\\poli\\informatica\\personaggi.txt", "r", encoding="utf-8")
filed1 = open("C:\\poli\\informatica\\domande1.txt","r", encoding="utf-8")
filed2 = open("C:\\poli\\informatica\\domande2.txt","r", encoding="utf-8")
filep.readline()

def dizionatore(file):
    personaggi = []
    tabella = []
    for riga in file :
        personaggio = {}
        lista = riga.rstrip("\n").split(";")
        personaggio["Nome"] = lista[0]
        personaggio["Sesso"] = lista[1]
        personaggio["Colore Capelli"] = lista[2]
        personaggio["Lunghezza Capelli"] = lista[3]
        personaggio["Occhiali"] = lista[4]
        personaggio["Cappello"] = lista[5]
        personaggio["Baffi"] = lista[6]
        personaggio["Barba"] = lista[7]
        personaggio["Pelato"] = lista[8]
        personaggi.append(personaggio)
    return personaggi

def leggimeli(lista) :
    for diz in lista :
        print(diz)     

def domande(file) :
    listadomande = []
    for riga in file :
        domanda = riga.rstrip("\n").split("=")
        listadomande.append(tuple(domanda))
    return listadomande

def matchatore(caratteristiche, personaggio) :
    for cara,valore in caratteristiche :
        if personaggio[cara] != valore:
            return False
    return True

def main(filedomande):
    personaggi = dizionatore(filep)
    leggimeli(personaggi)
    listadomande = domande(filedomande)
    for car, val in listadomande :
        ## personaggi = [personaggio for personaggio in personaggi if personaggio[car] == val ]
        print(f"Domanda : {car}={val}")    
        listafiltrata = []
        for personaggio in personaggi :
            if personaggio[car] == val:
                listafiltrata.append(personaggio)
        leggimeli(listafiltrata)
        personaggi=listafiltrata
    if len(personaggi) == 1 :
        print("Hai vintooooooo")
    else :
        print("Vabbè oh..")        




main(filed2)
