import requests

class CodigoVuelos:
    def __init__(self, api_key):
        self.api_key = api_key

    #Devuelve la información de un vuelo en específico a partir de un Código
    def obtenerVueloPorCodigo(self):
        url = f'http://api.aviationstack.com/v1/airports?access_key={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            flight = data['data']
            return flight
        else:
            return []