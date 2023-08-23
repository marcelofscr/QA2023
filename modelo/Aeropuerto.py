import requests

class Aeropuerto:
    def __init__(self, api_key):
        self.api_key = api_key

    def obtenerAeropuertos(self):
        url = f'http://api.aviationstack.com/v1/airports?access_key={self.api_key}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            airports = data['data']
            return airports
        else:
            return []