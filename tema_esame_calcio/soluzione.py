import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
print(script_directory)

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
        squadraCasa, golCasa = partita[0]
        squadraFuori, golFuori = partita[1]
        gol[squadraCasa] = (gol[squadraCasa][0] + golCasa,gol[squadraCasa][1] + golFuori )
        gol[squadraFuori] = (gol[squadraFuori][0] + golFuori,gol[squadraFuori][1] + golCasa )
        
        if golCasa > golFuori:
            punti[squadraCasa]+=3
        if  golCasa == golFuori:
            punti[squadraCasa]+=1
            punti[squadraFuori]+=1
        if golCasa < golFuori:
            punti[squadraFuori]+=3
    return punti, gol

def getRiepilogo(punti, goal):
    riepilogo=[]
    for k in punti.keys():
        fatti,subiti = goal[k]
        score=punti[k]
        riepilogo.append({"nome":k,"punti":score,"goal_fatti":fatti,"goal_subiti":subiti})
    return riepilogo

def orderBy(dictionaryList,propertyName,idName):
    sortableList = []
    for itm in dictionaryList:
        sortValue = itm[propertyName]
        idValue = itm[idName]
        sortableList.append((sortValue,idValue,itm))
    sortableList.sort()
    return [item for _,_,item in sortableList]
    
    

def main():
    punti, gol = assegna_punti(partite(script_directory+"/torneo.txt"))
    riepilogo = getRiepilogo(punti=punti,goal=gol)
    classifica = orderBy(riepilogo,"punti","nome")
    classifica.reverse()
    print("============")
    print(" Classifica ")
    print("============")
    for n,info in enumerate(classifica):
        icon = "  "
        if(n==0):
            icon = "\U0001F3C6"
        elif(n==1):
            icon = "\U0001F948"
        elif(n==2):
            icon = "\U0001F949"
        elif(n==len(classifica)-1):
            icon = "\U0001F4A9"
        print("{n} - {i[nome]:10} {ico} : Punti {i[punti]:2}, Goal Fatti:{i[goal_fatti]:2}, Goal Subiti:{i[goal_subiti]:2}   ".format(n=n,i=info,ico=icon))
    print()
    print("=================")
    print(" Miglior attacco ")
    print("=================")
    classifica = orderBy(riepilogo,"goal_fatti","nome")
    classifica.reverse()
    for n,info in enumerate(classifica):
        print("{n} - {i[nome]:10} : Goal Fatti:{i[goal_fatti]:2}".format(n=n,i=info))
    print()
    print("=================")
    print(" Miglior difesa ")
    print("=================")
    classifica = orderBy(riepilogo,"goal_subiti","nome")
    for n,info in enumerate(classifica):
        print("{n} - {i[nome]:10} : Goal Subiti:{i[goal_subiti]:2}".format(n=n,i=info))




main()
