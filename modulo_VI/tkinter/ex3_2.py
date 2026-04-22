import tkinter as tk


def mostrar():
    seleccionados = []

    if python_var.get():
        seleccionados.append("Python")
    if java_var.get():
        seleccionados.append("Java")
    if js_var.get():
        seleccionados.append("JavaScript")

    label.config(text=", ".join(seleccionados))


# configuracion de la ventana principal
root = tk.Tk()
root.title("Check Button Multiples")
root.geometry("300x300")

# variables para cada boton
python_var = tk.IntVar()
java_var = tk.IntVar()
js_var = tk.IntVar()

# botones
tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="Java", variable=java_var).pack()
tk.Checkbutton(root, text="JavaScript", variable=js_var).pack()

# boton que muestra el estada de cada uno
tk.Button(root, text="Mostrar", command=mostrar).pack()

# label para mostrar resultados
label = tk.Label(root, text="")
label.pack()

root.mainloop()
