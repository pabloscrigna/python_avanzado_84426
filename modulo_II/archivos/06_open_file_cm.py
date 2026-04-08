# Context manager

# file = open()

with open("../archivos_demo/texto.txt", "r") as file:
    contenido = file.read()
    print("contenido: ", contenido)

# No es necesario hacer file.close() --> lo hace automaticamente el context manager

with open("archivo_escritura.txt", "a") as file:
    file.write("\n Desde el context manager")
    
# aca el archivo ya esta cerrado
# file.write("Hola")

print("Continua el programa")
