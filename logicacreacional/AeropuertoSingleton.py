from logicadenegocios.Aeropuerto import Aeropuerto

"""
La clase AeropuertoSingleton implementa el patrón Singleton para garantizar
que solo exista una instancia de la clase Aeropuerto con una clave API dada.
Attributes:
    __instance (AeropuertoSingleton): Almacena la instancia única de AeropuertoSingleton.
Methods:
     __init__(self, api_key): Inicializa una instancia de la clase con una clave API.
    getInstance(cls, api_key): Obtiene la instancia única de la clase AeropuertoSingleton.
"""
class AeropuertoSingleton:
    
    __instance__ = None

    """
    Inicializa una nueva instancia de AeropuertoSingleton con una clave API.
    Args:
        api_key (str): La clave API necesaria para inicializar Vuelo.
    """
    def __init__(self, api_key):
        self.api_key = api_key
    
    """
    Método estático que devuelve la instancia única de la clase AeropuertoSingleton.
    Args:
        api_key (str): La clave API necesaria para inicializar Aeropuerto.
    Returns:
        AeropuertoSingleton: La instancia única de AeropuertoSingleton.
    """
    def getInstance(cls, api_key):
        
        if(AeropuertoSingleton.__instance__ is None):
            AeropuertoSingleton.__instance__ = Aeropuerto.__new__(cls)
            AeropuertoSingleton.__instance__.api_key = api_key
        return AeropuertoSingleton.__instance__



