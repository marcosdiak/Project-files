"""
En este script está definida la creación de los barcos de la máquina de forma aleatoria.
- Mostrará por pantalla un mensaje cuando ya se hayan colocado.

"""


import numpy as np
import random

tablero_fantasma = np.full((10,10), ' ')

def eslora_fantasma():

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
            coors_posiN = tablero_fantasma[fila:fila - eslora:-1, col]
            coors_posiE = tablero_fantasma[fila, col: col + eslora]
            coors_posiS = tablero_fantasma[fila:fila + eslora, col]
            coors_posiO = tablero_fantasma[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_fantasma[fila:fila - eslora: -1, col] = '0'
                eslora1.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_fantasma[fila, col : col + eslora] = '0'
                eslora1.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_fantasma[fila:fila + eslora, col] = '0'
                eslora1.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_fantasma[fila, col : col - eslora: -1] = '0'
                eslora1.append(current_pos)

        if len(eslora2) < 3:
            eslora = 2
            coors_posiN = tablero_fantasma[fila:fila - eslora:-1, col]
            coors_posiE = tablero_fantasma[fila, col: col + eslora]
            coors_posiS = tablero_fantasma[fila:fila + eslora, col]
            coors_posiO = tablero_fantasma[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_fantasma[fila:fila - eslora: -1, col] = '0'
                eslora2.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_fantasma[fila, col: col + eslora] = '0'
                eslora2.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_fantasma[fila:fila + eslora, col] = '0'
                eslora2.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_fantasma[fila, col: col - eslora: -1] = '0'
                eslora2.append(current_pos)

        if len(eslora3) < 2:
            eslora = 3
            coors_posiN = tablero_fantasma[fila:fila - eslora:-1, col]
            coors_posiE = tablero_fantasma[fila, col: col + eslora]
            coors_posiS = tablero_fantasma[fila:fila + eslora, col]
            coors_posiO = tablero_fantasma[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_fantasma[fila:fila - eslora: -1, col] = '0'
                eslora3.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_fantasma[fila, col: col + eslora] = '0'
                eslora3.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_fantasma[fila:fila + eslora, col] = '0'
                eslora3.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_fantasma[fila, col: col - eslora: -1] = '0'
                eslora3.append(current_pos)

        if len(eslora4) < 1:
            eslora = 4
            # Recogemos las 4 posiciones colindantes a 'current_pos'
            coors_posiN = tablero_fantasma[fila:fila - eslora:-1, col]
            coors_posiE = tablero_fantasma[fila, col: col + eslora]
            coors_posiS = tablero_fantasma[fila:fila + eslora, col]
            coors_posiO = tablero_fantasma[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_fantasma[fila:fila - eslora: -1, col] = '0'
                eslora4.append(current_pos)

            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_fantasma[fila, col: col + eslora] = '0'
                eslora4.append(current_pos)

            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_fantasma[fila:fila + eslora, col] = '0'
                eslora4.append(current_pos)

            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_fantasma[fila, col: col - eslora: -1] = '0'
                eslora4.append(current_pos)


        else:
            print("Los barcos de la máquina ya han sido colocados\n")

            break
