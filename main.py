import tkinter as tk
from vista.menuPrincipal  import menuPrincipal  

def main():
    root = tk.Tk()
    menuprincipal = menuPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
