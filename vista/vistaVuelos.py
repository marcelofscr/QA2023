import tkinter as tk
from controlador.controladorVuelos import controladorVuelos  
from logicadenegocios.Vuelo import Vuelo
class vistaVuelos:
    def __init__(self, root):
        self.controller = controladorVuelos(Vuelo("83a922f7be03a2cbd4dda957dffcc2a3"))

        self.root = root
        self.root.title("Información")
        root.geometry("600x500")
        root.configure(bg="lightcyan")

        self.label1 = tk.Label(root, text="Código de origen:", font=("Helvetica", 16), bg= "lightcyan")
        self.label1.pack()

        self.entry_Origen = tk.Entry(root)
        self.entry_Origen.pack()

        self.label = tk.Label(root, text="Código de destino:", font=("Helvetica", 16), bg= "lightcyan")
        self.label.pack()

        self.entry_Destino = tk.Entry(root)
        self.entry_Destino.pack()

        self.button = tk.Button(root, text="Obtener vuelos", command=self.get_flights, bg="light blue", fg="white", font=("Helvetica", 12))
        self.button.pack()

        self.text = tk.Text(root)
        self.text.pack()

    def get_flights(self):
        iata_origen = self.entry_Origen.get().upper()
        iata_destino = self.entry_Destino.get().upper()
        flights = self.controller.get_flights(iata_origen, iata_destino)
        
        self.text.delete(1.0, tk.END)
        
        for flight in flights:
            try:
                airline_name = flight['airline']['name']
                flight_number = flight['flight']['iata']
                departure_scheduled = flight['departure']['scheduled']
                arrival_scheduled = flight['arrival']['scheduled']
                status = flight["flight_status"]
                self.text.insert(tk.END, f"Aerolínea: {airline_name}\n")
                self.text.insert(tk.END, f"Número de vuelo: {flight_number}\n")
                self.text.insert(tk.END, f"Estado: {status}\n")
                self.text.insert(tk.END, f"Hora de salida programada: {departure_scheduled}\n")
                self.text.insert(tk.END, f"Hora de llegada programada: {arrival_scheduled}\n")
                self.text.insert(tk.END, "--------------------------\n")
            except: 
                self.text.insert(tk.END,f"SE ENCONTRÓ UN DATO NULL")

            