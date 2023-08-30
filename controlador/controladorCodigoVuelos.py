class ControladorCodigoVuelos:
    def __init__(self, model):
        self.model = model

    def get_flights_by_code(self, codigoVuelo):
        try: 
            int(codigoVuelo)
            listaVuelos = self.model.obtenerVuelos()
            print(listaVuelos)
            if listaVuelos == []:
                return "No se encontraron vuelos disponibles" 
            else:
                InformacionVuelo = [flight for flight in listaVuelos if flight['flight']['number'] == codigoVuelo]
                return InformacionVuelo
        except ValueError:
            # Handle the exception
            print('Please enter an integer')