import tkinter as tk
from controlador.controladorAeropuerto import controladorAeropuerto  
from modelo.Aeropuerto import Aeropuerto 

class vistaAeropuerto:
    def __init__(self, root):
        self.controller = controladorAeropuerto(Aeropuerto("83a922f7be03a2cbd4dda957dffcc2a3"))

        self.root = root
        self.root.title("Información")
        root.geometry("600x500")
        root.configure(bg="lightcyan")

        self.label = tk.Label(root, text="Filtro:", font=("Helvetica", 16), bg= "lightcyan")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Obtener Aeropuertos", command=self.get_airports, bg="light blue", fg="white", font=("Helvetica", 12))
        self.button.pack()

        self.text = tk.Text(root)
        self.text.pack()


    def get_airports(self):
        letter = self.entry.get().upper()
        airports = self.controller.get_airports(letter)
        self.text.delete(1.0, tk.END)
        for airport in airports:
            self.text.insert(tk.END, f"{airport['airport_name']} - {airport['iata_code']}\n")

