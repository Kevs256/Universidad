numero=input("ingrese el numero a transformar")
baseInicial=input("ingrese la base de el numero anterior")
baseFinal=input("ingrese la base a la que quiere transformar")

def tentoOther(numero,baseFinal):
    numero=int(numero)
    baseFinal=int(baseFinal)
    dividendo=numero
    divisor=baseFinal
    residuo=1
    cociente=1
    numeros=[]
    while(dividendo>=divisor):
        residuo=dividendo%divisor
        cociente=dividendo//divisor
        dividendo=cociente
        numeros.append(residuo)
    numeros.append(cociente)
    numeros.reverse()
    return numeros

def othertoTen(numero,baseInicial):
    digitos=len(str(numero))
    baseInicial=int(baseInicial)
    uno=1
    resultado=0
    for n in str(numero):
        numeroFinal=int(n)*baseInicial**(digitos-uno)
        resultado=resultado+numeroFinal
        uno=uno+1
    return resultado

def revisor(numero,baseInicial):
    #0 valido y 1 invalido
    for n in numero:
        if (int(n)>=int(baseInicial)):
            validacion=1
            break
        else:
            validacion=0
    return validacion

validacion=revisor(numero,baseInicial)

if (validacion==0):
    if (baseInicial == "10"):
        resultado=tentoOther(numero,baseFinal)
        print("el resultado en base ",baseInicial,"a base ",baseFinal,"es ", resultado)
    elif (baseInicial != "10"):
        preresultado=othertoTen(numero,baseInicial)
        resultado=tentoOther(preresultado,baseFinal)
        print("el resultado en base ",baseInicial,"a base ",baseFinal,"es ", resultado)
else:
    print("ha introducido un numero invalido para relizar el cambio de base, ya que uno de los digitos del numero es mayor que la base donde se desarrolla")