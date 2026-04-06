"""
abre un archivo en modo lectura y lee todas las lineas de su contenido
"""

# abrir el archivo en modo lectura
file = open("texto_1.txt", "r")

# leemos todas las lineas del archivo
lineas = file.readlines()

# muestro contenido del archivo
print("file readlines:", lineas)

# linea por linea
for linea in lineas:
    print("linea", linea)

# cierro el archivo
file.close()
