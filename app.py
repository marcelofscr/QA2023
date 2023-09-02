from flask import Flask, render_template, request


from modelo.Aeropuerto import Aeropuerto
from modelo.Vuelos import Vuelos
from controlador.controladorAeropuerto import controladorAeropuerto
from controlador.controladorVuelos import controladorVuelos
from controlador.controladorVuelosActualesSalida import controladorVuelosActualesSalida
from controlador.controladorVuelosActuales import controladorVuelosActuales
from controlador.controladorClima import controladorClima
from controlador.controladorCodigoVuelos import controladorCodigoVuelos

app = Flask(__name__)
controller = controladorAeropuerto(Aeropuerto("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerLlegada = controladorVuelosActuales(Vuelos("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerSalida = controladorVuelosActualesSalida(Vuelos("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerRuta = controladorVuelos(Vuelos("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerClima = controladorClima(Aeropuerto("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerCodigoVuelos = controladorCodigoVuelos(Vuelos("83a922f7be03a2cbd4dda957dffcc2a3"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_airports', methods=['POST'])
def get_airports():
    letra = request.form['letra'].upper()
    aeropuertos = controller.get_airports(letra)
    aeropuertos.sort(key=lambda airport: airport['airport_name'])
    return render_template('vistaAeropuertos.html', aeropuertos=aeropuertos)

@app.route('/getVuelosActuales', methods=['POST'],)
def getVuelosActuales():
    iata = request.form['iata']
    vuelos = controllerLlegada.getVuelosActuales(iata)
    return render_template('vistaVuelosActuales.html', vuelos=vuelos)

@app.route('/getVuelosActualesSalida', methods=['POST'])
def getVuelosActualesSalida():
    iata = request.form['iataD']
    vueloSalidas = controllerSalida.getVuelosActualesSalida(iata)
    return render_template('vistaVuelosActualesSalida.html', flights=vueloSalidas)

@app.route('/get_flights', methods=['POST'])
def get_flights():
    iataO = request.form['iataOrigen']
    iataDs = request.form['iataDestino']
    vueloRutas = controllerRuta.get_flights(iataO,iataDs)
    return render_template('vistaVuelosRuta.html', flights=vueloRutas)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    iataAeropuerto = request.form['iataAeropuerto']
    clima = controllerClima.get_weather(iataAeropuerto)
    return render_template('vistaClima.html', airports=clima)

@app.route('/get_flights_by_code', methods=['POST'])
def get_flights_by_code():
    iataVuelo = request.form['iataVuelo']
    vuelosCodigo = controllerCodigoVuelos.get_flights_by_code(iataVuelo)
    return render_template('vistaCodigoVuelo.html', flights=vuelosCodigo)

if __name__ == '__main__':
    app.run(debug=True)
