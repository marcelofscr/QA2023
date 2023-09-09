from logicadenegocios.Vuelo import Vuelo

"""
La clase VueloSingleton implementa el patrón Singleton para garantizar
que solo exista una instancia de la clase Vuelo con una clave API dada.
Attributes:
    __instance (AeropuertoSingleton): Almacena la instancia única de VueloSingleton.
Methods:
     __init__(self, api_key): Inicializa una instancia de la clase con una clave API.
    getInstance(cls, api_key): Obtiene la instancia única de la clase VueloSingleton.
"""
class VueloSingleton:
    __instance__ = None

    """
    Inicializa una nueva instancia de VueloSingleton con una clave API.
    Args:
        api_key (str): La clave API necesaria para inicializar Vuelo.
    """
    def __init__(self, api_key):
        self.api_key = api_key

    """
    Obtiene la instancia única de la clase VueloSingleton o la crea si no existe.
    Args:
        api_key (str): La clave API necesaria para inicializar Vuelo.
    Returns:
        VueloSingleton: La instancia única de VueloSingleton.
    """
    def getInstance(cls, api_key):
        if(VueloSingleton.__instance__ is None):
            VueloSingleton.__instance__ = Vuelo.__new__(cls)
            VueloSingleton.__instance__.api_key = api_key
        return VueloSingleton.__instance__