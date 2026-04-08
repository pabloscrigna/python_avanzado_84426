"""
abre un archivo en modo lectura y lo va leyendo linea a linea
"""
# abrir el archivo en modo lectura
file = open("../archivos_demo/texto.txt", "r")

# linea por linea
while (linea := file.readline()):
    print("linea: ", linea)

# cierro el archivo
file.close()


