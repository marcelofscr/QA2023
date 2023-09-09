class controladorVuelosActualesSalida:
    # Método constructor de la clase
    def __init__(self, model):
        self.model = model

    """
    Obtiene una lista de vuelos actuales saliendo desde un aeropuerto especificado por su código IATA.
    Args:
        iata (str): El código IATA del aeropuerto de salida.
    Returns:
        list: Una lista de vuelos actuales saliendo desde el aeropuerto.
    """
    def getVuelosActualesSalida(self, iata):
        listaVuelosSalida = self.model.obtenerVuelosSalida(iata)
        return listaVuelosSalida