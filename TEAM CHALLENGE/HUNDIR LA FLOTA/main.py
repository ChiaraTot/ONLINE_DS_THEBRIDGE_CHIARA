#main.py

import numpy as np
from clases import Tablero

if __name__ == "__main__":
    print("------------------------------------------------------------------------")
    print("     ╔╗╔╗╔╗╔╗╔╗ ╔╗╔══╗ ╔══╗╔═══╗  ╔╗  ╔══╗  ╔══╗╔╗  ╔══╗╔════╗╔══╗")
    print("     ║║║║║║║║║╚═╝║║╔╗╚╗╚╗╔╝║╔═╗║  ║║  ║╔╗║  ║╔═╝║║  ║╔╗║╚═╗╔═╝║╔╗║")
    print("     ║╚╝║║║║║║╔╗ ║║║╚╗║ ║║ ║╚═╝║  ║║  ║╚╝║  ║╚═╗║║  ║║║║  ║║  ║╚╝║")
    print("     ║╔╗║║║║║║║╚╗║║║ ║║ ║║ ║╔╗╔╝  ║║  ║╔╗║  ║╔═╝║║  ║║║║  ║║  ║╔╗║")
    print("     ║║║║║╚╝║║║ ║║║╚═╝║╔╝╚╗║║║║   ║╚═╗║║║║  ║║  ║╚═╗║╚╝║  ║║  ║║║║")
    print("     ╚╝╚╝╚══╝╚╝ ╚╝╚═══╝╚══╝╚╝╚╝   ╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝  ╚╝  ╚╝╚╝")
    print("")
    print("╔════╗╔═══╗╔══╗╔╗  ╔╗  ╔═══╗╔══╗╔╗  ╔══╗ ╔═══╗╔╗ ╔╗   ╔╗╔╗╔══╗╔╗ ╔╗╔══╗ ")
    print("╚═╗╔═╝║╔══╝║╔╗║║║  ║║  ║╔══╝║╔╗║║║  ║╔╗╚╗║╔══╝║╚═╝║   ║║║║╚╗╔╝║╚═╝║║╔╗╚╗")
    print("  ║║  ║╚══╗║╚╝║║╚╗╔╝║  ║║╔═╗║║║║║║  ║║╚╗║║╚══╗║╔╗ ║   ║╚╝║ ║║ ║╔╗ ║║║╚╗║")
    print("  ║║  ║╔══╝║╔╗║║╔╗╔╗║  ║║╚╗║║║║║║║  ║║ ║║║╔══╝║║╚╗║   ║╔╗║ ║║ ║║╚╗║║║ ║║")
    print("  ║║  ║╚══╗║║║║║║╚╝║║  ║╚═╝║║╚╝║║╚═╗║╚═╝║║╚══╗║║ ║║   ║║║║╔╝╚╗║║ ║║║╚═╝║")
    print("  ╚╝  ╚═══╝╚╝╚╝╚╝  ╚╝  ╚═══╝╚══╝╚══╝╚═══╝╚═══╝╚╝ ╚╝   ╚╝╚╝╚══╝╚╝ ╚╝╚═══╝")
    print("")
    print("------------------------------------------------------------------------")
    print("                ¡¡Bienvedid@s a Hundir la Flota!!")
    print("            ¿Echamos una partidita? Sigue las instrucciones")
    print("------------------------------------------------------------------------")
    print("")
    print("")
    
    #Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
    # print("\n\nBienvenido al juego Hundir la Flota\n\nEstas son las instrucciones del juego:\n(1)blablabla\n(2)blablabla\n(3)blablabla\n")
    
    accion = input("Pulse Enter para jugar o 'q' para salir: ")
    if accion.lower() != 'q':

        #A continuación inicializa los tableros de ambos jugadores con los barcos.

        #Creamos los objetos tableros
        tab_humano = Tablero("humano1")
        tab_maquina = Tablero("maquina1")

        # Imprimimos los atributos del objeto tablero
        #print("\nJugadores:\n")
        #print("ID jugador humano:",tab_humano.jugador_id)
        #print("ID jugador máquina:",tab_maquina.jugador_id)
        #print(tab_humano.dimension)
        #print(tab_humano.tablero)
        #print(tab_humano.disparos)
        #print(tab_humano.barcos)
        
        print("\n\nGracias por jugar. Aquí están los tableros:")    

        # Inicializamos los tableros con barcos fijos o de coordenadas aleatorias
        tab_humano.ini_tablero_alea() # Inicializamos el tablero jugador humano con coordenadas aleatorias
        #Imprimimos el tablero del humano
        print("**********************")
        print("Tablero de ",tab_humano.jugador_id)
        print(tab_humano.tablero)
        #for nombre_barco,coordenadas in tab_humano.barcos_creados.items():
            #print(nombre_barco,":",coordenadas)
        #tab_maquina.ini_tablero_alea()

        tab_maquina.ini_tablero_alea() # Inicializamos el tablero de la maquina con coordenadas aleatorias
        #Imprimimos el tablero del humano
        print("\n\nTablero de ",tab_maquina.jugador_id)
        print(tab_maquina.tablero)
        print("**********************")
        #for nombre_barco,coordenadas in tab_maquina.barcos_creados.items():
            #print(nombre_barco,":",coordenadas)
        #tab_maquina.ini_tablero_alea()

        

        #Después de eso ya comienza el juego. Básicamente se irá ejecutando iterativamente en el while, y le irá preguntando coordenadas al usuario

        juego_terminado = False
        turno = "Jugador"

        while not juego_terminado:

            if turno == "Jugador":
                print("\nTurno del:", tab_humano.jugador_id)
                while True:
                    try:
                        respuesta = input("Introduce las coordenadas (fila columna) separadas por espacio o 'q' para salir: ")
                        if respuesta.lower() == 'q':
                            juego_terminado = True
                            break
                        fila, columna = map(int, respuesta.split())  
                        if 0 <= fila < tab_humano.dimension and 0 <= columna < tab_humano.dimension:  
                            break
                        else:
                            print(f"Las coordenadas deben estar entre 0 y {tab_humano.dimension - 1}.")
                    except ValueError:
                        print("Entrada inválida. Por favor, introduce dos números separados por espacio.")

                if juego_terminado:
                    break

                impacto = tab_maquina.recibir_disparo(fila, columna)
                if impacto:
                    print("\n¡Impacto! :)")
                else:
                    print("\nAgua :( ")
                    turno = "Máquina"

            else:
                # Turno de la máquina
                print("\n\nTurno de la maquina")
                import random

                # Se controla que la máquina no dispare sobre una coordenada en la que ya ha disparado
                while True:
                    fila = random.randint(0, tab_humano.dimension - 1)
                    columna = random.randint(0, tab_humano.dimension - 1)
                    if tab_humano.disparos[fila, columna] == " ":
                        break

                impacto = tab_humano.recibir_disparo(fila, columna)
                if impacto:
                    print("La máquina hizo impacto en tu tablero :( )")
                else:
                    print("La máquina falló :) ")
                    turno = "Jugador"



            # Condición de victoria
            if np.all(tab_maquina.tablero != "O"):
                print("¡Ganaste!")
                juego_terminado = True
            elif np.all(tab_humano.tablero != "O"):
                print("La máquina ganó.")
                juego_terminado = True

            input("Presione Enter para continuar")
            print("---------------------------")
            print("Tablero de ",tab_humano.jugador_id)    
            print(tab_humano.tablero)
            print("\n\nTablero de ",tab_maquina.jugador_id)
            print(tab_maquina.disparos)
            print("---------------------------")               

        print("FIN DEL JUEGO")


'''
        while not juego_terminado:
            accion = input("Presiona Enter para continuar o 'q' para salir: ")
            if accion.lower() == 'q':
                break

            if turno == "Jugador":
                print("\n\nTurno del jugador")
                # Pedir coordenadas al jugador
                fila, columna = map(int, input("Introduce las coordenadas (fila columna) separadas por espacio: ").split())
                impacto = tab_maquina.recibir_disparo(fila, columna)
                if impacto:
                    print("\n\n¡Impacto!")
                else:
                    print("\n\nAgua.")
                    turno = "Máquina"
            else:
                # Turno de la máquina
                print("\n\nTurno de la maquina")
                import random
                fila = random.randint(0, tab_humano.dimension - 1)
                columna = random.randint(0, tab_humano.dimension - 1)
                impacto = tab_humano.recibir_disparo(fila, columna)
                if impacto:
                    print("La máquina hizo impacto en tu tablero.")
                else:
                    print("La máquina falló.")
                    turno = "Jugador"

            print("\n\nTablero de ",tab_humano.jugador_id)    
            print(tab_humano.tablero)
            print("\n\nTablero de ",tab_maquina.jugador_id)
            print(tab_maquina.disparos)

            # Condición de victoria
            if np.all(tab_maquina.tablero != "O"):
                print("¡Ganaste!")
                juego_terminado = True
            elif np.all(tab_humano.tablero != "O"):
                print("La máquina ganó.")
                juego_terminado = True

        print("FIN DEL JUEGO")
'''