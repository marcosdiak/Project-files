import random
import numpy as np

tablero_clase = np.full((10,10), ' ')

# Aquí se va a colocar un barco de eslora concreta de forma aleatoria en el tablero
# Le doy algunas coordenadas como utilizadas para que las tenga en cuenta
tablero_clase[(0,1),(1,1)] = 0
tablero_clase[(1),3:7] = 0

eslora = 4

while True:

    orient = random.choice(['N', 'S', 'E', 'O'])
    current_pos = np.random.randint(10, size = 2)
    print(orient)
    print(current_pos)

    fila = current_pos[0]
    col = current_pos[1]

    # Recogemos las 4 posiciones colindantes a 'current_pos'
    coors_posiN = tablero_clase[fila:fila - eslora:-1, col]
    coors_posiE = tablero_clase[fila, col : col + eslora]
    coors_posiS = tablero_clase[fila:fila + eslora, col]
    coors_posiO = tablero_clase[fila, col : col - eslora: -1]

    # Ahora hay que comprobar si esas posiciones son válidas #

    # Orientación 'N'orte:
    if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
        tablero_clase[fila:fila - eslora: -1, col] = '0'
        break

    # Orientación 'E'ste:
    elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
        tablero_clase[fila, col : col + eslora] = '0'
        break

    # Orientación 'S'ur:
    elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
        tablero_clase[fila:fila + eslora, col] = '0'
        break

    # Orientación 'O'este
    elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
        tablero_clase[fila, col : col - eslora: -1] = '0'
        break


print(tablero_clase)