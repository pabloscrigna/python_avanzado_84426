"""
Selecciones multiples
"""
import tkinter as tk


def mostrar():
    indices = lista.curselection()

    if indices:
        seleccionados = [lista.get(i) for i in indices]
        label.config(text=", ".join(seleccionados))
    else:
        label.config(text="No seleccionaste nada")


# configuro la ventana
root = tk.Tk()
root.title("List box multiple seleccion")
root.geometry("300x300")

lista = tk.Listbox(root, selectmode=tk.MULTIPLE)
lista.pack()

for item in ["Python", "Java", "C++", "JavaScript"]:
    lista.insert(tk.END, item)


tk.Button(root, text="Mostrar", command=mostrar).pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()
