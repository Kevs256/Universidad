import math

inicial=2
final=50
##deben haber 15

divisores=2
siguiente=0
resultados =[]

for i in range(0,final-inicial+1):
    numero=inicial+i
    raizcadauno=math.sqrt(numero)
    if (divisores>math.sqrt(numero)):
        primo=1
    while (divisores<=raizcadauno):
        primo=1
        if numero%divisores == 0:
            primo=0
            break
        divisores=divisores + 1
    divisores=2
    if (primo == 1):
        resultados.append(inicial+i)
print(resultados)
