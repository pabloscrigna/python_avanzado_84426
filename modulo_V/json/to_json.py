import json


print("--- Python object ---> JSON string")

# diccionario en python
data = {
    "nombre": "Pablo",
    "edad": 30,
    "peso": 56.8,
    "activo": True,
    "notas": [10, 45, 67],
    "direccion": None
}


# dumps, convierte a json los datos que se envian como parametro.
# retorna string json 
json_string = json.dumps(data, indent=4)

print("json string: ", json_string)
print("tipo json string: ", type(json_string))

print("\n--- JSON string ---> Python object")

# json.loads convierte a objeto python el string json que se pasa como parametro
object_python = json.loads(json_string)

print("python object : ", object_python)
print("tipo: ", type(object_python))


