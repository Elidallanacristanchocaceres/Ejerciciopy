class Dispositivo:
    def __init__(self, name, potencia_w):
        self.name = name
        self.potencia_w = potencia_w


class Dependencia:
    def __init__(self, name):
        self.name = name
        self.dispositivos = []

    def registrar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def calcular_consumo_kwh(self):
        consumo_total_kwh = 0
        for dispositivo in self.dispositivos:
            consumo_total_kwh += dispositivo.potencia_w / 1000
        return consumo_total_kwh


dependen = []


def record_dependence():
    name = input("Ingresa el nombre de la dependencia :")
    dependencia = Dependencia(name)
    dependen.append(dependencia)
    print("La dependencia se registro exitosamente.")


def register_consum():
    name = input("Coloca la dependencia en la que quieres registrar el consumo : ")
    for dependencia in dependen:
        if dependencia.name == name:
            name_dispositivo = input("Cual es el nombre del dispositivo? : ")
            potencia_w = float(input("Escribe la potencia del dispositivo en Watts : "))
            dispositivo = Dispositivo(name_dispositivo, potencia_w)
            dependencia.registrar_dispositivo(dispositivo)
            print("El consumo se registro con exito.")
            return
    print("La dependencia que ingreso no se encuentra registrada.")


def calcularEmisionesCo2(consumo_kwh, factor_emision):
    return consumo_kwh * factor_emision


def verCo2Producido():
    for dependencia in dependen:
        consumo_kwh = dependencia.calcular_consumo_kwh()
        print(f"Dependencia: {dependencia.name}")
        print(f"Consumo de electricidad (kWh): {consumo_kwh}")
        factor_emision = 0.5 / 1000  # Usando factor de emisión térmica como ejemplo
        emisiones_co2 = calcularEmisionesCo2(consumo_kwh, factor_emision)
        print(f"Emisiones de CO2 (tCO2eq): {emisiones_co2}")


def dependenciaMayorCo2():
    mayor_emisiones = 0
    dependencia_mayor = None
    for dependencia in dependen:
        consumo_kwh = dependencia.calcular_consumo_kwh()
        factor_emision = 0.5 / 1000  # Usando factor de emisión térmica como ejemplo
        emisiones_co2 = calcularEmisionesCo2(consumo_kwh, factor_emision)
        if emisiones_co2 > mayor_emisiones:
            mayor_emisiones = emisiones_co2
            dependencia_mayor = dependencia.name
    print(f"La dependencia que más CO2 produce es: {dependencia_mayor}")


def main():
    while True:
        print("\n** Menú Principal **")
        print("-1. *Registrar La Dependencia")
        print("-2. *Registrar El Consumo por Dependencia")
        print("-3. *Ver CO2 Producido")
        print("-4. *La Dependencia que Produce Mayor CO2")
        print("-5. *Finalizar")
        opc = input("Haz el siguiente paso, ingresa el número de la opción: ")

        if opc == "1":
            record_dependence()
        elif opc == "2":
            register_consum()
        elif opc == "3":
            verCo2Producido()
        elif opc == "4":
            dependenciaMayorCo2()
        elif opc == "5":
            print("Se finalizo el programa, vuelve pronto...")
            break
        else:
            print("La opc que colocaste no es válida Por favor, elige una opción correcta.")


if __name__ == "__main__":
    main()
