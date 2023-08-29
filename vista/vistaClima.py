import tkinter as tk
from controlador.controladorClima import controladorClima  
from modelo.Aeropuerto import Aeropuerto 

class vistaClima:
    def __init__(self, root):
        self.controller = controladorClima(Aeropuerto("83a922f7be03a2cbd4dda957dffcc2a3"))

        self.root = root
        self.root.title("Información")
        root.geometry("600x500")
        root.configure(bg="lightcyan")

        self.label = tk.Label(root, text="Código aeropuerto:", font=("Helvetica", 16), bg= "lightcyan")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Obtener información clima", command=self.get_airportsWeather, bg="light blue", fg="white", font=("Helvetica", 12))
        self.button.pack()

        self.text = tk.Text(root)
        self.text.pack()



    def get_airportsWeather(self):
        CodeAirport = self.entry.get().upper()
        airports = self.controller.get_weather(CodeAirport)
        self.text.delete(1.0, tk.END)
        for airport in airports:
            self.text.insert(tk.END, f"Aeropuerto: {airport['airport_name']}\n")
            self.text.insert(tk.END, f"Ciudad: {airport['timezone']}\n")
            self.text.insert(tk.END,f"CONDICIONES ACTUALES:\n")
            self.text.insert(tk.END, f"Latitud: {airport['latitude']}\n")
            self.text.insert(tk.END, f"Longitud: {airport['longitude']}\n")
            self.text.insert(tk.END, f"Temperatura: {airport['gmt']}\n")
            self.text.insert(tk.END, f"Visibilidad: {airport['geoname_id']}\n")
