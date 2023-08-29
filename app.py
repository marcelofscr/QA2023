from flask import Flask, render_template, request
from controlador.controladorAeropuerto import controladorAeropuerto
from modelo.Aeropuerto import Aeropuerto

app = Flask(__name__)
controller = controladorAeropuerto(Aeropuerto("83a922f7be03a2cbd4dda957dffcc2a3"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_airports', methods=['POST'])
def get_airports():
    letra = request.form['letra'].upper()
    aeropuertos = controller.get_airports(letra)
    aeropuertos.sort(key=lambda airport: airport['airport_name'])
    return render_template('vistaAeropuertos.html', aeropuertos=aeropuertos)

if __name__ == '__main__':
    app.run(debug=True)
