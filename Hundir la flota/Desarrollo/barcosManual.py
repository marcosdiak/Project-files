# Aquí haremos la parte sencilla de colocar los barcos de forma manual

import random
import numpy as np

tablero_clase = np.full((10,10), ' ')

def barcos_manual():

    # 4 barcos de eslora = 1
    tablero_clase[(2,2)] = '0'
    tablero_clase[(7, 8)] = '0'

    # 3 barcos de 2 posiciones de eslora
    tablero_clase[(0, 1), (1, 1)] = '0'
    tablero_clase[(2,3),(2,4)] = '0'

    # 2 barcos de 3 posiciones de eslora
    tablero_clase[4, 0:4] = '0'
    tablero_clase[8:5:-1 , 9] = '0'

    # 1 barco de 4 posiciones de eslora
    tablero_clase[(1), 3:7] = '0'

    print(tablero_clase)

barcos_manual()
