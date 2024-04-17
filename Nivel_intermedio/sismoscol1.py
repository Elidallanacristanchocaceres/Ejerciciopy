class Ciudad:
    def __init__(self, name):
        self.name = name
        self.sismos = []

    def agregar_sismo(self, magnitud):
        self.sismos.append(magnitud)

def regis_ciudad(cities):
    name_ciudad = input("Cual es el nombre de la ciudad: ")
    ciudad = Ciudad(name_ciudad)
    cities.append(ciudad)
    print("La cidad que ingresaste fue registrada con exito.")

def regis_sismo(cities):
    if not cities:
        print("No se encontraron ciudades registradas.")
        return

    magnitudes = []
    for ciudad in cities:
        magnitud = float(input(f"Cual es la magnitud del sismo en {ciudad.name} : "))
        magnitudes.append(magnitud)
        ciudad.agregar_sismo(magnitud)

    print("Los sismos fueron registrados con exito.")

def buscarSismosPorCiudad(cities):
    name_ciudad = input("Ingresa el nombre de la ciudad : ")
    for ciudad in cities:
        if ciudad.name.lower() == name_ciudad.lower():
            print(f"Sismos registrados en {ciudad.name}: {', '.join(map(str, ciudad.sismos))}")
            return
    print("La ciudad que ingresaste no se encuentra.")

def riesgoDeInforme(cities):
    if not cities:
        print("No se encontraron ciudades registradas.")
        return

    for ciudad in cities:
        prome = sum(ciudad.sismos) / len(ciudad.sismos)
        if prome < 2.5:
            print(f"Esta ciudad {ciudad.name} se encuentra en riesgo amarillo.")
        elif 2.5 <= prome <= 4.5:
            print(f"Esta ciudad {ciudad.name} se encuntra en riesgo naranja.")
        else:
            print(f"Esta ciudad {ciudad.name} se encuentra en riesgo rojo.")

def main():
    cities = []

    while True:
        print("\nMenú:")
        print("1. regis de Ciudad")
        print("2. regis de Sismos")
        print("3. Buscar sismos por ciudad")
        print("4. Informe del riesgo")
        print("5. Finalizar")

        opcion = input("Ingrese el numero de la opcion que deseas : ")

        if opcion == "1":
            regis_ciudad(cities)
        elif opcion == "2":
            regis_sismo(cities)
        elif opcion == "3":
            buscarSismosPorCiudad(cities)
        elif opcion == "4":
            riesgoDeInforme(cities)
        elif opcion == "5":
            print("¡Haz finalizado, Hasta luego!")
            break
        else:
            print("La opcio que ingresaste no es valida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
