# 'Entrega' es el directorio previo a realizar el merge con el proyecto de Fred

import time

from Desarrollo.barcosFuncion import *
from Desarrollo.barcosFantasma import *
from Desarrollo.disparoFantasma import *

while True:

        print("Bienvenido al juego de hundir la flota, ¿qué deseas hacer?"
              "\n1) Iniciar el juego"
              "\n2) Leer las instrucciones"
              "\n3) Abandonar el juego")

        opcion = input()

        if opcion == '1':
            print("\nTus barcos serán colocados de forma aleatoria en el mapa."
                  "\nSerás el primero en disparar."
                  "\n¡Suerte!"
                  "\n......................"
                  "\n...... cargando ......"
                  "\n......................"
                  "\n   hundir la flota "
                  "\n......................")

            try:
                dificultad = int(input("Por favor, selecciona el nivel de dificultad:"
                                                    "\n1) Nivel sencillo"
                                                   "\n2) Nivel moderado"
                                                   "\n3) Nivel difícil\n"))

            except (ValueError):                 # para excepcionar si el usuario introduce 'str'
                print("Nivel no válido, por favor elija 1, 2 ó 3")
                continue

            if dificultad not in (1, 2, 3):     # para asegurar sólo opciones 1, 2 ó 3
                print("Nivel no válido, por favor elija 1, 2 ó 3")
                continue

            eslora()                            # función para colocar los barcos del usuario en el tablero
            eslora_fantasma()                   # función para colocar los barcos de la máquina en el tablero
            disparos_user = []
            disparos_fantasma = []

            while True:

                print("¿Qué deseas hacer?"
                      "\n1) Disparar"
                      "\n2) Leer las instrucciones"
                      "\n3) Abandonar la partida")        # abandona la partida, no el juego

                opcion = input()

                if opcion == '1':

                    a = [0,1,2,3,4,5,6,7,8,9]

                    if '0' not in tablero_fantasma:
                        print("¡Enhorabuena, has ganado!")

                    else:

                        try:
                            c1 = int(input("Introduce coordenada x: "))
                            c2 = int(input("Introduce coordenada y: "))
                            c_user = (c1, c2)

                        except (IndexError, ValueError):
                            print("Valor incorrecto, introduzca valores numéricos para tablero de 10x10\n")
                            continue

                        if c1 in a and c2 in a:

                            if c_user in disparos_user:
                                print("Esa coordenada ya ha sido utilizada")

                            elif tablero_fantasma[c_user] != "-" and tablero_fantasma[c_user] != "X":

                                    if tablero_fantasma[c_user] == "0":
                                        tablero_fantasma[c_user] = "X"
                                        disparos_user.append(c_user)
                                        print("Disparo del usuario:\n", c_user)
                                        print("¡Tocado!\n")
                                        print("Tablero de la máquina\n",np.where(tablero_fantasma == '0', ' ',
                                                                                 tablero_fantasma))

                                    elif tablero_fantasma[c_user] == " ":
                                        tablero_fantasma[c_user] = "-"
                                        disparos_user.append(c_user)
                                        print("Disparo del usuario:\n", c_user)
                                        print("Agua\n")
                                        print("Tablero de la máquina\n",np.where(tablero_fantasma == '0', ' ',
                                                                                 tablero_fantasma))

                                        print("\n... Turno de la máquina ...")
                                        time.sleep(1.5)  # para que no salga la .info inmediata
                                        disparar_fantasma(tablero_usuario, dificultad)

                        else:
                            print("Coordenadas incorrectas, introduzca valores numéricos para tablero de 10x10\n")

                if opcion == '2':
                    txt = open("Instrucciones.txt", 'r')
                    print(txt.read())

                elif opcion == '3':
                    print("¿Estás seguro de que quieres abandonar la partida?"
                          "\ny / n")
                    choice = input()

                    if choice == 'y':
                        print(".. abandonando la partida ..")
                        tablero_usuario[tablero_usuario != ' '] = ' '      # limpio los tableros para poder usarlos
                        tablero_fantasma[tablero_fantasma != ' '] = ' '    # si inicio una nueva partida
                        break

                    else:
                        print("Continúas jugando")

                else:
                    print("Elige opción 1, 2 ó 3.")

        elif opcion == '2':
            txt = open("Instrucciones.txt", 'r')
            print(txt.read())

        elif opcion == '3':
            print(".. juego desconectado ..")
            break

        else:
            print("Elige opción 1, 2 ó 3.")

