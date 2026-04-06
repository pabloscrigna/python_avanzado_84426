"""
abrimos un archivo en modo append, si el archivo existe
escribe al final. si el archivo no existe, lo crea
"""

# abrir el archivo modo agregar (append)
file = open("../archivos_demo/archivo_escritura.txt", "a")

# escribimos dos lineas
file.write("\nTercera linea\n")
file.write("Cuarta linea")

# cerramos el archivo
file.close()
