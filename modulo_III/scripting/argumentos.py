# built-in functions: len print int
# libreria standar : datetime sys
# librerias propias
# librerias que hay que instalar para usar

import sys


argumentos = sys.argv

print("argumentos: ", argumentos)


for argumento in argumentos:
    print(f"argumento: {argumento} , tipo: {type(argumento)}")

