class controladorVuelos:
    def __init__(self, model):
        self.model = model

    def get_flights(self,iata_origen,iata_destino):
        listaVuelos = self.model.obtenerVuelos()
        print(listaVuelos)
        if listaVuelos == []:
            return "No se encontraron vuelos disponibles" 
        else:
            listaVuelosFiltro = [flight for flight in listaVuelos if flight['departure']['iata'] == iata_origen.upper() and flight['arrival']['iata'] == iata_destino.upper()]
            return listaVuelos
          


         
    
        