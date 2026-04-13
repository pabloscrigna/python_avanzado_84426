import os

# listdir
archivos = os.listdir()
print(archivos)

# getcwd
print("ruta actual: ", os.getcwd())

#mkdir
os.mkdir("nueva_carpeta")

print("so:", os.name)


os.system("ls -lart")