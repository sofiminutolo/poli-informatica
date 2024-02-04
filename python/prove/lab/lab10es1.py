
def soluzione1(src,dst):
    filetxt = open(src, "r", encoding = "UTF-8")
    """while astr != "" :
        print(astr,end='')        # l'end fa in modo che tolga l'acapo che ti mette in automatico
        astr = filetxt.readline()"""


    testo = filetxt.readlines()
    filetxt.close()
    filetxt2 = open(dst, "w", encoding = "UTF-8")
    for n, riga in enumerate(testo):
        rigaout = f"/*{n+1}*/{riga}"
        filetxt2.write(rigaout)

    filetxt2.close()
    
def soluzione2(src=None,dst=None):
    filetxt = open(src, "r", encoding = "UTF-8")
    outfile = open(dst, "w", encoding = "UTF-8")
    for n, riga in enumerate(filetxt):
        print(f"/*{n+1}*/{riga}",file=outfile,end='')
    outfile.close()        
    filetxt.close()
# soluzione1("python\\prove\\testo2.txt","output2.txt")
soluzione2("python\\prove\\testo2.txt","output2.txt")