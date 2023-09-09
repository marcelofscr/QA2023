class controladorClima:
    # Método constructor de la clase
    def __init__(self, model):
        self.model = model

    """
    Obtiene información meteorológica para un aeropuerto específico.
    Args:
        codeAirport (str): El código IATA del aeropuerto para el que se consulta el clima.
    Returns:
        list or str: Una lista de información meteorológica o un mensaje de error si no se encuentra el aeropuerto.
    """
    def get_weather(self, codeAirport):
        listaAeropuertos = self.model.obtenerAeropuertos()
        if codeAirport == []:
            return "No es posible consultar el clima" # Retorna un mensaje de error si el código del aeropuerto está vacío
        else: # Filtra los aeropuertos por código IATA
            listaAeropuertoFiltro = [airport for airport in listaAeropuertos if airport['iata_code'] == codeAirport.upper()]
            return listaAeropuertoFiltro