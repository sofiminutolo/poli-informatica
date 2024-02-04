""""inputfile = open("C:\\poli\\informatica\\python\\prove\\input.txt", "r", encoding = "UTF-8")
testo = inputfile.readlines()
testo.reverse()
outputfile = open("output.txt", "w", encoding = "UTF-8")
outputfile.writelines(testo)
inputfile.close()
outputfile.close()"""

"""variabile = "cacca"
testi = "cc.txt,cacca.txt,cesso.txt"
documenti = testi.split(",")
for v in documenti:
    testo = open(v, "r", encoding= "utf-8")
    righe = testo.readlines()
    for riga in righe :
        riga1 = riga.lower()
        if variabile in riga1 :
            print(f"{v}: {riga}", end ="")
    testo.close()"""


from sympy import *
init_printing()
var('x y z a')

import math 

x = Symbol('x')
solve_univariate_inequality()