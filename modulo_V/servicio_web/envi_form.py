import requests

URL = "http://localhost:8880/form"


def enviar_formulario():
    print("=== Enviar Formulario ===")

    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    mensaje = input("Ingrese su mensaje: ")

    data = {
        "name": nombre,
        "email": email,
        "message": mensaje
    }

    response = requests.post(URL, data=data)

    print("\n--- RESPUESTA DEL SERVIDOR ---")
    print("Status:", response.status_code)
    print(response.text)


if __name__ == "__main__":
    enviar_formulario()