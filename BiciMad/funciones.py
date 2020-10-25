"""
Implementa una función que tenga las siguientes características:

Nombre: dist_estaciones
Input: (est1, est2, comunidad). Son dos objetos de tipo int, con dos indentificadores de estación,
        y otro de tipo ComunidadMadrid.

Output: la distancia entre ambas estaciones.

"""

def dist_estaciones(est1, est2, comunidad):

    # voy a asegurarme si los ids son correctos y que tengo ambos

    ubicadores = []
    for u in comunidad.estaciones:
        if u.id in [est1,est2]:
            ubicadores.append(u)

    if len(ubicadores) == 2:

        print("Has elegido las estaciones %s y %s" % (ubicadores[0].name, ubicadores[1].name))
        print("La distancia entre ambas es de", (round(ubicadores[0].distancia(ubicadores[1].longitude,
                                                                            ubicadores[1].latitude),2)), "km")

        # le he metido un round() para que me devuelva sólo 2 decimales

        # los valores que arrojaba la distancia no eran correctos porque había invertido longitud y latitud
        # en el momento de llamar a la función

    else:
        print("Al menos uno de los identificadores no es correcto")


    # todos los print() a continuación los usé cuando no era capaz de llamar a la función
    # me servían para asegurarme de que los ubicadores eran correctos y que llamando a sus
    # longitudes y latitudes de forma individual me los mostraba

        #print(ubicadores)
        #print(type(ubicadores))
        #print(len(ubicadores))

        #print(ubicadores[0].longitude)
        #print(ubicadores[0].latitude)
        #print(ubicadores[1].longitude)
        #print(ubicadores[1].latitude)


