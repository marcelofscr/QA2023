from flask import Flask, render_template, request

# Importar clases y módulos personalizados desde la lógica de negocios y la lógica creacional.
from logicadenegocios.Aeropuerto import Aeropuerto
from logicadenegocios.Vuelo import Vuelo
from logicacreacional.AeropuertoSingleton import AeropuertoSingleton
from logicacreacional.VueloSingleton import VueloSingleton

# Importar controladores personalizados.
from controlador.controladorAeropuerto import controladorAeropuerto
from controlador.controladorVuelos import controladorVuelos
from controlador.controladorVuelosActualesSalida import controladorVuelosActualesSalida
from controlador.controladorVuelosActuales import controladorVuelosActuales
from controlador.controladorClima import controladorClima
from controlador.controladorCodigoVuelos import controladorCodigoVuelos

# Crear una instancia de la aplicación Flask.
app = Flask(__name__)

# Crear una única instancia de las clases Aeropuerto y Vuelo utilizando el patrón de diseño Singleton.
aeropuerto = AeropuertoSingleton.getInstance(Aeropuerto,"83a922f7be03a2cbd4dda957dffcc2a3")
vuelo = VueloSingleton.getInstance(Vuelo, "83a922f7be03a2cbd4dda957dffcc2a3")

# Crear controladores para las diferentes funcionalidades de la aplicación.
controllerAeropuerto = controladorAeropuerto(aeropuerto)
controllerLlegada = controladorVuelosActuales(vuelo)
controllerSalida = controladorVuelosActualesSalida(vuelo)
controllerRuta = controladorVuelos(vuelo)
controllerClima = controladorClima(vuelo)
controllerCodigoVuelos = controladorCodigoVuelos(vuelo)

# Ruta principal que renderiza la página de inicio (index.html).
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener aeropuertos basados en una letra ingresada.
@app.route('/get_airports', methods=['POST'])
def get_airports():
    letra = request.form['letra'].upper()
    aeropuertos = controllerAeropuerto.get_airports(letra)
    aeropuertos.sort(key=lambda airport: airport['airport_name'])
    return render_template('vistaAeropuertos.html', aeropuertos=aeropuertos)

# Ruta para obtener vuelos actuales basados en una IATA ingresada.
@app.route('/getVuelosActuales', methods=['POST'],)
def getVuelosActuales():
    iata = request.form['iata']
    vuelos = controllerLlegada.getVuelosActuales(iata)
    return render_template('vistaVuelosActuales.html', vuelos=vuelos)

# Ruta para obtener vuelos actuales de salida basados en una IATA ingresada.
@app.route('/getVuelosActualesSalida', methods=['POST'])
def getVuelosActualesSalida():
    iata = request.form['iataD']
    vueloSalidas = controllerSalida.getVuelosActualesSalida(iata)
    return render_template('vistaVuelosActualesSalida.html', flights=vueloSalidas)

# Ruta para obtener vuelos basados en un origen y destino ingresados.
@app.route('/get_flights', methods=['POST'])
def get_flights():
    iataO = request.form['iataOrigen']
    iataDs = request.form['iataDestino']
    vueloRutas = controllerRuta.get_flights(iataO,iataDs)
    return render_template('vistaVuelosRuta.html', flights=vueloRutas)

# Ruta para obtener información climática de un aeropuerto basado en una IATA ingresada.
@app.route('/get_weather', methods=['POST'])
def get_weather():
    iataAeropuerto = request.form['iataAeropuerto']
    clima = controllerClima.get_weather(iataAeropuerto)
    return render_template('vistaClima.html', airports=clima)

# Ruta para obtener vuelos basados en un código de vuelo (IATA) ingresado.
@app.route('/get_flights_by_code', methods=['POST'])
def get_flights_by_code():
    iataVuelo = request.form['iataVuelo']
    vuelosCodigo = controllerCodigoVuelos.get_flights_by_code(iataVuelo)
    return render_template('vistaCodigoVuelo.html', flights=vuelosCodigo)

# Ejecuta la aplicación Flask en modo de depuración (debug) cuando el script se ejecuta.
if __name__ == '__main__':
    app.run(debug=True)
