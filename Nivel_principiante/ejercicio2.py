import os
nombre = input('Cual es su nombre :')
edad = int(input('Ingrese su edad :'))

alt = float(input ("Cual es su altura :"))
peso = float (input("Cual es su peso :"))

IMC = float (peso/ (alt**2))
os.system('cls')
if IMC >= 18.5 and IMC <= 24.9 :
        print (f"El estudiante {nombre} con años {edad} IMC {IMC} su peso es NORMAL :")
elif IMC >= 25.0 and IMC <= 29.9 :
        print (f"El estudiante {nombre} con años {edad} IMC {IMC} su peso es SOBREPESO :")
elif IMC >= 30.0 and IMC <= 34.9:
        print (f"El estudiante {nombre} con años {edad} IMC {IMC} su peso es OBESIDAD 1 :")
elif IMC >= 35.0 and IMC <= 39.9 :
        print (f"El estudiante {nombre} con años {edad} IMC {IMC} su peso es OBESIDAD 2 :")
elif IMC >= 40.0 :
        print (f"El estudiante {nombre} con años {edad} IMC {IMC} su peso es OBESIDAD 3 :")

        



