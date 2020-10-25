import numpy as np
import random

tablero_usuario = np.full((10,10), ' ')

# Hacemos una función con un único parámetro de entrada que sea la eslora del barco
# Esto tiene como fin que posicione de forma aleatoria los barcos de la máquina


'''  

def eslora(size):

    eslora = size
    barcos_list = []

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
            barcos_list.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...
            break


        # Orientación 'E'ste:
        elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
            tablero_clase[fila, col : col + eslora] = '0'
            barcos_list.append(current_pos)
            break

        # Orientación 'S'ur:
        elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
            tablero_clase[fila:fila + eslora, col] = '0'
            barcos_list.append(current_pos)
            break

        # Orientación 'O'este
        elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
            tablero_clase[fila, col : col - eslora: -1] = '0'
            barcos_list.append(current_pos)
            break

    print(barcos_list)
    print(tablero_clase)
    
    '''

    # hasta aquí funciona generar barco y guardarlo en una lista

    # --------- # # --------- # # --------- # # --------- #

    # A partir de aquí voy a probar a automatizar la creación de barcos de la misma eslora

'''


def eslora(size):

    eslora = size
    barcos_list = []

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

        if len(barcos_list) < eslora:

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_clase[fila:fila - eslora: -1, col] = '0'
                barcos_list.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...



            # Orientación 'E'ste:
            elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                tablero_clase[fila, col : col + eslora] = '0'
                barcos_list.append(current_pos)


            # Orientación 'S'ur:
            elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                tablero_clase[fila:fila + eslora, col] = '0'
                barcos_list.append(current_pos)


            # Orientación 'O'este
            elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                tablero_clase[fila, col : col - eslora: -1] = '0'
                barcos_list.append(current_pos)


        else:
            print("Ya están todos los barcos creados")

            break

    print(len(barcos_list))
    print(barcos_list)
    print(tablero_clase)

#eslora(3)

'''

    # hasta aquí funciona la creación de varios barcos de misma eslora

    # --------- # # --------- # # --------- # # --------- #

    # ahora voy a probar a automatizar la creación de barcos según su eslora

# 4 barcos de 1 posición de eslora
# 3 barcos de 2 posiciones de eslora
# 2 barcos de 3 posiciones de eslora
# 1 barco de 4 posiciones de eslora

def eslora():     # quito el 'size' porque voy a definir las esloras directamente debajo

    eslora1 = []
    eslora2 = []
    eslora3 = []
    eslora4 = []

    while True:

        orient = random.choice(['N', 'S', 'E', 'O'])
        current_pos = np.random.randint(10, size = 2)
        #print(orient)
        #print(current_pos)

        fila = current_pos[0]
        col = current_pos[1]

        # Ahora hay que comprobar si esas posiciones son válidas #

        if len(eslora1) < 4:
            eslora = 1
            # Recogemos las 4 posiciones colindantes a 'current_pos'
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]   # he tenido que meterlo en cada 'if' porque
            coors_posiE = tablero_usuario[fila, col: col + eslora]      # la eslora la defino dentro de cada uno
            coors_posiS = tablero_usuario[fila:fila + eslora, col]      # si la dejaba arriba daba error puesto que
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]  # aún no era una variable definida

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora1.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

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
            # Recogemos las 4 posiciones colindantes a 'current_pos'
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora2.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

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
            # Recogemos las 4 posiciones colindantes a 'current_pos'
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora3.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

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
            # Recogemos las 4 posiciones colindantes a 'current_pos'
            coors_posiN = tablero_usuario[fila:fila - eslora:-1, col]
            coors_posiE = tablero_usuario[fila, col: col + eslora]
            coors_posiS = tablero_usuario[fila:fila + eslora, col]
            coors_posiO = tablero_usuario[fila, col: col - eslora: -1]

            # Orientación 'N'orte:
            if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                tablero_usuario[fila:fila - eslora: -1, col] = '0'
                eslora4.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

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

    #print("Los barcos de eslora 1 están ubicados en:", eslora1)
    print("Los barcos de eslora 1 están ubicados en:", (' '.join(map(str, eslora1))))
    print("Las coordenadas de inicio de los barcos de eslora 2 son:", (' '.join(map(str, eslora2))))
    print("Las coordenadas de inicio de los barcos de eslora 3 son:", (' '.join(map(str, eslora3))))
    print("La coordenada de inicio del barco de eslora 4 es:", (' '.join(map(str, eslora4))))
    print("\n Este es tu tablero: \n\n", tablero_usuario, "\n")

    # (' '.join(map(str, a)))
    # Use map() to convert each item in the list to a string if list is not a string, and then join them:

#eslora()

    # hasta aquí he logrado posicionar TODOS los barcos de la máquina de forma aleatoria según su eslora

    # --------- # # --------- # # --------- # # --------- #

