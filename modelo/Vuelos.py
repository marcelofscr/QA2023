import requests


class Vuelos:
    def __init__(self, api_key):
        self.api_key = api_key

    
    def obtenerVuelos(self, iataOrigen, iataDestino):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&dep_iata={iataOrigen}&arr_iata={iataDestino}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vuelosRuta = []
            for flight in data["data"]:
                airlineName = flight["airline"]["name"]
                flight_number2 = flight["flight"]["number"]
                departure_scheduled = flight['departure']['scheduled']
                arrival_scheduled = flight['arrival']['scheduled']
                status = flight["flight_status"]

                vuelosRuta.append({
                    "airline": airlineName,
                    "flight_number": flight_number2,
                    "departure_scheduled": departure_scheduled,
                    "arrival_scheduled": arrival_scheduled,
                    "status": status
                })
            return vuelosRuta

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
        
    #Retorna la información de un vuelo en específico a partir de un Código
    def obtenerVueloPorCodigo(self):
        url = f'http://api.aviationstack.com/v1/airports?access_key={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            informacionVuelo = []
            for vuelo in data["data"]:
                airline = vuelo["airline"]["name"]
                departure = vuelo["departure"]["airport"]
                destination = vuelo["arrival"]["airport"]
                departure_time = vuelo["departure"]["estimated"]
                estimated_arrival = vuelo["arrival"]["estimated"]
                status = ["flight_status"]

                informacionVuelo.append({
                    "airline": airline,
                    "departure": departure,
                    "destination": destination,
                    "departure_time": departure_time,
                    "estimated_arrival": estimated_arrival,
                    "status": status
                })
            return informacionVuelo
        else:
            return []