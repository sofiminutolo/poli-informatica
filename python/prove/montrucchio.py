from datetime import datetime 
import matplotlib.pyplot as pyplot
sensore34 = open("fireworks_34.csv", "r")
prima_linea = sensore34.readline() #perche è il "titolo", così è ignorata
asse_x = []
asse_y = []
for linea in sensore34:
    linea = linea.strip() # per l' a capo
    campi = linea.split(",") # le divide dove c'e la prima virgola
if campi[1] != "" :
    asse_x.append(datetime.strptime(campi[0]), "%Y - %m - %d %H:%M : %")
    asse_y.append(round(float(campi[1])))

pyplot.figure(figsize=(10,4))
pyplot.plot(asse_x,asse_y)
pyplot.savefig("figura.jpg")
sensore34.close()                   