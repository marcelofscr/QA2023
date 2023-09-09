class controladorCodigoVuelos:
    # Método constructor de la clase
    def __init__(self, model):
        self.model = model

    """
    Obtiene información de vuelos por su código IATA.
    Args:
        iataVuelo (str): El código IATA del vuelo para el que se consulta la información.
    Returns:
        list or str: Una lista de información de vuelos o un mensaje de error si no se encuentran vuelos.
    """
    def get_flights_by_code(self, iataVuelo):
        try: 
            listaVuelos = self.model.obtenerVueloPorCodigo(iataVuelo)
            print(listaVuelos)
            if listaVuelos == []: # Retorna un mensaje de error si no se encontraron vuelos
                return "No se encontraron vuelos disponibles" 
            else: #Filtra por código iata de vuelo
                InformacionVuelo = [flight for flight in listaVuelos if flight.get("flight_iata") == iataVuelo ]
                return InformacionVuelo
        except ValueError:
            # Handle the exception
            print('No disponible')