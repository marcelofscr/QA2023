class controladorAeropuerto:
    # Método constructor de la clase
    def __init__(self, model):
        self.model = model

    """
    Obtiene la lista de aeropuertos según una letra inicial de su nombre.
    Args:
        letra (str): La letra inicial para filtrar los aeropuertos. Use '*' para obtener todos.
    Returns:
        list: Una lista de diccionarios que representan aeropuertos.
    """
    def get_airports(self, letra):
        listaAeropuertos = self.model.obtenerAeropuertos()
        if letra == '*': # Muestra todos los aeropuertos
            return listaAeropuertos 
        else: # En caso de filtrar por letra
            listaAeropuertoFiltro = [airport for airport in listaAeropuertos if airport['airport_name'].startswith(letra.upper())]
            return listaAeropuertoFiltro