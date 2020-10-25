import math

class Estacion:

    def __init__(self, name, identificador, num_bicis, address, longitude, latitude):
        self.name = name
        self.id = identificador
        self.num_bicis = num_bicis
        self.address = address
        self.longitude = longitude
        self.latitude = latitude

    def distancia(self, longitude, latitude):
        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = latitude, longitude
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d


class ComunidadMadrid:

    """
    Cuando crees un objeto de esta clase tendrás que introducir como argumento de entrada
    una lista cuyo contenido sean todos los objetos de tipo Estacion.

    """

    def __init__(self, estaciones):

        self.estaciones = estaciones

    def get_ids(self):

        """
        Un método get_ids(self), sin parámetros de entrada,
        que devuelva una lista con todos los identificadores de estación en formato int.

        """

        lista_ids = []
        for x in self.estaciones:
            lista_ids.append(x.id)

        return (lista_ids)


    def busca_estacion(self, estacion, tipo_busqueda):
        if tipo_busqueda == "name":

            for i in self.estaciones:
                if i.name.lower() == estacion.lower():  # lo paso tod0 a minúsculas para evitar problemas
                    print(i.name)  # hay que investigar tildes y espacios
                    print("¿Qué más deseas hacer?")

            #  else:
            #     print("Estación no encontrada")   # esto puedo hacerlo con return y luego imprimir por pantalla

        elif tipo_busqueda == "id":

            for i in self.estaciones:
                if i.id == estacion:
                    print(i.name)
                    print("¿Qué más deseas hacer?")

# cuando se introduce un ID o nombre no existente, no indica que no lo ha encontrado






