import os
total_numeros = 0
total_pares = 0
suma_pares = 0
contador_pares = 0
suma_impares = 0
contador_impares = 0
menores_10 = 0
entre_20_50 = 0
mayores_100 = 0

numero = int(input("Ingrese un número entero positivo (ingrese un número negativo para terminar): "))
while numero >= 0:

    total_numeros += 1
    
    if numero % 2 == 0:
        total_pares += 1
        suma_pares += numero
        contador_pares += 1
    else:
        suma_impares += numero
        contador_impares += 1
    
    if numero < 10:
        menores_10 += 1
    
    if 20 <= numero <= 50:
        entre_20_50 += 1
    
    if numero > 100:
        mayores_100 += 1

    numero = int(input("Ingrese otro número entero positivo (ingrese un número negativo para terminar): "))

os.system('cls')

print("Reporte:")
print("a. Total de números ingresados:", total_numeros)
print("b. Total de números pares ingresados:", total_pares)
if contador_pares != 0:
    promedio_pares = suma_pares / contador_pares
    print("c. Promedio de los números pares:", promedio_pares)
if contador_impares != 0:
    promedio_impares = suma_impares / contador_impares
    print("d. Promedio de los números impares:", promedio_impares)
print("e. Cuantos números son menores que 10:", menores_10)
print("f. Cuantos números están entre 20 y 50:", entre_20_50)
print("g. Cuantos números son mayores que 100:", mayores_100)
