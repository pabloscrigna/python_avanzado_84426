import csv
from collections import defaultdict


# lee el archivo csv
with open("vuelos_asientos_pasajeros.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    filas = list(reader)

# Calcular ocupación por fila
for fila in filas:
    asientos = int(fila["asientos"])
    pasajeros = int(fila["pasajeros"])
    fila["ocupacion"] = round(pasajeros / asientos, 4) if asientos > 0 else 0

# Filtrar solo internacionales
internacionales = [f for f in filas if f["clasificacion_vuelo"] == "Internacional"]

# Totales por tipo de vuelo
totales = defaultdict(lambda: {"pasajeros": 0, "asientos": 0, "vuelos": 0})
for fila in filas:
    tipo = fila["clasificacion_vuelo"]
    totales[tipo]["pasajeros"] += int(fila["pasajeros"])
    totales[tipo]["asientos"]  += int(fila["asientos"])
    totales[tipo]["vuelos"]    += int(fila["vuelos"])
print(dict(totales))

# Día con más pasajeros internacionales
max_dia = max(internacionales, key=lambda f: int(f["pasajeros"]))
print(max_dia)

# Vuelos de cabotaje por año
por_anio = defaultdict(int)
for fila in filas:
    if fila["clasificacion_vuelo"] == "Cabotaje":
        anio = fila["indice_tiempo"][:4]  # "2017-01-01" -> "2017"
        por_anio[anio] += int(fila["vuelos"])
for anio, total in sorted(por_anio.items()):
    print(f"{anio}: {total:,} vuelos")