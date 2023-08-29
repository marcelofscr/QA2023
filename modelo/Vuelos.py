import requests


class Vuelos:
    def __init__(self, api_key):
        self.api_key = api_key

    def obtenerVuelos(self):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            flights = data['data']
            return flights
        else:
            return []