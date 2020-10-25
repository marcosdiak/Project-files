"""

Este es el script que hay que lanzar para iniciar 'hundir la flota'

"""

from funciones import *
from variables import *

while True:

      print("........................................"
            "\n........................................"
            "\n.-.-.-.	    HUNDIR LA FLOTA   	 .-.-.-."
            "\n........................................"
            "\n........................................"
            "\n....... BY ............................."
            "\n........... MARCOS .... & .... FRED ...."
            "\n........................................"
            "\n........................................\n")

      print("Bienvenido al juego de hundir la flota, ¿qué deseas hacer?"
            "\n1) Iniciar el juego"
            "\n2) Leer las instrucciones"
            "\n3) Abandonar el juego")

      opcion = input()

      if opcion == '1':

            try:
                  difficulty = int(input("Por favor, selecciona el nivel de dificultad:"
                                                    "\n1) Nivel sencillo"
                                                   "\n2) Nivel moderado"
                                                   "\n3) Nivel difícil\n"))

            except (ValueError):                 # para excepcionar si el usuario introduce 'str'
                print("Nivel no válido, por favor elija 1, 2 ó 3")
                continue

            if difficulty not in (1, 2, 3):     # para asegurar sólo opciones 1, 2 ó 3
                print("Nivel no válido, por favor elija 1, 2 ó 3")
                continue

            user_tab.colocacion_automatica()      # se crea el tablero del usuario con sus barcos
            machine_tab.colocacion_automatica()   # se crea el tablero de la máquina con sus barcos

            print("\nTus barcos serán colocados de forma aleatoria en el tablero."
                  "\nSerás el primero en disparar."
                  "\n¡Suerte!"
                  "\n"
                  "\n......................"
                  "\n...... cargando ......"
                  "\n......................"
                  "\n   hundir la flota "
                  "\n......................\n")

            time.sleep(1.5)

            user_tab.print_main()

            game("User", 20, 20, difficulty)    # lanzamos la función donde se desarrolla el juego completo

      elif opcion == '2':
            txt = open("Instrucciones.txt", 'r')
            print(txt.read())                    # lee el archivo de las instrucciones

      elif opcion == '3':
            print(".. juego desconectado ..")
            break

      else:
            print("Elige opción 1, 2 ó 3.")
