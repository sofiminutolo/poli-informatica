def partite(file):
    with open(file,"r", encoding="utf-8") as f :
        partite=[]
        for riga in f :
            campi = riga.rstrip("\n").split(":")
            partite.append([(campi[0],int(campi[2])),(campi[1],int(campi[3]))])
    return partite        

def assegna_punti(partite):
    punti = {
        "Inter": 0,
        "Milan":0,
        "Juventus":0,
        "Roma":0
    }
    gol = {
        "Inter": (0,0),
        "Milan":(0,0),
        "Juventus":(0,0),
        "Roma":(0,0)
    }
    for partita in partite :
        gol[partita[0][0]][0] += partita[0][1]
        gol[partita[0][1]][1] += partita[1][1]
        if partita[0][1] > partita[1][1]:
            punti[partita[0][0]]+=3
        if  partita[0][1] == partita[1][1]:
            punti[partita[0][0]] += 1
            puntic+= 1
        if partita[0][1] < partita[1][1]:
            punti[partita[1][0]]+= 3
    return punti, gol

print(assegna_punti(partite("torneo.txt")))