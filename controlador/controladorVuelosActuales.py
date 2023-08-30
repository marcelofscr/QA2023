class controladorVuelosActuales:
    def __init__(self, model):
        self.model = model

    def getVuelosActuales(self, iata):
        listaVuelos = self.model.obtenerVuelosLlegada(iata)
        return listaVuelos