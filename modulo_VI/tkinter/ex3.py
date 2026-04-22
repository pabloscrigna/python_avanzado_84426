"""
Casilla de verificacion
Checkbox basico

¿Cómo funciona?
IntVar() → guarda 0 o 1
variable=var → conecta el checkbox con la variable
var.get() → obtiene el estado
"""

import tkinter as tk


def mostrar():
    print(var.get())  # 1 = marcado, 0 = desmarcado


# configuracion de la ventana
root = tk.Tk()
root.title("Checkbox básico")
root.geometry("300x300")

# Variable asociada
var = tk.IntVar()

# Checkbutton
check = tk.Checkbutton(root, text="Acepto términos", variable=var)
check.pack()

tk.Button(root, text="Ver estado", command=mostrar).pack()

root.mainloop()
