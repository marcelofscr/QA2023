import tkinter as tk
from vista.vistaAeropuerto import vistaAeropuerto  
from vista.vistaVuelos import vistaVuelos
from vista.vistaClima import vistaClima

class menuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")
        root.geometry("600x500")
        root.configure(bg="lightcyan")

        labelGrandeMenu = tk.Label(root, text="Menu Principal:", font=("Helvetica", 16), bg= "lightcyan")
        labelGrandeMenu.pack(pady=20)
        self.button = tk.Button(root, text="Consulta Aeropuerto", command=self.abrirVistaAeropuerto, bg="light blue", fg="white", font=("Helvetica", 12))
        self.button.pack()
        self.button1 = tk.Button(root, text="Consulta Vuelos", command=self.abrirVistaVuelos, bg="light blue", fg="white", font=("Helvetica", 12))
        espacio = tk.Label(root, text="", bg="lightcyan")
        espacio.pack()
        self.button1.pack()
        self.button2 = tk.Button(root, text="Consulta Clima", command=self.abrirVistaClima, bg="light blue", fg="white", font=("Helvetica", 12))
        espacio1 = tk.Label(root, text="", bg="lightcyan")
        espacio1.pack()
        self.button2.pack()


    def abrirVistaAeropuerto(self):
        self.root.destroy()  
        vistaaeropuerto = vistaAeropuerto(tk.Tk())

    def abrirVistaVuelos(self):
        self.root.destroy()  
        vistavuelos = vistaVuelos(tk.Tk()) 

    def abrirVistaClima(self):
        self.root.destroy()  
        vistaclimas = vistaClima(tk.Tk()) 