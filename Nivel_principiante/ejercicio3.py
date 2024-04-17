import os

peso_ideal = 0
sobrepeso = 0
obesidad_grado_I = 0
obesidad_grado_II = 0
obesidad_grado_III = 0

personas = int(input('Digite la cantidad de alumnos: '))
for i in range(personas):
    print("\nalumno", i + 1)
    nombre = input('Cual es el nombre del alumno: ')
    edad = int(input('Ingrese la edad: '))
    peso = float(input('Ingrese su peso en kg: '))
    alt = float(input('Ingrese su altura en metros: '))

    IMC = (peso/ (alt**2))
    if IMC >= 18.5 and IMC <= 24.9: 
        peso_ideal += 1    
    elif IMC >= 25.0 and IMC <= 29.9: 
        sobrepeso += 1        
    elif IMC >= 30.0 and IMC <= 34.9: 
        obesidad_grado_I += 1        
    elif IMC >= 35.0 and IMC <= 39.9: 
        obesidad_grado_II += 1        
    elif IMC >= 40.0: 
        obesidad_grado_III += 1
        
os.system('cls')

print("1. Estuantes que se encuentra en peso ideal: ", peso_ideal)
print ("2. alumno que se encuentra en estado de sobrepeso :", sobrepeso)
print ("3. alumno que se encuentra en estado de obesidad grado I :", obesidad_grado_I)
print ("4. alumno que se encuentra en estado de obesidad grado II :", obesidad_grado_II)
print ("4. alumno que se encuentra en estado de obesidad grado III :", obesidad_grado_III)