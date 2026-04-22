import tkinter as tk


def actualizar():
    if var.get() == 1:
        label.config(text="Modo Activo")
    else:
        label.config(text="Modo Inactivo")


# configuracion de la ventana principal
root = tk.Tk()
root.title("Check Button")
root.geometry("300x300")

# variable a asociar al checkbutton
var = tk.IntVar()

# check button
check = tk.Checkbutton(root, text="Modo", variable=var, command=actualizar)
check.pack()

# label para mostrar estado 
label = tk.Label(root, text="Inactivo")
label.pack()

root.mainloop()
