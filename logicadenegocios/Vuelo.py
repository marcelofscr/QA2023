import requests
from datetime import datetime

class Vuelo:
    # Método constructor de la clase
    def __init__(self, api_key):
        self.api_key = api_key

    """
    Obtiene la información de vuelos entre dos aeropuertos especificados por sus códigos IATA.
    Args:
        iataOrigen (str): El código IATA del aeropuerto de origen.
        iataDestino (str): El código IATA del aeropuerto de destino.
    Returns:
        list: Una lista de diccionarios que representan la información de vuelos entre los aeropuertos.
    """
    def obtenerVuelos(self, iataOrigen, iataDestino):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&dep_iata={iataOrigen}&arr_iata={iataDestino}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vuelosRuta = []
            for flight in data["data"]:
                airlineName = flight["airline"]["name"]
                flight_iata = flight["flight"]["iata"]
                departure_scheduled = flight['departure']['scheduled']
                arrival_scheduled = flight['arrival']['scheduled']
                status = flight["flight_status"]

                vuelosRuta.append({
                    "airline": airlineName,
                    "flight_iata": flight_iata,
                    "departure_scheduled": departure_scheduled,
                    "arrival_scheduled": arrival_scheduled,
                    "status": status
                })
            return vuelosRuta

    """
    Obtiene la información de vuelos que llegan a un aeropuerto especificado por su código IATA.
    Args:
        iataAeropuerto (str): El código IATA del aeropuerto de llegada.
    Returns:
        list: Una lista de diccionarios que representan la información de vuelos que llegan al aeropuerto.
    """
    def obtenerVuelosLlegada(self, iataAeropuerto):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&arr_iata={iataAeropuerto}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vuelosLlegada = []
            for vuelo in data["data"]:
                airline = vuelo["airline"]["name"]
                flight_iata = vuelo["flight"]["iata"]
                departure = vuelo["departure"]["airport"]
                estimated_arrival = vuelo["arrival"]["estimated"]

                vuelosLlegada.append({
                    "airline": airline,
                    "flight_iata": flight_iata,
                    "departure": departure,
                    "estimated_arrival": estimated_arrival
                })
            return vuelosLlegada
        

    """
    Obtiene la información de vuelos que salen desde un aeropuerto especificado por su código IATA.
    Args:
        iataAeropuerto (str): El código IATA del aeropuerto de salida.
    Returns:
        list: Una lista de diccionarios que representan la información de vuelos que salen del aeropuerto.
    """
    def obtenerVuelosSalida(self, iataAeropuerto):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&dep_iata={iataAeropuerto}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            vuelosSalida = []
            for vuelo in data["data"]:
                airline = vuelo["airline"]["name"]
                flight_iata = vuelo["flight"]["iata"]
                destination = vuelo["arrival"]["airport"]
                departure_time = vuelo["departure"]["estimated"]

                vuelosSalida.append({
                    "airline": airline,
                    "flight_iata": flight_iata,
                    "destination": destination,
                    "departure_time": departure_time
                })
            return vuelosSalida
        
    """
    Obtiene información de un vuelo específico por su código IATA.
    Args:
        iataVuelo (str): El código IATA del vuelo que se desea consultar.
    Returns:
        list: Una lista de diccionarios que representan la información del vuelo.
    """
    def obtenerVueloPorCodigo(self, iataVuelo):
        url = f'http://api.aviationstack.com/v1/flights?access_key={self.api_key}&flight_iata={iataVuelo}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            vuelosCodigo = []
            for flight in data["data"]:
                flight_iata = flight["flight"]["iata"]
                airline = flight["airline"]["name"]
                departure = flight["departure"]["airport"]
                destination = flight["arrival"]["airport"]
                departure_time = flight["departure"]["estimated"]
                print("HolaPerros")
                print(departure_time)
                print("Hola")
                estimated_arrival = flight["arrival"]["estimated"]
                status = flight["flight_status"]

                vuelosCodigo.append({
                    "flight_iata": flight_iata,
                    "airline": airline,
                    "departure": departure,
                    "destination": destination,
                    "departure_time": departure_time,
                    "estimated_arrival": estimated_arrival,
                    "status": status
                })
            return vuelosCodigo
        else:
            return []