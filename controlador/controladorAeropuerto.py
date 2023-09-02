class controladorAeropuerto:
    def __init__(self, model):
        self.model = model

    def get_airports(self, letra):
        listaAeropuertos = self.model.obtenerAeropuertos()
        if letra == '*': # Muestra todos los aeropuertos
            return listaAeropuertos 
        else: # En caso de filtrar por letra
            listaAeropuertoFiltro = [airport for airport in listaAeropuertos if airport['airport_name'].startswith(letra.upper())]
            return listaAeropuertoFiltro