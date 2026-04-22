"""
¿Qué hace cada widget?
Label (Etiqueta) → muestra texto
Entry (Caja) → permite ingresar texto
Button (Botón) → ejecuta una acción (función)
"""
import tkinter as tk


# Función para el botón
def saludar():
    nombre = entry.get()
    label_resultado.config(text=f"Hola {nombre}!")


# Crear root principal
root = tk.Tk()
root.title("Ejemplo básico")
root.geometry("300x200")

# Etiqueta
label = tk.Label(root, text="Ingrese su nombre:")
label.pack()

# Caja de texto (Entry)
entry = tk.Entry(root)
entry.pack()

# Botón
boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack()

# Etiqueta para mostrar resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Ejecutar app
root.mainloop()
