"""
Ejecutar en un entorno virtual con pandas
pip install pandas
"""
import pandas as pd

# Leer el CSV
df = pd.read_csv("vuelos_asientos_pasajeros.csv", parse_dates=["indice_tiempo"])

# Vista general
# cantidad de filas y columnas
print(df.shape)
# tipo de datos de las columnas     
print(df.dtypes)
# las primeras 5 filas
print(df.head())

# Calcular ocupación (pasajeros / asientos)
df["ocupacion"] = df["pasajeros"] / df["asientos"]

# Filtrar solo vuelos internacionales
internacionales = df[df["clasificacion_vuelo"] == "Internacional"]

# Totales por tipo de vuelo
totales = df.groupby("clasificacion_vuelo")[["pasajeros", "asientos", "vuelos"]].sum()
print(totales)

# Promedio mensual de pasajeros (todos los vuelos)
df["anio_mes"] = df["indice_tiempo"].dt.to_period("M")
mensual = df.groupby(["anio_mes", "clasificacion_vuelo"])["pasajeros"].sum()
print(mensual.tail(10))

# Día con más pasajeros internacionales
max_dia = internacionales.loc[internacionales["pasajeros"].idxmax()]
print(max_dia)

# Año con más vuelos (cabotaje)
cabotaje = df[df["clasificacion_vuelo"] == "Cabotaje"].copy()
cabotaje["anio"] = cabotaje["indice_tiempo"].dt.year
por_anio = cabotaje.groupby("anio")["vuelos"].sum()
print(por_anio)