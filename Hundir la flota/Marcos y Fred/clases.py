import numpy as np
import random

class Tablero:
    '''

    Esta clase definirá los futuros objetos 'tablero', los tableros, sobre los que se desarrollará el juego.

    Hay dos tableros:
    - Tab, sobre el que se colocarán los barcos.
    - Tab2, que está vacío.

    Tab2 servirá como zona de impacto, donde se mostrarán los impactos que el usuario va realizando sobre tablero rival.
    Los impactos de la máquina se representan directamente en Tab, tablero del usuario con sus barcos.

    Se utilizará 'Tablero de la máquina' para referirnos a la zona de impacto.

    Por razones obvias no se muestra el tablero de la máquina con sus barcos.

    '''

    def __init__(self, id_jugador, long, lati, tab2=np.full((10, 10), " ")):
        self.long = long
        self.lati = lati
        self.tab = np.full((self.long, self.lati), " ")
        self.id_jugador = id_jugador
        self.tab2 = tab2

    def print_main(self):            # imprime por pantalla el tablero del usuario
        print(self.id_jugador)
        print()
        print(self.tab)
        print()

    def print_shoot_zone(self):       # imprime por pantalla el tablero de la máquina. Donde dispara el usuario
        print("Tablero de la máquina"
              "\n")
        print(self.tab2)
        print()

    def colocacion_automatica(self):  # función para colocar barcos de forma aleatoria en el tablero

        eslora1 = []
        eslora2 = []
        eslora3 = []
        eslora4 = []

        while True:

            orient = random.choice(['N', 'S', 'E', 'O'])
            current_pos = np.random.randint(10, size=2)
            fila = current_pos[0]
            col = current_pos[1]

            if len(eslora1) < 4:
                eslora = 1
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora1.append(current_pos)

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora1.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora1.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora1.append(current_pos)

            if len(eslora2) < 3:
                eslora = 2
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora2.append(current_pos)

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora2.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora2.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora2.append(current_pos)

            if len(eslora3) < 2:
                eslora = 3
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora3.append(current_pos)

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora3.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora3.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora3.append(current_pos)

            if len(eslora4) < 1:
                eslora = 4
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora4.append(current_pos)

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora4.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora4.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora4.append(current_pos)

            else:
                break

    def user_hit_or_not(self, long, lati):    # revisa los disparos del usuario para mostrarlos en tablero máquina
        if self.tab[long, lati] == "0":
            self.tab2[long, lati] = "X"
            return True
        else:
            self.tab2[long, lati] = "-"
            return False

    def machine_hit_or_not(self, long, lati):  # revisa los disparos de la máquina para mostrarlos en tablero usuario
        if self.tab[long, lati] == "0":
            self.tab[long, lati] = "X"
            return True
        else:
            self.tab[long, lati] = "-"
            return False

    def clean(self, long, lati):                # función para limpiar el tablero cuando se abandona la partida
        self.tab = np.full((self.long, self.lati), " ")
