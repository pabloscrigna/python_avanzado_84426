# importamos la libreria
import requests

# url a consultar
# retorna un json
url = "https://api.github.com"
# retorna html
# url = "https://www.ole.com.ar"

# hacemos el get y guardamos la respuesta c
response = requests.get(url)


# imprimimos el codigo de estado
print("status code: ", response.status_code)
print("response text")
# imprimimos la respuesta que viene en formato json
print(response.json())
# imprimimos la respuesta que viene en html
# print(response.text)
