"""
🔎 Claves del Combobox
combo["values"] → lista de opciones
combo.get() → valor seleccionado
combo.current(0) → selecciona por defecto

esta en ttk

El ttk.Combobox:

❌ Solo permite una opción
❌ No tiene modo múltiple

"""

import tkinter as tk
from tkinter import ttk


# Función
def mostrar():
    label.config(text=f"Elegiste: {combo.get()}")

# configuro la ventana
root = tk.Tk()
root.title("Combobox ejemplo")
root.geometry("300x300")

# Crear Combobox
combo = ttk.Combobox(root)
combo.pack()

# Opciones
combo["values"] = ["Python", "Java", "C++", "JavaScript"]

# Botón
boton = tk.Button(root, text="Mostrar", command=mostrar)
boton.pack()

# Etiqueta
label = tk.Label(root, text="")
label.pack()

root.mainloop()
