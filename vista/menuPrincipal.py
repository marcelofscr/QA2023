import tkinter as tk
from vista.vistaAeropuerto import vistaAeropuerto  

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


    def abrirVistaAeropuerto(self):
        self.root.destroy()  
        vistaaeropuerto = vistaAeropuerto(tk.Tk()) 
       