from clases import *
import random

def jugar():
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")
    
    jugador.inicializar_tablero()
    maquina.inicializar_tablero()
    
    juego_terminado = False
    turno = "Jugador"
    
    while not juego_terminado:
        if turno == "Jugador":
            # Pedir coordenadas al jugador
            fila, columna = map(int, input("Introduce las coordenadas (fila columna): ").split())
            impacto = maquina.disparo(fila, columna)
            if impacto:
                print("¡Impacto!")
            else:
                print("Agua.")
                turno = "Máquina"
        else:
            # Turno de la máquina
            import random
            fila = random.randint(0, jugador.dimension - 1)
            columna = random.randint(0, jugador.dimension - 1)
            impacto = jugador.disparo(fila, columna)
            if impacto:
                print("La máquina hizo impacto en tu tablero.")
            else:
                print("La máquina falló.")
                turno = "Jugador"

        # Condición de victoria
        if np.all(maquina.tablero != "O"):
            print("¡Ganaste!")
            juego_terminado = True
        elif np.all(jugador.tablero != "O"):
            print("La máquina ganó.")
            juego_terminado = True



def recibir_disparo(tablero, fila, columna):
    try:
        if not (0 <= fila < 10 and 0 <= columna < 10):
            raise ValueError("Coordenada fuera del tablero.")
        if tablero[fila, columna] == "O":
            tablero[fila, columna] = "X"
            print(f"Disparo en ({fila},{columna}): ¡Impacto!")
        elif tablero[fila, columna] == " ":
            tablero[fila, columna] = "-"
            print(f"Disparo en ({fila},{columna}): Agua.")
        else:
            print(f"Disparo en ({fila},{columna}): Ya disparado antes.")
    except ValueError as e:
        print(e)
        # Solicita al usuario que vuelva a introducir las coordenadas




def selecciona_dificultad():
    print("Seleccione el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    try:
        nivel = int(input("Ingrese el número del nivel deseado: "))
        if nivel not in [1, 2, 3]:
            raise ValueError("Opción de dificultad no válida.")
        return nivel
    except ValueError as e:
        print(e)
        return selecciona_dificultad()

def disparo_maquina(tablero_jugador, dificultad):
    intentos = dificultad
    for _ in range(intentos):
        fila, columna = random.randint(0, 9), random.randint(0, 9)
        recibir_disparo(tablero_jugador, fila, columna)

def pausa():
    input("Pulsa ENTER para continuar...")