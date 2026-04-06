"""
abre un archivo en modo lectura y lo va leyendo linea a linea
"""
# abrir el archivo en modo lectura
file = open("../archivos_demo/texto.txt", "r")

# linea por linea
# linea = file.readline()

#while linea:
while (linea := file.readline()):
    print("linea: ", linea)

    # linea = file.readline()

# cierro el archivo
file.close()


# operador walrus while (linea := file.readline()):