from funciones import *
from clases import *

import pandas as pd

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx")


tot_est = []
for index, row in df.iterrows():
    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5])
    tot_est.append(estacion)

comunidad = ComunidadMadrid(tot_est)

while True:
    print("Por favor, elige una opción"
          "\n1) Buscar estación por nombre o id"
          "\n2) Calcular distancia (entre ids)"
          "\n3) Salir del programa")

    # Primero me aseguro de que si el usuario pone letras no me rompe el programa

    try:
        opcion = int(input())

    except ValueError:
        print("Valor incorrecto, introduce 1, 2 ó 3")
        continue

    # Ahora defino qué hará cada una de las opciones

    if opcion == 3:
        print("Esperamos verte pronto")
        break

    elif opcion == 1:
        print("Por favor, introduce el nombre o el identificador de la estación: ")
        estacion = input()    # por defecto el input recoge 'str'

        if estacion in str(comunidad.get_ids()):     # pongo 'str' porque el input que recojo es 'str'
            tipo_busqueda = "id"                     # int(estacion) me rompía el programa a posteriori
            estacion = int(estacion)                 # ahora sí le digo que convierta el input a 'int'
            busqueda = comunidad.busca_estacion(estacion, tipo_busqueda)

            # numeros = np.arange(250)       # este rango podría ser el max() de los ids
            # antes de que me funcionara buscando los ids en el método get_ids() creé el array y funcionaba

        else:
            tipo_busqueda = "name"
            busqueda = comunidad.busca_estacion(estacion, tipo_busqueda)

            # tendría que ver cómo hago con las tildes


    elif opcion == 2:
        print("Indica los identificadores de las estaciones para calcular la distancia")
        est1 = int(input("Estación de salida: "))
        est2 = int(input("Estación de llegada: "))

        dist_estaciones(est1, est2, comunidad)

        #print("La distancia entre las estaciones es de", dist_estaciones(est1, est2, comunidad))

        break


    else:
        print("Respuesta no válida, introduce 1, 2 ó 3")

    # con este último else me aseguro de que si responde número pero no es 1, 2 ó 3 vuelve a preguntar