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
        

    def obtenerVuelosLlegada(self, iataAeropuerto):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&arr_iata={iataAeropuerto}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vuelosLlegada = []
            for vuelo in data["data"]:
                airline = vuelo["airline"]["name"]
                flight_number = vuelo["flight"]["number"]
                departure = vuelo["departure"]["airport"]
                estimated_arrival = vuelo["arrival"]["estimated"]

                vuelosLlegada.append({
                    "airline": airline,
                    "flight_number": flight_number,
                    "departure": departure,
                    "estimated_arrival": estimated_arrival
                })
            return vuelosLlegada
        

    def obtenerVuelosSalida(self, iataAeropuerto):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&dep_iata={iataAeropuerto}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vuelosSalida = []
            for vuelo in data["data"]:
                airline = vuelo["airline"]["name"]
                flight_number = vuelo["flight"]["number"]
                destination = vuelo["arrival"]["airport"]
                departure_time = vuelo["departure"]["estimated"]

                vuelosSalida.append({
                    "airline": airline,
                    "flight_number": flight_number,
                    "destination": destination,
                    "departure_time": departure_time
                })
            return vuelosSalida