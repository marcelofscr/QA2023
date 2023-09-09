class controladorVuelosActuales:
    # Método constructor de la clase
    def __init__(self, model):
        self.model = model

    """
    Obtiene una lista de vuelos actuales llegando a un aeropuerto especificado por su código IATA.
    Args:
        iata (str): El código IATA del aeropuerto de llegada.
    Returns:
        list: Una lista de vuelos actuales llegando al aeropuerto.
    """
    def getVuelosActuales(self, iata):
        listaVuelos = self.model.obtenerVuelosLlegada(iata)
        return listaVuelos