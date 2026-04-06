""""
abre un archivo en modo lectura (r) y lee todo su contenido
"""
# abro el archivo texto.tx en modo lectura
file = open("../archivos_demo/texto.txt", "r")

# leo todo el archivo
texto = file.read()

# muestro contenido del archivo
print("contenido del archivo: ", texto)

# cierro el archivo
file.close()
