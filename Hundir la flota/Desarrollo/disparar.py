import numpy as np
import random

# ESTA FUNCIÓN REALMENTE NO SE USA PORQUE EL USUARIO DISPARA INDICANDO MANUALMENTE COORDENADAS
# fue la función primaria para probar los disparos aleatorios sobre un tablero

disparos_user = []

def disparar(nombreTablero):    # nombreTablero es el nombre del tablero al que toma como referencia la función
    x = np.random.randint(10)
    y = np.random.randint(10)
    posicion = (x, y)

    # hay que guardar cada disparo y pintarlo cada vez para mostrar el tablero con las X y - (no los barcos)
    # debe tomar como referencia siempre el tablero de referencia para revisar 0, X, -
    # todo debe tomar, también, "las vidas" del jugador e indicar "hundido" si completa un barco

    if '0' not in nombreTablero:
        print("¡Enhorabuena, has ganado!")

    else:

        if nombreTablero[posicion] == "0":
            nombreTablero[posicion] = "X"
            disparos_user.append(posicion)
            print(posicion)
            print("¡Tocado!\n")
            print(nombreTablero)
            disparar(nombreTablero)

        elif nombreTablero[posicion] == " ":
            nombreTablero[posicion] = "-"
            disparos_user.append(posicion)
            print(posicion)
            print("Agua\n")
            print(nombreTablero)

        elif nombreTablero[posicion] == "X":
            disparar(nombreTablero)

        elif nombreTablero[posicion] == '-':
            disparar(nombreTablero)