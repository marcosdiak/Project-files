import time

from Desarrollo.barcosFuncion import *
from Desarrollo.barcosFantasma import *
from Desarrollo.disparoFantasma import *

"""
# Aquí vamos a intentar replicar dos tableros:
1- Mi tablero, donde coloco mis barcos de forma aleatoria ('barcosFuncion')
2- Los barcos de la máquina, colocados de forma aleatoria ('barcosFantasma')

- Se va a importar 'disparoFantasma' porque es el disparo que hará la máquina sobre mi tablero
- Habrá un menú donde yo elijo coordenada para disparar sobre los barcos de la máquina ('barcosFantasma')

"""

while True:

        print("Bienvenido al juego de hundir la flota, ¿qué deseas hacer?"
              "\n1) Iniciar el juego"
              "\n2) Leer las instrucciones"
              "\n3) Abandonar el juego")

        opcion = input()

        if opcion == '1':    # tengo que llamar a todas las funciones que inicien los tableros y corra el juego entero
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

            if dificultad not in (1, 2, 3):     # para asegurar que el usuario elige sólo 1, 2 ò 3
                print("Nivel no válido, por favor elija 1, 2 ó 3")
                continue

            eslora()            # sólo se ejecuta una única vez
            eslora_fantasma()   # sólo se ejecuta una única vez
            disparos_user = []
            disparos_fantasma = []

            while True:

                print("¿Qué deseas hacer?"
                      "\n1) Disparar"
                      "\n2) Leer las instrucciones"
                      "\n3) Abandonar la partida")

                opcion = input()

                if opcion == '1':

                    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # defino esta variable para excepcionar error de índice

                    if '0' not in tablero_fantasma:
                        print("¡Enhorabuena, has ganado!")

                    else:

                        try:
                            c1 = int(input("Introduce coordenada x: "))
                            c2 = int(input("Introduce coordenada y: "))
                            c_user = (c1, c2)

                        except (IndexError, ValueError):  # no me está cogiendo el IndexError
                            print("Valor incorrecto, introduzca valores numéricos para tablero de 10x10")
                            continue

                        if c1 in a and c2 in a:  # meto esto para asegurar valores dentro del tablero

                            if c_user in disparos_user:  # es decir, los que ya son "-" o "X"
                                print("Esa coordenada ya ha sido utilizada")


                            elif tablero_fantasma[c_user] != "-" and tablero_fantasma[c_user] != "X":
                                                             # es decir, los que son aún " " o "0"

                                    if tablero_fantasma[c_user] == "0":
                                        tablero_fantasma[c_user] = "X"
                                        disparos_user.append(c_user)
                                        print("Disparo del usuario:\n", c_user)
                                        print("¡Tocado!\n")
                                        print("Tablero de la máquina\n",np.where(tablero_fantasma == '0', ' ', tablero_fantasma))
                                        # aquí volverá al menú y me preguntará qué quiero hacer porque he acertado

                                    elif tablero_fantasma[c_user] == " ":
                                        tablero_fantasma[c_user] = "-"
                                        disparos_user.append(c_user)
                                        print("Disparo del usuario:\n", c_user)
                                        print("Agua\n")
                                        print("Tablero de la máquina\n",np.where(tablero_fantasma == '0', ' ', tablero_fantasma))

                                        print("\n.. Turno de la máquina...")
                                        time.sleep(1.5)   # con esto hay 2.4s de demora entre mi disparo y la máquina
                                        disparar_fantasma(tablero_usuario, dificultad)  # para salir del bucle llamo al fantasma
                                                                            # tirará aleatoriamente y cuando sea agua
                                                                           # volverá al menú de este 'while'

                        else:
                            print("Coordenadas incorrectas, introduzca valores numéricos para tablero de 10x10\n")


                if opcion == '2':
                    txt = open("Instrucciones.txt", 'r')
                    print(txt.read())

                elif opcion == '3':
                    print("¿Estás seguro de que quieres abandonar la partida?"
                          "\ny / n")
                    choice = input()

                    if choice == 'y':    # aquí se sale de la partida, no del juego. Hay que reiniciar tableros.
                        print(".. abandonando la partida ..")
                        tablero_usuario[tablero_usuario != ' '] = ' '  # sustituyo tod0 lo que no sea ' ' por ' '
                        tablero_fantasma[tablero_fantasma != ' '] = ' '
                        break
                        # con esas dos ejecuciones limpio los tableros antes del 'break'

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

