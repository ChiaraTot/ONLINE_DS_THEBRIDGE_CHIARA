import numpy as np
import random
from variables import DIMENSIONES_TABLERO, BARCOS

class Tablero:
    def __init__(self, jugador_id):
        self.jugador_id = jugador_id
        self.dimension = DIMENSIONES_TABLERO
        self.tablero = np.full((self.dimension, self.dimension), " ")
        self.disparos = np.full((self.dimension, self.dimension), " ")
        self.barcos = BARCOS 
        self.barcos_creados = {} # Diccionario que almacena las nombres y las coordenas de las piezas de los barcos
    '''
    def inicializar_tablero(self):
        # Colocar los barcos en el tablero de acuerdo a la configuración
        for tipo_barco, cantidad in self.barcos.items():
            for _ in range(cantidad):
                self.posicionar_barco(int(tipo_barco.split('_')[1]))
    '''

    def ini_tablero_alea(self):
        for tipo_barco,datos_barco in self.barcos.items(): # Recorro el diccionario de barcos (clave:valor)
            eslora = datos_barco[0] #La posicion 0 de la lista indica la eslora
            cant_barcos = datos_barco[1] #La posicion 1 de la lista indica la cantidad de barcos
            #print(f"Tipo de barco: {tipo_barco} -> eslora: {eslora}, cantidad: {cant_barcos}") #Imprimo tipo de barco, eslora y cantidad de barcos
            for i_barco in range(cant_barcos): # Repito tantas veces como indica en la cantidad de barcos por eslora
                #print(tipo_barco,i_barco)
                self.crea_barco_aleatorio(eslora,i_barco)
        return self.tablero
    

    def crea_barco_aleatorio(self,eslora,i_barco):
        num_max_filas = self.tablero.shape[0]
        num_max_columnas = self.tablero.shape[1]
        contador = 0
        num_intentos = 100
        while True:
            if contador >= num_intentos:
                print(f"No fue posible colocar un barco de eslora {eslora} tras {num_intentos} intentos.")
                return False

            contador += 1
            barco = []
            # Construimos el hipotetico barco
            pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
            #print("Pieza original:", pieza_original)
            barco.append(pieza_original)
            orientacion = random.choice(["N","S","O","E"])
            #print("Con orientacion", orientacion)
            fila = pieza_original[0]
            columna = pieza_original[1]
            for i in range(eslora - 1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                elif orientacion == "O":
                    columna -= 1
                pieza = (fila,columna)
                barco.append(pieza)
            tablero_temp = self.coloca_barco_plus(barco)
            if type(tablero_temp) == np.ndarray:
                #print(f"Hemos necesitado {contador} intentos")
                self.tablero = tablero_temp #Actualizamos el tablero luego de colocar el barco
                nombre_barco = 'barco_es'+ str(eslora) + "_0" + str(i_barco + 1) # Componemos el nombre del barco
                #print(nombre_barco)
                self.barcos_creados[nombre_barco] = barco # LLenamos el diccionario con las coordenadas del barco                
                return tablero_temp
            #print("Tengo que intentar colocar otro barco")

    # Funcion que revisa si es posible colocar el barco en el tablero
    def coloca_barco_plus(self,barco):
        # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
        tablero_temp = self.tablero.copy()
        num_max_filas = self.tablero.shape[0]
        num_max_columnas = self.tablero. shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0 or fila >= num_max_filas:
                #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna <0 or columna>= num_max_columnas:
                #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if self.tablero[pieza] == "O" or self.tablero[pieza] == "X":
                #print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp


    def recibir_disparo(self, fila, columna):
        if self.disparos[fila, columna] in ["X", "-"]:
            # Si ya se disparó en esta celda, no hacer nada.
            print("Ya has disparado en estas coordenadas.")
            return None

        if self.tablero[fila, columna] == "O":
            self.disparos[fila, columna] = "X"
            self.tablero[fila, columna] = "X"
            return True
        else:
            self.disparos[fila, columna] = "-"
            self.tablero[fila, columna] = "-"
            return False















