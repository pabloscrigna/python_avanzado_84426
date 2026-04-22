import tkinter as tk

# configuracion de la ventana principal
root = tk.Tk()
root.title("Check Button Multiples")
root.geometry("300x300")

opciones = ["Python", "Java", "C++", "JavaScript"]
vars_checks = {}

for opcion in opciones:
    var = tk.IntVar()
    chk = tk.Checkbutton(root, text=opcion, variable=var)
    chk.pack()
    vars_checks[opcion] = var


def mostrar():
    seleccionados = [op for op, var in vars_checks.items() if var.get()]
    label.config(text=", ".join(seleccionados))


tk.Button(root, text="Mostrar", command=mostrar).pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()
