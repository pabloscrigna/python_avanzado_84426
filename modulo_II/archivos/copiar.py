origen = "texto_1.txt"
destino = "salida_copiar.txt"

with open(origen, "r") as file:
    datos = file.read()

with open(destino, "w") as file:
    file.write(datos)


