from flask import Flask, render_template, request
from controlador.controladorAeropuerto import controladorAeropuerto
from modelo.Aeropuerto import Aeropuerto
from modelo.Vuelos import Vuelos
from controlador.controladorVuelosActualesSalida import controladorVuelosActualesSalida
from controlador.controladorVuelosActuales import controladorVuelosActuales

app = Flask(__name__)
controller = controladorAeropuerto(Aeropuerto("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerLlegada = controladorVuelosActuales(Vuelos("83a922f7be03a2cbd4dda957dffcc2a3"))
controllerSalida = controladorVuelosActualesSalida(Vuelos("83a922f7be03a2cbd4dda957dffcc2a3"))

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

if __name__ == '__main__':
    app.run(debug=True)
