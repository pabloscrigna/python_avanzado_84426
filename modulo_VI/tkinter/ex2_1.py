"""
Listbox

Claves del Listbox
insert(indice, valor) → agrega elementos
curselection() → devuelve el índice seleccionado
get(indice) → obtiene el valor

lista = tk.Listbox(root, selectmode=tk.MULTIPLE)
"""
import tkinter as tk


# Función para obtener selección
def mostrar_seleccion():
    seleccion = lista.get(lista.curselection())
    label.config(text=f"Elegiste: {seleccion}")


# reamos la ventana
root = tk.Tk()
root.title("Listbox ejemplo")
root.geometry("300x300")

# Crear Listbox
lista = tk.Listbox(root)
# lista = tk.Listbox(root, selectmode=tk.MULTIPLE)
lista.pack()

# Agregar elementos
lista.insert(0, "Python")
lista.insert(1, "Java")
lista.insert(2, "C++")
lista.insert(3, "JavaScript")

# Botón
boton = tk.Button(root, text="Mostrar", command=mostrar_seleccion)
boton.pack()

# Etiqueta
label = tk.Label(root, text="")
label.pack()

root.mainloop()
