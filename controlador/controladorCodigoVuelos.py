class controladorCodigoVuelos:
    def __init__(self, model):
        self.model = model

    def get_flights_by_code(self, iataVuelo):
        try: 
            listaVuelos = self.model.obtenerVueloPorCodigo(iataVuelo)
            print(listaVuelos)
            if listaVuelos == []:
                return "No se encontraron vuelos disponibles" 
            else:
                InformacionVuelo = [flight for flight in listaVuelos if flight.get("flight_iata") == iataVuelo ]
                return InformacionVuelo
        except ValueError:
            # Handle the exception
            print('No disponible')