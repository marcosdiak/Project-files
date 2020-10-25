import numpy as np
import time

from variables import *

def game(turn: object = None, machine_lives: object = None, user_lives: object = None,
         difficulty : object = None) -> object:

    while True:

        if turn == "User":

            print("¿Qué deseas hacer?"
                  "\n1) Disparar"
                  "\n2) Leer las instrucciones"
                  "\n3) Mostrar vidas del usuario"
                  "\n4) Mostrar vidas de la máquina"
                  "\n5) Abandonar la partida")

            opcion = input()

            if opcion == '1':

                a = [0,1,2,3,4,5,6,7,8,9]  # variable definida para asegurar los valores de las coordenadas

                try:
                    user_shoot_long = int(input("Introduce coordenada x: "))
                    user_shoot_lati = int(input("Introduce coordenada y: "))

                except (IndexError, ValueError):  # para evitar que rompa cuando se introduce 'str'
                    print("Valor incorrecto, introduzca valores numéricos para tablero de 10x10\n")
                    continue

                if user_shoot_long in a and user_shoot_lati in a:

                    if [user_shoot_long, user_shoot_lati] not in user_lista:
                        user_lista.append([user_shoot_long, user_shoot_lati])

                        x = machine_tab.user_hit_or_not(user_shoot_long, user_shoot_lati)

                        if x is True:

                            print("Coordenada [%s, %s]" % (user_shoot_long, user_shoot_lati))
                            print("\n¡Tocado!"
                                  "\n")
                            time.sleep(1)
                            machine_lives -= 1

                            if machine_lives == 0:
                                print("\n¡Has ganado, enhorabuena!")
                                break
                            machine_tab.print_shoot_zone()
                            time.sleep(1)

                            print("\nVidas restante de la máquina:", machine_lives)
                            print("\nTu turno\n")

                            turn = "User"

                        else:

                            print("Coordenada [%s, %s]" % (user_shoot_long, user_shoot_lati))
                            print("\n¡Agua!"
                                  "\n")

                            machine_tab.print_shoot_zone()
                            user_tab.print_main()

                            time.sleep(1)

                            print("\n.. es el turno de la máquina ..\n")
                            time.sleep(1)

                            turn = "Machine"

                    else:
                        print("\nEsa coordenada ya ha sido utilizada"
                              "\n")
                        turn = "User"

                else:
                    print("\nCoordenadas incorrectas, introduzca valores numéricos para tablero de 10x10\n"
                          "\n")
                    turn = "User"

            if opcion == '2':
                txt = open("Instrucciones.txt", 'r')
                print(txt.read())


            if opcion == '3':
                print("Vidas restante del usuario:", user_lives, "\n")

            if opcion == '4':
                print("Vidas restante de la máquina:", machine_lives,"\n")

            if opcion == '5':
                print("¿Estás seguro de que quieres abandonar la partida?"
                      "\ny / n")
                choice = input()

                if choice == 'y':
                    print(".. abandonando la partida ..")
                    user_tab.clean(10,10)
                    machine_tab.clean(10,10)    # al abandonar partida reinicio los tableros

                    break

                else:
                    print("Continúas jugando")


        elif turn == "Machine":

            if difficulty == 1:    # asigna cómo se comporta el juego según el nivel de dificultad elegido

                n = range(0, 1)
                for i in n:
                    machine_shoot_long = np.random.randint(10)
                    machine_shoot_lati = np.random.randint(10)
                    if [machine_shoot_long, machine_shoot_lati] not in machine_lista:
                        x = user_tab.machine_hit_or_not(machine_shoot_long, machine_shoot_lati)

                        if x is True:
                            machine_lista.append([machine_shoot_long, machine_shoot_lati])
                            break

                        else:
                            machine_lista.append([machine_shoot_long, machine_shoot_lati])

                    else:
                        turn = 'Machine'

                if x is True:
                    print("Coordenada [%s, %s]" % (machine_shoot_long, machine_shoot_lati))
                    print("\n¡Tocado!"
                          "\n")
                    time.sleep(1.)

                    user_lives -= 1

                    if user_lives == 0:
                        print("\nLa máquina ha ganado la partida")
                        break
                    user_tab.print_main()
                    time.sleep(1)

                    print("\nVidas restante del usuario:", user_lives)
                    print("\n.. es el turno de la máquina ..")

                    turn = "Machine"

                else:
                    print("Coordenada [%s, %s]" % (machine_shoot_long, machine_shoot_lati))
                    print("\n¡Agua!"
                          "\n")
                    time.sleep(1)

                    user_tab.print_main()
                    machine_tab.print_shoot_zone()
                    time.sleep(1.5)

                    print("Tu turno")
                    turn = "User"

            elif difficulty == 2:

                n = range(0, 4)
                for i in n:
                    machine_shoot_long = np.random.randint(10)
                    machine_shoot_lati = np.random.randint(10)
                    if [machine_shoot_long, machine_shoot_lati] not in machine_lista:
                        x = user_tab.machine_hit_or_not(machine_shoot_long, machine_shoot_lati)

                        if x is True:
                            machine_lista.append([machine_shoot_long, machine_shoot_lati])
                            break

                        else:
                            machine_lista.append([machine_shoot_long, machine_shoot_lati])

                    else:
                        turn = 'Machine'

                if x is True:
                    print("Coordenada [%s, %s]" % (machine_shoot_long, machine_shoot_lati))
                    print("\n¡Tocado!"
                          "\n")
                    time.sleep(1)

                    user_lives -= 1

                    if user_lives == 0:
                        print("\nLa máquina ha ganado la partida")
                        break
                    user_tab.print_main()
                    time.sleep(1)

                    print("\nVidas restante del usuario:", user_lives)
                    print("\n.. es el turno de la máquina ..")

                    turn = "Machine"

                else:
                    print("Coordenada [%s, %s]" % (machine_shoot_long, machine_shoot_lati))
                    print("\n¡Agua!"
                          "\n")
                    time.sleep(1)

                    user_tab.print_main()
                    machine_tab.print_shoot_zone()
                    time.sleep(1.5)

                    print("Tu turno")
                    turn = "User"


            if difficulty == 3:

                n = range(0, 8)
                for i in n:
                    machine_shoot_long = np.random.randint(10)
                    machine_shoot_lati = np.random.randint(10)
                    if [machine_shoot_long, machine_shoot_lati] not in machine_lista:
                        x = user_tab.machine_hit_or_not(machine_shoot_long, machine_shoot_lati)

                        if x is True:
                            machine_lista.append([machine_shoot_long, machine_shoot_lati])
                            break

                        else:
                            machine_lista.append([machine_shoot_long, machine_shoot_lati])

                    else:
                        turn = 'Machine'

                if x is True:
                    print("Coordenada [%s, %s]" % (machine_shoot_long, machine_shoot_lati))
                    print("\n¡Tocado!"
                          "\n")
                    time.sleep(1.)

                    user_lives -= 1

                    if user_lives == 0:
                        print("\nLa máquina ha ganado la partida")
                        break
                    user_tab.print_main()
                    time.sleep(1)

                    print("\nVidas restante del usuario:", user_lives)
                    print("\n.. es el turno de la máquina ..")

                    turn = "Machine"

                else:
                    print("Coordenada [%s, %s]" % (machine_shoot_long, machine_shoot_lati))
                    print("\n¡Agua!"
                          "\n")
                    time.sleep(1)

                    user_tab.print_main()
                    machine_tab.print_shoot_zone()
                    time.sleep(1.5)

                    print("Tu turno")
                    turn = "User"
