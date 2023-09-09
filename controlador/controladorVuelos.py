class controladorVuelos:
    # Método constructor de la clase
    def __init__(self, model):
        self.model = model

    """
    Obtiene una lista de vuelos entre dos aeropuertos especificados por sus códigos IATA.
    Args:
        iata_origen (str): El código IATA del aeropuerto de origen.
        iata_destino (str): El código IATA del aeropuerto de destino.
    Returns:
        list: Una lista de vuelos disponibles entre los dos aeropuertos.
    """
    def get_flights(self,iata_origen,iata_destino):
        listaVuelosRuta = self.model.obtenerVuelos(iata_origen,iata_destino)
        return listaVuelosRuta
          


         
    
        