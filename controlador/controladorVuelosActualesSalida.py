class controladorVuelosActualesSalida:
    def __init__(self, model):
        self.model = model

    def getVuelosActualesSalida(self, iata):
        listaVuelosSalida = self.model.obtenerVuelosSalida(iata)
        return listaVuelosSalida