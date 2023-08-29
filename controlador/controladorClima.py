class controladorClima:
    def __init__(self, model):
        self.model = model

    def get_weather(self, codeAirport):
        listaAeropuertos = self.model.obtenerAeropuertos()
        if codeAirport == []:
            return "No es posible consultar el clima" 
        else:
            listaAeropuertoFiltro = [airport for airport in listaAeropuertos if airport['iata_code'] == codeAirport.upper()]
            return listaAeropuertoFiltro