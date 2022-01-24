import math

inicial=1000000000
final=1000000100

divisores=2
siguiente=0
resultados =[]

for i in range(0,final-inicial+1):
    numero=inicial+i
    raizcadauno=math.sqrt(numero)
    while (divisores<raizcadauno):
        primo=1
        if numero%divisores == 0:
            primo=0
            break
        divisores=divisores + 1
    divisores=2
    if (primo == 1):
        resultados.append(inicial+i)
print(resultados)
