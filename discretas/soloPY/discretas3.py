numeroInicial=1000
numeroFinal=10000

def fiboRange(numeroInicial,numeroFinal):
    n=1
    anUno=1
    anDos=1
    anTres=0
    print("1")
    print("1")
    while(n<=numeroFinal):
        anTres=anUno+anDos
        anUno=anDos
        anDos=anTres
        if (n>=numeroInicial):
            print(anTres)
        n=n+1
        

fiboRange(numeroInicial,numeroFinal)

