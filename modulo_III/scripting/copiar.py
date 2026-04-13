"""
usage: python3 copiar.py arch_origen arch_destino
usage: python3 copiar.py arch_origen  --> error
"""
import sys


argumentos = sys.argv


if len(argumentos) < 3:
    print("usage: python3 copiar.py arch_origen arch_destino")
    exit(1)


origen = argumentos[1]    # texto_1.txt
destino = argumentos[2]

print(f"copiando archivo origen: {origen} hacia el archivo destino {destino}")

with open(origen, "r") as file:
    datos = file.read()

with open(destino, "w") as file:
    file.write(datos)
