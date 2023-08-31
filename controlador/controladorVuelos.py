class controladorVuelos:
    def __init__(self, model):
        self.model = model

    def get_flights(self,iata_origen,iata_destino):
        listaVuelosRuta = self.model.obtenerVuelos(iata_origen,iata_destino)
        return listaVuelosRuta
          


         
    
        