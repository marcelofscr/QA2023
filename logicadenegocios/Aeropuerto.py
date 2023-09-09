import requests

class Aeropuerto:
    # Método constructor de la clase
    def __init__(self, api_key):
        self.api_key = api_key

    """
    Obtiene una lista de todos los aeropuertos disponibles.
    Returns:
        list: Una lista de diccionarios que representan la información de los aeropuertos.
    """
    def obtenerAeropuertos(self):
        url = f'http://api.aviationstack.com/v1/airports?access_key={self.api_key}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            airports = data['data']
            return airports
        else: # Retorna una lista vacía si no se pudo obtener la información de los aeropuertos
            return []
    