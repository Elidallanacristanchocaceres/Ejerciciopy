class Jugador:
    def __init__(self, id_jugador, name, años, catego):
        self.id_jugador = id_jugador
        self.name = name
        self.años = años
        self.catego = catego
        self.part_jugados = 0
        self.part_ganados = 0
        self.part_perdidos = 0
        self.punt_a_favor = 0

class TorneoTenisDeMesa:
    def __init__(self):
        self.catego = {'Novato': [], 'Intermedio': [], 'Avanzado' : []}

    def regis_jugador(self, id_jugador, name, años, catego):
        jugador = Jugador(id_jugador, name, años, catego)
        if catego in self.catego.keys():
            if (catego == 'Novato' and 15 <= años <= 16) or \
               (catego == 'Intermedio' and 17 <= años <= 20) or \
               (catego == 'Avanzado' and años > 20):
                self.catego[catego].append(jugador)
                print(f"{name} Se encuentra en el torneo de tenis de mesa de la categoría {catego} :")
            else:
                print(f"{name} es demasiado joven o viejo para ser novato, intermedio o avanzado :")
        else:
            print("Hay un problema, no se encuentra esa catego. :")

    def ini_torneo(self):
        for catego, jugadores in self.catego.items():
            if len(jugadores) < 5:
                print(f"Hace falta más jugadores en la categoría {catego} para poder iniciar el torneo :")
            else:
                print(f"Comienza el torneo de tenis de mesa en la categoría {catego} :")

    def registrar_partido(self, id_juga_ganador, id_juga_perdedor, punt_ganador, punt_perdedor):
        juga_ganador = None
        juga_perdedor = None

        for catego, jugadores in self.catego.items():
            for jugador in jugadores:
                if jugador.id_jugador == id_juga_ganador:
                    juga_ganador = jugador
                elif jugador.id_jugador == id_juga_perdedor:
                    juga_perdedor = jugador

        if juga_ganador is not None and juga_perdedor is not None:
            juga_ganador.part_jugados += 1
            juga_perdedor.part_jugados += 1
            juga_ganador.part_ganados += 1
            juga_perdedor.part_perdidos += 1
            juga_ganador.punt_a_favor += punt_ganador - punt_perdedor
            print("El partido fue registrado con exito :")
        else:
            print("Hubo un error, no se encontro ninguno de los jugadores :")

    def mostrar_estadis(self):
        for catego, jugadores in self.catego.items():
            print(f"--- Categoría: {catego} ---")
            print("ID Jugador Partidos Jugados Partidos Ganados Partidos Perdidos punt a Favor :")
            for jugador in jugadores:
                print(f"{jugador.id_jugador} {jugador.name} {jugador.part_jugados} {jugador.part_ganados} {jugador.part_perdidos} {jugador.punt_a_favor}")

    def obtener_ganador_catego(self, catego):
        if catego in self.catego.keys():
            jugadores_catego = self.catego[catego]
            if jugadores_catego:
                ganador = max(jugadores_catego, key=lambda jugador: jugador.punt_a_favor)
                print(f"¡El ganador que esta en la categoría {catego} es {ganador.name} con {ganador.punt_a_favor} punt a favor! :")
            else:
                print(f"No se encontro jugadores registrados en la catego {catego} :")
        else:
            print("¡Esta catego no se encuntra registrada, coloca una valida :")

def regis_jugador_manualmente(torneo):
    id_jugador = int(input("Siguiente opc, ingresa el ID del jugador : "))
    name = input("¿Cual es el nombre del jugador? : ")
    años = int(input("Escriba los años que tiene? : "))
    catego = input("Selecciona la catego en la que quieres inscribirlo? ***(Novato/Intermedio/Avanzado)*** : ")
    torneo.regis_jugador(id_jugador, name, años, catego)

# Función principal
def main():
    torneo = TorneoTenisDeMesa()
    while True:
        
        print("\n**** Menú **** : ")
        print("-1. *Registrar un jugador : ")
        print("-2. *Iniciar el torneo :")
        print("-3. *Registrar resultado de un partido : ")
        print("-4. *Mostrar las estadísticas :")
        print("-5. *Obtener el ganador de una categoría :")
        print("-6. *Salir")
        opc = input("Escoge la opc que desees: ")
        continuar = input("¿Desea registrar un jugador? (s/n) : ")

        if opc == "1":
            regis_jugador_manualmente(torneo)
        elif opc == "2":
            torneo.ini_torneo()
        elif opc == "3":
            id_juga_ganador = int(input("Escribe el ID del jugador ganador : "))
            id_juga_perdedor = int(input("Escribe el ID del jugador perdedor : "))
            punt_ganador = int(input("Caules fueron los punt del jugador ganador : "))
            punt_perdedor = int(input("Cuales fueron los punt del jugador perdedor : "))
            torneo.registrar_partido(id_juga_ganador, id_juga_perdedor, punt_ganador, punt_perdedor)
        elif opc == "4":
            torneo.mostrar_estadis()
        elif opc == "5":
            catego = input("Escoge la categoría en la que quieres conocer al ganador? : ")
            torneo.obtener_ganador_catego(catego)
        elif opc == "6":
            print("¡Haz finalizado, hasta luego!")
            break
        else:
            print("La pción que ingresaste no es válida. Coloca una opción del 1 al 6 de lo contrario sera erroneo :")

if __name__ == "__main__":
    main()
