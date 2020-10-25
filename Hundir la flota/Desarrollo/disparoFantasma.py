import numpy as np
import random

# Hay que crear un disparo que me muestre los golpes pero no dónde están los barcos


disparos_fantasma = []

"""

def disparar_fantasma(nombreTablero):  # nombreTablero es el nombre del tablero al que toma como referencia la función
    x = np.random.randint(10)
    y = np.random.randint(10)
    posicion = (x, y)

    if '0' not in nombreTablero:
        print("La máquina ha ganado")    # Si ya no quedan '0' en este caso gana la máquina
                                         # porque estos son los disparos que hará sobre el tablero del usuario
    else:

        if nombreTablero[posicion] == "0":
            nombreTablero[posicion] = "X"
            disparos_fantasma.append(posicion)
            print("\nDisparo de la máquina:\n", posicion)
            print("¡Tocado!\n")
            print("Tablero del usuario\n", nombreTablero)
            #print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
            disparar_fantasma(nombreTablero)

        elif nombreTablero[posicion] == " ":
            nombreTablero[posicion] = "-"
            disparos_fantasma.append(posicion)
            print("\nDisparo de la máquina:\n", posicion)
            print("Agua\n")
            print("Tablero del usuario\n", nombreTablero)
            #print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))

        elif nombreTablero[posicion] == "X":
            disparar_fantasma(nombreTablero)

        elif nombreTablero[posicion] == '-':
            disparar_fantasma(nombreTablero)

"""

    # Hasta aquí funciona perfectamente el disparo en un tablero mostrando los impactos pero no los barcos
    # Es la función de disparo por defecto si no se añaden niveles de dificultad

    # ------------------------------------- #

    # A partir de aquí voy a tratar de introducir 3 niveles de dificultad en el disparo aleatorio
    # Nivel 1: se realiza un único disparo aleatorio (igual que lo diseñado arriba)
    # Nivel 2: se realizan dos disparos aleatorios y, en caso de haber '0' en uno, se queda con ese
    # Nivel 3: se realizan tres disparos aleatorios y, en caso de haber '0' en uno, se queda con ese

"""
def disparar_fantasma(nombreTablero, dificultad):  # ya le añado el parámetro de entrada dificultad

    if '0' not in nombreTablero:
        print("La máquina ha ganado")  # Si ya no quedan '0' en este caso gana la máquina
        # porque estos son los disparos que hará sobre el tablero del usuario

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
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion] == " ":
                nombreTablero[posicion] = "-"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("Agua\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara

            elif nombreTablero[posicion] == "X":
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion] == '-':
                disparar_fantasma(nombreTablero, dificultad)

        elif dificultad == 2:

            posicion = ()

            x = np.random.randint(10)
            y = np.random.randint(10)
            posicion1 = (x, y)

            z = np.random.randint(10)    # añado otra tirada random para comprobar si alguna de las dos es '0'
            k = np.random.randint(10)
            posicion2 = (z, k)

            if nombreTablero[posicion1] == '0':   # primero comprueba la primera tirada y si es '0 se la queda
                posicion = posicion1
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion2] == '0':  # comprueba la segunda tirada cuando la primera no es '0'
                posicion = posicion2
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara
                disparar_fantasma(nombreTablero, dificultad)

            else:

                posicion = random.choice([posicion1, posicion2])  # cuando ninguna es '0' elige una de las dos

                if nombreTablero[posicion] == " ":
                    nombreTablero[posicion] = "-"
                    disparos_fantasma.append(posicion)
                    print("\nDisparo de la máquina:\n", posicion)
                    print("Agua\n")
                    print("Tablero del usuario\n", nombreTablero)
                    # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))  # máscara

                elif nombreTablero[posicion] == "X":
                    disparar_fantasma(nombreTablero, dificultad)

                elif nombreTablero[posicion] == '-':
                    disparar_fantasma(nombreTablero, dificultad)

        elif dificultad == 3:

            posicion = ()

            x = np.random.randint(10)
            y = np.random.randint(10)
            posicion1 = (x, y)

            z = np.random.randint(10)
            k = np.random.randint(10)
            posicion2 = (z, k)

            i = np.random.randint(10)      # añado otra tirada random para comprobar si alguna de las tres es '0'
            j = np.random.randint(10)
            posicion3 = (i, j)

            if nombreTablero[posicion1] == '0':
                posicion = posicion1
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion2] == '0':
                posicion = posicion2
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion3] == '0':    # comprueba la tercera tirada cuando ninguna de las anteriores es '0'
                posicion = posicion3
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara
                disparar_fantasma(nombreTablero, dificultad)

            else:

                posicion = random.choice([posicion1, posicion2, posicion3])  # ¿ninguna es '0'? Elige una de ellas random

                if nombreTablero[posicion] == " ":
                    nombreTablero[posicion] = "-"
                    disparos_fantasma.append(posicion)
                    print("\nDisparo de la máquina:\n", posicion)
                    print("Agua\n")
                    print("Tablero del usuario\n", nombreTablero)
                    # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))

                elif nombreTablero[posicion] == "X":
                    disparar_fantasma(nombreTablero, dificultad)

                elif nombreTablero[posicion] == '-':
                    disparar_fantasma(nombreTablero, dificultad)


    # A partir de aquí añado una prueba para hacer tests, incorporando muchas más coordenadas
    # La máquina se hace "una máquina" disparando y acierta con mucha regularidad
"""

"""
        elif dificultad == 4:

            posicion = ()

            x = np.random.randint(10)
            y = np.random.randint(10)
            posicion1 = (x, y)

            z = np.random.randint(10)    # añado otra tirada random para comprobar si alguna de las dos es '0'
            k = np.random.randint(10)
            posicion2 = (z, k)

            i = np.random.randint(10)
            j = np.random.randint(10)
            posicion3 = (i, j)

            a = np.random.randint(10)
            b = np.random.randint(10)
            posicion4 = (a, b)

            c = np.random.randint(10)
            d = np.random.randint(10)
            posicion5 = (c, d)

            h = np.random.randint(10)
            f = np.random.randint(10)
            posicion6 = (h, f)

            if nombreTablero[posicion1] == '0':   # si la una o la otra tiene un '0', coge esa. ¿Cómo se hace eso?
                posicion = posicion1
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion2] == '0':
                posicion = posicion2
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion3] == '0':  # si la una o la otra tiene un '0', coge esa. ¿Cómo se hace eso?
                posicion = posicion3
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
                disparar_fantasma(nombreTablero, dificultad)

            elif nombreTablero[posicion4] == '0':  # si la una o la otra tiene un '0', coge esa. ¿Cómo se hace eso?
                posicion = posicion4
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
                disparar_fantasma(nombreTablero, dificultad)


            elif nombreTablero[posicion5] == '0':
                posicion = posicion5
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
                disparar_fantasma(nombreTablero, dificultad)


            elif nombreTablero[posicion6] == '0':
                posicion = posicion6
                nombreTablero[posicion] = "X"
                disparos_fantasma.append(posicion)
                print("\nDisparo de la máquina:\n", posicion)
                print("¡Tocado!\n")
                print("Tablero del usuario\n", nombreTablero)
                # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))   # máscara para sustituir '0' por ' '
                disparar_fantasma(nombreTablero, dificultad)

            else:

                posicion = random.choice([posicion1, posicion2, posicion3, posicion4, posicion5, posicion6])

                if nombreTablero[posicion] == " ":
                    nombreTablero[posicion] = "-"
                    disparos_fantasma.append(posicion)
                    print("\nDisparo de la máquina:\n", posicion)
                    print("Agua\n")
                    print("Tablero del usuario\n", nombreTablero)
                    # print("Tablero del usuario\n",np.where(nombreTablero == '0', ' ', nombreTablero))

                elif nombreTablero[posicion] == "X":
                    disparar_fantasma(nombreTablero, dificultad)

                elif nombreTablero[posicion] == '-':
                    disparar_fantasma(nombreTablero, dificultad) 
                    
                    
                 
                     """

    # Hasta aquí funciona tod0 perfectamente con distintos niveles
    # Sin embargo, el código queda demasiado largo a medida que se añaden niveles de dificultad

        # --------------------------------- #
        # --------------------------------- #

    # A partir de aquí se añadirá una modalidad para incrementar la dificultad con facilidad


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

            n = range(0, 4)     # añado este rango para incrementar las veces que intenta encontrar un '0'
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