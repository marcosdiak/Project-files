"""
En este script está definido el disparo random de la máquina sobre el tablero del usuario.
- Habrá dos parámetros de entrada:
    · El tablero al que apunta la función (será el tablero del usuario)
    · La dificultad del juego (que tendrá 3 niveles y la elige el usuario al iniciar el juego)

"""

import numpy as np
import random

disparos_fantasma = []

def disparar_fantasma(nombreTablero, dificultad):

    if '0' not in nombreTablero:
        print("La máquina ha ganado")

    else:

        if dificultad == 1:

            x = np.random.randint(10)
            y = np.random.randint(10)
            posicion = (x, y)

            if nombreTablero[posicion] == "0":
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion] == " ":
                nombreTablero[posicion] = "-"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("Agua\n")
                print("Tablero del usuario\n", nombreTablero)

            elif nombreTablero[posicion] == "X":
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion] == '-':
                disparar_fantasma(nombreTablero, dificultad)


        elif dificultad == 2:

            posicion = ()

            n = range(0, 4)
            for i in n:
                x = np.random.randint(10)
                y = np.random.randint(10)
                posicion = (x, y)
                if nombreTablero[posicion] == '0':
                    disparos_fantasma.append(posicion)
                    break
                else:
                    disparos_fantasma.append(posicion)

            if nombreTablero[posicion] == '0':
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                disparar_fantasma(nombreTablero, dificultad)

            else:

                posicion = disparos_fantasma[-1]

                if nombreTablero[posicion] == " ":
                    nombreTablero[posicion] = "-"
                    disparos_fantasma.append(posicion)
                    print("\nDisparo de la máquina:\n", posicion)
                    print("Agua\n")
                    print("Tablero del usuario\n", nombreTablero)

                elif nombreTablero[posicion] == "X":
                    disparar_fantasma(nombreTablero, dificultad)

                elif nombreTablero[posicion] == '-':
                    disparar_fantasma(nombreTablero, dificultad)

        elif dificultad == 3:

            posicion = ()

            n = range(0, 8)
            for i in n:
                x = np.random.randint(10)
                y = np.random.randint(10)
                posicion = (x, y)
                if nombreTablero[posicion] == '0':
                    disparos_fantasma.append(posicion)
                    break
                else:
                    disparos_fantasma.append(posicion)

            if nombreTablero[posicion] == '0':
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                disparar_fantasma(nombreTablero, dificultad)

            else:

                posicion = disparos_fantasma[-1]

                if nombreTablero[posicion] == " ":
                    nombreTablero[posicion] = "-"
                    disparos_fantasma.append(posicion)
                    print("\nDisparo de la máquina:\n", posicion)
                    print("Agua\n")
                    print("Tablero del usuario\n", nombreTablero)

                elif nombreTablero[posicion] == "X":
                    disparar_fantasma(nombreTablero, dificultad)

                elif nombreTablero[posicion] == '-':
                    disparar_fantasma(nombreTablero, dificultad)