"""
En este script está la función de creación de los barcos del usuario.
- Se realizará de forma aleatoria.
- Imprimirá por pantalla el tablero del usuario con los barcos posicionados y sus coordenadas

"""

import numpy as np
import random

tablero_usuario = np.full((10,10), ' ')

def eslora():

    eslora1 = []
    eslora2 = []
    eslora3 = []
    eslora4 = []

    while True:

        orient = random.choice(['N', 'S', 'E', 'O'])
        current_pos = np.random.randint(10, size = 2)
        fila = current_pos[0]
        col = current_pos[1]

        if len(eslora1) < 4:
            eslora = 1
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora1.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_usuario[fila, col : col + eslora] = '0'
                eslora1.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_usuario[fila:fila + eslora, col] = '0'
                eslora1.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_usuario[fila, col : col - eslora: -1] = '0'
                eslora1.append(current_pos)

        if len(eslora2) < 3:
            eslora = 2
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora2.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_usuario[fila, col: col + eslora] = '0'
                eslora2.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_usuario[fila:fila + eslora, col] = '0'
                eslora2.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_usuario[fila, col: col - eslora: -1] = '0'
                eslora2.append(current_pos)

        if len(eslora3) < 2:
            eslora = 3
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora3.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_usuario[fila, col: col + eslora] = '0'
                eslora3.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_usuario[fila:fila + eslora, col] = '0'
                eslora3.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_usuario[fila, col: col - eslora: -1] = '0'
                eslora3.append(current_pos)

        if len(eslora4) < 1:
            eslora = 4
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora4.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_usuario[fila, col: col + eslora] = '0'
                eslora4.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_usuario[fila:fila + eslora, col] = '0'
                eslora4.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_usuario[fila, col: col - eslora: -1] = '0'
                eslora4.append(current_pos)

        else:
            print("\nYa están todos tus barcos creados:")

            break

    print("Los barcos de eslora 1 están ubicados en:", (' '.join(map(str, eslora1))))
    print("Las coordenadas de inicio de los barcos de eslora 2 son:", (' '.join(map(str, eslora2))))
    print("Las coordenadas de inicio de los barcos de eslora 3 son:", (' '.join(map(str, eslora3))))
    print("La coordenada de inicio del barco de eslora 4 es:", (' '.join(map(str, eslora4))))
    print("\n Este es tu tablero: \n\n", tablero_usuario, "\n")
