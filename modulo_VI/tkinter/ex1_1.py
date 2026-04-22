import tkinter as tk


def sumar():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    resultado.config(text=f"Resultado: {n1 + n2}")


# defino mi ventana
root = tk.Tk()
root.title("Sumador")
root.geometry("300x200")

# Cajas
entry1 = tk.Entry(root)
# lo muestra y lo ubica automaticmente
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Etiqueta resultado
resultado = tk.Label(root, text="Resultado:")
resultado.pack()

# Botón
boton = tk.Button(root, text="Sumar", command=sumar)
boton.pack()

root.mainloop()
