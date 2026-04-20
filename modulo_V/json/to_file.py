import json


print("--- Python object ---> JSON string file")

# dict en python
data = {
    "nombre": "Pablo",
    "edad": 30,
    "peso": 56.8,
    "activo": True,
    "notas": [10, 45, 67],
    "direccion": None
}


# abro un archivo en modo escritura
with open("datos.json", "w") as file:
    # dump: convierte un objeto python a un string json y lo escribe en el archivo file
    json.dump(data, file, indent=4)


print("--- JSON string file ---> Python object")

# abr un archivo en modo lectura
with open("datos.json", "r") as file:
    # json load, lee un archivo en formato json y retorna el contenido en formato python
    python_object = json.load(file)


print("object: ", python_object)
print("object type:", type(python_object))
