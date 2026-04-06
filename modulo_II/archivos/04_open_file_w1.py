"""
abrimos un archivo en modo escritura y escribimos dos lineas
si el archivo existe lo borra
"""
# abrir el archivo modo escritura
file = open("../archivos_demo/archivo_escritura.txt", "w")

# escribimos dos lineas
file.write("Primera linea de mi nuevo archivo\n")
file.write("Segunda linea")

# cerramos el archivo
file.close()
