from Desarrollo.barcosFantasma import *
from Desarrollo.disparoFantasma import *

"""
# Al ejecutar este script se puede jugar a adivinar dónde están los barcos de la máquina.
# Ignorar el mensaje "tablero del usuario". Se debe a que a una de las funciones a las que
# se llama, 'disparar_fantasma(nombreTablero)', lleva implícito mostrar el tablero del
# usuario cuando se ejecuta el juego completo.

# Además, por defecto, los barcos de la máquina se muestran por pantalla.
# Hay que modificar la línea del print() en la función 'disparar_fantasma(nombreTablero)'

# Habría que habilitar la función 'disparar_fantasma(nombreTablero)', pues por defecto está la que añade dificultad

"""

eslora_fantasma()    # sólo se ejecuta una única vez

while True:  # debe haber un bucle donde se ejecute el juego completo
             # deben existir turnos de tirada, de modo que este ejemplo de abajo puede ser útil
             # por cada 'agua' se interrumpe y pregunta qué paso dar

    if '-':
        print("¿Qué deseas hacer?"
              "\n1) Disparo random"
              "\n2) Introducir coordenada"
              "\n3) Abandonar el juego")

        opcion = input()

        if opcion == '1':
            disparar_fantasma(tablero_fantasma)

        elif opcion == '2':

            try:
                c1 = int(input("Introduce coordenada x: "))
                c2 = int(input("Introduce coordenada y: "))
                c_user = (c1, c2)

            except (IndexError, ValueError):   # no me está cogiendo el IndexError
                print("Valor incorrecto, introduzca valores numéricos para tablero de 10x10")
                continue

            if c_user in disparos_fantasma:
                print("Esa coordenada ya ha sido utilizada")

            else:

                if tablero_fantasma[c_user] == "0":
                    tablero_fantasma[c_user] = "X"
                    disparos_fantasma.append(c_user)
                    print(c_user)
                    print("¡Tocado!\n")
                    print(np.where(tablero_fantasma == '0', ' ', tablero_fantasma))

                elif tablero_fantasma[c_user] == " ":
                    tablero_fantasma[c_user] = "-"
                    disparos_fantasma.append(c_user)
                    print(c_user)
                    print("Agua\n")
                    print(np.where(tablero_fantasma == '0', ' ', tablero_fantasma))


        elif opcion == '3':
            print("Hasta luego")
            break

        else:
            print("Elige opción 1, 2 ó 3.")

